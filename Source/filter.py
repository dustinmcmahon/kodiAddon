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
import random
import xbmcgui
import re
import time
from datetime import datetime
from datetime import datetime
import shut

# *** filter helper functions ***

# builds the filter strings for each field


def _filterList_(name, valueList):
    defaultReturn = {}
    if len(valueList) == 1:
        defaultReturn = {"operator": "is",
                         "field": name, "value": valueList[0]}
    elif len(valueList) > 1:
        for x in valueList:
            if defaultReturn == {}:
                defaultReturn = []
            defaultReturn.append(x)
        defaultReturn = {"operator": "contains",
                         "field": name, "value": defaultReturn}
    return defaultReturn

# applies the include or exclude list to the pre filtered list


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
                if (x == y['title']):
                    videoList.remove(y)
        returnList = videoList
    return returnList

# applies the length filter to the pre filtered list


def _filterLength(videos, lengths):
    removeVideos = []
    min = lengths[0]
    max = lengths[1]

    for x in videos:
        if (((min != 0) & (x['runtime'] < min)) | ((max != 0) & (x['runtime'] > max))):
            removeVideos.append(x)

    for y in removeVideos:
        videos.remove(y)

    return videos

# applies the watch status filter to the pre filtered list


def _filterWatchStatus(videos, status):
    returnList = []
    if (len(status) > 1):
        return videos
    elif (status[0] == 0):
        for x in videos:
            if (x['playcount'] == 0):
                returnList.append(x)
    else:
        for x in videos:
            if (x['playcount'] > 0):
                returnList.append(x)
    return returnList


# *** playback functions ***
# Dustin's assignment
def _playOne(videoList, mostWatched):
    result = []
    if (not mostWatched):
        result.append(random.choice(videoList))
    else:
        for x in videoList:
            if (result != {} or x['playcount'] > result['playcount']):
                result = x
    return result

# Hsu's Assignment


def _getPC(video):
    print(video['title'])
    return video['playcount']


def _showList(videoList, mostWatched):
    if (mostWatched):
        videoList.sort(key=_getPC, reverse=True)
        returnList = videoList
    else:
        returnList = videoList
    return returnList

# Hsu's Assignment


def _getTitle(video):
    return video['title']


def _getfirstAired(video: dict):
    firstaired_str = video['firstaired']  # M I put this
    if (firstaired_str):
        ''' date_obj = datetime.strptime(firstaired_str, "%Y-%m-%d")
         return date_obj'''
        return firstaired_str
    else:
        return datetime.min


def _loopPlay(videoList, mostWatched, mediaTypes):
    movieList = []
    episodeList = []
    for mediaType in mediaTypes:
        if (mediaType == 'movie'):
            if (mostWatched):
                videoList.sort(key=_getPC, reverse=True)
                movieList = videoList
            else:
                videoList.sort(key=_getTitle)
                movieList = videoList
            return movieList
        elif (mediaType == 'episode'):
            if (mostWatched):
                videoList.sort(key=_getPC, reverse=True)
                episodeList = videoList
            else:
                videoList.sort(key=_getfirstAired)
                episodeList = videoList
            return episodeList


# Take this gui
"""    xbmc.PlayList(xbmc.PLAYLIST_VIDEO).clear()
    for video in sort_videoList:
        listitem = xbmcgui.ListItem(label=video['title'], path=video['url'])
        listitem.addThumbnailImage(video['thumbnail'])
        listitem.setInfo('video', video)
        xbmc.PlayList(xbmc.PLAYLIST_VIDEO).add(
            url=video['url'], listitem=listitem)
    print(xbmc.PlayList(xbmc.PLAYLIST_VIDEO))
    xbmc.Player().play(xbmc.PlayList(xbmc.PLAYLIST_VIDEO))
"""
"""playList = xbmc.Playlist(1)
    videos = videoList
    for video in videos:
        picture = video.pop('pic')
        url = video.pop('url')
        listitem = xbmcgui.ListItem(video['title'])
        listitem.setInfo('video', video)
        listitem.setThumbnailImage(picture)
        playList.add(url, listitem)
        '''play=xbmc.PlayList(xbmc.xbmc.PLAYLIST_VIDEO)'''
    xbmc.Player().play(playList)"""


def filter(options: searchOptions.SearchOptions):
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

    xbmc.log(f"filters: {filterList}")
    for x in mediaTypes:
        if (x == 'movie'):
            if filterList == []:
                command = {
                    "jsonrpc": "2.0",
                    "method": "VideoLibrary.GetMovies",
                    "params": {
                        "properties": ["uniqueid", "art", "thumbnail", "playcount", "file", "runtime", "rating", "title"],
                        "sort": {"order": "ascending", "method": "label"}
                    },
                    "id": "library"}
            else:
                command = {
                    "jsonrpc": "2.0",
                    "method": "VideoLibrary.GetMovies",
                    "params": {
                        "filter": {"or": filterList},
                        "properties": ["uniqueid", "art", "thumbnail", "playcount", "file", "runtime", "rating", "title"],
                        "sort": {"order": "ascending", "method": "label"}
                    },
                    "id": "library"}
            movieList = json.loads(xbmc.executeJSONRPC(
                json.dumps(command)))['result']['movies']
        elif (x == 'episode'):
            if filterList == []:
                command = {
                    "jsonrpc": "2.0",
                    "method": "VideoLibrary.GetEpisodes",
                    "params": {
                        "properties": ["uniqueid", "art", "thumbnail", "rating", "file", "playcount", 'title', 'runtime', 'firstaired', 'showtitle'],
                        "sort": {"order": "ascending", "method": "label"}
                    },
                    "id": "library"}
            else:
                command = {
                    "jsonrpc": "2.0",
                    "method": "VideoLibrary.GetEpisodes",
                    "params": {
                        # get_genre_filer() = {"field": "genre", "operator": "is", "value": genre}
                        "filter": {"or": filterList},
                        "properties": ["uniqueid", "art", "thumbnail", "rating", "file", "playcount", 'title', 'runtime', 'firstaired', 'showtitle'],
                        "sort": {"order": "ascending", "method": "label"}
                    },
                    "id": "library"}
            episodeList = json.loads(xbmc.executeJSONRPC(json.dumps(command)))[
                'result']['episodes']

    videoList = []
    if (episodeList != []):
        videoList += episodeList
    if (movieList != []):
        videoList += movieList

    videoList = _filterIncExc(
        videoList, options.getInclude(), options.getExclude())
    videoList = _filterLength(videoList, options.getLength())
    videoList = _filterWatchStatus(videoList, options.getWatchStatus())

    result = []
    if options.getPBFunction() == 1:
        result = _playOne(videoList, options.getMostWatched())
    elif options.getPBFunction() == 2:
        result = _showList(videoList, options.getMostWatched())
    if options.getPBFunction() == 2:
        result = _showList(videoList, options.getMostWatched())
    elif options.getPBFunction() == 3:
        result = _loopPlay(
            videoList, options.getMostWatched(), options.getMediaType())

    return result


def unitTest(options: searchOptions.SearchOptions):
    '''
    print(_filterList_('genre', options.getGenre()))
    print(_filterList_('tag', options.getTag()))
    print(_filterList_('cast', options.getCast()))
    print(_filterList_('director', options.getDirector()))
    print(_filterList_('year', options.getYear()))
    print(_filterList_('studio', options.getStudio()))
    print(_filterList_('rating', options.getRating()))
    '''

    print(filter(options))
    print(shut.shutdownTime(options.getShutTime()))
