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
    def show_Play(self, x, y, radius, color):
        playPath = gui.imagesFolder + "PLAY.png"
        play = xbmcgui.ControlImage(x, y, radius, radius, playPath, color)
        self.addControl(play)
    
    def setResults(self, so) -> None:
        so.setPBFunction(1)
        self.results = OurFilter.filter(so)
        ListShown = xbmcgui.ControlList(470, 150, 600, 400)
        self.addControl(ListShown)
        for something in self.results:
            item = xbmcgui.ListItem(something["title"])
            ListShown.addItem(item)

        self.PlayButton2 = xbmcgui.ControlButton(1125, 625, 150, 100, "    ")
        self.addControl(self.PlayButton2)
        self.show_Play (1010, 500, 400, 0xFF0000)
        self.PlayButton = xbmcgui.ControlButton(500, 200, 300, 400, "    ")
        self.addControl(self.PlayButton)
        self.image = xbmcgui.ControlImage(500, 200, 300, 400, "")
        self.addControl(self.image)

        self.show_Setting(10, 10, 400, 0xFF0000)
        
        if len(self.results) > 0:
            v = self.results[0]
            imageUrl = ""
            if 'episodeid' in self.results[0]:
                imageUrl = urllib.parse.unquote(v["art"]["thumb"])
            else:
                imageUrl = urllib.parse.unquote(v["art"]["poster"])
            imageUrl = imageUrl[len("image://"):][:-1]
            self.image.setImage(imageUrl)

    def show_Setting(self, x, y, radius, color):
        settingPath = gui.imagesFolder + "Settings.png"
        self.settingsButton = xbmcgui.ControlButton(x, y, 226, 77, "")
        setting = xbmcgui.ControlImage(x, y, radius, radius, settingPath, color)
        self.addControl(self.settingsButton)
        self.addControl(setting)


    def onAction(self, action: xbmcgui.Action) -> None:
        if action == xbmcgui.ACTION_PREVIOUS_MENU or action == xbmcgui.ACTION_NAV_BACK:
            self.close()

        if action == xbmcgui.ACTION_MOUSE_LEFT_CLICK:
            control = self.getFocus()

            if control.getId() == self.PlayButton.getId():
                player = xbmc.Player()
                player.play(self.results[0]['file'])

            if control.getId() == self.PlayButton2.getId():
                player = xbmc.Player()
                player.play(self.results[0]['file'])

            if control.getId() == self.settingsButton.getId():
                self.close()


class ShowListWindow(xbmcgui.Window):
    ITEMS_PER_PAGE = 8
    HALF_PAGE = ITEMS_PER_PAGE // 2
    LOOPY_WIDTH = 150 # Space from bottom of screen to bottom list
    LOOPY_HEIGHT = 10
    LOOPY_IMAGE_HEIGHT = 200 #thumbnail
    loopyimages = []
    movieButton = []

    loopyGrid: List[xbmcgui.ControlLabel]
    loopyGridImages:  List[xbmcgui.ControlImage]
    
    def show_Play(self, x, y, radius, color):
        playPath = gui.imagesFolder + "PLAY.png"
        play = xbmcgui.ControlImage(x, y, radius, radius, playPath, color)
        self.addControl(play)

    def show_Right(self, x, y, radius, color):
        RpagePath = gui.imagesFolder + "RightPage.png"
        Rpage = xbmcgui.ControlImage(x, y, radius, radius, RpagePath, color)
        self.addControl(Rpage)

    def show_Left(self, x, y, radius, color):
        LpagePath = gui.imagesFolder + "LeftPage.png"
        Lpage = xbmcgui.ControlImage(x, y, radius, radius, LpagePath, color)
        self.addControl(Lpage)

    def show_Setting(self, x, y, radius, color):
        settingPath = gui.imagesFolder + "Settings.png"
        self.settingsButton = xbmcgui.ControlButton(x, y, 226, 77, "")
        setting = xbmcgui.ControlImage(x, y, radius, radius, settingPath, color)
        self.addControl(self.settingsButton)
        self.addControl(setting)
    

    def __init__(self) -> None:
        self.page = 0
        self.maxPage = 0
        self.loopyGrid = []
        self.loopyGridImages = []
        self.loopyGridButtons = []
        for i in range(self.ITEMS_PER_PAGE):
            x = 200 * ((i % self.HALF_PAGE) + 1) # Space from left screen 
            if i < self.HALF_PAGE:
                self.loopyGrid.append(xbmcgui.ControlLabel(x, 150, self.LOOPY_WIDTH, self.LOOPY_HEIGHT, f"loopy do {i}")) #Space from the top of the screen to the top of the list
                self.loopyGridImages.append(xbmcgui.ControlImage(x, 200, self.LOOPY_WIDTH, self.LOOPY_IMAGE_HEIGHT, ""))
                self.loopyGridButtons.append(xbmcgui.ControlButton(x, 200, self.LOOPY_WIDTH, self.LOOPY_IMAGE_HEIGHT, ""))
            else:
                self.loopyGrid.append(xbmcgui.ControlLabel(x, 450, self.LOOPY_WIDTH, self.LOOPY_HEIGHT, f"loopy do {i}")) #Space in height between top and bottom lists
                self.loopyGridImages.append(xbmcgui.ControlImage(x, 500, self.LOOPY_WIDTH, self.LOOPY_IMAGE_HEIGHT, ""))
                self.loopyGridButtons.append(xbmcgui.ControlButton(x, 500, self.LOOPY_WIDTH, self.LOOPY_IMAGE_HEIGHT, ""))
                
        self.addControls(self.loopyGridButtons)
        self.addControls(self.loopyGrid)
        self.addControls(self.loopyGridImages)

        self.forwardPageButton = xbmcgui.ControlButton(1060, 342, 200, 100, "    ")
        self.addControl(self.forwardPageButton)

        self.backwardPageButton = xbmcgui.ControlButton(20, 342, 200, 100, "    ")
        self.addControl(self.backwardPageButton)

        self.results = None

    #Add a nothing in list, Nothing is in your list
    #Make it so that the include and exclude images show up tonight
    #Make it so that the objects are saved when i click the save button.
    #Try to pull everything and make it work, integrate everything.

    def onAction(self, action: xbmcgui.Action) -> None:
        if action == xbmcgui.ACTION_PREVIOUS_MENU or action == xbmcgui.ACTION_NAV_BACK:
            self.close()

        if action == xbmcgui.ACTION_MOUSE_LEFT_CLICK:
            control = self.getFocus()

            if control.getId() == self.forwardPageButton.getId():
                if (self.page + 1) <= self.maxPage:
                    self.page += 1
                    self.reloadLoopy()

            if control.getId() == self.backwardPageButton.getId():
                if (self.page - 1) >= 0:
                    self.page -= 1
                    self.reloadLoopy()

            for i, b in enumerate(self.loopyGridButtons):
                if b.getId() == control.getId():
                    movieIndex = self.page * self.ITEMS_PER_PAGE + i
                    player = xbmc.Player()
                    player.play(self.results[movieIndex]["file"])
                    break

            if control.getId() == self.settingsButton.getId():
                self.close()

    def reloadLoopy(self):
        self.so.setPBFunction(2)
        results = OurFilter.filter(self.so)
        self.results = results
        self.maxPage = len(results) // self.ITEMS_PER_PAGE

        start = self.page * self.ITEMS_PER_PAGE
        end = min(len(results), self.page * self.ITEMS_PER_PAGE + self.ITEMS_PER_PAGE)
        chunk = results[start:end]

        for i, v in enumerate(chunk):
            self.loopyGrid[i].setVisible(True)
            self.loopyGridImages[i].setVisible(True)
            label = self.loopyGrid[i]
            label.setLabel(v["title"])
            image = self.loopyGridImages[i]
            if 'episodeid' in v:
                imageUrl = urllib.parse.unquote(v["art"]["thumb"])
            else:
                imageUrl = urllib.parse.unquote(v["art"]["poster"])
            imageUrl = imageUrl[len("image://"):][:-1]
            image.setImage(imageUrl)

        for i in range(len(chunk), self.ITEMS_PER_PAGE ):
            self.loopyGrid[i].setVisible(False)
            self.loopyGridImages[i].setVisible(False)
            self.loopyGridButtons[i].setVisible(False)

    
    def setResults(self, so: searchOptions.SearchOptions) -> None:
        self.so = so
        self.reloadLoopy()
       
        self.show_Setting (10, 10, 400, 0xFF0000)
        self.show_Play (600, 600, 350, 0xFF0000)

        self.show_Right (1080, 325, 200, 0xFF0000)
        self.show_Left (0, 325, 200, 0xFF0000)

class LoopPlayWindow(xbmcgui.Window):
    ITEMS_PER_PAGE = 8
    HALF_PAGE = ITEMS_PER_PAGE // 2
    LOOPY_WIDTH = 150  # Space from bottom of screen to bottom list
    LOOPY_HEIGHT = 10
    LOOPY_IMAGE_HEIGHT = 200  # thumbnail
    loopyimages = []
    movieButtons = []

    loopyGrid: List[xbmcgui.ControlLabel]
    loopyGridImages:  List[xbmcgui.ControlImage]

    def show_circle(self, x, y, radius, color):
        circlePath = gui.imagesFolder + "circle.png"
        circle = xbmcgui.ControlImage(x, y, radius, radius, circlePath, color)
        self.addControl(circle)

    def show_Setting(self, x, y, radius, color):
        settingPath = gui.imagesFolder + "Settings.png"
        self.settingsButton = xbmcgui.ControlButton(x, y, 226, 77, "")
        setting = xbmcgui.ControlImage(x, y, radius, radius, settingPath, color)
        self.addControl(self.settingsButton)
        self.addControl(setting)

    def show_Play(self, x, y, radius, color):
        playPath = gui.imagesFolder + "PLAY.png"
        play = xbmcgui.ControlImage(x, y, radius, radius, playPath, color)
        self.addControl(play)

    def show_Right(self, x, y, radius, color):
        RpagePath = gui.imagesFolder + "RightPage.png"
        Rpage = xbmcgui.ControlImage(x, y, radius, radius, RpagePath, color)
        self.addControl(Rpage)

    def show_Left(self, x, y, radius, color):
        LpagePath = gui.imagesFolder + "LeftPage.png"
        Lpage = xbmcgui.ControlImage(x, y, radius, radius, LpagePath, color)
        self.addControl(Lpage)



    def __init__(self) -> None:
        self.page = 0
        self.maxPage = 0
        self.loopyGrid = []
        self.loopyGridImages = []
        for i in range(self.ITEMS_PER_PAGE):
            x = 200 * ((i % self.HALF_PAGE) + 1)  # Space from left screen
            if i < self.HALF_PAGE:
                self.loopyGrid.append(xbmcgui.ControlLabel(x, 150, self.LOOPY_WIDTH, self.LOOPY_HEIGHT, f"loopy do {i}")) #Space from the top of the screen to the top of the list
                self.loopyGridImages.append(xbmcgui.ControlImage(x, 200, self.LOOPY_WIDTH, self.LOOPY_IMAGE_HEIGHT, ""))
            else:
                self.loopyGrid.append(xbmcgui.ControlLabel(x, 450, self.LOOPY_WIDTH, self.LOOPY_HEIGHT, f"loopy do {i}")) #Space in height between top and bottom lists
                self.loopyGridImages.append(xbmcgui.ControlImage(x, 500, self.LOOPY_WIDTH, self.LOOPY_IMAGE_HEIGHT, ""))
                
        
        self.addControls(self.loopyGrid)
        self.addControls(self.loopyGridImages)

        self.forwardPageButton = xbmcgui.ControlButton(1060, 342, 200, 100, "    ")
        self.addControl(self.forwardPageButton)

        self.backwardPageButton = xbmcgui.ControlButton(20, 342, 200, 100, "    ")
        self.addControl(self.backwardPageButton)
    

        self.results = None

    def setResults(self, so: searchOptions.SearchOptions) -> None:
        self.so = so
        self.reloadLoopy()

        self.show_Setting (10, 10, 400, 0xFF0000)
        self.show_Play (1010, 500, 400, 0xFF0000)

        self.show_Right (1080, 325, 200, 0xFF0000)
        self.show_Left (0, 325, 200, 0xFF0000)


        

    def reloadLoopy(self):
        self.so.setPBFunction(3)
        results = OurFilter.filter(self.so)
        self.maxPage = len(results) // self.ITEMS_PER_PAGE

        start = self.page * self.ITEMS_PER_PAGE
        end = min(len(results), self.page * self.ITEMS_PER_PAGE + self.ITEMS_PER_PAGE)
        chunk = results[start:end]

        for i, v in enumerate(chunk):
            self.loopyGrid[i].setVisible(True)
            self.loopyGridImages[i].setVisible(True)
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

    def onAction(self, action: xbmcgui.Action) -> None:
        if action == xbmcgui.ACTION_PREVIOUS_MENU or action == xbmcgui.ACTION_NAV_BACK:
            self.close()

        if action == xbmcgui.ACTION_MOUSE_LEFT_CLICK:
            control = self.getFocus()

            if control.getId() == self.forwardPageButton.getId():
                if (self.page + 1) <= self.maxPage:
                    self.page += 1
                    self.reloadLoopy()

            if control.getId() == self.backwardPageButton.getId():
                if (self.page - 1) >= 0:
                    self.page -= 1
                    self.reloadLoopy()

            if control.getId() == self.settingsButton.getId():
                self.close()