import xbmc
import xbmcgui
import xbmcaddon
import metaData
import jsongets
import searchOptions
import searchProfile
import filter
import gui
# import kesGUI

searchProfile.install()

addon = xbmcaddon.Addon()

##

##

# interface = kesGUI.build()


class MyPlayer(xbmcgui.Window):
    def __init__(self):
        xbmcgui.Window.__init__(self)

        self.button = xbmcgui.ControlButton(
            50, 50, 400, 100, label="Play Random Movie", focusTexture="special://home/addons/script.random_movie_player/resources/skins/default/media/focused.png")
        self.addControl(self.button)

    def onControl(self, control):
        if control == self.button:
            xbmcgui.Dialog().ok('addonname', 'This message')
            # play_random_movie()

    # def onClick(self, controlID: int):
    #     if controlID == 10:
    #         play_random_movie()


"""
if (__name__ == "__main__"):
    w = MyPlayer()
    w.doModal()
    del w
"""

# **********************
'''
This is a function where we can compile all of our unit tests
Each Python file should have a single unit test function to test all other functions
'''
# **********************


def unitTest():
    # JSON RPC Testing
    print('** JSON GETS TESTING **')
    jsongets.unitTests()

    # Meta Data Unit Tests
    # Prints the results of each of the get meta data functions
    print('** META DATA TESTING **')
    metaData.testMetaData()

    # Search Option Unit Test
    # Creates a searchOption object, sets, adds, and removes each potential option and prints results, will finish by returning the options object
    print('** SEARCH OPTIONS TESTING **')
    options = searchOptions.unitTest()

    # Search Profile Unit Test
    print('** SEARCH PROFILE TESTING **')
    searchProfile.unitTest(options)

    # Filter Unit Tests
    print('** FILTER TESTING **')
    filter.unitTest(options)


unitTest()

gui.showGui()

# xbmcgui.Dialog().ok("KES", "Complete!")
