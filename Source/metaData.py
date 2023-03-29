import sqlite3
import os
import xbmcaddon

########
## This section doesnt work
addon = xbmcaddon.Addon()
videoDB = addon.getAddonInfo('path').replace("addons\\video.kodi.episode.selector\\", "userdata\\Database\\MyVideos121.db")

def getMetaData(dataType):
    connection = sqlite3.connect(videoDB)
    cursor = connection.cursor()

    query = "SELECT * FROM {}".format(dataType)
    cursor.execute(query)
    returnList = cursor.fetchall()

    connection.commit()
    connection.close()
    print(returnList)
    return 'Success!'

def testMetaData():
    print("Testing Actors: {}".format(getMetaData("actor")))
    print("Testing Genre: {}".format(getMetaData("genre")))
    print("Testing Studio: {}".format(getMetaData("studio")))
    print("Testing Tags: {}".format(getMetaData("tag")))

#this is the unit test for the getMetaData function
#testMetaData()

#######

def getActors():
    actors = xbmc.execcuteJSONRPC('{"jsonrpc": "2.0", "method": ""}')
    return actors

def getDirectors():
    return []

def getTags():
    return 

def getGenres():
    return []