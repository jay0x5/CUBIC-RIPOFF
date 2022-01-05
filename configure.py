'''
Author: Jay
Date pubished: 5th January 2022
Purpose: Automated script to unsquash the filesystem of Ubuntu ISO to allow chroot access
'''
import os
from write import write
import time

def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele

    return str1


write("Welcome to the Builder\n")
isoname = []
chosenone = []


def checkiso():
    write("Checking for Iso Image...\n")
    os.system("ls | grep -w '.iso\|ubuntu' > content.txt")
    file = open("content.txt","r")
    for names in file:
        stripp = names.strip()
        nlis = stripp.split()
        isoname.append(nlis)

    file.close()
    for res in isoname:
        res = listToString(res)
        name,exts = os.path.splitext(res)
        if exts == '.iso':
            write("found iso image: " + name + exts + "\n")
            r = name + exts
            chosenone.append(r)
            #write("Would you like to proceed with " + name + exts + " ?\n")
            #write("Enter yes or no\n[Yes] => will proceed\n[No] => will ask for name of desired iso image\n")
            #yon = input("Enter: ")
            #askuser1(yon,name,exts)
            run()


        else:
            write("ISO not found please re-run the program after properly adding the iso image to this folder!\n")
            exit()
    else:
      write("ISO not found please re-run the program after properly adding the iso image to this folder!\n")
      exit()

    #else:
       # print("Something went wrong! Please retry with a valid ISO Image")


    
def run():
    defolder = "unzipped"
    os.system("pwd > cwd.txt")
    cwdp1 = open("cwd.txt")
    cwdp2 = cwdp1.read()
    cwdp3 = slice(-1)
    cwdp4 = cwdp2[cwdp3]
    cisoname = input("Please choose a name for the working directory: ")
    stor = open("workdir.txt","w+")
    stor.write(cisoname)
    write(cisoname + " set as name for the custom iso and your workspace directory\n")
    isofile = listToString(chosenone)
    os.system("mkdir " + cisoname)
    write("made a folder by name " + cisoname +  "!\n")
    os.system("mkdir " +  defolder)
    write("Now copying the files to the folder " + "'" + defolder + "'" + " " + " please wait...\n")
    os.system("cp " + isofile + " " + defolder)
    write("copied the iso to the " + defolder +"  folder!\n")
    os.chdir(defolder)
    write("unzipping the iso file... Please wait\n")
    os.system("7z x " + isofile)
    os.chdir("casper")
    os.system("pwd > casperpath.txt")
    write("setting appropriate file permissions...\n")
    os.system("sudo chmod -R a+rw filesystem.squashfs")
    os.system("find $HOME -type d -iname " + cisoname + " | grep " + cisoname + " > pathofworkdir.txt")
    pathofworkdir1 = open("pathofworkdir.txt")
    pathofworkdir2 = pathofworkdir1.read()
    pathofworkdir3 = slice(-1)
    pathofworkdir = pathofworkdir2[pathofworkdir3]
    write("copying filesystem to workspace directory => " + cisoname + "\n")
    os.system("cp filesystem.squashfs " + str(pathofworkdir))
    write("Done copying\n")
    os.system("sudo rm -rf filesystem.squashfs")
    os.system("cp casperpath.txt " + pathofworkdir)
    os.system("sudo rm -rf pathofworkdir.txt")
    time.sleep(1)
    os.system("sudo rm -rf casperpath.txt")
    os.chdir(cwdp4)
    os.chdir(cisoname)
    #os.system("pwd")
    write("unsquashing and setting up the filesystem... for chroot\n")
    os.system("sudo unsquashfs filesystem.squashfs")
    os.system("sudo chmod -R a+rwX squashfs-root/")
    os.chdir("squashfs-root")
    os.system("sudo cp /etc/resolv.conf etc/")
    write("Done!, now you may modify your ISO with the following command => sudo chroot . bash\n") 

    
    exit()

checkiso()


    
