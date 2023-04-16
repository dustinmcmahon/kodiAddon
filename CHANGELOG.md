# Change Log

### 4/14/23
- created a string function for search options
- created get functions for search profiles
- created unit test for get functionality
- created update function for search profiles
- created the play one filter function

### 4/14/23
- filter function complete
- added watch status function
- setup playback functions

### 4/13/23
- searchOptions for episodes working
- filter for episodes working
- include/exclude filer working for movie & episode
- length filter working for movie & episode

### 4/11/23
- merged into main the GUI updates
- fixed issue with year being stored as an int when it should be a string
- updated test cases for searchOptions

### 4/10/23
- updated test cases in search options
- updated search profile save rating function to use a string instead of an int
- filter function working in that it pulls back a list of movies
- added getMovies, getYears, and getRatings to the metaData class

### 4/7/23
- Uploaded gui.py

### 4/6/23
- updated search option test cases to work with strings and not numbers
- finished create/delete functions for profiles
- finished unit testing for create/delete functions for profiles
- moved all unit tests to default.unitTest()
- searchOptions unit test returns a completed searchOption object to be tested with

### 4/5/23
- removed uninstall.py
- fixed install to always update the searchOptionType table to include all default options
- added unitTesting section to default.py
- finished Create functions for searchProfile

### 4/3/23
- renamed install.py to searchProfile.py
  - creates required db, tables, and default data required to save search profiles
  - added CRUD functions for search profile
    - insert working to add a new profile
    - functions for options have been started

### 4/2/23
- created test cases for the searchOption class

### 3/31/23
- added searchOption class
- created setters and getters and add/delete functions

### 3/29/23
- Moved profile DB
- Added Mac & Windows Install locations
- Wrapper for sqlite calls to video db
- Individual functions for getting meta data have been created
- These functions return an array of tuples [(id, title), (id2, title2)...]

### 3/27/23
- create an install and uninstall script
- create database for holding save profiles
  - create table for profile names
  - create table for search parameters

### 3/26/23
- source code updated
- renamed entry point to default.py
- filled out the addon.xml document
- created a window to display the UI in
- added KES logo

### 2/20/2023
- added uml diagram
  - drawio version
  - pgn version
  - gaphor version

### 2/1/2023
- created repo
- added folder/file structure