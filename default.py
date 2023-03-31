import xbmcgui

#Try again later
# dummy_list = [

#         {'MediaType':'Movie', 'Name': 'Movie 1', 'Rating': '5', 'Genre': 'Horror', 'Length': '130', 'Year': '2019'},
#         {'MediaType':'Epsiode', 'Name': 'Epsiode 2', 'Rating': '2', 'Genre': 'Slice-Of-Life', 'Length': '40', 'Year': '2020'},
#         {'MediaType':'Movie', 'Name': 'Movie 2', 'Rating': '4', 'Genre': 'Comedy', 'Length': '90', 'Year': '2023'},
#         {'MediaType':'Movie', 'Name': 'Movie 3', 'Rating': '3', 'Genre': 'Action', 'Length': '120', 'Year': '2022'},
#         {'MediaType':'Episode', 'Name': 'Epsode 2', 'Rating': '1', 'Genre': 'Romance', 'Length': '20', 'Year': '2021'}

#         ]


class MyWindow(xbmcgui.Window):
    def __init__(self) -> None:
        super().__init__()


     #The Identifying stuff
    def media_Type(self, text):
        label = xbmcgui.ControlLabel(50, 50, 200, 100, text)
        self.addControl(label)

    def watch_Status(self, text):
        label = xbmcgui.ControlLabel(190, 50, 200, 100, text)
        self.addControl(label)

    def rating(self, text):
        label = xbmcgui.ControlLabel(370, 50, 200, 100, text)
        self.addControl(label)

    def genre(self, text):
        label = xbmcgui.ControlLabel(520, 50, 200, 100, text)
        self.addControl(label)

    def length(self, text):
        label = xbmcgui.ControlLabel(670, 50, 200, 100, text)
        self.addControl(label)

    def year(self, text):
        label = xbmcgui.ControlLabel(830, 50, 200, 100, text)
        self.addControl(label)

    def tags(self, text):
        label = xbmcgui.ControlLabel(980, 50, 200, 100, text)
        self.addControl(label)

    def studio(self, text):
        label = xbmcgui.ControlLabel(1120, 50, 200, 100, text)
        self.addControl(label)


       #The Orange
    def show_circle(self, x, y, radius, color):
        circle = xbmcgui.ControlImage(x, y, radius, radius, "/Users/collegecarol/Desktop/Kodi/Kodi4/circle.png", color)
        self.addControl(circle)

    

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
    window.rating("Rating")
    window.genre("Genre")
    window.length("Length")
    window.year("Year")
    window.tags("Tags")
    window.studio("Studio")

    #Try again Later
    # button = window.getControl(200)
    # button.setLabel("Display List")
    # def display_list():
    #     dialog = xbmcgui.Dialog()
    #     dialog.ok("List", str(dummy_list))
    # button.setNavigation( xbmcgui.ACTION_SELECT_ITEM, lambda: display_list() )

    window.doModal()
    del window