import xbmcgui
import xbmc
import metaData

#Try again later
dummy_list = [
        {'MediaType':'Movie', 'Name': 'Movie 1', 'Rating': '5', 'Genre': 'Horror', 'Length': '130', 'Year': '2019'},
        {'MediaType':'Epsiode', 'Name': 'Epsiode 2', 'Rating': '2', 'Genre': 'Slice-Of-Life', 'Length': '40', 'Year': '2020'},
        {'MediaType':'Movie', 'Name': 'Movie 2', 'Rating': '4', 'Genre': 'Comedy', 'Length': '90', 'Year': '2023'},
        {'MediaType':'Movie', 'Name': 'Movie 3', 'Rating': '3', 'Genre': 'Action', 'Length': '120', 'Year': '2022'},
        {'MediaType':'Episode', 'Name': 'Epsode 2', 'Rating': '1', 'Genre': 'Romance', 'Length': '20', 'Year': '2021'}
]



class MyWindow(xbmcgui.Window):


    # def display_list(self):
    #         dialog = xbmcgui.Dialog()
    #         dialog.ok("List", str(dummy_list))

     #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\The Identifying stuff
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
    

       #The Orange
    def show_circle(self, x, y, radius, color):
        circle = xbmcgui.ControlImage(x, y, radius, radius, "/Users/collegecarol/Desktop/Kodi/Kodi4/circle.png", color)
        self.addControl(circle)

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
    # def __init__(mediaType) -> None:
    #     super().__init__()
    #     mediaType.button = xbmcgui.ControlButton(0, 10, 200, 106, "    ")
    #     mediaType.addControl(mediaType.button)

    #     mediaType.listThing = xbmcgui.ControlList(0, 100, 300, 200)
    #     mediaType.addControl(mediaType.listThing)
    #     # self.item1 = xbmcgui.ListItem("Item 1 but a ListItem")
    #     # self.listThing.addItem(self.item1)
    #     # self.listThing.addItem("Item2 but a string")
    #     for item in dummy_list:
    #         mediaType.listThing.addItem(str(item))

    #     mediaType.listThing.setVisible(False)

    # def onAction(mediaType, action: xbmcgui.Action) -> None:
    #     print(f"action: {action}")
    #     if action == xbmcgui.ACTION_PREVIOUS_MENU:
    #         mediaType.close()

    #     if action == xbmcgui.ACTION_MOUSE_LEFT_CLICK:
    #         control = mediaType.getFocus()
    #         if control.getId() == mediaType.button.getId():
    #             mediaType.listThing.setVisible(not mediaType.listThing.isVisible())
    #         text = "visible" if mediaType.listThing.isVisible() else "invisible"
    #         xbmc.log("button was pressed, listThing is now " + text)

    # def __init__(watchStatus) -> None:
    #     super().__init__()
    #     watchStatus.button = xbmcgui.ControlButton(150, 10, 200, 106, "    ")
    #     watchStatus.addControl(watchStatus.button)

    #     watchStatus.listThing = xbmcgui.ControlList(110, 100, 300, 200)
    #     watchStatus.addControl(watchStatus.listThing)
    #     for item in dummy_list:
    #         watchStatus.listThing.addItem(str(item))

    #     watchStatus.listThing.setVisible(False)


    # def onAction(watchStatus, action: xbmcgui.Action) -> None:
    #     print(f"action: {action}")
    #     if action == xbmcgui.ACTION_PREVIOUS_MENU:
    #         watchStatus.close()

    #     if action == xbmcgui.ACTION_MOUSE_LEFT_CLICK:
    #         control = watchStatus.getFocus()
    #         if control.getId() == watchStatus.button.getId():
    #             watchStatus.listThing.setVisible(not watchStatus.listThing.isVisible())
    #         text = "visible" if watchStatus.listThing.isVisible() else "invisible"
    #         xbmc.log("button was pressed, listThing is now " + text)

    # def __init__(ratingList) -> None:
    #     super().__init__()
    #     ratingList.button = xbmcgui.ControlButton(300, 10, 200, 106, "    ")
    #     ratingList.addControl(ratingList.button)

    #     ratingList.listThing = xbmcgui.ControlList(260, 100, 300, 100)
    #     ratingList.addControl(ratingList.listThing)
    #     for item in dummy_list:
    #         ratingList.listThing.addItem(str(item))

    #     ratingList.listThing.setVisible(False)

    # def __init__(genreList) -> None:
    #     super().__init__()
    #     genreList.button = xbmcgui.ControlButton(450, 10, 200, 106, "    ")
    #     genreList.addControl(genreList.button)

    #     genreList.listThing = xbmcgui.ControlList(410, 100, 300, 106)
    #     genreList.addControl(genreList.listThing)
    #     for item in dummy_list:
    #         genreList.listThing.addItem(str(item))

    #     genreList.listThing.setVisible(False)

    # def __init__(lengthList) -> None:
    #     super().__init__()
    #     lengthList.button = xbmcgui.ControlButton(600, 10, 200, 106, "    ")
    #     lengthList.addControl(lengthList.button)

    #     lengthList.listThing = xbmcgui.ControlList(460, 100, 300, 100)
    #     lengthList.addControl(lengthList.listThing)
    #     for item in dummy_list:
    #         lengthList.listThing.addItem(str(item))

    #     lengthList.listThing.setVisible(False)

    # def __init__(yearList) -> None:
    #     super().__init__()
    #     yearList.button = xbmcgui.ControlButton(750, 10, 200, 106, "    ")
    #     yearList.addControl(yearList.button)

    #     yearList.listThing = xbmcgui.ControlList(710, 100, 300, 100)
    #     yearList.addControl(yearList.listThing)
    #     for item in dummy_list:
    #         yearList.listThing.addItem(str(item))

    #     yearList.listThing.setVisible(False)

    # def __init__(tagsList) -> None:
    #     super().__init__()
    #     tagsList.button = xbmcgui.ControlButton(900, 10, 200, 100, "    ")
    #     tagsList.addControl(tagsList.button)

    #     tagsList.listThing = xbmcgui.ControlList(860, 100, 300, 100)
    #     tagsList.addControl(tagsList.listThing)
    #     for item in dummy_list:
    #         tagsList.listThing.addItem(str(item))

    #     tagsList.listThing.setVisible(False)

    # def __init__(studioList) -> None:
    #     super().__init__()
    #     studioList.button = xbmcgui.ControlButton(1050, 10, 200, 106, "    ")
    #     studioList.addControl(studioList.button)

    #     studioList.listThing = xbmcgui.ControlList(1010, 100, 300, 100)
    #     studioList.addControl(studioList.listThing)
    #     for item in dummy_list:
    #         studioList.listThing.addItem(str(item))

    #     studioList.listThing.setVisible(False)

    # def __init__(mostwatched) -> None:
    #     super().__init__()
    #     mostwatched.button = xbmcgui.ControlButton(0, 160, 200, 106, "    ")
    #     mostwatched.addControl(mostwatched.button)

    #     mostwatched.listThing = xbmcgui.ControlList(0, 250, 300, 200)
    #     mostwatched.addControl(mostwatched.listThing)
    #     for item in dummy_list:
    #         mostwatched.listThing.addItem(str(item))

    #     mostwatched.listThing.setVisible(False)

    def __init__(self) -> None:
        super().__init__()
        self.button1 = xbmcgui.ControlButton(150, 160, 200, 106, "    ")
        self.addControl(self.button1)

        self.listThing = xbmcgui.ControlList(110, 250, 300, 200)
        self.addControl(self.listThing)
        for item in metaData.getActors():
            self.listThing.addItem(str(item))
        self.listThing.setVisible(False)


        self.button = xbmcgui.ControlButton(300, 160, 200, 106, "    ")
        self.addControl(self.button)

        self.listThing = xbmcgui.ControlList(260, 250, 300, 200)
        self.addControl(self.listThing)
        for item in metaData.getDirectors():
            self.listThing.addItem(str(item))

        self.listThing.setVisible(False)

    

    # def __init__(directList) -> None:
    #     super().__init__()
    #     directList.button = xbmcgui.ControlButton(300, 160, 200, 106, "    ")
    #     directList.addControl(directList.button)

    #     directList.listThing = xbmcgui.ControlList(260, 250, 300, 200)
    #     directList.addControl(directList.listThing)
    #     for item in metaData.getDirectors():
    #         directList.listThing.addItem(str(item))

    #     directList.listThing.setVisible(False)


    def onAction(self, action: xbmcgui.Action) -> None:
        print(f"action: {action}")
        if action == xbmcgui.ACTION_PREVIOUS_MENU:
            self.close()

        if action == xbmcgui.ACTION_MOUSE_LEFT_CLICK:
            control = self.getFocus()
            if control.getId() == self.button.getId():
                self.listThing.setVisible(not self.listThing.isVisible())
            text = "visible" if self.listThing.isVisible() else "invisible"
            xbmc.log("button was pressed, listThing is now " + text)

        




     #Button displayed.
    

  #The Window
if __name__ == "__main__":
    window = MyWindow()

    #Orange
    window.show_circle (30, 35, 150, 0xFF0000)
    window.show_circle (180, 35, 150, 0xFF0000)
    window.show_circle (330, 35, 150, 0xFF0000)
    window.show_circle (480, 35, 150, 0xFF0000)
    window.show_circle (630, 35, 150, 0xFF0000)
    window.show_circle (780, 35, 150, 0xFF0000)
    window.show_circle (930, 35, 150, 0xFF0000)
    window.show_circle (1080, 35, 150, 0xFF0000)

    window.show_circle (30, 185, 150, 0xFF0000)
    window.show_circle (180, 185, 150, 0xFF0000)
    window.show_circle (330, 185, 150, 0xFF0000)


    window.show_circle (1080, 635, 200, 0xFF0000)
    window.show_circle (880, 635, 200, 0xFF0000)
    window.show_circle (680, 635, 200, 0xFF0000)
    window.show_circle (480, 635, 200, 0xFF0000)

    window.show_circle (35, 590, 300, 0xFF0000)

    #Identifying
    window.media_Type("MediaType")
    window.watch_Status("WatchStatus")
    window.rating_List("Rating")
    window.genre_List("Genre")
    window.length_List("Length")
    window.year_List("Year")
    window.tags_List("Tags")
    window.studio_List("Studio")
    window.most_Watched("MostWatched")
    window.casts_List("Casts")
    window.director_List("Director")

    window.playOne("Play One")
    window.loopPlay("Loop Play")
    window.showList("Show List")
    window.saveSearch("Save")
    window.shutDown("ShutDown Time")
    window.time("Hour          Min")



    # button.setNavigation( xbmcgui.ACTION_SELECT_ITEM, lambda: display_list() )

    

    window.doModal()
    del window