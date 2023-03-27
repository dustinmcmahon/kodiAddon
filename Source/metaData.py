import sqlite3

########
## This section doesnt work

videoDB = "..\\userdata\\Database\\MyVideos121.db"

def getMetaData(dataType):
    connection = sqlite3.connect(videoDB)
    cursor = connection.cursor()

    query = "SELECT * FROM {}".format(dataType)
    cursor.execute(query)
    returnList = cursor.fetchall()

    connection.commit()
    connection.close()
    return returnList

def testMetaData():
    print("Testing Actors: {}".format(getMetaData("actor")))
    print("Testing Genre: {}".format(getMetaData("genre")))
    print("Testing Studio: {}".format(getMetaData("studio")))
    print("Testing Tags: {}".format(getMetaData("tag")))

#this is the unit test for the getMetaData function
#testMetaData()

#######

infoHolder = xbmc.InfoTagVideo()

def getActors():
    return []