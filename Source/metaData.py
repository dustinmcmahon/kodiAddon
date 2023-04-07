import sqlite3
import os
import xbmc
import xbmcaddon

########
# This section doesnt work
addon = xbmcaddon.Addon()
if xbmc.getCondVisibility('system.platform.windows'):
    videoDB = addon.getAddonInfo('path').replace(
        "addons\\video.kodi.episode.selector\\", "userdata\\Database\\MyVideos121.db")
if xbmc.getCondVisibility('system.platform.osx'):
    videoDB = addon.getAddonInfo('path').replace(
        "addons/video.kodi.episode.selector/", "userdata/Database/MyVideos121.db")


def getMetaData(dataType):
    connection = sqlite3.connect(videoDB)
    cursor = connection.cursor()

    query = "SELECT * FROM {}".format(dataType)
    cursor.execute(query)
    returnList = cursor.fetchall()

    connection.commit()
    connection.close()
    return returnList

# unit test for functions


def testMetaData():
    print("Testing Actors: {}".format(getActors()))
    print("Testing Directors: {}".format(getDirectors()))
    print("Testing Genre: {}".format(getGenres()))
    print("Testing Studio: {}".format(getStudios()))
    print("Testing Tags: {}".format(getTags()))


def getActors():
    connection = sqlite3.connect(videoDB)
    actors = connection.cursor().execute(
        'SELECT actor_id, name FROM actor').fetchall()
    connection.commit()
    connection.close()
    return actors


def getActor(actorID):
    connection = sqlite3.connect(videoDB)
    name = connection.cursor().execute(
        'SELECT name FROM actor WHERE actor_id = {}'.format(actorID)).fetchall()
    connection.commit()
    connection.close()
    return name


def getActorRole(actorID, mediaID):
    connection = sqlite3.connect(videoDB)
    role = connection.cursor().execute(
        'SELECT role FROM actor_link WHERE actor_id = {} AND media_id = {}'.format(actorID, mediaID)).fetchall()
    connection.commit()
    connection.close()
    return role


def getDirectors():
    connection = sqlite3.connect(videoDB)
    directors = connection.cursor().execute(
        'SELECT actor.actor_id,actor.name FROM director_link LEFT JOIN actor ON director_link.actor_id = actor.actor_id').fetchall()
    connection.commit()
    connection.close()
    return directors


def getGenres():
    connection = sqlite3.connect(videoDB)
    genres = connection.cursor().execute('SELECT * FROM genre').fetchall()
    connection.commit()
    connection.close()
    return genres


def getStudios():
    connection = sqlite3.connect(videoDB)
    studios = connection.cursor().execute('SELECT * FROM studio').fetchall()
    connection.commit()
    connection.close()
    return studios


def getTags():
    connection = sqlite3.connect(videoDB)
    tags = connection.cursor().execute('SELECT * FROM tag').fetchall()
    connection.commit()
    connection.close()
    return tags
