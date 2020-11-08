#Author: Pinaki Vazarkar
#Professor: Jordan Moline
"""
 Your program this week will use the OS library in order to validate that a directory exists before creating a file in that directory.
 Your program will prompt the user for the directory they would like to save the file in as well as the name of the file.
 The program should then prompt the user for their name, address, and phone number.
 Your program will write this data to a comma separated line in a file and store the file in the directory specified by the user.
"""
import os
import sys

if __name__=='__main__':

    print("Hello and Welcome!")
    print("You will asked for a directory where you want to save your file, a filename and you name, address and phonenumber")

    while True:
        #dirpath=r"/Users/pinakivazarkar/Documents/BellevueHW/ComputerProgramming"
        dirpath = input("Please enter a directory name where you would like to store your file or q to quit: ")

        if dirpath.lower()=='q':
            sys.exit()

        if  not os.path.dirname(dirpath):
            print("Sorry that directory does not exist.  Please try again or q to quit")
        else:
            validfilename=input("Please enter a file name, no extensions please ")
            validfilename=validfilename.split('.')[0]

            yourname=input("\nPlease enter your Name.  Eg. John Doe")
            youraddress=input("Please enter you address: Eg. 12 Crickets Lane, SleepyHollow, MA 99999")
            yourphonenumber=input("Please enter in your phone number.  Eg: 888-999-5555")

            fullfilename=r"{d}/{f}.csv".format(d=dirpath, f=validfilename)
            with open(fullfilename, 'w') as fh:
                fh.write("{n} , {a}, {p}".format(n=yourname, a=youraddress, p=yourphonenumber))
            fh.close()

            print("\nThank-you, this is what you entered for Name, Address and Phone Number ")

            with open(fullfilename, 'r') as rf:
                mylines=rf.readlines()

            print(mylines)
            rf.close()

            break