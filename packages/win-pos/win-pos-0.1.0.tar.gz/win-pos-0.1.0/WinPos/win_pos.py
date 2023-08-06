import pywintypes
import win32gui
from typing import Callable, Tuple, Union


class WindowData(Exception):
    pass


def get_window_hwnd(name: Union[str, Callable[[str], bool]]) -> Union[None, str]:
    def is_desired_window(window_title):
        if callable(name):
            return name(window_title)
        return window_title == name
    
    def callback(hwnd, args):
        if is_desired_window(win32gui.GetWindowText(hwnd)):
            raise WindowData(hwnd)
    
    if isinstance(name, str):
        hwnd = win32gui.FindWindow(None, name)
        return None if hwnd is 0 else hwnd
    try:
        win32gui.EnumWindows(callback, None)
    except WindowData as e:
        return e.args[0]
    return None


def get_window_pos_from_hwnd(hwnd: str) -> Union[None, Tuple[int, int, int, int]]:
    try:
        rect = win32gui.GetWindowRect(hwnd)
    except pywintypes.error:
        return None
    return rect[0], rect[1], rect[2] - rect[0], rect[3] - rect[1]


def get_window_pos(name: Union[str, Callable[[str], bool]]) -> Union[None, Tuple[int, int, int, int]]:
    hwnd = get_window_hwnd(name)
    if hwnd is None:
        return hwnd
    return get_window_pos_from_hwnd(hwnd)
