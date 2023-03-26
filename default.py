
import xbmcgui
import xbmcaddon
from resources import random_movie_player
from resources.random_movie_player import play_random_movie

addon = xbmcaddon.Addon()


class MyPlayer(xbmcgui.Window):
    def __init__(self):
        xbmcgui.Window.__init__(self)

        self.button = xbmcgui.ControlButton(
            50, 50, 400, 100, label="Play Random Movie", focusTexture="special://home/addons/script.random_movie_player/resources/skins/default/media/focused.png")
        self.addControl(self.button)

    def onControl(self, control):
        if control == self.button:
            xbmcgui.Dialog().ok('addonname', 'This message')
            # play_random_movie()

    # def onClick(self, controlID: int):
    #     if controlID == 10:
    #         play_random_movie()


if (__name__ == "__main__"):
    w = MyPlayer()
    w.doModal()
    del w
