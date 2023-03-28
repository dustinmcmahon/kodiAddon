import sqlite3
import xbmcaddon

addon = xbmcaddon.Addon()
addonPath = addon.getAddonInfo('path')

def createDB():
    connection = sqlite3.connect("{}\kesProfile.db".format(addonPath))
    cursor = connection.cursor()
    createTables(cursor)

def createTables(cursor: sqlite3.Cursor):
    cursor.executescript("""
        BEGIN;
        CREATE TABLE IF NOT EXISTS profile(id INTEGER, name TEXT, dateUsedLast date, timeUsedLast timestamp);
        CREATE TABLE IF NOT EXISTS searchOption(id INTEGER, title TEXT);
        CREATE TABLE IF NOT EXISTS profileOptions(id INTEGER, r_profile INTEGER, r_searchOption INTEGER, value);
        COMMIT;
    """)