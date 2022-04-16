import win32api
import win32con

def readkey(path, qvalue):
    key = win32api.RegOpenKeyEx(win32con.HKEY_LOCAL_MACHINE, f"{path}" , 0 , win32con.KEY_READ)
    rvalue = win32api.RegQueryValueEx(key, f"{qvalue}")
    win32api.RegCloseKey(key)

    (value, useless) = rvalue

    return value

def writevalue_string(path, qvalue, updateval):
    key = win32api.RegOpenKeyEx(win32con.HKEY_LOCAL_MACHINE, f"{path}" , 0 , win32con.KEY_WRITE)
    rvalue = win32api.RegSetValueEx(key, f"{qvalue}", 0, win32con.REG_SZ, f"{updateval}")
    win32api.RegCloseKey(key)

def writevalue_binary(path, qvalue, updateval):
    key = win32api.RegOpenKeyEx(win32con.HKEY_LOCAL_MACHINE, f"{path}" , 0 , win32con.KEY_WRITE)
    rvalue = win32api.RegSetValueEx(key, f"{qvalue}", 0, win32con.REG_BINARY, f"{updateval}")
    win32api.RegCloseKey(key)

def writevalue_dword(path, qvalue, updateval):
    key = win32api.RegOpenKeyEx(win32con.HKEY_LOCAL_MACHINE, f"{path}" , 0 , win32con.KEY_WRITE)
    rvalue = win32api.RegSetValueEx(key, f"{qvalue}", 0, win32con.REG_DWORD, f"{updateval}")
    win32api.RegCloseKey(key)

def writevalue_qword(path, qvalue, updateval):
    key = win32api.RegOpenKeyEx(win32con.HKEY_LOCAL_MACHINE, f"{path}" , 0 , win32con.KEY_WRITE)
    rvalue = win32api.RegSetValueEx(key, f"{qvalue}", 0, win32con.REG_QWORD, f"{updateval}")
    win32api.RegCloseKey(key)
