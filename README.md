A basic script to allow you to chroot inside any stock ubuntu ISO instead of doing the samething manually or installing CUBIC software
wrote this script just as a hobby


**How to Use:**

**Step1**:Create a folder with desired name

**Step2**:Then put your ubuntu iso image inside the folder, make sure not to edit its name and keep it default

**Step3**: Download or clone this repository

**Step4**:Now for the final step, put the configure.py and write.py inside that folder and run the configure.py and follow the prompts

**Step5**: Once you are done with the configure.py script, you can enter the chroot environment with "sudo chroot . bash"

**Step6**: After you are done configuring the filesystem, exit and run mksq.py to squash the filesystem again and put it inside the appropriate folder

**Step7**: Now for the final step copy all the extracted files to a pendrive or any bootable device and boot in your custom configured ubuntu os :D

Note: I have tested it on Linux mint with ubuntu-20.04-desktop-amd64 ISO file, so you may test it on different ubuntu versions with different ubuntu iso files and you all are free to let me know about behaviour changes or any bugs or issues to be addressed in script


**If you have any issues with the script, you may bring that up as an Issue here on github or contact me at => contactjay0x5@gmail.com**


