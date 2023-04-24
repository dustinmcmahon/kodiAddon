import xbmcgui
import xbmc
import xbmcaddon
import metaData
import searchOptions
import filter as OurFilter
import gui


class PlayOneWindow(xbmcgui.Window):
    def setResults(self, so) -> None:
        so.setPBFunction(1)
        results = OurFilter.filter(so)
        ListShown = xbmcgui.ControlList(400, 400, 200, 400)
        self.addControl(ListShown)
        for something in results:
            item = xbmcgui.ListItem(something["title"])
            ListShown.addItem(item)


class ShowListWindow(xbmcgui.Window):
    def setResults(self, so: searchOptions.SearchOptions) -> None:
        so.setPBFunction(2)
        results = OurFilter.filter(so)
        ListShown = xbmcgui.ControlList(400, 400, 200, 400)
        self.addControl(ListShown)
        for something in results:
            item = xbmcgui.ListItem(something["title"])
            ListShown.addItem(item)
#Conrol image with control button underneath it.

class LoopPlayWindow(xbmcgui.Window):
    ITEMS_PER_PAGE = 8
    HALF_PAGE = ITEMS_PER_PAGE // 2
    LOOPY_WIDTH = 500 #Space from bottom of screen to bottom list
    LOOPY_HEIGHT = 10

    loopyGrid: list[xbmcgui.ControlLabel]

    def __init__(self) -> None:
        self.page = 0
        self.loopyGrid = []
        for i in range(self.ITEMS_PER_PAGE):
            x = 300 * ((i % self.HALF_PAGE) + 1) #Space from left screen 
            if i < self.HALF_PAGE:
                self.loopyGrid.append(xbmcgui.ControlLabel(x, 150, self.LOOPY_WIDTH, self.LOOPY_HEIGHT, f"loopy do {i}")) #Space from the top of the screen to the top of the list
            else:
                self.loopyGrid.append(xbmcgui.ControlLabel(x, 400, self.LOOPY_WIDTH, self.LOOPY_HEIGHT, f"loopy do {i}")) #Space in height between top and bottom lists
        self.addControls(self.loopyGrid)

        self.forwardPageButton = xbmcgui.ControlButton(1080, 350, 200, 106, "    ")
        self.addControl(self.forwardPageButton)

        self.backwardPageButton = xbmcgui.ControlButton(0, 350, 200, 106, "    ")
        self.addControl(self.backwardPageButton)

        self.results = None
        

    # def Example1(self, text):
    #     label = xbmcgui.ControlLabel(200, 100, 200, 100, text)
    #     self.addControl(label)

    # def Example2(self, text):
    #     label = xbmcgui.ControlLabel(400, 100, 200, 100, text)
    #     self.addControl(label)

    # def Example3(self, text):
    #     label = xbmcgui.ControlLabel(200, 300, 200, 100, text)
    #     self.addControl(label)

    # def Example4(self, text):
    #     label = xbmcgui.ControlLabel(400, 300, 200, 100, text)
    #     self.addControl(label)

    def setResults(self, so: searchOptions.SearchOptions) -> None:
        so.setPBFunction(3)
        results = OurFilter.filter(so)

        start = self.page * self.ITEMS_PER_PAGE
        end = min(len(results), self.page * self.ITEMS_PER_PAGE + 4)
        chunk = results[start:end]

        for i, v in enumerate(chunk):
            label = self.loopyGrid[i]
            label.setLabel(v["title"])
        
        # if len(results) < self.ITEMS_PER_PAGE:
        #     for i in range(len(results), self.ITEMS_PER_PAGE):
        #         self.loopyGrid[i].setLabel("empty")

        # ListShown = xbmcgui.ControlList(400, 400, 200, 400)
        # self.addControl(ListShown)
        # for something in results:
        #     item = xbmcgui.ListItem(something["title"])
        #     ListShown.addItem(item)


        # Cherry1 = ListShown.getListItem(0)
        # Cherry2 = ListShown.getListItem(1)
        # Cherry3 = ListShown.getListItem(3)
        # Cherry4 = ListShown.getListItem(4)
        # self.Example1(Cherry1.getLabel())
        # self.Example2(Cherry2.getLabel())
        # self.Example3(Cherry3.getLabel())
        # self.Example4(Cherry4.getLabel())