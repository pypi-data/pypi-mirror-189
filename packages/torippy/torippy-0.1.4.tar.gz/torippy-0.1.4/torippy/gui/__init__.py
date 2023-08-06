from typing import Literal, Optional
import pyautogui
from pyautogui import Point
from PIL.Image import Image
from dataclasses import dataclass
import ctypes
from functools import singledispatch

from .keycode import KeyCode


def get_mouse_pos():
    """現在のマウスの位置を取得"""
    return pyautogui.position()


def get_screen_size():
    """スクリーンサイズを取得"""
    return pyautogui.size()


def moveto_mouse(x: int, y: int, duration=0):
    """マウスを(x, y)に動かす"""
    pyautogui.moveTo(x, y, duration)


def move_relative_mouse(x: int, y: int, duration=0):
    """マウスを(x, y)だけ相対的に動かす"""
    pyautogui.moveTo(x, y, duration)


def click_mouse(
    x: int,
    y: int,
    num_of_clicks=1,
    interval=0,
    button: Literal["left", "middle", "right"] = "left",
):
    """(x, y)をクリック（指定がない場合は現在のマウスの位置をクリック）"""
    pyautogui.click(x, y, num_of_clicks, interval, button)


@dataclass
class Region:
    x: int
    y: int
    width: int
    height: int


@singledispatch
def _screenshot(
    x1: Optional[int] = None,
    y1: Optional[int] = None,
    x2: Optional[int] = None,
    y2: Optional[int] = None,
) -> Image:
    if x1 and y1 and x2 and y2:
        return pyautogui.screenshot(
            region=(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))
        )
    else:
        return pyautogui.screenshot()


@_screenshot.register
def _(pos1: Point, pos2: Point) -> Image:
    return _screenshot(pos1.x, pos1.y, pos2.x, pos2.y)


@_screenshot.register
def _(region: Region) -> Image:
    return _screenshot(region.x, region.y, region.width, region.height)


def screenshot(
    x1: Optional[int] = None,
    y1: Optional[int] = None,
    x2: Optional[int] = None,
    y2: Optional[int] = None,
    pos1: Optional[Point] = None,
    pos2: Optional[Point] = None,
    region: Optional[Region] = None,
):
    """スクリーンショットを取得

    (x1, y1), (x2, y2) の２点から成る矩形を取得
        x1: int, y1: int, x2: int, y2: int

    pyautogui.Pointの2点から成る矩形を取得
        pos1: pyautogui.Point, pos2: pyautogui.Point

    Region(x, y, width, height) からなる矩形を取得
        region: Region
    """
    if region:
        _screenshot(region)
    elif pos1 and pos2:
        _screenshot(pos1, pos2)
    else:
        _screenshot(x1, y1, x2, y2)


def screenshot_2click():
    pos1 = get_clicked_pos(KeyCode.VK_LBUTTON)
    pos2 = get_clicked_pos(KeyCode.VK_LBUTTON)
    return _screenshot(pos1, pos2)


def get_clicked_pos(keycode: KeyCode = KeyCode.VK_LBUTTON):
    while True:
        if ctypes.windll.user32.GetAsyncKeyState(keycode.value) == 0x8001:
            return get_mouse_pos()
