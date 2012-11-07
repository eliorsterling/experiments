'''
  untar_and_delete.py
  by Paul Mason (pdm126@hotmail.co.uk)
  and Lisha Sterling (lishevita@gmail.com)
  
  Does what it says on the tin.
  Extracts tarballs from a specfied directory
  into a directory of your choice.
  Will remove tarballs after extraction if you want.
  
  Uses python < 2.7
      change raw_input() to input() for python >3.0
      
  License: GNU Public License v.3
           http://www.gnu.org/licenses/gpl.html
  
'''

import os
import sys
import re
import tarfile

path_to_tarballs = raw_input("Which directory holds the tarballs?")

def unzipthese(tarballs, delete):
	extractTarPath = raw_input("What is the destination directory? ('.' is current directory)")
	for tarball in tarballs:
		extractThis = path_to_tarballs +"/"+ tarball
		tfile = tarfile.open(extractThis)
		tfile.extractall(extractTarPath)
		if delete == "y" or delete == "Y":
		    print("Removing *"+ extractThis+"*")
		    os.remove(extractThis)
		
	

tarballs = []
dirEntries = os.listdir(path_to_tarballs)
for entry in dirEntries:
  if re.match(".*\.tar\.gz", entry):
  	tarballs.append(entry)
  	print(entry)
    
unzip = raw_input("Unzip all?(y/N) ")
delete = raw_input("Delete tarballs after extraction? (y/N)")
if unzip == "y" or unzip == "Y":
    unzipthese(tarballs, delete)
        
        
    
