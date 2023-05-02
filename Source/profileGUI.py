import xbmcgui
import xbmcaddon
from xbmcgui import Action, Control
import searchOptions
import guiPlayWindows
import searchProfile
import gui
import filter
from typing import List

# Class for the buttons to extend
class SaveSearchBtn(xbmcgui.ControlButton):

    profileName: str

    def getProfileName(self) -> str:
        return self.profileName
    
    def setProfileName(self, name: str):
        self.profileName = name
        return self

    def actionTaken(self):
        print(f'Some Button Pressed on {self.getProfileName()}')

# Class for the Play One Button
class PlayOneBtn(SaveSearchBtn):

    def actionTaken(self):
        options = searchProfile.getProfile(self.getProfileName())
        options.setPBFunction(1)
        if filter.filter(options):
            poWindow = guiPlayWindows.PlayOneWindow()
            poWindow.setResults(options)
            poWindow.doModal()
            del poWindow
        else:
            xbmcgui.Dialog().ok("Error", "Your list is empty!")


# Class for the Loop Play Button
class LoopPlayBtn(SaveSearchBtn):

    def actionTaken(self):
        options = searchProfile.getProfile(self.getProfileName())
        options.setPBFunction(3)
        if filter.filter(options):
            lpWindow = guiPlayWindows.LoopPlayWindow()
            lpWindow.setResults(options)
            lpWindow.doModal()
            del lpWindow
        else:
            xbmcgui.Dialog().ok("Error", "Your list is empty!")

# Class for Show List Button
class ShowListBtn(SaveSearchBtn):
    
    def actionTaken(self):
        options = searchProfile.getProfile(self.getProfileName())
        options.setPBFunction(2)
        if filter.filter(options):
            slWindow = guiPlayWindows.ShowListWindow()
            slWindow.setResults(options)
            slWindow.doModal()
            del slWindow
        else:
            xbmcgui.Dialog().ok("Error", "Your list is empty!")

# Class for Edit Profile Button
class EditProfileBtn(SaveSearchBtn):
    
    def actionTaken(self):
        print(f'Edit Profile {self.getProfileName()}')
class SavedSearch(xbmcgui.Window):

    controlList: List[SaveSearchBtn]

    # constructor for window
    def __init__(self):
        
        # ensure there are profiles to display
        profiles = searchProfile.getAllProfiles()
        if (profiles == []):
            # show the search options settings window instead
            gui.showGui()

        # build inherited object
        super().__init__()
        
        addon = xbmcaddon.Addon()
        imagesFolder = addon.getAddonInfo('path') + "/images/"

        # window specific info
        controls: List(xbmcgui.Control) = []
        self.controlList = []
        v: int = 200
        for x in profiles:
            controls.append(xbmcgui.ControlLabel(100, v-75, 400, 50, x[0]))
            editBtn = EditProfileBtn(200, v, 150, 75, 'Edit Profile', focusTexture=f'{imagesFolder}circle.png', noFocusTexture=f'{imagesFolder}circle.png')
            editBtn.profileName = x[0]
            controls.append(editBtn)
            self.controlList.append(editBtn)
            poBtn = PlayOneBtn(400, v, 150, 75, 'Play One', focusTexture=f'{imagesFolder}circle.png', noFocusTexture=f'{imagesFolder}circle.png')
            poBtn.profileName = x[0]
            controls.append(poBtn)
            self.controlList.append(poBtn)
            lpBtn = LoopPlayBtn(600, v, 150, 75, 'Loop Play', focusTexture=f'{imagesFolder}circle.png', noFocusTexture=f'{imagesFolder}circle.png')
            lpBtn.profileName = x[0]
            controls.append(lpBtn)
            self.controlList.append(lpBtn)
            slBtn = ShowListBtn(800, v, 150, 75, 'Show List', focusTexture=f'{imagesFolder}circle.png', noFocusTexture=f'{imagesFolder}circle.png')
            slBtn.profileName = x[0]
            controls.append(slBtn)
            self.controlList.append(slBtn)
            v+=200
        self.addControls(controls)

    def onControl(self, control: xbmcgui.Control):
        for x in self.controlList:
            if x.getId() == control.getId():
                x.actionTaken()
        print(control.getLabel())