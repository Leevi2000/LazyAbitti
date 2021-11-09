import Module
import os

def Main():

    currentVersion = Module.CurrentVer() #Returns the current version probably downloaded
    newestVersion = Module.GetNewest() #Checks name of the newest abitti version via web scraping

    print("Last version downloaded: " + currentVersion)

    if currentVersion != newestVersion: 
        print("Update Available")
        print("Starting download")
        Module.GoToWebsite("https://static.abitti.fi/etcher-usb/koe-etcher.zip") #Open download link
        Module.WriteNewVersion(newestVersion) #Changes text file version name
        print("Abitti version name in the txt file has been updated to: " + newestVersion)
    else:
        print("No updates available")

    os.system("pause") #So that the cmd window doesn't close immediately

Main()
    








