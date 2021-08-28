path = "/RISHI/H2K/H2KProjects/SEDAP/demofile_a.txt"

'''
mode of opration
'r' - read - default
'w' - write - wipe out existing content
'a' - append - appends new content to existing content
'x' - create - creation

't' - text
'b' - binary
'''

with open(path, 'a') as file:
    for i in range(10,20):
        line = "This is Line Number {}\n".format(i)
        file.write(line)
    file.close()
