'''
Author: Jay
Date pubished: 5th January 2022
Purpose: Automated script to squash the reconfigured filesystem of Ubuntu ISO to allow the user boot in his/her newly customized Ubuntu OS
'''
import os
from write import write


write("Welcome to the file squashing script\n")
workdir = open("workdir.txt","r")
workr = workdir.read()
os.chdir(workr)
write("Removing the older filesystem.squashfs\n")
os.system("sudo rm -rf filesystem.squashfs")
write("Proceeding to squash the file now\n")        
os.system("sudo mksquashfs squashfs-root filesystem.squashfs -comp xz")
write("squashing done now copying the new filesystem to the iso image\n")
casp = open("casperpath.txt", "r")
caspath = casp.read()
print(caspath)
os.system("cp filesystem.squashfs " + caspath)
os.system("sudo rm -rf casperpath.txt")
write("Done... now you may copy the unzipped folder to a bootable device and boot in your custom Ubuntu OS :DD\n")



