import xbmcgui
import xbmc
import searchOptions
import searchProfile
import gui
from typing import List

class SavedSearch(xbmcgui.Window):
    
    def makeGroup(self, name: str) -> xbmcgui.ControlGroup:
        result = xbmcgui.ControlGroup(100, 100, 600, 100)
        return result
    


    def showGui(self):
        profiles = searchProfile.getAllProfiles()
        if (profiles == []):
            gui.showGui()
        groups: List(xbmcgui.ControlGroup) = []
        for x in profiles:
            g = self.makeGroup(x[0])
            self.addControl(g)
            groups.append(g)
            


        self.show()
        self.doModal()
        del self