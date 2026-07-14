#!/usr/bin/env python3
#
#from File2 import myfile2


def myfile ():
    print ("This code is being run from test.py")
    print (" The file name: __name__ %s" %__name__)
    if __name__ == "__main__":
        print ("File, test.py, is being run directly")
    else:
        print ("File, test.py, is being imported")

def main ():
    print ("The beginning of the test module")
    myfile ()
    print ("In between call to myfile2 and myfile1 in File2.py")
#    myfile2 ()

if __name__ == '__main__':
    main ()
