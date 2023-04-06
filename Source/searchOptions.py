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
        self.length = [0, 0]
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

    def addGenre(self, genreID):
        self.genre.append(genreID)

    def removeGenre(self, genreID):
        self.genre.remove(genreID)

    # tag functions
    def getTag(self):
        return self.tag

    def setTag(self, newTag):
        self.tag = newTag

    def addTag(self, tagID):
        self.tag.append(tagID)

    def removeTag(self, tagID):
        self.tag.remove(tagID)

    # cast functions
    def getCast(self):
        return self.cast

    def setCast(self, newCast):
        self.cast = newCast

    def addCast(self, castID):
        self.cast.append(castID)

    def removeCast(self, castID):
        self.cast.remove(castID)

    # director functions
    def getDirector(self):
        return self.director

    def setDirector(self, newDirector):
        self.director = newDirector

    def addDirector(self, directorID):
        self.director.append(directorID)

    def removeDirector(self, directorID):
        self.director.remove(directorID)

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

    def addStudio(self, studioID):
        self.studio.append(studioID)

    def removeStudio(self, studioID):
        self.studio.remove(studioID)

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
    testCase.setGenre([3, 5, 7])
    testCase.addGenre(1)
    testCase.removeGenre(3)
    print(testCase.getGenre())

    # Tag Testing
    print('Tag')
    testCase.setTag([3, 5, 7])
    testCase.addTag(1)
    testCase.removeTag(3)
    print(testCase.getTag())

    # Cast Testing
    print('Cast')
    testCase.setCast([3, 5, 7])
    testCase.addCast(1)
    testCase.removeCast(3)
    print(testCase.getCast())

    # Director Testing
    print('Director')
    testCase.setDirector([3, 5, 7])
    testCase.addDirector(1)
    testCase.removeDirector(3)
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
    print('Length')
    testCase.setMINLength(10)
    testCase.setMAXLength(1258)
    print(testCase.getLength())

    # Year Testing
    print('Year')
    testCase.setYear([3, 5, 7])
    testCase.addYear(1)
    testCase.removeYear(3)
    print(testCase.getYear())

    # Rating Testing
    print('Rating')
    testCase.setRating([3, 5, 7])
    testCase.addRating(1)
    testCase.removeRating(3)
    print(testCase.getRating())

    # Media Type Testing
    print('Media Type')
    print(testCase.getMediaType())
    testCase.removeMediaType('episode')
    print(testCase.getMediaType())

    # Studio Testing
    print('Studio')
    testCase.setStudio([3, 5, 7])
    testCase.addStudio(1)
    testCase.removeStudio(3)
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