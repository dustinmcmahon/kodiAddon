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
    print("Testing Meta Data Functions")
    print("Testing Actors: {}".format(getActors()))
    print("Testing Directors: {}".format(getDirectors()))
    print("Testing Genre: {}".format(getGenres()))
    print("Testing Studio: {}".format(getStudios()))
    print("Testing Tags: {}".format(getTags()))
    print("Testing Ratings: {}".format(getRatings()))
    print("Testing Years: {}".format(getYears()))
    print("Testing Movies: {}".format(getMovies()))


# get all of the actors in the system
# [(id, name)...]
def getActors():
    connection = sqlite3.connect(videoDB)
    actors = connection.cursor().execute(
        'SELECT actor_id, name FROM actor').fetchall()
    connection.commit()
    connection.close()
    return actors

# get into about a single actor by using their ID
# [(name)...]


def getActor(actorID):
    connection = sqlite3.connect(videoDB)
    name = connection.cursor().execute(
        'SELECT name FROM actor WHERE actor_id = {}'.format(actorID)).fetchall()
    connection.commit()
    connection.close()
    return name

# get the role of an actor give an actor id and media id


def getActorRole(actorID, mediaID):
    connection = sqlite3.connect(videoDB)
    role = connection.cursor().execute(
        'SELECT role FROM actor_link WHERE actor_id = {} AND media_id = {}'.format(actorID, mediaID)).fetchall()
    connection.commit()
    connection.close()
    return role

# get a list of directors
# [(id,name)...]


def getDirectors():
    connection = sqlite3.connect(videoDB)
    directors = connection.cursor().execute(
        'SELECT DISTINCT actor.actor_id,actor.name FROM director_link LEFT JOIN actor ON director_link.actor_id = actor.actor_id').fetchall()
    connection.commit()
    connection.close()
    return directors

# get a list of genres
# [(id,title)...]


def getGenres():
    connection = sqlite3.connect(videoDB)
    genres = connection.cursor().execute('SELECT * FROM genre').fetchall()
    connection.commit()
    connection.close()
    return genres

# get a list of studios
# [(id, name)...]


def getStudios():
    connection = sqlite3.connect(videoDB)
    studios = connection.cursor().execute('SELECT * FROM studio').fetchall()
    connection.commit()
    connection.close()
    return studios

# get a list of tags
# [(id, name)...]


def getTags():
    connection = sqlite3.connect(videoDB)
    tags = connection.cursor().execute('SELECT * FROM tag').fetchall()
    connection.commit()
    connection.close()
    return tags

# get a list of ratings from the movies
# [(rating)]


def getRatings():
    connection = sqlite3.connect(videoDB)
    ratings = connection.cursor().execute(
        'SELECT DISTINCT c12 FROM movie').fetchall()
    connection.commit()
    connection.close()
    return ratings

# get a list of years from the movies
# [(year)]


def getYears():
    connection = sqlite3.connect(videoDB)
    years = connection.cursor().execute('SELECT premiered FROM movie').fetchall()
    connection.commit()
    connection.close()
    result = []
    for x in years:
        if (result.count(x) == 0):
            result.append(x)
    return result

# geta list of movies
# [(id, title)...]


def getMovies():
    connection = sqlite3.connect(videoDB)
    movies = connection.cursor().execute('SELECT idMovie,c00 FROM movie').fetchall()
    connection.commit()
    connection.close()
    return movies
