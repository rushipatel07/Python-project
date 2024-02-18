# problem: Your local university's Raptors fan club maintains a register of its active members on a .txt document. Every month they update the file by removing the members who are not active. You have been tasked with automating this with your Python skills.
# Given the file currentMem, Remove each member with a 'no' in their Active column. Keep track of each of the removed members and append them to the exMem file. Make sure that the format of the original files in preserved. (Hint: Do this by reading/writing whole lines and ensuring the header remains )
# Run the code block below prior to starting the exercise. The skeleton code has been provided for you. Edit only the cleanFiles function.

# code provided by coursera

from random import randint as rnd

memReg = '/members.txt'
exReg = '/inactive.txt'
fee =('yes','no')

def genFiles(current,old):
    with open(current,'w+') as writefile: 
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"

        for rowno in range(20):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[rnd(0,1)]))


    with open(old,'w+') as writefile: 
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"
        for rowno in range(3):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[1]))


genFiles(memReg,exReg)

# self code.

def cleanFiles(currentMem, exMem):
    with open(currentMem, 'r+') as writeFile:
        with open(exMem, 'a+') as appendFile:
            writeFile.seek(0)
            members = writeFile.readlines()
            header = members[0]
            members.pop(0)
            inactive = [member for member in members if 'no' in member]
            writeFile.seek(0)
    
            for member in members:
                if member in inactive:
                    appendFile.write(member)
                else:
                    writeFile.write(member)
            writeFile.truncate()

# code provided by coursera.
            
memReg = '/members.txt'
exReg = '/inactive.txt'
cleanFiles(memReg,exReg)


headers = "Membership No  Date Joined  Active  \n"
with open(memReg,'r') as readFile:
    print("Active Members: \n\n")
    print(readFile.read())
    
with open(exReg,'r') as readFile:
    print("Inactive Members: \n\n")
    print(readFile.read())