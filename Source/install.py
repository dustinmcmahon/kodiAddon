import sqlite3
import os
import xbmc
import xbmcaddon

addon = xbmcaddon.Addon()
if xbmc.getCondVisibility('system.platform.windows'):
    addonDataFolder = addon.getAddonInfo('path').replace("addons\\video.kodi.episode.selector\\", "userdata\\addon_data\\video.kodi.episode.selector\\")
if xbmc.getCondVisibility('system.platform.osx'):
    addonDataFolder = addon.getAddonInfo('path').replace("addons/video.kodi.episode.selector/", "userdata/addon_data/video.kodi.episode.selector/")

def install():
    if not os.path.exists(addonDataFolder):
        #create folder for addon data
        os.mkdir(addonDataFolder)
    if not os.path.exists("{}\kesProfile.db".format(addonDataFolder)):
        createDB()

def createDB():
    connection = sqlite3.connect("{}\kesProfile.db".format(addonDataFolder))
    cursor = connection.cursor()
    createTables(cursor)
    fillTable(cursor)

def createTables(cursor: sqlite3.Cursor):
    cursor.executescript("""
        BEGIN;
        CREATE TABLE IF NOT EXISTS profile(id INTEGER PRIMARY KEY, name TEXT, dateUsedLast date, timeUsedLast timestamp);
        CREATE TABLE IF NOT EXISTS searchOptionDefaults(id INTEGER PRIMARY KEY, title TEXT UNIQUE ON CONFLICT IGNORE);
        CREATE TABLE IF NOT EXISTS profileOptions(id INTEGER PRIMARY KEY, r_profile INTEGER REFERENCES profile(id), r_searchOptionDefault INTEGER REFERENCES searchOptionDefaults(id), value);
        COMMIT;
    """)

def fillTable(cursor: sqlite3.Cursor):
    cursor.executescript("""
        BEGIN;
        INSERT OR IGNORE INTO searchOptionDefaults (title) values ('mediaType'),('watchStatus'),('tag'),('length'),('studio'),('mostWatched'),('genre'),('rating'),('cast'),('year'),('director');
        COMMIT;
    """)

def uninstall():
    if not os.path.exists("{}\kesProfile.db".format(addonDataFolder)):
        os.remove("{}\kesProfile.db".format(addonDataFolder))