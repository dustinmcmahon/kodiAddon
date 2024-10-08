import sqlite3
import os
import xbmc
import xbmcaddon
import searchOptions

addon = xbmcaddon.Addon()
if xbmc.getCondVisibility('system.platform.windows'):
    addonDataFolder = addon.getAddonInfo('path').replace(
        "addons\\video.kodi.episode.selector\\", "userdata\\addon_data\\video.kodi.episode.selector\\")
if xbmc.getCondVisibility('system.platform.osx') or xbmc.getCondVisibility('system.platform.linux'):
    addonDataFolder = addon.getAddonInfo('path').replace(
        "addons/video.kodi.episode.selector/", "userdata/addon_data/video.kodi.episode.selector/")
kesDBPath = "{}kesProfile.db".format(addonDataFolder)

# ************************
# *** Public Functions ***
# ************************

# ************************
# *** Setup Functions ****
# ************************

def install():
    if not os.path.exists(addonDataFolder):
        # create folder for addon data
        os.mkdir(addonDataFolder)
    createDB()

# Create the Database to hold profile data


def createDB():
    connection = sqlite3.connect(kesDBPath)
    cursor = connection.cursor()
    createTables(cursor)
    fillTable(cursor)

# Create the Tables that hold profile data


def createTables(cursor: sqlite3.Cursor):
    cursor.executescript("""
        BEGIN;
        CREATE TABLE IF NOT EXISTS profile(id INTEGER PRIMARY KEY, name TEXT, dateUsedLast date, timeUsedLast timestamp);
        CREATE TABLE IF NOT EXISTS searchOptionType(id INTEGER PRIMARY KEY, title TEXT UNIQUE ON CONFLICT IGNORE);
        CREATE TABLE IF NOT EXISTS profileOptions(id INTEGER PRIMARY KEY, r_profile INTEGER REFERENCES profile(id), r_searchOptionType INTEGER REFERENCES searchOptionType(id), value);
        COMMIT;
    """)

# Fill the searchOptionDefaults table with the type of options


def fillTable(cursor: sqlite3.Cursor):
    cursor.executescript("""
        BEGIN;
        INSERT OR IGNORE INTO searchOptionType (title) VALUES ('mediaType'),('watchStatus'),('tag'),('lengthMIN'),('lengthMAX'),('include'),('exclude'),('studio'),('mostWatched'),('genre'),('rating'),('cast'),('year'),('director');
        COMMIT;
    """)


def uninstall():
    if not os.path.exists("{}\kesProfile.db".format(addonDataFolder)):
        os.remove("{}\kesProfile.db".format(addonDataFolder))

# ************************
# *** Usable Functions ***
# ************************

# delete a profile from the system
# name should be the string of the save profile you would like to remove


# ************************
# *** Usable Functions ***
# ************************

# delete a profile from the system
# name should be the string of the save profile you would like to remove
def removeProfile(name: str):
    connection = sqlite3.connect(kesDBPath)
    cursor = connection.cursor()
    profileID = _getProfileID(name, cursor)
    _deleteAllOptions(profileID, cursor)
    _deleteProfile(profileID, cursor)
    connection.commit()
    connection.close()

# add a profile to the system
# name should be the string you would like to use to name the profile
# options is the set of search options you would like to save


# add a profile to the system
# name should be the string you would like to use to name the profile
# options is the set of search options you would like to save
def addProfile(name: str, options: searchOptions.SearchOptions):
    connection = sqlite3.connect(kesDBPath)
    cursor = connection.cursor()
    profileID = _getProfileID(name, cursor)
    _addOptions(profileID, options, cursor)
    connection.commit()
    connection.close()

# update an existing profile
# name should be the string of the current profile
# options should be the search options you would like to update to


# update an existing profile
# name should be the string of the current profile
# options should be the search options you would like to update to
def updateProfile(name: str, options: searchOptions.SearchOptions):
    connection = sqlite3.connect(kesDBPath)
    cursor = connection.cursor()
    profileID = _getProfileID(name, cursor)
    _deleteAllOptions(profileID, cursor)
    _addOptions(profileID, options, cursor)
    connection.commit()
    connection.close()

# get profile
# this will get a profile given a name


# get profile
# this will get a profile given a name
def getProfile(name: str) -> searchOptions.SearchOptions:
    connection = sqlite3.connect(kesDBPath)
    cursor = connection.cursor()
    profileID = _getProfileID(name, cursor)
    profile = _getProfileOptions(profileID, cursor)
    connection.commit()
    connection.close()
    return profile

# get a list of all profiles
# this will give a list of all profile names


def getAllProfiles():
    connection = sqlite3.connect(kesDBPath)
    cursor = connection.cursor()
    profiles = cursor.execute('SELECT name FROM profile;').fetchall()
    connection.commit()
    connection.close()
    return profiles


# get a list of all profiles
# this will give a list of all profile names
def getAllProfiles():
    connection = sqlite3.connect(kesDBPath)
    cursor = connection.cursor()
    profiles = cursor.execute('SELECT name FROM profile;').fetchall()
    connection.commit()
    connection.close()
    return profiles


# ************************
# ** Private Functions ***
# ************************

# get the id of the profile based on the name
# create one if it does not exist
def _getProfileID(name: str, cursor: sqlite3.Cursor) -> int:
    profiles = cursor.execute(
        "SELECT id FROM profile WHERE name = '{}';".format(name)).fetchall()
    if len(profiles) == 0:
        profiles = cursor.execute(
            "INSERT INTO profile (name) VALUES ('{}');".format(name)).fetchall()
        return _getProfileID(name, cursor)
    return profiles[0][0]

# Trigger the C portion of the CRUD Operations for all options


def _addOptions(profileID: int, options: searchOptions, cursor: sqlite3.Cursor):
    _addGenres(profileID, options.getGenre(), cursor)
    _addTags(profileID, options.getTag(), cursor)
    _addCast(profileID, options.getCast(), cursor)
    _addDirector(profileID, options.getDirector(), cursor)
    _addIncludes(profileID, options.getInclude(), cursor)
    _addExcludes(profileID, options.getExclude(), cursor)
    _addWatchStatus(profileID, options.getWatchStatus(), cursor)
    _addLength(profileID, options.getLength(), cursor)
    _addYears(profileID, options.getYear(), cursor)
    _addRating(profileID, options.getRating(), cursor)
    _addMediaType(profileID, options.getMediaType(), cursor)
    _addStudios(profileID, options.getStudio(), cursor)
    _addMostWatched(profileID, options.getMostWatched(), cursor)

# Trigger CRUD Operations for genre


def _addGenres(profileID: int, genres, cursor: sqlite3.Cursor):
    if len(genres) != 0:
        valueList = ""
        defaultID = cursor.execute(
            "SELECT id FROM searchOptionType WHERE title = 'genre';").fetchall()[0][0]
        for x in genres:
            valueList = "('{}',{},{})".format(x, profileID, defaultID) if valueList == "" else "{},('{}',{},{})".format(
                valueList, x, profileID, defaultID)
        cursor.execute(
            "INSERT INTO profileOptions (value,r_profile,r_searchOptionType) VALUES {};".format(valueList))


def _getGenres(profileID: int, cursor: sqlite3.Cursor):
    defaultID = cursor.execute(
        "SELECT id FROM searchOptionType WHERE title = 'genre';").fetchall()[0][0]
    tempList = cursor.execute("SELECT value FROM profileOptions WHERE r_profile = {} AND r_searchOptionType = {};".format(
        profileID, defaultID)).fetchall()
    returnList = []
    for x in tempList:
        returnList.append(x[0])
    return returnList

# Trigger CRUD Operations for tags


def _addTags(profileID: int, tags, cursor: sqlite3.Cursor):
    if len(tags) != 0:
        valueList = ""
        defaultID = cursor.execute(
            "SELECT id FROM searchOptionType WHERE title = 'tag';").fetchall()[0][0]
        for x in tags:
            valueList = "('{}',{},{})".format(x, profileID, defaultID) if valueList == "" else "{},('{}',{},{})".format(
                valueList, x, profileID, defaultID)
        cursor.execute(
            "INSERT INTO profileOptions (value,r_profile,r_searchOptionType) VALUES {};".format(valueList))


def _getTags(profileID: int, cursor: sqlite3.Cursor):
    defaultID = cursor.execute(
        "SELECT id FROM searchOptionType WHERE title = 'tag';").fetchall()[0][0]
    tempList = cursor.execute("SELECT value FROM profileOptions WHERE r_profile = {} AND r_searchOptionType = {};".format(
        profileID, defaultID)).fetchall()
    returnList = []
    for x in tempList:
        returnList.append(x[0])
    return returnList

# Trigger CRUD Operations for cast


def _addCast(profileID: int, cast, cursor: sqlite3.Cursor):
    if len(cast) != 0:
        valueList = ""
        defaultID = cursor.execute(
            "SELECT id FROM searchOptionType WHERE title = 'cast';").fetchall()[0][0]
        for x in cast:
            valueList = "('{}',{},{})".format(x, profileID, defaultID) if valueList == "" else "{},('{}',{},{})".format(
                valueList, x, profileID, defaultID)
        cursor.execute(
            "INSERT INTO profileOptions (value,r_profile,r_searchOptionType) VALUES {};".format(valueList))


def _getCast(profileID: int, cursor: sqlite3.Cursor):
    defaultID = cursor.execute(
        "SELECT id FROM searchOptionType WHERE title = 'cast';").fetchall()[0][0]
    tempList = cursor.execute("SELECT value FROM profileOptions WHERE r_profile = {} AND r_searchOptionType = {};".format(
        profileID, defaultID)).fetchall()
    returnList = []
    for x in tempList:
        returnList.append(x[0])
    return returnList

# Trigger CRUD Operations for director


def _addDirector(profileID: int, director, cursor: sqlite3.Cursor):
    if len(director) != 0:
        valueList = ""
        defaultID = cursor.execute(
            "SELECT id FROM searchOptionType WHERE title = 'director';").fetchall()[0][0]
        for x in director:
            valueList = "('{}',{},{})".format(x, profileID, defaultID) if valueList == "" else "{},('{}',{},{})".format(
                valueList, x, profileID, defaultID)
        cursor.execute(
            "INSERT INTO profileOptions (value,r_profile,r_searchOptionType) VALUES {};".format(valueList))


def _getDirector(profileID: int, cursor: sqlite3.Cursor):
    defaultID = cursor.execute(
        "SELECT id FROM searchOptionType WHERE title = 'director';").fetchall()[0][0]
    tempList = cursor.execute("SELECT value FROM profileOptions WHERE r_profile = {} AND r_searchOptionType = {};".format(
        profileID, defaultID)).fetchall()
    returnList = []
    for x in tempList:
        returnList.append(x[0])
    return returnList

# Trigger CRUD Operations for include list


def _addIncludes(profileID: int, includes, cursor: sqlite3.Cursor):
    if len(includes) != 0:
        valueList = ""
        defaultID = cursor.execute(
            "SELECT id FROM searchOptionType WHERE title = 'include';").fetchall()[0][0]
        for x in includes:
            valueList = "('{}',{},{})".format(x, profileID, defaultID) if valueList == "" else "{},('{}',{},{})".format(
                valueList, x, profileID, defaultID)
        cursor.execute(
            "INSERT INTO profileOptions (value,r_profile,r_searchOptionType) VALUES {};".format(valueList))


def _getIncludes(profileID: int, cursor: sqlite3.Cursor):
    defaultID = cursor.execute(
        "SELECT id FROM searchOptionType WHERE title = 'include';").fetchall()[0][0]
    tempList = cursor.execute("SELECT value FROM profileOptions WHERE r_profile = {} AND r_searchOptionType = {};".format(
        profileID, defaultID)).fetchall()
    returnList = []
    for x in tempList:
        returnList.append(x[0])
    return returnList

# Trigger CRUD Operations for exclude list


def _addExcludes(profileID: int, excludes, cursor: sqlite3.Cursor):
    if len(excludes) != 0:
        valueList = ""
        defaultID = cursor.execute(
            "SELECT id FROM searchOptionType WHERE title = 'exclude';").fetchall()[0][0]
        for x in excludes:
            valueList = "('{}',{},{})".format(x, profileID, defaultID) if valueList == "" else "{},('{}',{},{})".format(
                valueList, x, profileID, defaultID)
        cursor.execute(
            "INSERT INTO profileOptions (value,r_profile,r_searchOptionType) VALUES {};".format(valueList))


def _getExcludes(profileID: int, cursor: sqlite3.Cursor):
    defaultID = cursor.execute(
        "SELECT id FROM searchOptionType WHERE title = 'exclude';").fetchall()[0][0]
    tempList = cursor.execute("SELECT value FROM profileOptions WHERE r_profile = {} AND r_searchOptionType = {};".format(
        profileID, defaultID)).fetchall()
    returnList = []
    for x in tempList:
        returnList.append(x[0])
    return returnList

# Trigger CRUD Operations for Watch Status


def _addWatchStatus(profileID: int, watchStatus: int, cursor: sqlite3.Cursor):
    if len(watchStatus) != 0:
        valueList = ""
        defaultID = cursor.execute(
            "SELECT id FROM searchOptionType WHERE title = 'watchStatus';").fetchall()[0][0]
        for x in watchStatus:
            valueList = "({},{},{})".format(x, profileID, defaultID) if valueList == "" else "{},({},{},{})".format(
                valueList, x, profileID, defaultID)
        cursor.execute(
            "INSERT INTO profileOptions (value,r_profile,r_searchOptionType) VALUES {};".format(valueList))


def _getWatchStatus(profileID: int, cursor: sqlite3.Cursor) -> int:
    defaultID = cursor.execute("SELECT id FROM searchOptionType WHERE title = 'watchStatus';").fetchall()[0][0]
    tempList = cursor.execute("SELECT value FROM profileOptions WHERE r_profile = {} AND r_searchOptionType = {};".format(profileID, defaultID)).fetchall()
    result = []
    for x in tempList:
        result.append(x[0])
    return result

# Trigger CRUD Operations for length


def _addLength(profileID: int, length, cursor: sqlite3.Cursor):
    minID = cursor.execute(
        "SELECT id FROM searchOptionType WHERE title = 'lengthMIN';").fetchall()[0][0]
    maxID = cursor.execute(
        "SELECT id FROM searchOptionType WHERE title = 'lengthMAX';").fetchall()[0][0]
    cursor.execute("INSERT INTO profileOptions (value, r_profile, r_searchOptionType) VALUES ({},{},{}), ({},{},{});".format(
        length[0], profileID, minID, length[1], profileID, maxID))


def _getMinLength(profileID: int, cursor: sqlite3.Cursor) -> int:
    defaultID = cursor.execute(
        "SELECT id FROM searchOptionType WHERE title = 'lengthMIN';").fetchall()[0][0]
    return cursor.execute("SELECT value FROM profileOptions WHERE r_profile = {} AND r_searchOptionType = {};".format(profileID, defaultID)).fetchall()[0][0]


def _getMaxLength(profileID: int, cursor: sqlite3.Cursor) -> int:
    defaultID = cursor.execute(
        "SELECT id FROM searchOptionType WHERE title = 'lengthMAX';").fetchall()[0][0]
    return cursor.execute("SELECT value FROM profileOptions WHERE r_profile = {} AND r_searchOptionType = {};".format(profileID, defaultID)).fetchall()[0][0]

# Trigger CRUD Operations for year


def _addYears(profileID: int, years, cursor: sqlite3.Cursor):
    if len(years) != 0:
        valueList = ""
        defaultID = cursor.execute(
            "SELECT id FROM searchOptionType WHERE title = 'year';").fetchall()[0][0]
        for x in years:
            valueList = "('{}',{},{})".format(x, profileID, defaultID) if valueList == "" else "{},('{}',{},{})".format(
                valueList, x, profileID, defaultID)
        cursor.execute(
            "INSERT INTO profileOptions (value,r_profile,r_searchOptionType) VALUES {};".format(valueList))


def _getYears(profileID: int, cursor: sqlite3.Cursor):
    defaultID = cursor.execute(
        "SELECT id FROM searchOptionType WHERE title = 'year';").fetchall()[0][0]
    tempList = cursor.execute("SELECT value FROM profileOptions WHERE r_profile = {} AND r_searchOptionType = {};".format(
        profileID, defaultID)).fetchall()
    returnList = []
    for x in tempList:
        returnList.append(x[0])
    return returnList

# Trigger CRUD Operations for rating


def _addRating(profileID: int, rating, cursor: sqlite3.Cursor):
    if len(rating) != 0:
        valueList = ""
        defaultID = cursor.execute(
            "SELECT id FROM searchOptionType WHERE title = 'rating';").fetchall()[0][0]
        for x in rating:
            valueList = "('{}',{},{})".format(x, profileID, defaultID) if valueList == "" else "{},('{}',{},{})".format(
                valueList, x, profileID, defaultID)
        cursor.execute(
            "INSERT INTO profileOptions (value,r_profile,r_searchOptionType) VALUES {};".format(valueList))


def _getRating(profileID: int, cursor: sqlite3.Cursor):
    defaultID = cursor.execute(
        "SELECT id FROM searchOptionType WHERE title = 'rating';").fetchall()[0][0]
    tempList = cursor.execute("SELECT value FROM profileOptions WHERE r_profile = {} AND r_searchOptionType = {};".format(
        profileID, defaultID)).fetchall()
    returnList = []
    for x in tempList:
        returnList.append(x[0])
    return returnList

# Trigger CRUD Operations for media type


def _addMediaType(profileID: int, mediaType, cursor: sqlite3.Cursor):
    if len(mediaType) != 0:
        valueList = ""
        defaultID = cursor.execute(
            "SELECT id FROM searchOptionType WHERE title = 'mediaType';").fetchall()[0][0]
        for x in mediaType:
            valueList = "('{}',{},{})".format(x, profileID, defaultID) if valueList == "" else "{},('{}',{},{})".format(
                valueList, x, profileID, defaultID)
        cursor.execute(
            "INSERT INTO profileOptions (value,r_profile,r_searchOptionType) VALUES {};".format(valueList))


def _getMediaType(profileID: int, cursor: sqlite3.Cursor):
    defaultID = cursor.execute(
        "SELECT id FROM searchOptionType WHERE title = 'mediaType';").fetchall()[0][0]
    tempList = cursor.execute("SELECT value FROM profileOptions WHERE r_profile = {} AND r_searchOptionType = {};".format(
        profileID, defaultID)).fetchall()
    returnList = []
    for x in tempList:
        returnList.append(x[0])
    return returnList

# Trigger CRUD Operations for studios


def _addStudios(profileID: int, studios, cursor: sqlite3.Cursor):
    if len(studios) != 0:
        valueList = ""
        defaultID = cursor.execute(
            "SELECT id FROM searchOptionType WHERE title = 'studio';").fetchall()[0][0]
        for x in studios:
            valueList = "('{}',{},{})".format(x, profileID, defaultID) if valueList == "" else "{},('{}',{},{})".format(
                valueList, x, profileID, defaultID)
        cursor.execute(
            "INSERT INTO profileOptions (value,r_profile,r_searchOptionType) VALUES {};".format(valueList))


def _getStudios(profileID: int, cursor: sqlite3.Cursor):
    defaultID = cursor.execute(
        "SELECT id FROM searchOptionType WHERE title = 'studio';").fetchall()[0][0]
    tempList = cursor.execute("SELECT value FROM profileOptions WHERE r_profile = {} AND r_searchOptionType = {};".format(
        profileID, defaultID)).fetchall()
    returnList = []
    for x in tempList:
        returnList.append(x[0])
    return returnList

# Trigger CRUD Operations for Most Watched


def _addMostWatched(profileID: int, mostWatched, cursor: sqlite3.Cursor):
    defaultID = cursor.execute(
        "SELECT id FROM searchOptionType WHERE title = 'mostWatched';").fetchall()[0][0]
    cursor.execute("INSERT INTO profileOptions (value,r_profile,r_searchOptionType) VALUES ('{}',{},{});".format(
        mostWatched, profileID, defaultID))


def _getMostWatched(profileID: int, cursor: sqlite3.Cursor) -> bool:
    defaultID = cursor.execute(
        "SELECT id FROM searchOptionType WHERE title = 'mostWatched';").fetchall()[0][0]
    return cursor.execute("SELECT value FROM profileOptions WHERE r_profile = {} AND r_searchOptionType = {};".format(profileID, defaultID)).fetchall()[0][0]

# Delete Functions


def _deleteAllOptions(profileID: int, cursor: sqlite3.Cursor):
    cursor.execute(
        "DELETE FROM profileOptions WHERE r_profile = {}".format(profileID))


def _deleteProfile(profileID: int, cursor: sqlite3.Cursor):
    cursor.execute("DELETE FROM profile WHERE id = {}".format(profileID))


def _getProfileOptions(profileID: int, cursor: sqlite3.Cursor) -> searchOptions.SearchOptions:
    profile = searchOptions.SearchOptions()

    # this will call a bunch of _get* functions to get the array of values for each property
    profile.setGenre(_getGenres(profileID, cursor))
    profile.setTag(_getTags(profileID, cursor))
    profile.setCast(_getCast(profileID, cursor))
    profile.setDirector(_getDirector(profileID, cursor))
    profile.setInclude(_getIncludes(profileID, cursor))
    profile.setExclude(_getExcludes(profileID, cursor))
    profile.setWatchStatus(_getWatchStatus(profileID, cursor))
    profile.setMINLength(_getMinLength(profileID, cursor))
    profile.setMAXLength(_getMaxLength(profileID, cursor))
    profile.setYear(_getYears(profileID, cursor))
    profile.setRating(_getRating(profileID, cursor))
    profile.setMediaType(_getMediaType(profileID, cursor))
    profile.setStudio(_getStudios(profileID, cursor))
    profile.setMostWatched(_getMostWatched(profileID, cursor))

    return profile

# test cases


def unitTest(options: searchOptions.SearchOptions):

    addProfile('dustin', options)
    print('Profile Added')

    testProfile = getProfile('dustin')
    print("Get Profile: {}".format(testProfile))

    removeProfile('dustin')
    print('Profile Deleted')
