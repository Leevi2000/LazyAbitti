import requests
from bs4 import BeautifulSoup
import os
import sys
   
def GetNewest(): #Returns newest abitti version
        headeria= {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 OPR/80.0.4170.61'    }
        page = requests.get("https://www.abitti.fi/fi/paivitykset/", headers=headeria)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find("section", class_="details")
        sContainer = results.find("div", class_="container")
        testi2 = sContainer.find("b")
        newestVer = testi2.text
       
        return newestVer

def CurrentVer():

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

def WriteNewVersion(versionName):
     path_to_script = sys.argv[0]
     path_to_script_dir = os.path.dirname(os.path.abspath(path_to_script))

     file = open(os.path.join(path_to_script_dir, "version.txt"), "w")
     file.write(versionName)
     file.close()




    
    
    
    
    
