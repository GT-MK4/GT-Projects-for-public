import os
import shutil
current_dir = os.path.dirname(os.path.realpath(__file__))
print("welcome to GT organize.py script")
for filename in os.listdir(current_dir):
    if filename.endswith((".png" ,".jpeg" ,".jpg")):
        if not os.path.exists("images"):
           os.mkdir("images")
        shutil.copy(filename , "images")
        os.remove(filename)
        print("images done")
    if filename.endswith((".py" ,".css" ,".html","js")):
        if not os.path.exists("codes"):
           os.mkdir("codes")
        shutil.copy(filename , "codes")
        os.remove(filename)
        print("codes done")
    if filename.endswith((".mp4" ,".webm" ,".mkv")):
        if not os.path.exists("videos"):
           os.mkdir("videos")
        shutil.copy(filename , "videos")
        os.remove(filename)
        print("videos done")
    if filename.endswith((".pdf" ,".word" ,".doc" ,".docx")):
        if not os.path.exists("docs"):
           os.mkdir("docs")
        shutil.copy(filename , "docs")
        os.remove(filename)
        print("docs done")
    if filename.endswith((".zip" ,".rar" ,".tar" ,".gz" ,".7z")):
        if not os.path.exists("archives"):
           os.mkdir("archives")
        shutil.copy(filename , "archives")
        os.remove(filename)
        print("archives done")
    if filename.endswith((".dmg" ,".exe" ,".msi" ,".pkg" ,".deb")):
        if not os.path.exists("apps"):
           os.mkdir("apps")
        shutil.copy(filename , "apps")
        os.remove(filename)
        print("apps done")
print("everything done")
