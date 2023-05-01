import subprocess
from gi import require_version

require_version('Nautilus', '4.0')
require_version('Gtk', '4.0')


from gi.repository import Nautilus, GObject
from gettext import gettext

TERMINAL= "kitty"

class Nautilus_terminal(GObject.GObject, Nautilus.MenuProvider):
    def __init__(self):
        super().__init__()
        self.path=""
        self.selected=False
        self.item= Nautilus.MenuItem(name="nautilus_open_terminal",
                                     label=gettext(f"Open in {TERMINAL}"),
                                     tip=gettext(f"Open dierectory in {TERMINAL}")
                                     )
        self.item.connect("activate", self.opening)
        

    """Get selected directory path"""
    def get_file_items(self, files):
        if not( len(files)>=1) or not(files[0].is_directory()):
            return None
        self.path= files[0].get_uri().replace("file://","")
        self.selected = True
        return [self.item]


    """get current directory path"""
    def get_background_items(self, directory):
        if not directory.is_directory() or self.selected:
            self.selected = False
            return None

        self.path = directory.get_uri().replace("file://","")
        return[self.item]
    """Open Terminal"""   
    def opening(self,e):
        subprocess.Popen([TERMINAL,self.path])
