import requests
from bs4 import BeautifulSoup
import os
import sys
import webbrowser

def GetNewest(): #Returns newest abitti version
        headeria= {'User-Agent': 'Mozilla/5.0'}
        page = requests.get("https://www.abitti.fi/fi/paivitykset/", headers=headeria)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find("section", class_="details")
        sContainer = results.find("div", class_="container")
        testi2 = sContainer.find("b")
        newestVer = testi2.text
       
        return newestVer

def CurrentVer(): #Reads text file about last downloaded version

    path_to_script = sys.argv[0]
    path_to_script_dir = os.path.dirname(os.path.abspath(path_to_script))

    try:
        file = open(os.path.join(path_to_script_dir, "version.txt"), "r")
        version = file.read()
        file.close()
        return version

    except:
        file = open(os.path.join(path_to_script_dir, "version.txt"), "w")
        file.close()
        return "txt file empty"

def WriteNewVersion(versionName): #Inserts the new downloaded version name to text file

     path_to_script = sys.argv[0]
     path_to_script_dir = os.path.dirname(os.path.abspath(path_to_script))

     file = open(os.path.join(path_to_script_dir, "version.txt"), "w")
     file.write(versionName)
     file.close()

def GoToWebsite(websiteURL): #Opens URL on your windows-pc default browser
    
    webbrowser.get('windows-default').open(websiteURL, new=2)
    




    
    
    
    
    
