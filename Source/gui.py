import xbmcgui
import xbmc
import xbmcaddon
import metaData
import searchOptions
import filter as OurFilter
import shut

import guiPlayWindows
import searchProfile

class IncludeWindow(xbmcgui.Window):
    # TODO: write the code

    def show_Setting(self, x, y, radius, color):
        settingPath = imagesFolder + "Settings.png"
        setting = xbmcgui.ControlImage(x, y, radius, radius, settingPath, color)
        self.addControl(setting)

    def show_Back(self, x, y, radius, color):
        backPath = imagesFolder + "IncludeBackground.png"
        backGround = xbmcgui.ControlImage(x, y, radius, radius, backPath, color)
        self.addControl(backGround)

    def show_Arrow(self, x, y, radius, color):
        backPath = imagesFolder + "IncludeBackground.png"
        backGround = xbmcgui.ControlImage(x, y, radius, radius, backPath, color)
        self.addControl(backGround)

    def include_List(self, text):
        label = xbmcgui.ControlLabel(350, 50, 200, 100, text)
        self.addControl(label)

    def exclude_List(self, text):
        label = xbmcgui.ControlLabel(830, 50, 200, 100, text)
        self.addControl(label)

    def __init__(self) -> None:
        super().__init__()      
        self.show_Back (10, 50, 600, 0xFF0000)
        self.show_Back (500, 50, 600, 0xFF0000)
        self.include_List("Include")
        self.exclude_List("Exclude")
        self.show_Setting (10, 10, 300, 0xFF0000)


    pass

    #     for i in range(0, 8):
    #         cookie = page * 8  # index into list based on page
            
    #         if i < 4:
    #             topLabels[i].
    #             xbmc.PlayList(xbmc.PLAYLIST_VIDEO).clear()

    # for video in sort_videoList:
    #     listitem = xbmcgui.ListItem(label=video['title'], path=video['url'])
    #     listitem.addThumbnailImage(video['thumbnail'])
    #     listitem.setInfo('video', video)
    #     xbmc.PlayList(xbmc.PLAYLIST_VIDEO).add(
    #         url=video['url'], listitem=listitem)
    # print(xbmc.PlayList(xbmc.PLAYLIST_VIDEO))
    # xbmc.Player().play(xbmc.PlayList(xbmc.PLAYLIST_VIDEO))

    #         else:
    #             bottomLabels[i]



    
# xbmc.PlayList(xbmc.PLAYLIST_VIDEO).clear()
#     for video in sort_videoList:
#         listitem = xbmcgui.ListItem(label=video['title'], path=video['url'])
#         listitem.addThumbnailImage(video['thumbnail'])
#         listitem.setInfo('video', video)
#         xbmc.PlayList(xbmc.PLAYLIST_VIDEO).add(
#             url=video['url'], listitem=listitem)
#     print(xbmc.PlayList(xbmc.PLAYLIST_VIDEO))
#     xbmc.Player().play(xbmc.PlayList(xbmc.PLAYLIST_VIDEO))

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
    #         dialog.ok("List", str(dummy_list)) blah

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

        self.ratingButton = xbmcgui.ControlButton(300, 10, 200, 106, "    ")
        self.addControl(self.ratingButton)

        self.genreButton = xbmcgui.ControlButton(450, 10, 200, 106, "    ")
        self.addControl(self.genreButton)

        self.lengthList = xbmcgui.ControlButton(600, 10, 200, 106, "    ")
        self.addControl(self.lengthList)

        self.yearButton = xbmcgui.ControlButton(750, 10, 200, 106, "    ")
        self.addControl(self.yearButton)

        self.tagsButton = xbmcgui.ControlButton(900, 10, 200, 106, "    ")
        self.addControl(self.tagsButton)

        self.studioButton = xbmcgui.ControlButton(1050, 10, 200, 106, "    ")
        self.addControl(self.studioButton)

        self.mostWatched = xbmcgui.ControlButton(0, 160, 200, 106, "    ")
        self.addControl(self.mostWatched)

        self.castsButton = xbmcgui.ControlButton(150, 160, 200, 106, "    ")
        self.addControl(self.castsButton)

        self.directorButton = xbmcgui.ControlButton(300, 160, 200, 106, "    ")
        self.addControl(self.directorButton)

        self.includeList = xbmcgui.ControlButton(450, 160, 200, 106, "    ")
        self.addControl(self.includeList)

        self.showListButton = xbmcgui.ControlButton(880, 610, 180, 110, "    ")
        self.addControl(self.showListButton)

        self.playOneButton = xbmcgui.ControlButton(1080, 610, 180, 110, "    ")
        self.addControl(self.playOneButton)

        self.loopPlayButton = xbmcgui.ControlButton(680, 610, 180, 110, "    ")
        self.addControl(self.loopPlayButton)

        self.saveButton = xbmcgui.ControlButton(480, 610, 180, 110, "    ")
        self.addControl(self.saveButton)

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



        self.hourInput = xbmcgui.ControlEdit(120, 660, 50, 30, " ")
        self.minuteInput = xbmcgui.ControlEdit(200, 660, 50, 30, " ")
        self.activateTime = xbmcgui.ControlButton(120, 590, 200, 50, " ")
        self.addControl(self.hourInput)
        self.addControl(self.minuteInput)
        self.addControl(self.activateTime)
        hourValue = self.hourInput.getText()
        minuteValue = self.minuteInput.getText()
        self.time("Hour          Min")
        xbmc.log("This is the number of hours" + hourValue)
        xbmc.log("This is the number of minutes" + minuteValue)

        #Use controlImage to get the filename with the URL

        self.mediaTypeList = xbmcgui.ControlList(0, 100, 300, 200, selectedColor = SELECTED_COLOR)
        self.mediaTypeListBack = self.show_backList(30, 100, 200, 100, 0xFF0000)
        self.mediaTypeListBack.setVisible(False)
        self.addControl(self.mediaTypeList)
        self.mediaTypeList.addItem(str("Movie"))
        self.mediaTypeList.addItem(str("Episode"))
        self.mediaTypeList.setVisible(False)
        self.mediaTypeList.getListItem(0).select(True)

        self.watchStatusList = xbmcgui.ControlList(150, 100, 300, 200, selectedColor = SELECTED_COLOR)
        self.listBack2 = self.show_backList(180, 100, 220, 100, 0xFF0000)
        self.listBack2.setVisible(False)
        self.addControl(self.watchStatusList)
        self.watchStatusList.addItem(str("Watched"))
        self.watchStatusList.addItem(str("Unwatched"))
        self.watchStatusList.setVisible(False)

        self.ratingList = xbmcgui.ControlList(300, 100, 300, 200, selectedColor = SELECTED_COLOR)
        self.listBack3 = self.show_backList(330, 100, 220, 100, 0xFF0000)
        self.listBack3.setVisible(False)
        self.addControl(self.ratingList)
        for item in metaData.getRatings():
            self.ratingList.addItem(item[0])
        self.ratingList.setVisible(False)

        self.genreList = xbmcgui.ControlList(440, 100, 300, 200, selectedColor = SELECTED_COLOR)
        self.listBack4 = self.show_backList(470, 100, 220, 300, 0xFF0000)
        self.listBack4.setVisible(False)
        self.addControl(self.genreList)
        for item in metaData.getGenres():
            self.genreList.addItem(item[1])
        self.genreList.setVisible(False)

        # self.lengthList = xbmcgui.ControlList(600, 100, 300, 200)
        self.listBack5 = self.show_backList(625, 100, 300, 300, 0xFF0000)
        self.minInput = xbmcgui.ControlEdit(630, 100, 150, 30, "Minimum = ")
        self.maxInput = xbmcgui.ControlEdit(630, 150, 150, 30, "Maximum =  ")
        self.addControl(self.minInput)
        self.addControl(self.maxInput)
        self.minInput.setText("0")
        self.maxInput.setText("300")

        xbmc.log(f"minInput is at {self.minInput.getX()} {self.minInput.getY()}")
        xbmc.log(f"maxInput is at {self.maxInput.getX()} {self.maxInput.getY()}")
        # self.minInput.setPosition(700, 130)
        self.listBack5.setVisible(False)
        # self.addControl(self.lengthList)
        # self.lengthList.setVisible(False)
        self.minInput.setVisible(False)
        self.maxInput.setVisible(False)

        self.yearList = xbmcgui.ControlList(710, 100, 300, 200, selectedColor = SELECTED_COLOR)
        self.listBack6 = self.show_backList(740, 100, 480, 300, 0xFF0000)
        self.listBack6.setVisible(False)
        self.addControl(self.yearList)
        years = metaData.getYears()
        for item in sorted(years):
            self.yearList.addItem(item[0][:4])
        self.yearList.setVisible(False)

        self.tagsList = xbmcgui.ControlList(890, 100, 300, 200, selectedColor = SELECTED_COLOR)
        self.listBack7 = self.show_backList(920, 100, 400, 300, 0xFF0000)
        self.listBack7.setVisible(False)
        self.addControl(self.tagsList)
        for item in sorted(metaData.getTags()):
            self.tagsList.addItem(item[1])
        self.tagsList.setVisible(False)

        self.studioList = xbmcgui.ControlList(1040, 100, 260, 200, selectedColor = SELECTED_COLOR)
        self.listBack8 = self.show_backList(1070, 100, 480, 200, 0xFF0000)
        self.listBack8.setVisible(False)
        self.addControl(self.studioList)
        for item in metaData.getStudios():
            self.studioList.addItem(item[1])
        self.studioList.setVisible(False)

        self.mostWatchedList = xbmcgui.ControlList(0, 250, 300, 200, selectedColor = SELECTED_COLOR)
        self.listBack9 = self.show_backList(30, 250, 200, 100, 0xFF0000)
        self.listBack9.setVisible(False)
        self.addControl(self.mostWatchedList)
        self.mostWatchedList.addItem(str("On"))
        self.mostWatchedList.addItem(str("Off"))
        self.mostWatchedList.setVisible(False)

        self.castsList = xbmcgui.ControlList(150, 250, 300, 200, selectedColor = SELECTED_COLOR)
        self.listBack10 = self.show_backList(180, 250, 400, 300, 0xFF0000)
        self.listBack10.setVisible(False)
        self.addControl(self.castsList)
        for item in metaData.getActors():
            self.castsList.addItem(item[1])
        self.castsList.setVisible(False)

        self.directorList = xbmcgui.ControlList(300, 250, 300, 200, selectedColor = SELECTED_COLOR)
        self.listBack11 = self.show_backList(330, 250, 400, 300, 0xFF0000)
        self.listBack11.setVisible(False)
        self.addControl(self.directorList)
        for item in metaData.getDirectors():
            self.directorList.addItem(item[1])
        self.directorList.setVisible(False)

        # self.list12 = xbmcgui.ControlList(410, 250, 300, 200)
        # self.addControl(self.list12)
        # for item in dummy_list:
        #     self.list12.addItem(str(item))
        # self.list12.setVisible(False)


    def onAction(self, action: xbmcgui.Action) -> None:
        # print(f"action: {action}")
        if action == xbmcgui.ACTION_PREVIOUS_MENU or action == xbmcgui.ACTION_NAV_BACK:
            self.close()

        if action == xbmcgui.ACTION_MOUSE_LEFT_CLICK:
            control = self.getFocus()
            if control.getId() == self.mediaType.getId():
                self.mediaTypeListBack.setVisible(not self.mediaTypeListBack.isVisible())
                self.mediaTypeList.setVisible(not self.mediaTypeList.isVisible())
                text = "visible" if self.mediaTypeList.isVisible() else "invisible"
                text2 = "visible" if self.mediaTypeListBack.isVisible() else "invisible"
                xbmc.log("button was pressed, List Background is now " + text2)
                xbmc.log("button was pressed, list1 is now " + text)

            #The getting options thing
            if control.getId() == self.mediaTypeList.getId():
                global MediaTypeItem
                selectedMediaTypeItem = self.mediaTypeList.getSelectedItem()

                # xbmc.log(selectedMediaTypeItem.getLabel() + " was clicked from MediaType option")
                MediaTypeItem = selectedMediaTypeItem

                selectedMediaTypeItem.select(not selectedMediaTypeItem.isSelected())
                xbmc.log(f"{selectedMediaTypeItem.getLabel()} selected status: {selectedMediaTypeItem.isSelected()}")

            if control.getId() == self.watchStatus.getId():
                self.listBack2.setVisible(not self.listBack2.isVisible())
                self.watchStatusList.setVisible(not self.watchStatusList.isVisible())
                text = "visible" if self.watchStatusList.isVisible() else "invisible"
                text2 = "visible" if self.listBack2.isVisible() else "invisible"
                xbmc.log("button was pressed, List Background is now " + text2)
                xbmc.log("button was pressed, watchStatusList is now " + text)

            #The getting options thing
            if control.getId() == self.watchStatusList.getId():
                global WatchStatusItem
                selectedWatchStatusItem = self.watchStatusList.getSelectedItem()
                xbmc.log( selectedWatchStatusItem.getLabel() + " was clicked from WatchStatus option")
                WatchStatusItem = selectedWatchStatusItem

                selectedWatchStatusItem.select(not selectedWatchStatusItem.isSelected())
                xbmc.log(f"{selectedWatchStatusItem.getLabel()} selected status: {selectedWatchStatusItem.isSelected()}")



            if control.getId() == self.ratingButton.getId():
                self.listBack3.setVisible(not self.listBack3.isVisible())
                self.ratingList.setVisible(not self.ratingList.isVisible())
                text = "visible" if self.ratingList.isVisible() else "invisible"
                text2 = "visible" if self.listBack3.isVisible() else "invisible"
                xbmc.log("button was pressed, List Background is now " + text2)
                xbmc.log("button was pressed, ratingList is now " + text)

            #The getting options thing
            if control.getId() == self.ratingList.getId():
                global RatingItem
                selectedRatingItem = self.ratingList.getSelectedItem()
                xbmc.log( selectedRatingItem.getLabel() + " was clicked from Rating option")
                RatingItem = selectedRatingItem

                selectedRatingItem.select(not selectedRatingItem.isSelected())
                xbmc.log(f"{selectedRatingItem.getLabel()} selected status: {selectedRatingItem.isSelected()}")


            if control.getId() == self.genreButton.getId():
                self.listBack4.setVisible(not self.listBack4.isVisible())
                self.genreList.setVisible(not self.genreList.isVisible())
                text = "visible" if self.genreList.isVisible() else "invisible"
                text2 = "visible" if self.listBack4.isVisible() else "invisible"
                xbmc.log("button was pressed, List Background is now " + text2)
                xbmc.log("button was pressed, genreList is now " + text)

            #The getting options thing
            if control.getId() == self.genreList.getId():
                global GenreItem
                selectedGenreItem = self.genreList.getSelectedItem()
                xbmc.log( selectedGenreItem.getLabel() + " was clicked from Genre option")
                GenreItem = selectedGenreItem

                selectedGenreItem.select(not selectedGenreItem.isSelected())
                xbmc.log(f"{selectedGenreItem.getLabel()} selected status: {selectedGenreItem.isSelected()}")

            #For length
            if control.getId() == self.lengthList.getId():
                self.listBack5.setVisible(not self.listBack5.isVisible())
                # self.lengthList.setVisible(not self.lengthList.isVisible())
                # text = "visible" if self.lengthList.isVisible() else "invisible"
                text2 = "visible" if self.listBack5.isVisible() else "invisible"
                xbmc.log("button was pressed, List Background is now " + text2)
                # xbmc.log("button was pressed, lengthList is now " + text)
                self.minInput.setVisible(not self.minInput.isVisible())
                self.maxInput.setVisible(not self.maxInput.isVisible())
                text3 = "visible" if self.minInput.isVisible() else "invisible"
                text3 = "visible" if self.maxInput.isVisible() else "invisible"
                xbmc.log("button was pressed, min Button is now " + text3)
                minValue = self.minInput.getText()
                maxValue = self.maxInput.getText()
                xbmc.log(minValue + " is the input for minimum length")
                xbmc.log(maxValue + " is the input for maximum length")


            if control.getId() == self.yearButton.getId():
                self.listBack6.setVisible(not self.listBack6.isVisible())
                self.yearList.setVisible(not self.yearList.isVisible())
                text = "visible" if self.yearList.isVisible() else "invisible"
                text2 = "visible" if self.listBack6.isVisible() else "invisible"
                xbmc.log("button was pressed, List Background is now " + text2)
                xbmc.log("button was pressed, yearList is now " + text)

            #The getting options thing
            if control.getId() == self.yearList.getId():
                global YearItem
                selectedYearItem = self.yearList.getSelectedItem()
                xbmc.log( selectedYearItem.getLabel() + " was clicked from Year option")
                YearItem = selectedYearItem

                selectedYearItem.select(not selectedYearItem.isSelected())
                xbmc.log(f"{selectedYearItem.getLabel()} selected status: {selectedYearItem.isSelected()}")


            if control.getId() == self.tagsButton.getId():
                self.listBack7.setVisible(not self.listBack7.isVisible())
                self.tagsList.setVisible(not self.tagsList.isVisible())
                text = "visible" if self.tagsList.isVisible() else "invisible"
                text2 = "visible" if self.listBack7.isVisible() else "invisible"
                xbmc.log("button was pressed, List Background is now " + text2)
                xbmc.log("button was pressed, tagsList is now " + text)

            #The getting options thing
            if control.getId() == self.tagsList.getId():
                global TagsItem
                selectedTagItem = self.tagsList.getSelectedItem()
                xbmc.log( selectedTagItem.getLabel() + " was clicked from Tags option")
                TagsItem = selectedTagItem

                selectedTagItem.select(not selectedTagItem.isSelected())
                xbmc.log(f"{selectedTagItem.getLabel()} selected status: {selectedTagItem.isSelected()}")


            if control.getId() == self.studioButton.getId():
                self.listBack8.setVisible(not self.listBack8.isVisible())
                self.studioList.setVisible(not self.studioList.isVisible())
                text = "visible" if self.studioList.isVisible() else "invisible"
                text2 = "visible" if self.listBack8.isVisible() else "invisible"
                xbmc.log("button was pressed, List Background is now " + text2)
                xbmc.log("button was pressed, studioList is now " + text)

            #The getting options thing
            if control.getId() == self.studioList.getId():
                global StudioItem
                selectedStudioItem = self.studioList.getSelectedItem()
                xbmc.log( selectedStudioItem.getLabel() + " was clicked from Studio option")
                StudioItem = selectedStudioItem

                selectedStudioItem.select(not selectedStudioItem.isSelected())
                xbmc.log(f"{selectedStudioItem.getLabel()} selected status: {selectedStudioItem.isSelected()}")


            if control.getId() == self.mostWatched.getId():
                self.listBack9.setVisible(not self.listBack9.isVisible())
                self.mostWatchedList.setVisible(not self.mostWatchedList.isVisible())
                text = "visible" if self.mostWatchedList.isVisible() else "invisible"
                text2 = "visible" if self.listBack9.isVisible() else "invisible"
                xbmc.log("button was pressed, List Background is now " + text2)
                xbmc.log("button was pressed, mostWatchedList is now " + text)

            #The getting options thing
            if control.getId() == self.mostWatchedList.getId():
                global MostWatchedItem
                selectedMostWatchedItem = self.mostWatchedList.getSelectedItem()
                xbmc.log( selectedMostWatchedItem.getLabel() + " was clicked from MostWatched option")
                MostWatchedItem = selectedMostWatchedItem

                selectedMostWatchedItem.select(not selectedMostWatchedItem.isSelected())
                xbmc.log(f"{selectedMostWatchedItem.getLabel()} selected status: {selectedMostWatchedItem.isSelected()}")


            if control.getId() == self.castsButton.getId():
                self.listBack10.setVisible(not self.listBack10.isVisible())
                self.castsList.setVisible(not self.castsList.isVisible())
                text = "visible" if self.castsList.isVisible() else "invisible"
                text2 = "visible" if self.listBack10.isVisible() else "invisible"
                xbmc.log("button was pressed, List Background is now " + text2)
                xbmc.log("button was pressed, castsList is now " + text)
            
            #The getting options thing
            if control.getId() == self.castsList.getId():
                global CastsItem
                selectedCastsItem = self.castsList.getSelectedItem()
                xbmc.log( selectedCastsItem.getLabel() + " was clicked from Casts option")
                CastsItem = selectedCastsItem

                selectedCastsItem.select(not selectedCastsItem.isSelected())
                xbmc.log(f"{selectedCastsItem.getLabel()} selected status: {selectedCastsItem.isSelected()}")


            if control.getId() == self.directorButton.getId():
                self.listBack11.setVisible(not self.listBack11.isVisible())
                self.directorList.setVisible(not self.directorList.isVisible())
                text = "visible" if self.directorList.isVisible() else "invisible"
                text2 = "visible" if self.listBack11.isVisible() else "invisible"
                xbmc.log("button was pressed, List Background is now " + text2)
                xbmc.log("button was pressed, directorList is now " + text)

                #The getting options thing
            if control.getId() == self.directorList.getId():
                global DirectorItem
                selectedDirectorItem = self.directorList.getSelectedItem()
                xbmc.log( selectedDirectorItem.getLabel() + " was clicked from Director option")
                DirectorItem = selectedDirectorItem

                selectedDirectorItem.select(not selectedDirectorItem.isSelected())
                xbmc.log(f"{selectedDirectorItem.getLabel()} selected status: {selectedDirectorItem.isSelected()}")


            if control.getId() == self.includeList.getId():
                includeWindow = IncludeWindow()
                includeWindow.doModal()
                del includeWindow

            if control.getId() == self.saveButton.getId(): #//////////////////////////////////////////////////////////////////////////
                dialog = xbmcgui.Dialog().input("Give Your Saved Search A Name!")
                so = searchOptions.SearchOptions()

                mediaTypes = []
                for i in range(self.mediaTypeList.size()):
                    item = self.mediaTypeList.getListItem(i)
                    if item.isSelected():
                        mediaTypes.append(item.getLabel().lower())
                so.setMediaType(mediaTypes)
                if not so.getMediaType():
                    so.setMediaType(["movie"])

                watchStatuses = []
                for i in range(self.watchStatusList.size()):
                    item = self.watchStatusList.getListItem(i)
                    if item.isSelected() and item.getLabel().lower() == "unwatched":
                        watchStatuses.append(0)
                    elif item.isSelected() and item.getLabel().lower() == "watched":
                        watchStatuses.append(1)

                if watchStatuses:
                    so.setWatchStatus(watchStatuses)
                else:
                    so.setWatchStatus([0])

                ratings = []
                for i in range(self.ratingList.size()):
                    item = self.ratingList.getListItem(i)
                    if item.isSelected():
                        ratings.append(item.getLabel())
                so.setRating(ratings)
                
                genres = []
                for i in range(self.genreList.size()):
                    item = self.genreList.getListItem(i)
                    if item.isSelected():
                        genres.append(item.getLabel().lower())
                so.setGenre(genres)

                #Length Stuff
                minValue = self.minInput.getText()
                maxValue = self.maxInput.getText()

                # check if min and max value are numbers
                if not minValue.isdigit() or not maxValue.isdigit():
                    xbmcgui.Dialog().ok("Silly Human!", "Length min and max must be numbers! (specified in minutes)")
                    return
                
                so.setMINLength(int(minValue) * 60)
                so.setMAXLength(int(maxValue) * 60)

                years = []
                for i in range(self.yearList.size()):
                    item = self.yearList.getListItem(i)
                    if item.isSelected():
                        years.append(item.getLabel().lower())
                so.setYear(years)

                tagses = []
                for i in range(self.tagsList.size()):
                    item = self.tagsList.getListItem(i)
                    if item.isSelected():
                        tagses.append(item.getLabel().lower())
                so.setTag(tagses)

                studios = []
                for i in range(self.studioList.size()):
                    item = self.studioList.getListItem(i)
                    if item.isSelected():
                        studios.append(item.getLabel().lower())
                so.setStudio(studios)

                mostWatchedes = []
                for i in range(self.mostWatchedList.size()):
                    item = self.mostWatchedList.getListItem(i)
                    if item.isSelected():
                        mostWatchedes.append(item.getLabel().lower())
                so.setMostWatched(mostWatchedes)

                castes = []
                for i in range(self.castsList.size()):
                    item = self.castsList.getListItem(i)
                    if item.isSelected():
                        castes.append(item.getLabel().lower())
                so.setCast(castes)

                directores = []
                for i in range(self.directorList.size()):
                    item = self.directorList.getListItem(i)
                    if item.isSelected():
                        directores.append(item.getLabel().lower())
                so.setDirector(directores)
                
                
                searchProfile.addProfile(dialog, so)

            if control.getId() == self.playOneButton.getId(): #//////////////////////////////////////////////////////////////////////////////
                so = searchOptions.SearchOptions()

                # each thing is a list of stuff so we build a regular python list from kodi's lists
                # and put that into the search options object with set<option>(options)
                # where <option> is stuff like mediaType, genre, etc.
                # repeat for each search option that the gui can work with
                mediaTypes = []
                for i in range(self.mediaTypeList.size()):
                    item = self.mediaTypeList.getListItem(i)
                    if item.isSelected():
                        mediaTypes.append(item.getLabel().lower())
                so.setMediaType(mediaTypes)
                if not so.getMediaType():
                    so.setMediaType(["movie"])

                watchStatuses = []
                for i in range(self.watchStatusList.size()):
                    item = self.watchStatusList.getListItem(i)
                    if item.isSelected() and item.getLabel().lower() == "unwatched":
                        watchStatuses.append(0)
                    elif item.isSelected() and item.getLabel().lower() == "watched":
                        watchStatuses.append(1)

                if watchStatuses:
                    so.setWatchStatus(watchStatuses)
                else:
                    so.setWatchStatus([0])

                ratings = []
                for i in range(self.ratingList.size()):
                    item = self.ratingList.getListItem(i)
                    if item.isSelected():
                        ratings.append(item.getLabel())
                so.setRating(ratings)
                
                genres = []
                for i in range(self.genreList.size()):
                    item = self.genreList.getListItem(i)
                    if item.isSelected():
                        genres.append(item.getLabel().lower())
                so.setGenre(genres)

                #Length Stuff
                minValue = self.minInput.getText()
                maxValue = self.maxInput.getText()

                # check if min and max value are numbers
                if not minValue.isdigit() or not maxValue.isdigit():
                    xbmcgui.Dialog().ok("Silly Human!", "Length min and max must be numbers! (specified in minutes)")
                    return
                
                so.setMINLength(int(minValue) * 60)
                so.setMAXLength(int(maxValue) * 60)

                years = []
                for i in range(self.yearList.size()):
                    item = self.yearList.getListItem(i)
                    if item.isSelected():
                        years.append(item.getLabel().lower())
                so.setYear(years)

                tagses = []
                for i in range(self.tagsList.size()):
                    item = self.tagsList.getListItem(i)
                    if item.isSelected():
                        tagses.append(item.getLabel().lower())
                so.setTag(tagses)

                studios = []
                for i in range(self.studioList.size()):
                    item = self.studioList.getListItem(i)
                    if item.isSelected():
                        studios.append(item.getLabel().lower())
                so.setStudio(studios)

                mostWatchedes = []
                for i in range(self.mostWatchedList.size()):
                    item = self.mostWatchedList.getListItem(i)
                    if item.isSelected():
                        mostWatchedes.append(item.getLabel().lower())
                so.setMostWatched(mostWatchedes)

                castes = []
                for i in range(self.castsList.size()):
                    item = self.castsList.getListItem(i)
                    if item.isSelected():
                        castes.append(item.getLabel().lower())
                so.setCast(castes)

                directores = []
                for i in range(self.directorList.size()):
                    item = self.directorList.getListItem(i)
                    if item.isSelected():
                        directores.append(item.getLabel().lower())
                so.setDirector(directores)

                so.setPBFunction(1)
                if OurFilter.filter(so):
                    playOneWindow = guiPlayWindows.PlayOneWindow()
                    playOneWindow.setResults(so)
                    playOneWindow.doModal()
                    del playOneWindow
                else:
                    xbmcgui.Dialog().ok("Error", "There Is Nothing!!")

            if control.getId() == self.loopPlayButton.getId(): #////////////////////////////////////////////////////////////////////////
                so = searchOptions.SearchOptions()

                # each thing is a list of stuff so we build a regular python list from kodi's lists
                # and put that into the search options object with set<option>(options)
                # where <option> is stuff like mediaType, genre, etc.
                # repeat for each search option that the gui can work with
                mediaTypes = []
                for i in range(self.mediaTypeList.size()):
                    item = self.mediaTypeList.getListItem(i)
                    if item.isSelected():
                        mediaTypes.append(item.getLabel().lower())
                so.setMediaType(mediaTypes)
                if not so.getMediaType():
                    so.setMediaType(["movie"])

                watchStatuses = []
                for i in range(self.watchStatusList.size()):
                    item = self.watchStatusList.getListItem(i)
                    if item.isSelected() and item.getLabel().lower() == "unwatched":
                        watchStatuses.append(0)
                    elif item.isSelected() and item.getLabel().lower() == "watched":
                        watchStatuses.append(1)

                if watchStatuses:
                    so.setWatchStatus(watchStatuses)
                else:
                    so.setWatchStatus([0])

                ratings = []
                for i in range(self.ratingList.size()):
                    item = self.ratingList.getListItem(i)
                    if item.isSelected():
                        ratings.append(item.getLabel())
                so.setRating(ratings)
                
                genres = []
                for i in range(self.genreList.size()):
                    item = self.genreList.getListItem(i)
                    if item.isSelected():
                        genres.append(item.getLabel().lower())
                so.setGenre(genres)

                #Length Stuff
                minValue = self.minInput.getText()
                maxValue = self.maxInput.getText()

                # check if min and max value are numbers
                if not minValue.isdigit() or not maxValue.isdigit():
                    xbmcgui.Dialog().ok("Silly Human!", "Length min and max must be numbers! (specified in minutes)")
                    return
                
                so.setMINLength(int(minValue) * 60)
                so.setMAXLength(int(maxValue) * 60)

                years = []
                for i in range(self.yearList.size()):
                    item = self.yearList.getListItem(i)
                    if item.isSelected():
                        years.append(item.getLabel().lower())
                so.setYear(years)

                tagses = []
                for i in range(self.tagsList.size()):
                    item = self.tagsList.getListItem(i)
                    if item.isSelected():
                        tagses.append(item.getLabel().lower())
                so.setTag(tagses)

                studios = []
                for i in range(self.studioList.size()):
                    item = self.studioList.getListItem(i)
                    if item.isSelected():
                        studios.append(item.getLabel().lower())
                so.setStudio(studios)

                mostWatchedes = False
                for i in range(self.mostWatchedList.size()):
                    item = self.mostWatchedList.getListItem(i)
                    if item.isSelected():
                        if item.getLabel().lower() == 'on':
                            mostWatchedes = True
                so.setMostWatched(mostWatchedes)

                castes = []
                for i in range(self.castsList.size()):
                    item = self.castsList.getListItem(i)
                    if item.isSelected():
                        castes.append(item.getLabel().lower())
                so.setCast(castes)

                directores = []
                for i in range(self.directorList.size()):
                    item = self.directorList.getListItem(i)
                    if item.isSelected():
                        directores.append(item.getLabel().lower())
                so.setDirector(directores)

                so.setPBFunction(3)
                if OurFilter.filter(so):
                    loopPlay = guiPlayWindows.LoopPlayWindow()
                    loopPlay.setResults(so)
                    loopPlay.doModal()
                    del loopPlay
                else:
                    xbmcgui.Dialog().ok("Error", "Your Playlist is empty!")

            # start of filter stuff
            if control.getId() == self.showListButton.getId():  #//////////////////////////////////////////////////////////////////////////
                # show list button clicked, generate search options from gui
                so = searchOptions.SearchOptions()

                # each thing is a list of stuff so we build a regular python list from kodi's lists
                # and put that into the search options object with set<option>(options)
                # where <option> is stuff like mediaType, genre, etc.
                # repeat for each search option that the gui can work with
                mediaTypes = []
                for i in range(self.mediaTypeList.size()):
                    item = self.mediaTypeList.getListItem(i)
                    if item.isSelected():
                        mediaTypes.append(item.getLabel().lower())
                so.setMediaType(mediaTypes)
                if not so.getMediaType():
                    so.setMediaType(["movie"])

                watchStatuses = []
                for i in range(self.watchStatusList.size()):
                    item = self.watchStatusList.getListItem(i)

                    if item.isSelected() and item.getLabel().lower() == "unwatched":
                        watchStatuses.append(0)
                    elif item.isSelected() and item.getLabel().lower() == "watched":
                        watchStatuses.append(1)

                if watchStatuses:
                    so.setWatchStatus(watchStatuses)
                else:
                    so.setWatchStatus([0, 0])

                ratings = []
                for i in range(self.ratingList.size()):
                    item = self.ratingList.getListItem(i)
                    if item.isSelected():
                        ratings.append(item.getLabel())
                so.setRating(ratings)
                
                genres = []
                for i in range(self.genreList.size()):
                    item = self.genreList.getListItem(i)
                    if item.isSelected():
                        genres.append(item.getLabel().lower())
                so.setGenre(genres)

                #Length Stuff
                minValue = self.minInput.getText()
                maxValue = self.maxInput.getText()

                # check if min and max value are numbers
                if not minValue.isdigit() or not maxValue.isdigit():
                    xbmcgui.Dialog().ok("Silly Human!", "Length min and max must be numbers! (specified in minutes)")
                    return
                
                so.setMINLength(int(minValue) * 60)
                so.setMAXLength(int(maxValue) * 60)

                years = []
                for i in range(self.yearList.size()):
                    item = self.yearList.getListItem(i)
                    if item.isSelected():
                        years.append(item.getLabel().lower())
                so.setYear(years)

                tagses = []
                for i in range(self.tagsList.size()):
                    item = self.tagsList.getListItem(i)
                    if item.isSelected():
                        tagses.append(item.getLabel().lower())
                so.setTag(tagses)

                studios = []
                for i in range(self.studioList.size()):
                    item = self.studioList.getListItem(i)
                    if item.isSelected():
                        studios.append(item.getLabel().lower())
                so.setStudio(studios)

                mostWatchedes = []
                for i in range(self.mostWatchedList.size()):
                    item = self.mostWatchedList.getListItem(i)
                    if item.isSelected():
                        mostWatchedes.append(item.getLabel().lower())
                so.setMostWatched(mostWatchedes)

                castes = []
                for i in range(self.castsList.size()):
                    item = self.castsList.getListItem(i)
                    if item.isSelected():
                        castes.append(item.getLabel().lower())
                so.setCast(castes)

                directores = []
                for i in range(self.directorList.size()):
                    item = self.directorList.getListItem(i)
                    if item.isSelected():
                        directores.append(item.getLabel().lower())
                so.setDirector(directores)

                # TODO take into account watch status later- True or false. 0 ones that have been. 1 have not. 0 and 1 get passed is both.

                #Add this to LoopPLay and PlayOne
                so.setPBFunction(2)
                if OurFilter.filter(so):
                    showListWindow = guiPlayWindows.ShowListWindow()
                    showListWindow.setResults(so)
                    showListWindow.doModal()
                    del showListWindow
                else:
                    xbmcgui.Dialog().ok("Error", "Your list is empty!")

                #End of add things to Loopplay and PlayOne

                # print("Filter results:")
                # for result in results:
                #     xbmc.log(f"{result}")
                # xbmc.log(f"backup print: {results}")
            # end of the code I tried testing
            if control.getId() == self.activateTime.getId():
                xbmc.log("shutting down some time...")
                shut.shutdownTime([int(self.hourInput.getText()), int(self.minuteInput.getText())])
            

#Global Variables for options
SELECTED_COLOR = "0xFF000000" #For the highlightedness of the selected list item

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
