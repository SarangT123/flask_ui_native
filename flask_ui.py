import pip
import os
import time
import platform
try:
    __import__('webview')
except ImportError:
    pip.main(['install', 'webview'])
import webview


def run(host):
    """if any error comes up you might have not setup your flask app correctly"""
    if platform.system() == 'Linux':
        os.system('flask run &')
        webview.create_window(
            'Flask boilerplate app', host, background_color='#FFFFFF', js_api=True, frameless=True)
        webview.start()
        os.system('pkill flask')
    elif platform.system() == 'Windows':
        os.system('flask run &')
        webview.create_window(
            'Flask boilerplate app', host, background_color='#FFFFFF', js_api=True, frameless=True)
        webview.start()
        os.system('taskkill /F /IM flask.exe')
    else:
        import tkinter
        from tkinter import messagebox

        root = tkinter.Tk()
        root.withdraw()

        messagebox.showwarning('Error', 'This is not supported on your OS')
        root.destroy()
        exit()
