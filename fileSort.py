# this script orgnizes the files is a specific directory 
# into folders depending on the extention/type of each file

import os
import shutil
import time

word = ['doc','docm','docx','docx','dotx','dot']
pdf = ['pdf']
ppt = [ 'ppt', 'pot', 'pps', 'pptx', 'potx', 'ppsx', 'thmx']
excel = ['xlsx','xlsm','xlsb','xltx']
img = ['jpeg', 'gif', 'png' ,'tiff','psd','eps','ai','indd','raw','webp','jpg']
videos = ['mp4','mov','avi','wmv','avchd','webm','flv','vlc']
installables = ['exe']
zipped = ['zip','rar'] 

# the path/directory that needs to be organized
mypath = "C:/Users/Rama/Downloads/test directory"

# check if the directory exists 
if os.path.exists(mypath) != 1 :
       print('path doesnt exist')
       exit()

print('Your folder path is"',mypath,'"')


#create folders to strore/organize the files IF they dont already exist 
os.makedirs(mypath+"\! documents/word", exist_ok=True)
os.makedirs(mypath+"\! documents/pdf", exist_ok=True)
os.makedirs(mypath+"\! documents/ppt", exist_ok=True)
os.makedirs(mypath+"\! documents/excel", exist_ok=True)
os.makedirs(mypath+"/! images", exist_ok=True)
os.makedirs(mypath+"/! videos", exist_ok=True)
os.makedirs(mypath+"/! installable", exist_ok=True)
os.makedirs(mypath+"/! zip", exist_ok=True)
os.makedirs(mypath+"/! other", exist_ok=True)
os.makedirs(mypath+"/! folders", exist_ok=True)

##########################


# get a list of all files that already exist in the folder

before = dict ([(f, None) for f in os.listdir (mypath)])

def moveToFolder(dir):

    if dir.split('/')[-1].find('!')!=-1:
         return
    
    if dir.find('.') == -1:
        shutil.move( mypath+'/'+dir, mypath+"/! folders/"+dir)
        return
    extention = dir.split('.')[-1].lower()
    if extention in word :
         shutil.move( mypath+'/'+dir, mypath+"/! documents/word/"+dir)
    elif extention in pdf:
         shutil.move( mypath+'/'+dir, mypath+"/! documents/pdf/"+dir)
    elif extention in ppt:
         shutil.move( mypath+'/'+dir, mypath+"/! documents/ppt/"+dir)
    elif extention in excel:
         shutil.move( mypath+'/'+dir, mypath+"/! documents/excel/"+dir)
    elif extention in img:
         shutil.move( mypath+'/'+dir, mypath+"/! images/"+dir)
    elif extention in videos:
         shutil.move( mypath+'/'+dir, mypath+"/! videos/"+dir)
    elif extention in installables:
         shutil.move( mypath+'/'+dir, mypath+"/! installable/"+dir)
    elif extention in zipped:
         shutil.move( mypath+'/'+dir, mypath+"/! zip/"+dir)
    else :
         shutil.move( mypath+'/'+dir, mypath+"/! other/"+dir) 
    # print(dir.split('.')[-1])

for item in before:
    moveToFolder(item)
print('files have been organised')

while 1:
        after = dict ([(f, None) for f in os.listdir (mypath)])
        added = [f for f in after if not f in before]
        if added:
                for item in added:
                    moveToFolder(item)
