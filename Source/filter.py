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

# {"field": "genre", "operator": "contains", "value": ["", "", ""]}
# {"field": "genre", "operator": "is", "value": ""}


def _genre_filter_(genreList):
    defaultReturn = {}
    if len(genreList) == 1:
        defaultReturn = {"field": "genre",
                         "operator": "is", "value": genreList[0]}
    elif len(genreList) > 1:
        for x in genreList:
            if defaultReturn == {}:
                defaultReturn = x
            else:
                defaultReturn
    return defaultReturn

# Filter function
# Pass in the Search Options


def filter(options: searchOptions):
    genreFilter = _genre_filter_(options.getGenre())
    tagFilter = _tag_filter_(options.getTag())
    castFilter = _cast_filter_(options.getCast())
    directorFilter = _director_filter_(options.getDirector())
    includeFilter = _include_filter_(options.getInclude())
    excludeFilter = _exclude_filter_(options.getExclude())
    lengthFilter = _length_filter_(options.getLength())
    yearFilter = _year_filter_(options.getYear())
    studioFilter = _studio_filter_(options.getStudio())
    ratingFilter = _rating_filter_(options.getRating())

    filterList = []
    if genreFilter != {}:
        filterList.append(genreFilter)
    if tagFilter != {}:
        filterList.append(tagFilter)
    if castFilter != {}:
        filterList.append(castFilter)
    if directorFilter != {}:
        filterList.append(directorFilter)
    if includeFilter != {}:
        filterList.append(includeFilter)
    if excludeFilter != {}:
        filterList.append(excludeFilter)
    if lengthFilter != {}:
        filterList.append(lengthFilter)
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
            # get_genre_filer() = {"field": "genre", "operator": "is", "value": genre}
            "filter": {"or": filterList},
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
