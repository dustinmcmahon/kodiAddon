"""import xbmcgui
import xbmc
import xbmcaddon
import metaData

class IncludeWindow(xbmcgui.Window):
    # TODO: write the code
    def include_List(self, text):
        label = xbmcgui.ControlLabel(370, 50, 200, 100, text)
        self.addControl(label)

    def exclude_List(self, text):
        label = xbmcgui.ControlLabel(830, 50, 200, 100, text)
        self.addControl(label)

    def __init__(self) -> None:
        super().__init__()      
        self.include_List("Include")
        self.exclude_List("Exclude")

    pass

#Try again later
dummy_list = [
        {'MediaType':'Movie', 'Name': 'Movie 1', 'Rating': '5', 'Genre': 'Horror', 'Length': '130', 'Year': '2019'},
        {'MediaType':'Epsiode', 'Name': 'Epsiode 2', 'Rating': '2', 'Genre': 'Slice-Of-Life', 'Length': '40', 'Year': '2020'},
        {'MediaType':'Movie', 'Name': 'Movie 2', 'Rating': '4', 'Genre': 'Comedy', 'Length': '90', 'Year': '2023'},
        {'MediaType':'Movie', 'Name': 'Movie 3', 'Rating': '3', 'Genre': 'Action', 'Length': '120', 'Year': '2022'},
        {'MediaType':'Episode', 'Name': 'Epsode 2', 'Rating': '1', 'Genre': 'Romance', 'Length': '20', 'Year': '2021'}
]
media_Length_List = [
    "0 to 30 minutes", "0 to 60 minutes", "0 to 90 minutes",
    "0 to 120 minutes", "30 to 60 minutes", "30 to 90 minutes",
    "30 to 120 minutes", "60 to 90 minutes", "60 to 120 minutes",
    "90 to 120 minutes", "30 minutes and more ", "60 minutes and more ",
    "90 minutes and more ","120 minutes and more "
]


addon = xbmcaddon.Addon()
addonDataFolder = ""
if xbmc.getCondVisibility('system.platform.windows'):
    addonDataFolder = addon.getAddonInfo('path').replace("addons\\video.kodi.episode.selector\\", "userdata\\addon_data\\video.kodi.episode.selector\\")
if xbmc.getCondVisibility('system.platform.osx') or xbmc.getCondVisibility('system.platform.linux'):
    addonDataFolder = addon.getAddonInfo('path').replace("addons/video.kodi.episode.selector/", "userdata/addon_data/video.kodi.episode.selector/")

imagesFolder = addon.getAddonInfo('path') + "/images/"


def show_options_window():
    # Create a window from the XML file
    optionspath = addon.getAddonInfo('path') + "optionsWindow.xml"
    dialog = xbmcgui.WindowXMLDialog(optionspath)

    # Display the window
    dialog.doModal()

def options():
    show_options_window()
class MyWindow(xbmcgui.Window):
    # def display_list(self):
    #         dialog = xbmcgui.Dialog()
    #         dialog.ok("List", str(dummy_list))

     #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\The Identifying
    def media_Type(self, text):
        label = xbmcgui.ControlLabel(50, 50, 200, 100, text)
        self.addControl(label)

    def watch_Status(self, text):
        label = xbmcgui.ControlLabel(190, 50, 200, 100, text)
        self.addControl(label)

    def rating_List(self, text):
        label = xbmcgui.ControlLabel(370, 50, 200, 100, text)
        self.addControl(label)

    def genre_List(self, text):
        label = xbmcgui.ControlLabel(520, 50, 200, 100, text)
        self.addControl(label)

    def length_List(self, text):
        label = xbmcgui.ControlLabel(670, 50, 200, 100, text)
        self.addControl(label)

    def year_List(self, text):
        label = xbmcgui.ControlLabel(830, 50, 200, 100, text)
        self.addControl(label)

    def tags_List(self, text):
        label = xbmcgui.ControlLabel(980, 50, 200, 100, text)
        self.addControl(label)

    def studio_List(self, text):
        label = xbmcgui.ControlLabel(1120, 50, 200, 100, text)
        self.addControl(label)

    def most_Watched(self, text):
        label = xbmcgui.ControlLabel( 37, 200, 200, 100, text)
        self.addControl(label)

    def casts_List(self, text):
        label = xbmcgui.ControlLabel(225, 200, 200, 100, text)
        self.addControl(label)

    def director_List(self, text):
        label = xbmcgui.ControlLabel(360, 200, 300, 200, text)
        self.addControl(label)

    def include_List(self, text):
        label = xbmcgui.ControlLabel(515, 200, 300, 200, text)
        self.addControl(label)

    def playOne(self, text):
        label = xbmcgui.ControlLabel(1130, 660, 300, 200, text)
        self.addControl(label)

    def showList(self, text):
        label = xbmcgui.ControlLabel(935, 660, 300, 200, text)
        self.addControl(label)

    def loopPlay(self, text):
        label = xbmcgui.ControlLabel(725, 660, 300, 200, text)
        self.addControl(label)

    def saveSearch(self, text):
        label = xbmcgui.ControlLabel(555, 660, 300, 200, text)
        self.addControl(label)

    def shutDown(self, text):
        label = xbmcgui.ControlLabel(95, 610, 300, 200, text)
        self.addControl(label)

    def time(self, text):
        label = xbmcgui.ControlLabel(95, 660, 300, 200, text)
        self.addControl(label)
    

       #The images
    def show_circle(self, x, y, radius, color):
        circlePath = imagesFolder + "circle.png"
        circle = xbmcgui.ControlImage(x, y, radius, radius, circlePath, color)
        self.addControl(circle)

    def show_backList(self, x, y, width, height, color):
        backPath = imagesFolder + "ListBackground.png"
        backgroundList = xbmcgui.ControlImage(x, y, width, height, backPath, color)
        self.addControl(backgroundList)
        return backgroundList

    def show_timerSquare(self, x, y, radius, color):
        timerPath = imagesFolder + "TimeBackground.png"
        timeGroundList = xbmcgui.ControlImage(x, y, radius, radius, timerPath, color)
        self.addControl(timeGroundList)
        return timeGroundList

    # def onClick(self, controlId: int):
    #     xbmc.log(f"something was clicked! {controlId}")
    #     if controlId == self.button.getId():
    #         xbmc.log("the DisplayList button was pressed!")
    #         self.display_list()

    # def get_names(items):
    # list = []
    # for item in items:
    #     name = item.get('name', None)
    #     if name is not None:
    #         names.append(name)
    # return names
  
    

    #IDK
    # names_only = get_names(dummy_list)
    # dummy_list = create_dummy_list()

    # first_params = []
    # for param in dummy_list:
    #     first_params.append(param[0])
    #//////////////////////////////////////Types of Buttons 







    def __init__(self) -> None:
        super().__init__()

        self.mediaType = xbmcgui.ControlButton(0, 10, 200, 106, "    ")
        self.addControl(self.mediaType)

        self.watchStatus = xbmcgui.ControlButton(150, 10, 200, 106, "    ")
        self.addControl(self.watchStatus)

        self.ratingList = xbmcgui.ControlButton(300, 10, 200, 106, "    ")
        self.addControl(self.ratingList)

        self.genreList = xbmcgui.ControlButton(450, 10, 200, 106, "    ")
        self.addControl(self.genreList)

        self.lengthList = xbmcgui.ControlButton(600, 10, 200, 106, "    ")
        self.addControl(self.lengthList)

        self.yearList = xbmcgui.ControlButton(750, 10, 200, 106, "    ")
        self.addControl(self.yearList)

        self.tagsList = xbmcgui.ControlButton(900, 10, 200, 106, "    ")
        self.addControl(self.tagsList)

        self.studioList = xbmcgui.ControlButton(1050, 10, 200, 106, "    ")
        self.addControl(self.studioList)

        self.mostWatched = xbmcgui.ControlButton(0, 160, 200, 106, "    ")
        self.addControl(self.mostWatched)

        self.castsList = xbmcgui.ControlButton(150, 160, 200, 106, "    ")
        self.addControl(self.castsList)

        self.directorList = xbmcgui.ControlButton(300, 160, 200, 106, "    ")
        self.addControl(self.directorList)

        self.includeList = xbmcgui.ControlButton(450, 160, 200, 106, "    ")
        self.addControl(self.includeList)

        #Orange
        self.show_circle (30, 35, 150, 0xFF0000)
        self.show_circle (180, 35, 150, 0xFF0000)
        self.show_circle (330, 35, 150, 0xFF0000)
        self.show_circle (480, 35, 150, 0xFF0000)
        self.show_circle (630, 35, 150, 0xFF0000)
        self.show_circle (780, 35, 150, 0xFF0000)
        self.show_circle (930, 35, 150, 0xFF0000)
        self.show_circle (1080, 35, 150, 0xFF0000)

        self.show_circle (30, 185, 150, 0xFF0000)
        self.show_circle (180, 185, 150, 0xFF0000)
        self.show_circle (330, 185, 150, 0xFF0000)
        self.show_circle (480, 185, 150, 0xFF0000)

        self.show_circle (1080, 635, 200, 0xFF0000)
        self.show_circle (880, 635, 200, 0xFF0000)
        self.show_circle (680, 635, 200, 0xFF0000)
        self.show_circle (480, 635, 200, 0xFF0000)

        self.show_circle (35, 590, 300, 0xFF0000)
        self.show_timerSquare(120, 630, 100, 0xFF0000)
        self.show_timerSquare(205, 630, 100, 0xFF0000)


        #Identifying
        self.media_Type("MediaType")
        self.watch_Status("WatchStatus")
        self.rating_List("Rating")
        self.genre_List("Genre")
        self.length_List("Length")
        self.year_List("Year")
        self.tags_List("Tags")
        self.studio_List("Studio")
        self.most_Watched("MostWatched")
        self.casts_List("Casts")
        self.director_List("Director")
        self.include_List("Include")

        self.playOne("Play One")
        self.loopPlay("Loop Play")
        self.showList("Show List")
        self.saveSearch("Save")
        self.shutDown("ShutDown Time")
        self.time("Hour          Min")


        self.list1 = xbmcgui.ControlList(0, 100, 300, 200)
        self.listBack1 = self.show_backList(30, 100, 200, 100, 0xFF0000)
        self.listBack1.setVisible(False)
        self.addControl(self.list1)
        self.list1.addItem(str("Movies"))
        self.list1.addItem(str("Episodes"))
        self.list1.setVisible(False)

        self.list2 = xbmcgui.ControlList(150, 100, 300, 200)
        self.listBack2 = self.show_backList(180, 100, 220, 100, 0xFF0000)
        self.listBack2.setVisible(False)
        self.addControl(self.list2)
        self.list2.addItem(str("Watched"))
        self.list2.addItem(str("Unwatched"))
        self.list2.setVisible(False)

        self.list3 = xbmcgui.ControlList(260, 100, 300, 200)
        self.listBack3 = self.show_backList(280, 100, 480, 300, 0xFF0000)
        self.listBack3.setVisible(False)
        self.addControl(self.list3)
        for item in metaData.getRatings():
            self.list3.addItem(item[0])
        self.list3.setVisible(False)

        self.list4 = xbmcgui.ControlList(440, 100, 300, 200)
        self.listBack4 = self.show_backList(470, 100, 220, 300, 0xFF0000)
        self.listBack4.setVisible(False)
        self.addControl(self.list4)
        for item in metaData.getGenres():
            self.list4.addItem(item[1])
        self.list4.setVisible(False)

        # self.list5 = xbmcgui.ControlList(600, 100, 300, 200)
        self.listBack5 = self.show_backList(625, 100, 300, 300, 0xFF0000)
        self.minInput = xbmcgui.ControlEdit(630, 100, 150, 30, "Minimum = ")
        self.maxInput = xbmcgui.ControlEdit(630, 150, 150, 30, "Maximum =  ")
        self.addControl(self.minInput)
        self.addControl(self.maxInput)
        xbmc.log(f"minInput is at {self.minInput.getX()} {self.minInput.getY()}")
        xbmc.log(f"maxInput is at {self.maxInput.getX()} {self.maxInput.getY()}")
        # self.minInput.setPosition(700, 130)
        self.listBack5.setVisible(False)
        # self.addControl(self.list5)
        # self.list5.setVisible(False)
        self.minInput.setVisible(False)
        self.maxInput.setVisible(False)

        self.list6 = xbmcgui.ControlList(710, 100, 300, 200)
        self.listBack6 = self.show_backList(740, 100, 480, 300, 0xFF0000)
        self.listBack6.setVisible(False)
        self.addControl(self.list6)
        for item in metaData.getYears(): 
            self.list6.addItem(item[0])
        self.list6.setVisible(False)

        self.list7 = xbmcgui.ControlList(890, 100, 300, 200)
        self.listBack7 = self.show_backList(920, 100, 400, 300, 0xFF0000)
        self.listBack7.setVisible(False)
        self.addControl(self.list7)
        for item in metaData.getTags():
            self.list7.addItem(item[1])
        self.list7.setVisible(False)

        self.list8 = xbmcgui.ControlList(1040, 100, 260, 200)
        self.listBack8 = self.show_backList(1070, 100, 480, 200, 0xFF0000)
        self.listBack8.setVisible(False)
        self.addControl(self.list8)
        for item in metaData.getStudios():
            self.list8.addItem(item[1])
        self.list8.setVisible(False)

        self.list9 = xbmcgui.ControlList(0, 250, 300, 200)
        self.listBack9 = self.show_backList(30, 250, 480, 300, 0xFF0000)
        self.listBack9.setVisible(False)
        self.addControl(self.list9)
        self.list9.addItem(str("On"))
        self.list9.addItem(str("Off"))
        self.list9.setVisible(False)

        self.list10 = xbmcgui.ControlList(150, 250, 300, 200)
        self.listBack10 = self.show_backList(180, 250, 400, 300, 0xFF0000)
        self.listBack10.setVisible(False)
        self.addControl(self.list10)
        for item in metaData.getActors():
            self.list10.addItem(item[1])
        self.list10.setVisible(False)

        self.list11 = xbmcgui.ControlList(300, 250, 300, 200)
        self.listBack11 = self.show_backList(330, 250, 220, 300, 0xFF0000)
        self.listBack11.setVisible(False)
        self.addControl(self.list11)
        for item in metaData.getDirectors():
            self.list11.addItem(item[1])
        self.list11.setVisible(False)

        self.list12 = xbmcgui.ControlList(410, 250, 300, 200)
        self.addControl(self.list12)
        for item in dummy_list:
            self.list12.addItem(str(item))
        self.list12.setVisible(False)


    def onAction(self, action: xbmcgui.Action) -> None:
        # print(f"action: {action}")
        if action == xbmcgui.ACTION_PREVIOUS_MENU or action == xbmcgui.ACTION_NAV_BACK:
            self.close()

        if action == xbmcgui.ACTION_MOUSE_LEFT_CLICK:
            control = self.getFocus()
            if control.getId() == self.mediaType.getId():
                self.listBack1.setVisible(not self.listBack1.isVisible())
                self.list1.setVisible(not self.list1.isVisible())
                text = "visible" if self.list1.isVisible() else "invisible"
                text2 = "visible" if self.listBack1.isVisible() else "invisible"
                xbmc.log("button was pressed, List Background is now " + text2)
                xbmc.log("button was pressed, list1 is now " + text)

            #The getting options thing
            if control.getId() == self.list1.getId():
                global MediaTypeItem
                SelectedMediaTypeItem = self.list1.getSelectedItem()
                #self.This = SelectedMediaTypeItem.getlabel()
                xbmc.log( SelectedMediaTypeItem.getLabel() + " was clicked from MediaType option")
                MediaTypeItem = SelectedMediaTypeItem

            if control.getId() == self.watchStatus.getId():
                self.listBack2.setVisible(not self.listBack2.isVisible())
                self.list2.setVisible(not self.list2.isVisible())
                text = "visible" if self.list2.isVisible() else "invisible"
                text2 = "visible" if self.listBack2.isVisible() else "invisible"
                xbmc.log("button was pressed, List Background is now " + text2)
                xbmc.log("button was pressed, list2 is now " + text)

            #The getting options thing
            if control.getId() == self.list2.getId():
                global WatchStatusItem
                SelectedWatchStatusItem = self.list2.getSelectedItem()
                xbmc.log( SelectedWatchStatusItem.getLabel() + " was clicked from WatchStatus option")
                WatchStatusItem = SelectedWatchStatusItem

            if control.getId() == self.ratingList.getId():
                self.listBack3.setVisible(not self.listBack3.isVisible())
                self.list3.setVisible(not self.list3.isVisible())
                text = "visible" if self.list3.isVisible() else "invisible"
                text2 = "visible" if self.listBack3.isVisible() else "invisible"
                xbmc.log("button was pressed, List Background is now " + text2)
                xbmc.log("button was pressed, list3 is now " + text)

            #The getting options thing
            if control.getId() == self.list3.getId():
                global RatingItem
                SelectedRating = self.list3.getSelectedItem()
                xbmc.log( SelectedRating.getLabel() + " was clicked from Rating option")
                RatingItem = SelectedRating

            if control.getId() == self.genreList.getId():
                self.listBack4.setVisible(not self.listBack4.isVisible())
                self.list4.setVisible(not self.list4.isVisible())
                text = "visible" if self.list4.isVisible() else "invisible"
                text2 = "visible" if self.listBack4.isVisible() else "invisible"
                xbmc.log("button was pressed, List Background is now " + text2)
                xbmc.log("button was pressed, list4 is now " + text)

            #The getting options thing
            if control.getId() == self.list4.getId():
                global GenreItem
                SelectedGenreItem = self.list4.getSelectedItem()
                xbmc.log( SelectedGenreItem.getLabel() + " was clicked from Genre option")
                GenreItem = SelectedGenreItem

            if control.getId() == self.lengthList.getId():
                self.listBack5.setVisible(not self.listBack5.isVisible())
                # self.list5.setVisible(not self.list5.isVisible())
                # text = "visible" if self.list5.isVisible() else "invisible"
                text2 = "visible" if self.listBack5.isVisible() else "invisible"
                xbmc.log("button was pressed, List Background is now " + text2)
                # xbmc.log("button was pressed, list5 is now " + text)
                self.minInput.setVisible(not self.minInput.isVisible())
                self.maxInput.setVisible(not self.maxInput.isVisible())
                text3 = "visible" if self.minInput.isVisible() else "invisible"
                text3 = "visible" if self.maxInput.isVisible() else "invisible"
                xbmc.log("button was pressed, min Button is now " + text3)
                minValue = self.minInput.getText()
                maxValue = self.maxInput.getText()
                xbmc.log(minValue + " is the input for minimum length")
                xbmc.log(maxValue + " is the input for maximum length")

            


            #The getting options thing
            # if control.getId() == self.list5.getId():
            #     global LengthItem
            #     SelectedLengthItem = self.list5.getSelectedItem()
            #     xbmc.log( SelectedLengthItem.getLabel() + " was clicked from Length option")
            #     LengthItem = SelectedLengthItem

            if control.getId() == self.yearList.getId():
                self.listBack6.setVisible(not self.listBack6.isVisible())
                self.list6.setVisible(not self.list6.isVisible())
                text = "visible" if self.list6.isVisible() else "invisible"
                text2 = "visible" if self.listBack6.isVisible() else "invisible"
                xbmc.log("button was pressed, List Background is now " + text2)
                xbmc.log("button was pressed, list6 is now " + text)

            #The getting options thing
            if control.getId() == self.list6.getId():
                global YearItem
                SelectedYearItem = self.list6.getSelectedItem()
                xbmc.log( SelectedYearItem.getLabel() + " was clicked from Year option")
                YearItem = SelectedYearItem

            if control.getId() == self.tagsList.getId():
                self.listBack7.setVisible(not self.listBack7.isVisible())
                self.list7.setVisible(not self.list7.isVisible())
                text = "visible" if self.list7.isVisible() else "invisible"
                text2 = "visible" if self.listBack7.isVisible() else "invisible"
                xbmc.log("button was pressed, List Background is now " + text2)
                xbmc.log("button was pressed, list7 is now " + text)

            #The getting options thing
            if control.getId() == self.list7.getId():
                global TagsItem
                SelectedTagItem = self.list7.getSelectedItem()
                xbmc.log( SelectedTagItem.getLabel() + " was clicked from Tags option")
                TagsItem = SelectedTagItem

            if control.getId() == self.studioList.getId():
                self.listBack8.setVisible(not self.listBack8.isVisible())
                self.list8.setVisible(not self.list8.isVisible())
                text = "visible" if self.list8.isVisible() else "invisible"
                text2 = "visible" if self.listBack8.isVisible() else "invisible"
                xbmc.log("button was pressed, List Background is now " + text2)
                xbmc.log("button was pressed, list8 is now " + text)

            #The getting options thing
            if control.getId() == self.list8.getId():
                global StudioItem
                SelectedStudioItem = self.list8.getSelectedItem()
                xbmc.log( SelectedStudioItem.getLabel() + " was clicked from Studio option")
                StudioItem = SelectedStudioItem

            if control.getId() == self.mostWatched.getId():
                self.listBack9.setVisible(not self.listBack9.isVisible())
                self.list9.setVisible(not self.list9.isVisible())
                text = "visible" if self.list9.isVisible() else "invisible"
                text2 = "visible" if self.listBack9.isVisible() else "invisible"
                xbmc.log("button was pressed, List Background is now " + text2)
                xbmc.log("button was pressed, list9 is now " + text)

            #The getting options thing
            if control.getId() == self.list9.getId():
                global MostWatchedItem
                SelectedMostWatchedItem = self.list9.getSelectedItem()
                xbmc.log( SelectedMostWatchedItem.getLabel() + " was clicked from MostWatched option")
                MostWatchedItem = SelectedMostWatchedItem

            if control.getId() == self.castsList.getId():
                self.listBack10.setVisible(not self.listBack10.isVisible())
                self.list10.setVisible(not self.list10.isVisible())
                text = "visible" if self.list10.isVisible() else "invisible"
                text2 = "visible" if self.listBack10.isVisible() else "invisible"
                xbmc.log("button was pressed, List Background is now " + text2)
                xbmc.log("button was pressed, list10 is now " + text)
            
            #The getting options thing
            if control.getId() == self.list10.getId():
                global CastsItem
                SelectedCastsItem = self.list10.getSelectedItem()
                xbmc.log( SelectedCastsItem.getLabel() + " was clicked from Casts option")
                CastsItem = SelectedCastsItem

            if control.getId() == self.directorList.getId():
                self.listBack11.setVisible(not self.listBack11.isVisible())
                self.list11.setVisible(not self.list11.isVisible())
                text = "visible" if self.list11.isVisible() else "invisible"
                text2 = "visible" if self.listBack11.isVisible() else "invisible"
                xbmc.log("button was pressed, List Background is now " + text2)
                xbmc.log("button was pressed, list11 is now " + text)

                #The getting options thing
            if control.getId() == self.list11.getId():
                global DirectorItem
                SelectedDirectorItem = self.list11.getSelectedItem()
                xbmc.log( SelectedDirectorItem.getLabel() + " was clicked from Director option")
                DirectorItem = SelectedDirectorItem

            if control.getId() == self.includeList.getId():
                includeWindow = IncludeWindow()
                includeWindow.doModal()
                del includeWindow

                # self.list12.setVisible(not self.list12.isVisible())
                # text = "visible" if self.list12.isVisible() else "invisible"
                # xbmc.log("button was pressed, list12 is now " + text)




#Global Variables for options

MediaTypeItem = None
def getMediaTypeItem() -> str:
    return MediaTypeItem

WatchstatusItem = None
def getWatchStatusItem() -> str:
    return MediaTypeItem

RatingsItem = None
def getRatingsItem() -> str:
    return RatingsItem

GenreItem = None
def getGenreItem() -> str:
    return GenreItem

LengthItem = None
def getLengthItem() -> str:
    return LengthItem

YearItem = None
def getYearItem() -> str:
    return YearItem

TagsItem = None
def getTagsItem() -> str:
    return TagsItem

StudioItem = None
def getStudioItem() -> str:
    return StudioItem

MostWatchedItem = None
def getMostWatchedItem() -> str:
    return MostWatchedItem

CastsItem = None
def getCastsItem() -> str:
    return CastsItem

DirectorItem = None
def getDirectorItem() -> str:
    return DirectorItem

IncludeItem = None
def getIncludeItem() -> str:
    return IncludeItem




    
  #The Window
def showGui():
    window = MyWindow()
    width = window.getWidth()
    height = window.getHeight()
    xbmc.log(f"{width} by {height}")

    # button.setNavigation( xbmcgui.ACTION_SELECT_ITEM, lambda: display_list() )
    
    window.doModal()
    del window
"""
