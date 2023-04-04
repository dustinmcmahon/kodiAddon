import xbmc
import json


def by_genre(genre):
    command = {
        "jsonrpc": "2.0",
        "method": "VideoLibrary.GetEpisodes",
        "params": {
            "filter": {"field": "genre", "operator": "is", "value": genre},
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
        return None
