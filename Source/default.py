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

searchProfile.install()

addon = xbmcaddon.Addon()

# **********************
'''
This is a function where we can compile all of our unit tests
Each Python file should have a single unit test function to test all other functions
'''
# **********************

if (unitTests.run()):
    xbmc.log("Unit Testing Complete!", 0)
else:
    xbmc.log("Unit Testing Failed!", 0)

# gui.showGui()
