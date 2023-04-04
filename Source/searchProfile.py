import sqlite3
import os
import xbmc
import xbmcaddon
import searchOptions

addon = xbmcaddon.Addon()
if xbmc.getCondVisibility('system.platform.windows'):
    addonDataFolder = addon.getAddonInfo('path').replace("addons\\video.kodi.episode.selector\\", "userdata\\addon_data\\video.kodi.episode.selector\\")
if xbmc.getCondVisibility('system.platform.osx'):
    addonDataFolder = addon.getAddonInfo('path').replace("addons/video.kodi.episode.selector/", "userdata/addon_data/video.kodi.episode.selector/")
kesDBPath = "{}kesProfile.db".format(addonDataFolder)

def install():
    if not os.path.exists(addonDataFolder):
        #create folder for addon data
        os.mkdir(addonDataFolder)
    if not os.path.exists(kesDBPath):
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

def addProfile(name: str, options: searchOptions):
    connection = sqlite3.connect(kesDBPath)
    cursor = connection.cursor()
    profiles = cursor.execute("SELECT id FROM profile WHERE name = '{}';".format(name)).fetchall()
    if len(profiles) == 0:
        profiles = _insertProfile(name)
    profileID = profiles[0].id
    _addOptions(profileID, options)

def _insertProfile(name: str):
    connection = sqlite3.connect(kesDBPath)
    cursor = connection.cursor()
    return cursor.execute("INSERT INTO profile (name) VALUES ({}) RETURNING id;".format(name)).fetchall()

# Trigger CRUD Operations for all options
def _addOptions(profileID: int, options: searchOptions):
    _addGenres(profileID, options.getGenre())
    _addTags(profileID, options.getTag())
    _addCast(profileID, options.getCast())
    _addDirector(profileID, options.getDirector())
    _addIncludes(profileID, options.getInclude())
    _addExcludes(profileID, options.getExclude())
    _addWatchStatus(profileID, options.getWatchStatus())
    _addLength(profileID, options.getLength())
    _addYears(profileID, options.getYear())
    _addRating(profileID, options.getRating())
    _addMediaType(profileID, options.getMediaType)
    _addStudios(profileID, options.getStudio)
    _addMostWatched(profileID, options.getMostWatched)

# Trigger CRUD Operations for genre
def _addGenres(profileID: int, genres):
    return True

# Trigger CRUD Operations for tags
def _addTags(profileID: int, tags):
    return True

# Trigger CRUD Operations for cast
def _addCast(profileID: int, cast):
    return True

# Trigger CRUD Operations for director
def _addDirector(profileID: int, director):
    return True

# Trigger CRUD Operations for include list
def _addIncludes(profileID: int, includes):
    return True

# Trigger CRUD Operations for exclude list
def _addExcludes(profileID: int, exludes):
    return True

# Trigger CRUD Operations for Watch Status
def _addWatchStatus(profileID: int, watchStatus):
    return True

# Trigger CRUD Operations for length
def _addLength(profileID: int, length):
    return True

# Trigger CRUD Operations for year
def _addYears(profileID: int, years):
    return True

# Trigger CRUD Operations for rating
def _addRating(profileID: int, rating):
    return True

# Trigger CRUD Operations for media type
def _addMediaType(profileID: int, mediaType):
    return True

# Trigger CRUD Operations for studios
def _addStudios(profileID: int, studios):
    return True

# Trigger CRUD Operations for Most Watched
def _addMostWatched(profileID: int, mostWatched):
    return True

# test cases
def unitTest():
    options = searchOptions()
    addProfile('dustin', options)