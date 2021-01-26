# --------------------------------------------------------------
#  menu.py
#  Version: 1.0.0
#  Last Updated: May 6th, 2019
# --------------------------------------------------------------

# --------------------------------------------------------------
#  GLOBAL IMPORTS ::::::::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------

import nuke
import platform

# Define where .nuke directory is on each OS's network.
Win_Dir = 'C:\Users\jkrishnaswamy\.nuke'
MacOSX_Dir = '/Users/jkrishnaswamy/.nuke'
Linux_Dir = '/home/jkrishnaswamy/.nuke'

# Automatically set global directory
if platform.system() == "Windows":
	dir = Win_Dir
elif platform.system() == "Darwin":
	dir = MacOSX_Dir
elif platform.system() == "Linux":
	dir = Linux_Dir
else:
	dir = None



