import shutil

txt = open("path.txt", "r")
read = txt.read()
print(read)
if read == "":
    path = input("File Path: ")
    path = path.replace('"', '')

    shutil.copyfile('ouch.ogg', path) #copy file to roblox
    print("File copied.")
    txt.close()
    txt = open("path.txt", "w")
    txt.write(path)
    txt.close()
    quit()
else:
    path = read


shutil.copyfile('ouch.ogg', path) #copy file to roblox
print("File copied.")