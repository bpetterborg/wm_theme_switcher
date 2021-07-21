#!/usr/bin/env python

#
#   Script to automate switching of WM config and 
#   GTK theme based on time of day.
#
#	YOU MUST SET THE WM_CONFIG_FILE VARIABLE TO YOUR WM CONFIG.
#   
#   TODO:
#   	- Add autodecection of WM and config location
#   	- Add some kind of UI or config file to set it up.
#
#


# imports
from sultan.api import Sultan	# run commands to set GTK theme or move files
from datetime import datetime	# get time of day
import os						# edit files
import time

# vars
s = Sultan()
current_time = datetime.now()
WM_CONFIG_PATH = '/home/ben/.config/sway/'
WM_CONFIG_FILE = WM_CONFIG_PATH + 'config'

def set_theme_dark():
	# move the wm config elsewhere
	print('Setting theme to Dark')
	s.mv(WM_CONFIG_FILE, WM_CONFIG_PATH + 'config.light.old')
	s.mv(WM_CONFIG_PATH + '/sway/config.dark.old' , WM_CONFIG_FILE)

def set_theme_light():
	# move the wm config elsewhere
	print('Setting theme to Light')
	s.mv(WM_CONFIG_FILE, WM_CONFIG_PATH + 'config.dark.old')
	s.mv(WM_CONFIG_PATH + '/sway/config.light.old' , WM_CONFIG_FILE)



# main stuff


while True:

	current_dir = os.getcwd()

	if current_time == '20:00:00':
		set_theme_dark()

	elif current_time == '07:00:00':
		set_theme_light()
