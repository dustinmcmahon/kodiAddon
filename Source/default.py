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


if (unitTests.run()):
    xbmc.log("Unit Testing Complete!", 0)
else:
    xbmc.log("Unit Testing Failed!", 0)


#gui.showGui()