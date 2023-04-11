# imports may not be needed

class SearchOptions:

    def __init__(self):  # when object created
        self.genre = []
        self.tag = []
        self.cast = []
        self.director = []
        self.include = []
        self.exclude = []
        self.watchStatus = []
        self.length = [0, 0] # time based in seconds
        self.year = []
        self.rating = []
        self.mediaType = ['movie', 'episode']
        self.studio = []
        self.mostWatched = False
        self.function = 0  # possible options: 1 = playOne, 2 = showList, 3 = loopPlay

    # genre functions
    def getGenre(self):
        return self.genre

    def setGenre(self, newGenre):
        self.genre = newGenre

    def addGenre(self, genreName):
        self.genre.append(genreName)

    def removeGenre(self, genreName):
        self.genre.remove(genreName)

    # tag functions
    def getTag(self):
        return self.tag

    def setTag(self, newTag):
        self.tag = newTag

    def addTag(self, tagName):
        self.tag.append(tagName)

    def removeTag(self, tagName):
        self.tag.remove(tagName)

    # cast functions
    def getCast(self):
        return self.cast

    def setCast(self, newCast):
        self.cast = newCast

    def addCast(self, castName):
        self.cast.append(castName)

    def removeCast(self, castName):
        self.cast.remove(castName)

    # director functions
    def getDirector(self):
        return self.director

    def setDirector(self, newDirector):
        self.director = newDirector

    def addDirector(self, directorName):
        self.director.append(directorName)

    def removeDirector(self, directorName):
        self.director.remove(directorName)

    # include functions
    def getInclude(self):
        return self.include

    def setInclude(self, newInclude):
        self.include = newInclude

    def addInclude(self, includeID):
        self.include.append(includeID)

    def removeInclude(self, includeID):
        self.include.remove(includeID)

    # exclude functions
    def getExclude(self):
        return self.exclude

    def setExclude(self, newExclude):
        self.exclude = newExclude

    def addExclude(self, excludeID):
        self.exclude.append(excludeID)

    def removeExclude(self, excludeID):
        self.exclude.remove(excludeID)

    # watchStatus functions
    def getWatchStatus(self):
        return self.watchStatus

    def setWatchStatus(self, newWatchStatus):
        self.watchStatus = newWatchStatus

    def addWatchStatus(self, watchStatusVal):
        self.watchStatus.append(watchStatusVal)

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

# Unit Test Cases


def unitTest():
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
    testCase.setInclude([3, 5, 7])
    testCase.addInclude(1)
    testCase.removeInclude(3)
    print(testCase.getInclude())

    # Exclude Testing
    print('Exclude')
    testCase.setExclude([3, 5, 7])
    testCase.addExclude(1)
    testCase.removeExclude(3)
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
    testCase.setMINLength(10)
    testCase.setMAXLength(1258)
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
    testCase.setPBFunction(2)
    print(testCase.getPBFunction())

    return testCase