import os

path = "/RISHI/H2K/H2KProjects/SEDAP/"
all_watch_time_files = []
if os.path.exists(path):
    print("Directory Exists")
    list_of_files = os.listdir(path)
    for eachFile in list_of_files:
        if 'CustomerWatchTime' in eachFile:
            all_watch_time_files.append(eachFile)
        else:
            print(eachFile)
    print("************ All Watch Time FIles ********")
    for eachWatchTimeFIle in all_watch_time_files:
        print(eachWatchTimeFIle)

temp_path = "/RISHI/H2K/H2KProjects/SEDAP/temp"

if os.path.exists(temp_path):
    print("Temp directory exists")
else:
    os.mkdir(temp_path)
    print("Directory is created")

os.rmdir("/RISHI/H2K/H2KProjects/SEDAP/newDir")

# Moving Customer Watch time files to temp directory
