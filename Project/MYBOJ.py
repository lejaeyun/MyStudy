from PIL import ImageGrab 
import win32gui 

hwnd = win32gui.FindWindow(None, '제목 없음 - 메모장') 
win32gui.SetForegroundWindow(hwnd)
dimensions = win32gui.GetWindowRect(hwnd) 

image = ImageGrab.grab(dimensions) 
image.show() 
