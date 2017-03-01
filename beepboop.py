#!/usr/bin/python3
##me@danielpeluso.com
###print numbers 1 - {arg3}
####multiples of arg1 print beep
###multiples of arg2 print boop
##multiples of arg1 and arg2 print beepboop
#

import sys

if __name__ == '__main__' :
   try:
       start = int(input("Start value:"))
   except ValueError:
       print("That aint no number")
       sys.exit(0) 
   try:
       end = int(input("End value:"))
   except ValueError:
       print("That aint no number")
       sys.exit(0)
   try:
       fm = int(input("First multiple:"))
   except ValueError:
       print("That aint no number")
       sys.exit(0)
   try:
       sm = int(input("Second multiple:"))
   except ValueError:
       print("That ain't no number")
       sys.exit(0)
   except KeyboardInterrupt:
       print("User cancel")

for i in range(start, end):
	if i % fm == 0 and i % sm == 0:
		print("beepboop")
	elif i % sm == 0:
		print("boop")
	elif i % fm == 0:
		print("beep")
	else:
		print(i)
