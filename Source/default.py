import xbmc
import xbmcgui
import xbmcaddon
import metaData
import jsongets
import searchOptions
import searchProfile
import filter
import gui
import unitTests
import time
import profileGUI

searchProfile.install()

addon = xbmcaddon.Addon()

# **********************
'''
This is a function where we can compile all of our unit tests
Each Python file should have a single unit test function to test all other functions
'''
# **********************


"""if (unitTests.run()):
    xbmc.log("Unit Testing Complete!", 0)
else:
    xbmc.log("Unit Testing Failed!", 0)
"""

# gui.showGui()

dialog = xbmcgui.Dialog()
result = dialog.contextmenu(['Play', 'New Search', 'Saved Search'])

if (result == 0):
    so = searchOptions.SearchOptions()
    so.setPBFunction(1)
    so.setWatchStatus([])
    movie = filter.filter(so)
    player = xbmc.Player()
    player.play(movie[0]['file'])

if (result == 1):
    gui.showGui()

elif (result == 2):
    window = profileGUI.SavedSearch().doModal()
    del window
