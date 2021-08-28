import os

path = "/RISHI/H2K/H2KProjects/SEDAP/CustomerWatchTime_04052021.csv"

if os.path.exists(path):
    print("File Exists")
else:
    print("File is Not Transferred yet")