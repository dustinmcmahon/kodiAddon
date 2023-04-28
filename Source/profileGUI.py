import xbmcgui
import xbmc
import searchOptions
import searchProfile
import gui
from typing import List

# Class for the buttons to extend
class SaveSearchBtn(xbmcgui.ControlButton):

    profileName: str

    def getProfileName(self) -> str:
        return self.profileName
    
    def setProfileName(self, name: str):
        self.profileName = name

    def actionTaken(self):
        print(f'Some Button Pressed on {self.getProfileName()}')

class PlayOneBtn(SaveSearchBtn):

    def __init__(self):
        result = super()
        result.setLabel('Play One')
        return result

    def actionTaken(self):
        print(f'Play One Pressed on {self.getProfileName()}')


class LoopPlayBtn(SaveSearchBtn):

    def __init__(self):
        result = super()
        result.setLabel('Loop Play')
        return result

    def actionTaken(self):
        print(f'Loop Play Pressed on {self.getProfileName()}')

class ShowListBtn(SaveSearchBtn):

    def __init__(self):
        result = super()
        result.setLabel('Edit')
        return result
    
    def actionTaken(self):
        print(f'Edit Profile {self.getProfileName()}')

class EditProfileBtn(SaveSearchBtn):

    def __init__(self):
        result = super()
        result.setLabel('Show List')
        return result
    
    def actionTaken(self):
        print(f'Show List Pressed on {self.getProfileName()}')
class SavedSearch(xbmcgui.Window):
    
    def makeGroup(self, name: str) -> xbmcgui.ControlGroup:
        result = xbmcgui.ControlGroup(0,0,100,100)
        return result
    


    def showGui(self):
        profiles = searchProfile.getAllProfiles()
        if (profiles == []):
            gui.showGui()
        groups: List(xbmcgui.ControlGroup) = []
        for x in profiles:
            groups.append(self.makeGroup(x[0]))

        xbmcgui.ControlButton()

        self.show()
        self.doModal()
        del self