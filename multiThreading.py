import os
import re
import time

import win32api
import concurrent.futures
start= time.perf_counter()
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
    Drive=win32api.GetLogicalDriveStrings().split('\000')[:-1]
    with concurrent.futures.ThreadPoolExecutor() as executor:
        tr = [executor.submit(find_file,drive,rex) for drive in Drive]
    for i in concurrent.futures.as_completed(tr):
        i.result()

print(find_file_in_all_drives('sample.txt'))
finish=time.perf_counter()
print(f'finished in {finish - start} seconds')