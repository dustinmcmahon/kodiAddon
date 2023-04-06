import json
import xbmc


def getMovies():
    movies = xbmc.executeJSONRPC('{"jsonrpc": "2.0", "method": "VideoLibrary.GetMovies", "params": { "properties": ["art", "rating", "thumbnail", "playcount", "file"], "sort": {"order": "ascending", "method": "label"}}, "id": "libMovies"}'
                                 )

    response_obj = json.loads(movies)
    if "result" in response_obj:
        movies = response_obj["result"]["movies"]
        # movies_str = '\n'.join([movie['label'] for movie in movies])
        # print(movies_str)
        return movies
    else:
        print("No movie found")
        return None


def getTVshows():
    tvshows = xbmc.executeJSONRPC('{"jsonrpc": "2.0", "method": "VideoLibrary.GetTVShows","params": {"properties": ["art", "genre", "plot", "title", "originaltitle", "year", "rating", "thumbnail", "playcount", "file", "fanart"],"sort": {"order": "ascending", "method": "label"}},"id": "libTvShows"}'
                                  )
    response_obj = json.loads(tvshows)
    if "result" in response_obj:
        tvshows = response_obj["result"]["tvshows"]
        # tvshows_str = '\n'.join([tvshow['label'] for tvshow in tvshows])
        # print(tvshows_str)
        return tvshows
    else:
        print("no tvshows found")
        return None


def getMovieDetails(movie_id):
    movie_details = {
        "jsonrpc": "2.0",
        "method": "VideoLibrary.GetMovieDetails",
        "params": {
            "movieid": movie_id,
            "properties": ["title", "plot", "rating", "year", "runtime", "cast", "director", "genre", "studio", "thumbnail", "fanart", "file"]
        },
        "id": "movie_details"
    }
    json_string = json.dumps(movie_details)
    response = xbmc.executeJSONRPC(json_string)
    response_obj = json.loads(response)
    if "result" in response_obj:
        movie_details = response_obj["result"]["moviedetails"]
        # movie_details_str = '\n'.join(
        #     [f'{key}: {value}' for key, value in movie_details.items()])
        # print(movie_details_str)
        return movie_details
    else:
        print("No movie details found.")
        return None


def getTVshowDetails(tvshow_id):
    tvshow_details = {
        "jsonrpc": "2.0",
        "method": "VideoLibrary.GetTVShowDetails",
        "params": {
            "tvshowid": tvshow_id,
            # "properties": ["title", "plot", "rating", "year", "runtime", "cast", "director", "genre", "studio", "thumbnail", "fanart", "file", "seasons", "episode"]
            "properties": ["title", "plot", "genre", "rating", "year", "season", "episode", "cast", "thumbnail"]
        },
        "id": "tvshow_details"
    }

    json_string = json.dumps(tvshow_details)
    response = xbmc.executeJSONRPC(json_string)
    response_obj = json.loads(response)
    if "result" in response_obj:
        tvshow_details = response_obj["result"]["tvshowdetails"]
        # tvshow_details_str = '\n'.join(
        #     [f'{key}: {value}' for key, value in tvshow_details.items()])
        # print(tvshow_details_str)
        return tvshow_details
    else:
        print("No Tv show details found.")
        return None
