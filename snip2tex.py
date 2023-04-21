# -*- coding: utf-8 -*-
"""
===================================
Program : snip2tex/snip2tex.py
===================================
Summary:
"""
__author__ =  "Sadman Ahmed Shanto"
__date__ = "04/21/2023"
__email__ = "shanto@usc.edu"

#libraries used
import subprocess
import rumps

# Define the command to execute
command = "/Users/shanto/anaconda3/bin/latexocr"

# Define a function to execute the command and return the output
def execute_command():
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

# Define the path to the icon file (replace with your own path)
icon_path = "icon.png"

# Create a rumps App class
class LatexOCRApp(rumps.App):
    
    def __init__(self):
        super(LatexOCRApp, self).__init__("LatexOCR", icon=icon_path)
    
    # Define the "Execute" menu item
    @rumps.clicked("Execute")
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
