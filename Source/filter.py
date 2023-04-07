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
        defaultReturn = {"field": name, "operator": "is", "value": valueList[0]}
    elif len(valueList) > 1:
        for x in valueList:
            if defaultReturn == {}:
                defaultReturn = []
            defaultReturn.append(x)
        defaultReturn = {"field": name, "operator": "contains", "value": defaultReturn}
    return defaultReturn

# Filter function
## Pass in the Search Options
def filter(options: searchOptions):
    genreFilter = _filterList_('genre', options.getGenre())
    tagFilter = _filterList_('tag', options.getTag())
    castFilter = _filterList_('cast', options.getCast())
    directorFilter = _filterList_('director', options.getDirector())
    #includeFilter = _filterList_(options.getInclude())
    #excludeFilter = _filterList_(options.getExclude())
    #lengthFilter = _filterList_(options.getLength())
    yearFilter = _filterList_('year', options.getYear())
    studioFilter = _filterList_('studio', options.getStudio())
    ratingFilter = _filterList_('rating', options.getRating())

    filterList = []
    if genreFilter != {}:
        filterList.append(genreFilter)
    if tagFilter != {}:
        filterList.append(tagFilter)
    if castFilter != {}:
        filterList.append(castFilter)
    if directorFilter != {}:
        filterList.append(directorFilter)
    '''
    if includeFilter != {}:
        filterList.append(includeFilter)
    if excludeFilter != {}:
        filterList.append(excludeFilter)
    if lengthFilter != {}:
        filterList.append(lengthFilter)
    '''
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
    videoList = []
    if options.getPBFunction() == 1:
        playOne(videoList)
    elif options.getPBFunction() == 2:
        showList(videoList)
    elif options.getPBFunction() == 3:
        loopPlay(videoList)

    command = {
        "jsonrpc": "2.0",
        "method": "VideoLibrary.GetEpisodes",
        "params": {
            "filter": { "or" : filterList }, # get_genre_filer() = {"field": "genre", "operator": "is", "value": genre}
            "properties": ["art", "rating", "thumbnail", "playcount", "file"],
            "sort": {"order": "ascending", "method": "label"}
        },
        "id": "library"}
    
    response = xbmc.executeJSONRPC(json.dumps(command))
    response_obj = json.loads(response)
    if "result" in response_obj:
        items = response_obj["result"]["episodes"]
        items.extend(response_obj["result"]["movies"])
        return items
    else:
        print("no item found")
        return {}


def unitTest(options: searchOptions):
    print(_filterList_('genre', options.getGenre()))
    print(_filterList_('tag', options.getTag()))
    print(_filterList_('cast', options.getCast()))
    print(_filterList_('director', options.getDirector()))
    print(_filterList_('year', options.getYear()))
    print(_filterList_('studio', options.getStudio()))
    print(_filterList_('rating', options.getRating()))