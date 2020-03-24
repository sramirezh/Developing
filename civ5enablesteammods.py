"""
A quick and dirty script I wrote to help install Civilization V mods under
Mac OS X.  It only works with the Steam version.  The App Store version puts
its files in different places.  Feel free to modify this script to support
the latter also, but please send me a copy too!

Edward K. Chew
ekc@lgl.kos.net

Version 1.0.3 by AlanH June 19 2014
Changed the 7za command to use full paths, 
and to extract the mods into separate subfolders in the Mods folder.

"""

import os, subprocess, sys

print("Civ5 Enable Steam Mods 1.0.3")

# Stop hiding the Mods button.
userDir = os.path.expanduser("~")
steamDir = os.path.join(
	userDir,
	"Library",
	"Application Support",
	"Steam")
parDir = os.path.join(
	steamDir,
	"SteamApps",
	"common",
	"sid meier's civilization v",
	"Civilization V.app",
	"Contents",
	"Home",
	"assets",
	"UI",
	"FrontEnd")
path0 = os.path.join(parDir, "MainMenu_orig.lua")
path1 = os.path.join(parDir, "MainMenu.lua")
if not os.path.exists(path0):
	print("Activating the MODS button...")
	os.rename(path1, path0)
	with open(path0, "r") as file0:
		with open(path1, "w") as file1:
			for line in file0:
				line = line.replace(
					"Controls.ModsButton:SetHide",
					"-- Controls.ModsButton:SetHide")
				file1.write(line)

# Extract the compressed mod files.
def searchUserData(arg, dir0, fileNames):
	if dir0.find("/ugc/referenced/") < 0:
		return
	for fileName in fileNames:
		if	fileName.find("_orig.civ5mod") >= 0 or \
			fileName.find(".civ5mod") < 0:
			continue
		print("Expanding the file:", fileName)
		path0 = os.path.join(dir0, fileName)
		os.chdir("/")
		command = [path7za, "x", "-o/" + dir1[1:] + "/" + fileName.replace(".civ5mod",""), path0]
		print command
		exitCode = subprocess.call(command)
		if exitCode == 0:
			path1 = os.path.join(dir0,
				fileName.replace(".civ5mod", "_orig.civ5mod"))
			os.rename(path0, path1)
dir1 = os.path.join(
	userDir,
	"Documents",
	"Aspyr",
	"Sid Meier's Civilization 5",
	"MODS")
path7za = os.path.abspath(os.path.join(
	os.path.dirname(sys.argv[0]),
	"bin",
	"7za"))
os.path.walk(os.path.join(steamDir, "userdata"), searchUserData, None)
