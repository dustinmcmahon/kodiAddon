import metaData
import jsongets
import searchOptions
import searchProfile
import filter
import gui

def run():
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
    movieOptions = searchOptions.unitTestMovie()
    episodeOptions = searchOptions.unitTestEpisode()

    # Search Profile Unit Test
    print('** SEARCH PROFILE TESTING **')
    searchProfile.unitTest(movieOptions)

    # Filter Unit Tests
    print('** FILTER TESTING **')
    print(filter.unitTest(movieOptions))
    print(filter.unitTest(episodeOptions))

    return True
