#!/usr/bin/env python3
#
#from test import myfile

#this is where the test.py code sits after import

def myfile2 ():
    print ("File2 __name__ %s" %__name__)

    if __name__ == "__main__":
        print ("File, File2, is being run directly")
    else:
        print ("File, File2, is being imported")

def main ():
    print ("The beginning of the File2 program")
    myfile2 ()
    print ("In between call to myfile2 and myfile1 in File2.py")
#    myfile ()

if __name__ == '__main__':
    main ()
