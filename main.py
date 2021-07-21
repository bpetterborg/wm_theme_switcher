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
#		- Figure out how to stop running multiple times if 
#		  theme-changing functions have already run before.
#		  (maybe add a thing to check f the file already exists?)
#		- Make setting the time more user friendly.


# imports
from sultan.api import Sultan	# run commands to set GTK theme or move files
from datetime import datetime	# get time of day
import os						# edit files
import time

# vars
s = Sultan()
# get current time, represent as int
current_time = int(datetime.now().strftime("%H%M%S"))

WM_CONFIG_PATH = '/home/ben/.config/sway/'
WM_CONFIG_FILE = WM_CONFIG_PATH + 'config'

def set_theme_dark():
	# move the wm config elsewhere

	# if file hasn't already been moved, move it
		
		print('Setting theme to Dark')
		s.mv(WM_CONFIG_FILE, WM_CONFIG_PATH + 'config.light.old')
		s.mv(WM_CONFIG_PATH + '/sway/config.dark.old' , WM_CONFIG_FILE)
		sleep(3600000)

def set_theme_light():
	# move the wm config elsewhere
	print('Setting theme to Light')
	s.mv(WM_CONFIG_FILE, WM_CONFIG_PATH + 'config.dark.old')
	s.mv(WM_CONFIG_PATH + '/sway/config.light.old' , WM_CONFIG_FILE)



# main stuff


while True:

	current_dir = os.getcwd()

	if current_time < 203000 and current_time > 235959 or current_time < 0 and current_time > 65959:
		set_theme_dark()

	elif current_time < 70000 and current_time > 202959:
		set_theme_light()
