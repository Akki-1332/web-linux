#!/usr/bin/python3

import cgi
import subprocess as sp

print("content-type: text/html")
print()

cmd = cgi.FieldStorage().getvalue("c")
#print("hello akki...!!")
o = sp.getoutput("sudo " + cmd)
print(o)
