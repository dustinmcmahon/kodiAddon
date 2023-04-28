# imports may not be needed

"""class SearchOptions:

    def __init__(self):  # when object created
        self.genre = [] # this is a list of genre names
        self.tag = [] # this is a list of tag names
        self.cast = [] # this is a list of names
        self.director = [] # this is a list of director names
        self.include = [] # list of movie names
        self.exclude = [] # list of movie names
        self.watchStatus = [] # list of ints [0,1] 0 = unwatched, 1 = watched
        self.length = [0, 0]  # time based in seconds
        self.year = [] # this is a list of years
        self.rating = [] # this is a list of ratings
        self.mediaType = ['movie', 'episode'] # these are the two options
        self.studio = [] # this is a list of studio names
        self.mostWatched = False
        self.function = 0  # possible options: 1 = playOne, 2 = showList, 3 = loopPlay
        self.shutTime = [0, 0]  # time in hour and min

    def __str__(self) -> str:
        return f"genre: {self.genre}\ntag: {self.tag}\ncast: {self.cast}\ndirector: {self.director}\ninclude: {self.include}\nexclude: {self.exclude}\nwatchStatus: {self.watchStatus}\nlength: {self.length}\nyear: {self.year}\nrating: {self.rating}\nmediaType: {self.mediaType}\nstudio: {self.studio}\nmostWatched: {self.mostWatched}\nPB Func: {self.function}\n"

    # genre functions
    # get current genres
    def getGenre(self):
        return self.genre

    # set the genre
    ## newGenre should be a list
    def setGenre(self, newGenre):
        self.genre = newGenre

    # add a genre to the list
    ## genreName should be a string
    def addGenre(self, genreName):
        self.genre.append(genreName)

    # remove a genre
    ## genreName should be a string
    def removeGenre(self, genreName):
        self.genre.remove(genreName)

    # tag functions
    # get current tags
    def getTag(self):
        return self.tag

    # set the tags
    ## newTag should be a list of tags
    def setTag(self, newTag):
        self.tag = newTag

    # add a tag to the list
    ## tagName should be a string
    def addTag(self, tagName):
        self.tag.append(tagName)
    # remove a tag
    ## tagName should be a string
    def removeTag(self, tagName):
        self.tag.remove(tagName)

    # cast functions
    # get current cast
    def getCast(self):
        return self.cast

    # set the case
    ## newCast is a list of actors
    def setCast(self, newCast):
        self.cast = newCast

    # add a case member to the list
    ## castName should be a string
    def addCast(self, castName):
        self.cast.append(castName)

    # remove a cast member from the list
    ## castName should be a string
    def removeCast(self, castName):
        self.cast.remove(castName)

    # director functions
    # get the director
    def getDirector(self):
        return self.director

    # set the director
    ## newDirector should be a list of director names
    def setDirector(self, newDirector):
        self.director = newDirector

    # add director to the list
    ## directorName should be a string
    def addDirector(self, directorName):
        self.director.append(directorName)

    # remove a director from the list
    ## directorName should be a string
    def removeDirector(self, directorName):
        self.director.remove(directorName)

    # include functions
    # get the include list
    def getInclude(self):
        return self.include

    # set the include list
    ## newInclude should be a list of video titles
    def setInclude(self, newInclude):
        self.include = newInclude

    # add a video to the include list
    ## videoName should be a string
    def addInclude(self, videoName):
        self.include.append(videoName)

    # remove a video from the include list
    ## videoName should be a string
    def removeInclude(self, videoName):
        self.include.remove(videoName)

    # exclude functions
    # get the exclude list
    def getExclude(self):
        return self.exclude

    # set the exclude list
    ## new Exclude should be a list of video titles
    def setExclude(self, newExclude):
        self.exclude = newExclude

    # add to the exclude list
    ## videoName should be a string
    def addExclude(self, videoName):
        self.exclude.append(videoName)

    # remove from the exclude list
    ## videoName should be a string
    def removeExclude(self, videoName):
        self.exclude.remove(videoName)

    # watchStatus functions
    # get the watch status
    def getWatchStatus(self):
        return self.watchStatus

    # set the watch status
    # should be an array of 0 and or 1
    def setWatchStatus(self, newWatchStatus):
        self.watchStatus = newWatchStatus

    # add a watch status
    ## watchStatusVal should be an int (0,1)
    def addWatchStatus(self, watchStatusVal):
        self.watchStatus.append(watchStatusVal)

    # remove a watch status
    ## watchStatusVal should be an int (0,1)
    def removeWatchStatus(self, watchStatusVal):
        self.watchStatus.remove(watchStatusVal)

    # length functions
    # ['min_length', 'max_length']
    def getLength(self):
        return self.length

    # set to 0 to ignore min
    def setMINLength(self, lengthVal):
        self.length[0] = lengthVal

    # set to 0 to ignore max
    def setMAXLength(self, lengthVal):
        self.length[1] = lengthVal

    # year functions
    def getYear(self):
        return self.year

    def setYear(self, newYear):
        self.year = newYear

    def addYear(self, yearID):
        self.year.append(yearID)

    def removeYear(self, yearID):
        self.year.remove(yearID)

    # rating functions
    def getRating(self):
        return self.rating

    def setRating(self, newRating):
        self.rating = newRating

    def addRating(self, ratingVal):
        self.rating.append(ratingVal)

    def removeRating(self, ratingVal):
        self.rating.remove(ratingVal)

    # mediaType functions
    def getMediaType(self):
        return self.mediaType

    def setMediaType(self, newMediaType):
        self.mediaType = newMediaType

    def addMediaType(self, type):
        self.mediaType.append(type)

    def removeMediaType(self, type):
        self.mediaType.remove(type)

    # studio functions
    def getStudio(self):
        return self.studio

    def setStudio(self, newStudio):
        self.studio = newStudio

    def addStudio(self, studioName):
        self.studio.append(studioName)

    def removeStudio(self, studioName):
        self.studio.remove(studioName)

    # mostWatched functions
    def getMostWatched(self):
        return self.mostWatched

    def setMostWatched(self, value):
        self.mostWatched = value

    # Playback Functions
    def setPBFunction(self, value):
        self.function = value

    def getPBFunction(self):
        return self.function

    # Shutdowm time
    def getShutTime(self):
        return self.shutTime

    def setHours(self, hoursVal):
        self.shutTime[0] = hoursVal

    def setMins(self, minsVal):
        self.shutTime[1] = minsVal

# Unit Test Cases

# create a set of search options to test episodes


def unitTestEpisode():

    testCase = SearchOptions()
    testCase.setCast(['Atsushi Tamaru', 'Tadashi Miyazawa', 'Kousuke Toriumi'])
    testCase.setExclude(
        ["The Apocalypse", "The Battle of Loka", "The Depths of Palm", "Escape"])
    testCase.setGenre(['Science Fiction', 'Fantasy', 'Drama'])
    testCase.setTag(['fighting'])
    testCase.setInclude(["The Chou Family's Secret?", "Master and Servant",
                        "Lie", "Chaos", "Welcome to Express Delivery"])
    testCase.setMINLength(1300)
    testCase.setMAXLength(1600)
    testCase.setStudio(['Tencent Video'])
    testCase.setRating([])
    testCase.setDirector([])
    testCase.setWatchStatus([0, 1])
    testCase.setYear(['2016', '2017', '2018', '2019', '2020', '2021', '2022'])
    testCase.setMediaType(['episode'])
    testCase.setPBFunction(3)
    testCase.setMostWatched(False)
    testCase.setHours(18)
    testCase.setMins(47)

    return testCase

# full test with add and remove


def unitTestMovie():
    testCase = SearchOptions()

    # Genre Testing
    print('Genre')
    testCase.setGenre(['comedy', 'fantasy', 'crime'])
    testCase.addGenre('adventure')
    testCase.removeGenre('crime')
    print(testCase.getGenre())

    # Tag Testing
    print('Tag')
    testCase.setTag(['frozen', 'princess', 'cartoon'])
    testCase.addTag('winter')
    testCase.removeTag('cartoon')
    print(testCase.getTag())

    # Cast Testing
    print('Cast')
    testCase.setCast(['Idina Mendzel', 'Kristen Bell', 'Tom Cruise'])
    testCase.addCast('Josh Gad')
    testCase.removeCast('Tom Cruise')
    print(testCase.getCast())

    # Director Testing
    print('Director')
    testCase.setDirector(['Allison Schroeder', 'Jon Watts'])
    testCase.addDirector('Jennifer Lee')
    testCase.removeDirector('Jon Watts')
    print(testCase.getDirector())

    # Include Testing
    print('Include')
    testCase.setInclude(["Long Shot", "Frozen II"])
    testCase.addInclude("Frozen")
    testCase.removeInclude("Long Shot")
    print(testCase.getInclude())

    # Exclude Testing
    print('Exclude')
    testCase.setExclude(["Rise of the Guardians", "Fantastic Beasts: The Crimes of Grindelwald",
                        "Fantastic Beasts: The Secrets of Dumbledore", "Fantastic Beasts and Where to Find Them", "Frozen"])
    testCase.addExclude("Long Shot")
    testCase.removeExclude("Frozen")
    print(testCase.getExclude())

    # Watch Status Testing
    print('Watch Status')
    testCase.setWatchStatus([0])
    print('Set Status: {}'.format(testCase.getWatchStatus()))
    testCase.addWatchStatus(1)
    print('Add Status: {}'.format(testCase.getWatchStatus()))
    testCase.removeWatchStatus(0)
    print('Remove Status: {}'.format(testCase.getWatchStatus()))

    # Length Testing
    # Length of time in seconds
    print('Length')
    testCase.setMINLength(6100)
    testCase.setMAXLength(6200)
    print(testCase.getLength())

    # Year Testing
    print('Year')
    testCase.setYear(['2019', '2022', '1945'])
    testCase.addYear('1999')
    testCase.removeYear('1945')
    print(testCase.getYear())

    # Rating Testing
    print('Rating')
    testCase.setRating(["Rated R"])
    testCase.addRating("Rated PG")
    testCase.removeRating("Rated R")
    print(testCase.getRating())

    # Media Type Testing
    print('Media Type')
    print(testCase.getMediaType())
    testCase.removeMediaType('episode')
    print(testCase.getMediaType())

    # Studio Testing
    print('Studio')
    testCase.setStudio(['Universal'])
    testCase.addStudio('Walt Disney Pictures')
    testCase.removeStudio('Universal')
    print(testCase.getStudio())

    # Most Watched Testing
    print('Most Watched')
    print(testCase.getMostWatched())
    testCase.setMostWatched(True)
    print(testCase.getMostWatched())

    # Function Testing
    print('Playback Functions')
    testCase.setPBFunction(3)
    print(testCase.getPBFunction())

    # Function Testing
    print('shutTime')
    testCase.setHours(18)
    testCase.setMins(47)
    print(testCase.getShutTime())

    return testCase"""


# imports may not be needed

class SearchOptions:

    def __init__(self):  # when object created
        self.genre = []  # this is a list of genre names
        self.tag = []  # this is a list of tag names
        self.cast = []  # this is a list of names
        self.director = []  # this is a list of director names
        self.include = []  # list of movie names
        self.exclude = []  # list of movie names
        self.watchStatus = []  # list of ints [0,1] 0 = unwatched, 1 = watched
        self.length = [0, 0]  # time based in seconds
        self.year = []  # this is a list of years
        self.rating = []  # this is a list of ratings
        self.mediaType = ['movie', 'episode']  # these are the two options
        self.studio = []  # this is a list of studio names
        self.mostWatched = False
        self.function = 0  # possible options: 1 = playOne, 2 = showList, 3 = loopPlay
        self.shutTime = [0, 0]  # time in hour and min

    def __str__(self) -> str:
        return f"genre: {self.genre}\ntag: {self.tag}\ncast: {self.cast}\ndirector: {self.director}\ninclude: {self.include}\nexclude: {self.exclude}\nwatchStatus: {self.watchStatus}\nlength: {self.length}\nyear: {self.year}\nrating: {self.rating}\nmediaType: {self.mediaType}\nstudio: {self.studio}\nmostWatched: {self.mostWatched}\nPB Func: {self.function}\n"

    # genre functions
    # get current genres
    def getGenre(self):
        return self.genre

    # set the genre
    # newGenre should be a list
    def setGenre(self, newGenre):
        self.genre = newGenre

    # add a genre to the list
    # genreName should be a string
    def addGenre(self, genreName):
        self.genre.append(genreName)

    # remove a genre
    # genreName should be a string
    def removeGenre(self, genreName):
        self.genre.remove(genreName)

    # tag functions
    # get current tags
    def getTag(self):
        return self.tag

    # set the tags
    # newTag should be a list of tags
    def setTag(self, newTag):
        self.tag = newTag

    # add a tag to the list
    # tagName should be a string
    def addTag(self, tagName):
        self.tag.append(tagName)
    # remove a tag
    # tagName should be a string

    def removeTag(self, tagName):
        self.tag.remove(tagName)

    # cast functions
    # get current cast
    def getCast(self):
        return self.cast

    # set the case
    # newCast is a list of actors
    def setCast(self, newCast):
        self.cast = newCast

    # add a case member to the list
    # castName should be a string
    def addCast(self, castName):
        self.cast.append(castName)

    # remove a cast member from the list
    # castName should be a string
    def removeCast(self, castName):
        self.cast.remove(castName)

    # director functions
    # get the director
    def getDirector(self):
        return self.director

    # set the director
    # newDirector should be a list of director names
    def setDirector(self, newDirector):
        self.director = newDirector

    # add director to the list
    # directorName should be a string
    def addDirector(self, directorName):
        self.director.append(directorName)

    # remove a director from the list
    # directorName should be a string
    def removeDirector(self, directorName):
        self.director.remove(directorName)

    # include functions
    # get the include list
    def getInclude(self):
        return self.include

    # set the include list
    # newInclude should be a list of video titles
    def setInclude(self, newInclude):
        self.include = newInclude

    # add a video to the include list
    # videoName should be a string
    def addInclude(self, videoName):
        self.include.append(videoName)

    # remove a video from the include list
    # videoName should be a string
    def removeInclude(self, videoName):
        self.include.remove(videoName)

    # exclude functions
    # get the exclude list
    def getExclude(self):
        return self.exclude

    # set the exclude list
    # new Exclude should be a list of video titles
    def setExclude(self, newExclude):
        self.exclude = newExclude

    # add to the exclude list
    # videoName should be a string
    def addExclude(self, videoName):
        self.exclude.append(videoName)

    # remove from the exclude list
    # videoName should be a string
    def removeExclude(self, videoName):
        self.exclude.remove(videoName)

    # watchStatus functions
    # get the watch status
    def getWatchStatus(self):
        return self.watchStatus

    # set the watch status
    # should be an array of 0 and or 1
    def setWatchStatus(self, newWatchStatus):
        self.watchStatus = newWatchStatus

    # add a watch status
    # watchStatusVal should be an int (0,1)
    def addWatchStatus(self, watchStatusVal):
        self.watchStatus.append(watchStatusVal)

    # remove a watch status
    # watchStatusVal should be an int (0,1)
    def removeWatchStatus(self, watchStatusVal):
        self.watchStatus.remove(watchStatusVal)

    # length functions
    # ['min_length', 'max_length']
    def getLength(self):
        return self.length

    # set to 0 to ignore min
    def setMINLength(self, lengthVal):
        self.length[0] = lengthVal

    # set to 0 to ignore max
    def setMAXLength(self, lengthVal):
        self.length[1] = lengthVal

    # year functions
    def getYear(self):
        return self.year

    def setYear(self, newYear):
        self.year = newYear

    def addYear(self, yearID):
        self.year.append(yearID)

    def removeYear(self, yearID):
        self.year.remove(yearID)

    # rating functions
    def getRating(self):
        return self.rating

    def setRating(self, newRating):
        self.rating = newRating

    def addRating(self, ratingVal):
        self.rating.append(ratingVal)

    def removeRating(self, ratingVal):
        self.rating.remove(ratingVal)

    # mediaType functions
    def getMediaType(self):
        return self.mediaType

    def setMediaType(self, newMediaType):
        self.mediaType = newMediaType

    def addMediaType(self, type):
        self.mediaType.append(type)

    def removeMediaType(self, type):
        self.mediaType.remove(type)

    # studio functions
    def getStudio(self):
        return self.studio

    def setStudio(self, newStudio):
        self.studio = newStudio

    def addStudio(self, studioName):
        self.studio.append(studioName)

    def removeStudio(self, studioName):
        self.studio.remove(studioName)

    # mostWatched functions
    def getMostWatched(self):
        return self.mostWatched

    def setMostWatched(self, value):
        self.mostWatched = value

    # Playback Functions
    def setPBFunction(self, value):
        self.function = value

    def getPBFunction(self):
        return self.function

    # Shutdowm time
    def getShutTime(self):
        return self.shutTime

    def setHours(self, hoursVal):
        self.shutTime[0] = hoursVal

    def setMins(self, minsVal):
        self.shutTime[1] = minsVal

# Unit Test Cases

# create a set of search options to test episodes


def unitTestEpisode():

    testCase = SearchOptions()
    testCase.setCast(['Atsushi Tamaru', 'Tadashi Miyazawa', 'Kousuke Toriumi'])
    testCase.setExclude(
        ["The Apocalypse", "The Battle of Loka", "The Depths of Palm", "Escape"])
    testCase.setGenre(['Science Fiction', 'Fantasy', 'Drama'])
    testCase.setTag(['fighting'])
    testCase.setInclude(["The Chou Family's Secret?", "Master and Servant",
                        "Lie", "Chaos", "Welcome to Express Delivery"])
    testCase.setMINLength(1300)
    testCase.setMAXLength(1600)
    testCase.setStudio(['Tencent Video'])
    testCase.setRating([])
    testCase.setDirector([])
    testCase.setWatchStatus([0, 1])
    testCase.setYear(['2016', '2017', '2018', '2019', '2020', '2021', '2022'])
    testCase.setMediaType(['episode'])
    testCase.setPBFunction(3)
    testCase.setMostWatched(True)
    testCase.setHours(0)
    testCase.setMins(0)

    return testCase

# full test with add and remove


def unitTestMovie():
    testCase = SearchOptions()

    # Genre Testing
    print('Genre')
    testCase.setGenre(['comedy', 'fantasy', 'crime'])
    testCase.addGenre('adventure')
    testCase.removeGenre('crime')
    print(testCase.getGenre())

    # Tag Testing
    print('Tag')
    testCase.setTag(['frozen', 'princess', 'cartoon'])
    testCase.addTag('winter')
    testCase.removeTag('cartoon')
    print(testCase.getTag())

    # Cast Testing
    print('Cast')
    testCase.setCast(['Idina Mendzel', 'Kristen Bell', 'Tom Cruise'])
    testCase.addCast('Josh Gad')
    testCase.removeCast('Tom Cruise')
    print(testCase.getCast())

    # Director Testing
    print('Director')
    testCase.setDirector(['Allison Schroeder', 'Jon Watts'])
    testCase.addDirector('Jennifer Lee')
    testCase.removeDirector('Jon Watts')
    print(testCase.getDirector())

    # Include Testing
    print('Include')
    testCase.setInclude(["Long Shot", "Frozen II"])
    testCase.addInclude("Frozen")
    testCase.removeInclude("Long Shot")
    print(testCase.getInclude())

    # Exclude Testing
    print('Exclude')
    testCase.setExclude(["Rise of the Guardians", "Fantastic Beasts: The Crimes of Grindelwald",
                        "Fantastic Beasts: The Secrets of Dumbledore", "Fantastic Beasts and Where to Find Them", "Frozen"])
    testCase.addExclude("Long Shot")
    testCase.removeExclude("Frozen")
    print(testCase.getExclude())

    # Watch Status Testing
    print('Watch Status')
    testCase.setWatchStatus([0])
    print('Set Status: {}'.format(testCase.getWatchStatus()))
    testCase.addWatchStatus(1)
    print('Add Status: {}'.format(testCase.getWatchStatus()))
    testCase.removeWatchStatus(0)
    print('Remove Status: {}'.format(testCase.getWatchStatus()))

    # Length Testing
    # Length of time in seconds
    print('Length')
    testCase.setMINLength(6100)
    testCase.setMAXLength(6200)
    print(testCase.getLength())

    # Year Testing
    print('Year')
    testCase.setYear(['2019', '2022', '1945'])
    testCase.addYear('1999')
    testCase.removeYear('1945')
    print(testCase.getYear())

    # Rating Testing
    print('Rating')
    testCase.setRating(["Rated R"])
    testCase.addRating("Rated PG")
    testCase.removeRating("Rated R")
    print(testCase.getRating())

    # Media Type Testing
    print('Media Type')
    print(testCase.getMediaType())
    testCase.removeMediaType('episode')
    print(testCase.getMediaType())

    # Studio Testing
    print('Studio')
    testCase.setStudio(['Universal'])
    testCase.addStudio('Walt Disney Pictures')
    testCase.removeStudio('Universal')
    print(testCase.getStudio())

    # Most Watched Testing
    print('Most Watched')
    print(testCase.getMostWatched())
    testCase.setMostWatched(True)
    print(testCase.getMostWatched())

    # Function Testing
    print('Playback Functions')
    testCase.setPBFunction(3)
    print(testCase.getPBFunction())

    # Function Testing
    print('shutTime')
    testCase.setHours(0)
    testCase.setMins(0)
    print(testCase.getShutTime())

    return testCase
