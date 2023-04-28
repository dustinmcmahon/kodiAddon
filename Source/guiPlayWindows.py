import xbmcgui
import xbmc
import searchOptions
import filter as OurFilter
import gui
from typing import List
import urllib.parse
import xbmcvfs
import urllib.parse


class PlayOneWindow(xbmcgui.Window):

    def setResults(self, so) -> None:
        so.setPBFunction(1)
        results = OurFilter.filter(so)
        """ListShown = xbmcgui.ControlList(400, 400, 200, 400)
        self.addControl(ListShown)
        for something in results:
            item = xbmcgui.ListItem(something["title"])
            ListShown.addItem(item)

            

        self.image = xbmcgui.ControlImage(400, 450, 200, 400, "")
        self.addControl(self.image)

        if len(results) > 0:
            imageUrl = urllib.parse.unquote(results[0]["art"]["poster"])
            imageUrl = imageUrl[len("image://"):][:-1]
            self.image.setImage(imageUrl)"""

        # Immediately start playing when PlayOne is clicked.
        if results:
            player = xbmc.Player()
            player.play(results[0]['file'])


class ShowListWindow(xbmcgui.Window):
    ITEMS_PER_PAGE = 8
    HALF_PAGE = ITEMS_PER_PAGE // 2
    LOOPY_WIDTH = 150  # Space from bottom of screen to bottom list
    LOOPY_HEIGHT = 10
    LOOPY_IMAGE_HEIGHT = 200  # thumbnail
    loopyimages = []
    movieButton = []

    loopyGrid: list[xbmcgui.ControlLabel]
    loopyGridImages:  list[xbmcgui.ControlImage]

    def show_Setting(self, x, y, radius, color):
        settingPath = gui.imagesFolder + "Settings.png"
        setting = xbmcgui.ControlImage(
            x, y, radius, radius, settingPath, color)
        self.addControl(setting)

    def __init__(self) -> None:
        self.page = 0
        self.loopyGrid = []
        self.loopyGridImages = []
        for i in range(self.ITEMS_PER_PAGE):
            x = 200 * ((i % self.HALF_PAGE) + 1)  # Space from left screen
            if i < self.HALF_PAGE:
                # Space from the top of the screen to the top of the list
                self.loopyGrid.append(xbmcgui.ControlLabel(
                    x, 150, self.LOOPY_WIDTH, self.LOOPY_HEIGHT, f"loopy do {i}"))
                self.loopyGridImages.append(xbmcgui.ControlImage(
                    x, 200, self.LOOPY_WIDTH, self.LOOPY_IMAGE_HEIGHT, ""))
                # self.movieButton.append(xbmcgui.ControlButton( x , 200, self.LOOPY_WIDTH, self.LOOPY_IMAGE_HEIGHT, " "))

            else:
                # Space in height between top and bottom lists
                self.loopyGrid.append(xbmcgui.ControlLabel(
                    x, 400, self.LOOPY_WIDTH, self.LOOPY_HEIGHT, f"loopy do {i}"))
                self.loopyGridImages.append(xbmcgui.ControlImage(
                    x, 450, self.LOOPY_WIDTH, self.LOOPY_IMAGE_HEIGHT, ""))
                # self.movieButton.append(xbmcgui.ControlButton( x , 200, self.LOOPY_WIDTH, self.LOOPY_IMAGE_HEIGHT, " "))

        self.addControls(self.loopyGrid)
        self.addControls(self.loopyGridImages)

        self.forwardPageButton = xbmcgui.ControlButton(
            1080, 350, 150, 100, "    ")
        self.addControl(self.forwardPageButton)

        self.backwardPageButton = xbmcgui.ControlButton(
            0, 350, 150, 100, "    ")
        self.addControl(self.backwardPageButton)

        self.results = None

    def setResults(self, so: searchOptions.SearchOptions) -> None:
        so.setPBFunction(2)
        results = OurFilter.filter(so)

        start = self.page * self.ITEMS_PER_PAGE
        end = min(len(results), self.page * self.ITEMS_PER_PAGE + 4)
        chunk = results[start:end]

        """for i, v in enumerate(chunk):
            label = self.loopyGrid[i]
            label.setLabel(v["title"])
            image = self.loopyGridImages[i]
            imageUrl = urllib.parse.unquote(v["art"]["poster"])
            imageUrl = imageUrl[len("image://"):][:-1]
            image.setImage(imageUrl)"""

        for i, v in enumerate(chunk):
            label = self.loopyGrid[i]
            label.setLabel(v["title"])
            image = self.loopyGridImages[i]
            if 'episodeid' in v:
                imageUrl = urllib.parse.unquote(v["art"]["thumb"])
            else:
                imageUrl = urllib.parse.unquote(v["art"]["poster"])
            imageUrl = imageUrl[len("image://"):][:-1]
            image.setImage(imageUrl)

        for i in range(len(chunk), self.ITEMS_PER_PAGE):
            self.loopyGrid[i].setVisible(False)
            self.loopyGridImages[i].setVisible(False)

        self.show_Setting(10, 10, 300, 0xFF0000)

        self.show_Setting(10, 10, 300, 0xFF0000)
# Conrol image with control button underneath it.


class LoopPlayWindow(xbmcgui.Window):
    ITEMS_PER_PAGE = 8
    HALF_PAGE = ITEMS_PER_PAGE // 2
    LOOPY_WIDTH = 150  # Space from bottom of screen to bottom list
    LOOPY_HEIGHT = 10
    LOOPY_IMAGE_HEIGHT = 200  # thumbnail
    loopyimages = []
    movieButton = []

    loopyGrid: List[xbmcgui.ControlLabel]
    LoopyGridImages:  List[xbmcgui.ControlImage]

    def show_circle(self, x, y, radius, color):
        circlePath = gui.imagesFolder + "circle.png"
        circle = xbmcgui.ControlImage(x, y, radius, radius, circlePath, color)
        self.addControl(circle)

    def __init__(self) -> None:
        self.page = 0
        self.loopyGrid = []
        self.loopyGridImages = []
        for i in range(self.ITEMS_PER_PAGE):
            x = 200 * ((i % self.HALF_PAGE) + 1)  # Space from left screen
            if i < self.HALF_PAGE:
                # Space from the top of the screen to the top of the list
                self.loopyGrid.append(xbmcgui.ControlLabel(
                    x, 150, self.LOOPY_WIDTH, self.LOOPY_HEIGHT, f"loopy do {i}"))
                self.loopyGridImages.append(xbmcgui.ControlImage(
                    x, 200, self.LOOPY_WIDTH, self.LOOPY_IMAGE_HEIGHT, ""))
                # self.movieButton.append(xbmcgui.ControlButton( x , 200, self.LOOPY_WIDTH, self.LOOPY_IMAGE_HEIGHT, " "))

            else:
                # Space in height between top and bottom lists
                self.loopyGrid.append(xbmcgui.ControlLabel(
                    x, 400, self.LOOPY_WIDTH, self.LOOPY_HEIGHT, f"loopy do {i}"))
                self.loopyGridImages.append(xbmcgui.ControlImage(
                    x, 450, self.LOOPY_WIDTH, self.LOOPY_IMAGE_HEIGHT, ""))
                # self.movieButton.append(xbmcgui.ControlButton( x , 200, self.LOOPY_WIDTH, self.LOOPY_IMAGE_HEIGHT, " "))

        self.addControls(self.loopyGrid)
        self.addControls(self.loopyGridImages)

        self.forwardPageButton = xbmcgui.ControlButton(
            1080, 350, 150, 100, "    ")
        self.addControl(self.forwardPageButton)

        self.backwardPageButton = xbmcgui.ControlButton(
            0, 350, 150, 100, "    ")
        self.addControl(self.backwardPageButton)

        self.results = None

    def setResults(self, so: searchOptions.SearchOptions) -> None:
        so.setPBFunction(3)
        results = OurFilter.filter(so)

        start = self.page * self.ITEMS_PER_PAGE
        end = min(len(results), self.page * self.ITEMS_PER_PAGE + 4)
        chunk = results[start:end]

        for i, v in enumerate(chunk):
            label = self.loopyGrid[i]
            label.setLabel(v["title"])
            image = self.loopyGridImages[i]
            if 'episodeid' in v:
                imageUrl = urllib.parse.unquote(v["art"]["thumb"])
            else:
                imageUrl = urllib.parse.unquote(v["art"]["poster"])
            imageUrl = imageUrl[len("image://"):][:-1]
            image.setImage(imageUrl)

        for i in range(len(chunk), self.ITEMS_PER_PAGE):
            self.loopyGrid[i].setVisible(False)
            self.loopyGridImages[i].setVisible(False)

    # def onAction(self, action: xbmcgui.Action) -> None:
    #     # print(f"action: {action}")
    #     if action == xbmcgui.ACTION_PREVIOUS_MENU or action == xbmcgui.ACTION_NAV_BACK:
    #         self.close()

    #     if action == xbmcgui.ACTION_MOUSE_LEFT_CLICK:
    #         control = self.getFocus()

    #         if control.getId() == self.watchStatus.getId():
    #             self.listBack2.setVisible(not self.listBack2.isVisible())
    #             self.watchStatusList.setVisible(not self.watchStatusList.isVisible())
    #             text = "visible" if self.watchStatusList.isVisible() else "invisible"
    #             text2 = "visible" if self.listBack2.isVisible() else "invisible"
    #             xbmc.log("button was pressed, List Background is now " + text2)
    #             xbmc.log("button was pressed, watchStatusList is now " + text)

    #         #The getting options thing
    #         if control.getId() == self.watchStatusList.getId():
    #             global WatchStatusItem
    #             selectedWatchStatusItem = self.watchStatusList.getSelectedItem()
    #             xbmc.log( selectedWatchStatusItem.getLabel() + " was clicked from WatchStatus option")
    #             WatchStatusItem = selectedWatchStatusItem

    #             selectedWatchStatusItem.select(not selectedWatchStatusItem.isSelected())
    #             xbmc.log(f"{selectedWatchStatusItem.getLabel()} selected status: {selectedWatchStatusItem.isSelected()}")
