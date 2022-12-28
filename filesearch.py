import os
import re
import win32api
import threading
import time

def find_file(root_folder, rex):
    l = []
    for root, dirs, files in os.walk(root_folder):

        for f in files:
            result = rex.search(f)
            if result:
                l.append(os.path.join(root, f))
                print(l)

def find_file_in_all_drives(file_name):
    # create a regular expression for the file
    rex = re.compile(file_name)
    l=[]

    for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]:
        tr = threading.Thread(target=(find_file),args=[drive,rex])
        tr.start()

print(find_file_in_all_drives('Sample1.txt'))
finish=time.perf_counter()
print(f'Finished in {finish} seconds')

