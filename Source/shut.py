import xbmc
import xbmcaddon
import time
import searchOptions
import datetime


"""def shutdownTime(shutTimes):
    hours = shutTimes[0]
    minutes = shutTimes[1]
    time_to_quit = time.time() + hours * 3600 + minutes * 60
    while time_to_quit > 0:
        currentTime = time.time()
        if currentTime >= time_to_quit:
            print(time.time())
            xbmc.executebuiltin("Quit()")"""


def shutdownTime(shutTimes):
    hours = shutTimes[0]
    minutes = shutTimes[1]
    time_to_quit = datetime.time(hours, minutes)
    if time_to_quit != datetime.time(0, 0):
        current_time = datetime.datetime.now().time()
        time_diff = datetime.datetime.combine(datetime.date.today(
        ), time_to_quit) - datetime.datetime.combine(datetime.date.today(), current_time)
        time.sleep(time_diff.seconds)
        xbmc.executebuiltin("Quit()")
