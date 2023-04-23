import xbmc
import xbmcaddon
import time
import searchOptions


def shutdownTime(shutTimes):
    hours = shutTimes[0]
    minutes = shutTimes[1]
    time_to_quit = hours * 3600 + minutes * 60
    while time_to_quit > 0:
        currentTime = time.time()
        if currentTime >= time_to_quit:
            print(time.time())
            xbmc.executebuiltin("Quit()")
