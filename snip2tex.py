# -*- coding: utf-8 -*-
"""
===================================
Program : snip2tex/snip2tex.py
===================================
Summary:
"""
__author__ = "Sadman Ahmed Shanto"
__date__ = "04/22/2023"
__email__ = "shanto@usc.edu"

#libraries used
import os
import platform
import subprocess

# Define the command to execute
if platform.system() == "Windows":
    command = "C:\\path\\to\\latexocr.exe"
elif platform.system() == "Linux":
    command = "/path/to/latexocr"
else:  # macOS
    command = "/Users/shanto/anaconda3/bin/latexocr"

# Define a function to execute the command and return the output
def execute_command():
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

if platform.system() == "Darwin":  # macOS
    import rumps

    # Define the path to the icon file (replace with your own path)
    icon_path = "assets/icon.png"

    # Create a rumps App class
    class LatexOCRApp(rumps.App):

        def __init__(self):
            super(LatexOCRApp, self).__init__("LatexOCR", icon=icon_path)

        # Define the "Execute" menu item
        @rumps.clicked("Snip2TeX")
        def execute_menu_item(self, _):
            output = execute_command()
            rumps.alert(output)

        # Override the default behavior when the app is closed
        def quit(self, _):
            pass

    # Create an instance of the app
    app = LatexOCRApp()

    # Run the app
    app.run()

else:  # Windows and Linux
    import PySimpleGUI as sg

    # Define the GUI layout
    layout = [
        [sg.Button("Snip2TeX"), sg.Button("Quit")],
        [sg.Output(size=(80, 20))]
    ]

    # Create the window
    window = sg.Window("LatexOCR", layout)

    # Event loop
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == "Quit":
            break
        elif event == "Snip2TeX":
            output = execute_command()
            print(output)

    # Close the window
    window.close()
