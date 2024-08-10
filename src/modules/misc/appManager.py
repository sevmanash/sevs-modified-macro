import sys
import re
import os
class WindowMgr:
    """Encapsulates some calls to the winapi for window management"""

    def __init__ (self):
        """Constructor"""
        self._handle = None

    def find_window(self, class_name, window_name=None):
        """find a window by its class_name"""
        self._handle = win32gui.FindWindow(class_name, window_name)

    def _window_enum_callback(self, hwnd, wildcard):
        """Pass to win32gui.EnumWindows() to check all the opened windows"""
        if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) is not None:
            self._handle = hwnd

    def find_window_wildcard(self, wildcard):
        """find a window whose title matches the wildcard regex"""
        self._handle = None
        win32gui.EnumWindows(self._window_enum_callback, wildcard)

    def set_foreground(self):
        """put the window in the foreground"""
        #send the alt key. For some reason this is required to make it run consistently
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.SendKeys('%')
        win32gui.ShowWindow(self._handle, win32con.SW_NORMAL) #in case window is minimised
        win32gui.SetForegroundWindow(self._handle) #switch to window
    


def openAppMac(app="roblox"):
    runAppleScript('activate application "{}"'.format(app))
    os.system(f"open -a {app}")

def openAppWindows(name):
    w = WindowMgr()
    w.find_window_wildcard(f".*Roblox.*")
    w.set_foreground()

if sys.platform == "darwin":
    from appleScript import runAppleScript
    openApp = openAppMac
else:
    import win32gui, win32con,  win32com.client
    openApp = openAppWindows