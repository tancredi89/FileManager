from watchdog.events import FileSystemEventHandler as eh
from watchdog.observer import observer

import os
import json
import time

class MyHandler(eh):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "/" + filename
            new_destination = folder_destination + "/" + filename
            os.rename(src, new_destination)


folder_to_track = input("Type the folder to track path")
filename, file_extension = os.path.splitext(filename)
if file_extension == '.pdf':
    folderName = 'PDF'
elif file_extension == '.jpg' or file_extension == '.jpeg':
    folderName = 'Immages'
elif file_extension == '.mp4' or file_extension == '.avi':
    folder_name = 'Movies'
elif file_extension == '.doc' or file_extension == '.docx':
    folderName = 'Documents'
elif file_extension == '.xlxs' or file_extension == '.xlxm':
    folderName = 'Excel_Sheets'
else:
    folder_name = 'Uknown'
    
folder_destination = "/lagniliasa/Downloads/" + folderName
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive= True)
observer.start()



try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()

