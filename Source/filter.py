'''
' This is not completed Yet
' Tasks to be completed
' - filter functions for each field
' - get functions for media type
' - playback functions
'''

import xbmc
import json
import searchOptions

# {"field": name, "operator": "contains", "value": ["", "", ""]}
# {"field": name, "operator": "is", "value": ""}

def _filterList_(name,valueList):
    defaultReturn = {}
    if len(valueList) == 1:
        defaultReturn = {"operator": "is", "field": name, "value": valueList[0]}
    elif len(valueList) > 1:
        for x in valueList:
            if defaultReturn == {}:
                defaultReturn = []
            defaultReturn.append(x)
        defaultReturn = {"operator": "contains", "field": name, "value": defaultReturn}
    return defaultReturn

def _filterIncExc(videoList, inList, exList):
    returnList = []
    if (len(inList) < len(exList)):
        for x in inList:
            for y in videoList:
                if (x == y['title']):
                    returnList.append(y)
    else:
        for x in exList:
            for y in videoList:
                if(x == y['title']):
                    videoList.remove(y)
        returnList = videoList
    return returnList
    
        

def _filterLength(videos, lengths):
    removeVideos = []
    min = lengths[0]
    max = lengths[1]

    for x in videos:
        if ((( min != 0 ) & ( x['runtime'] < min )) | (( max != 0 ) & ( x['runtime'] > max ))):
            removeVideos.append(x)
    
    for y in removeVideos:
        videos.remove(y)

    return videos

# Filter function
## Pass in the Search Options
def filter(options: searchOptions):
    genreFilter = _filterList_('genre', options.getGenre())
    tagFilter = _filterList_('tag', options.getTag())
    castFilter = _filterList_('actor', options.getCast())
    directorFilter = _filterList_('director', options.getDirector())
    yearFilter = _filterList_('year', options.getYear())
    studioFilter = _filterList_('studio', options.getStudio())
    ratingFilter = _filterList_('mpaarating', options.getRating())

    filterList = []
    if genreFilter != {}:
        filterList.append(genreFilter)
    if tagFilter != {}:
        filterList.append(tagFilter)
    if castFilter != {}:
        filterList.append(castFilter)
    if directorFilter != {}:
        filterList.append(directorFilter)
    if yearFilter != {}:
        filterList.append(yearFilter)
    if studioFilter != {}:
        filterList.append(studioFilter)
    if ratingFilter != {}:
        filterList.append(ratingFilter)

    # if movie type
    # function call to get movie list
    # if episode type
    # function call to get episode list
    # combine show lists
    # trigger playback functions
    mediaTypes = options.getMediaType()
    movieList = []
    episodeList = []
    for x in mediaTypes:
        if(x == 'movie'):
            command = {
                "jsonrpc": "2.0",
                "method": "VideoLibrary.GetMovies",
                "params": {
                    "filter": { "or" : filterList }, # get_genre_filer() = {"field": "genre", "operator": "is", "value": genre}
                    "properties": ["uniqueid", "art", "thumbnail", "playcount", "file", "runtime", "rating", "title"],
                    "sort": {"order": "ascending", "method": "label"}
                },
                "id": "library"}
            print(command)
            movieList = json.loads(xbmc.executeJSONRPC(json.dumps(command)))['result']['movies']
        elif(x == 'episode'):
            command = {
                "jsonrpc": "2.0",
                "method": "VideoLibrary.GetEpisodes",
                "params": {
                    "filter": { "or" : filterList }, # get_genre_filer() = {"field": "genre", "operator": "is", "value": genre}
                    "properties": ["uniqueid", "art", "thumbnail", "rating", "file", "playcount", 'title', 'runtime'],
                    "sort": {"order": "ascending", "method": "label"}
                },
                "id": "library"}
            print(command)
            episodeList = json.loads(xbmc.executeJSONRPC(json.dumps(command)))['result']['episodes']

    videoList = []
    if (episodeList != []):
        videoList += episodeList
    if (movieList != []):
        videoList += movieList
    
    videoList = _filterIncExc(videoList, options.getInclude(), options.getExclude())
    videoList = _filterLength(videoList, options.getLength())
    #videoList = _filterWatchStatus(videoList, options.getWatchStatus())

    '''
    # These functions will handle the most watched filtering
    if options.getPBFunction() == 1:
        _playOne(videoList)
    elif options.getPBFunction() == 2:
        _showList(videoList)
    elif options.getPBFunction() == 3:
        _loopPlay(videoList)
    '''


def unitTest(options: searchOptions):
    '''
    print(_filterList_('genre', options.getGenre()))
    print(_filterList_('tag', options.getTag()))
    print(_filterList_('cast', options.getCast()))
    print(_filterList_('director', options.getDirector()))
    print(_filterList_('year', options.getYear()))
    print(_filterList_('studio', options.getStudio()))
    print(_filterList_('rating', options.getRating()))
    '''

    filter(options)
