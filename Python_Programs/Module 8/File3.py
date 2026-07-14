#!/usr/bin/env python3
#
#import test
#from test import myfile
from test import myfile as my

#this is where the test.py code sits after import

def myfile2 ():
    print ("File2 __name__ %s" %__name__)

    if __name__ == "__main__":
        print ("File, File2, is being run directly")
    else:
        print ("File, File2, is being imported")

def main ():
    print ("The beginning of the File3.py program")
    myfile2 ()
    #test.myfile ()
    #myfile ()
    my ()

if __name__ == '__main__':
    main ()