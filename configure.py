import os
from write import write

def listToString(s):

    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

    # return string
    return str1

pattern = 'FNMATCH_*.iso'
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
            chosenone.append(name)
            break
        else:
            write("ISO not found!\nKindly make sure there is only 1 iso which is to be reconfigured and has default name\n")
            return
        

    #else:
       # print("Something went wrong! Please retry with a valid ISO Image")
def run():
    write("Please wait...\n")
    print(chosenone)
    #os.system("7z x " +  )


checkiso()
run()

    
