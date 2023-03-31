#imports may not be needed

class SearchOptions:

    def __init__(self):  #   when object created
        self.genre = []
        self.tag = []
        self.cast = []
        self.director = []
        self.include = []
        self.exclude = []
        self.watchStatus = []
        self.length = []
        self.year = []
        self.rating = []
        self.mediaType = ['movie', 'episode']
        self.studio = []
        self.mostWatched = False

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

# Unit Test Cases
def unitTest():
    testCase = SearchOptions()
    testCase.setCast(1)