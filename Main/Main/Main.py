import Module
import webbrowser

newestVersion = ""

def Main():
    global newestVersion
    currentVersion = Module.CurrentVer()
    newestVersion = Module.GetNewest()

    if currentVersion != newestVersion:
        print("Update Available")
        GoToWebsite()
    else:
        print("No updates available")

def GoToWebsite():
    
    print("Opening website download link")
    webbrowser.get('windows-default').open("https://static.abitti.fi/etcher-usb/koe-etcher.zip", new=2)
    Module.WriteNewVersion(newestVersion)
    print("Abitti version name: " + newestVersion + " has been set to txt file")
   
Main()
    








