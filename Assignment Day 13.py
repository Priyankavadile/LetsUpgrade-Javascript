13

##Q1
##Remove the hardcoded part from the code with the help of configparser

import os
from configparser import ConfigParser
config=ConfigParser()
config.read("D://Py Ex/Advance-py//ex_config.ini")
path=config.get("Exten", "path")
old_text=config.get("Exten","OE")
New_text=config.get("Exten","NE")

os.chdir(path)
os.getcwd()

for file in os.listdir():
  if file.endswith(old_text):
    first_name=file.rsplit(".",1)[0]
    new_name=first_name+"."+New_text
    print(new_name)
    os.rename(file,new_name)


##Q2
##The question has been asked in an interview
##Please write the code in such a way so that it could give all path of a #file (same name ) which is present
##in multiple locations.

import os

resp =os.walk("C:\\Users\\priya\\Downloads") 
d1= {}
for r,d,f in resp:
  for file in f:
    d1.setdefault(file,[]).append(r)
print(d1)

file_name = input("Enter the file name ")
for k,v in d1.items():
  if file_name.lower() in k.lower() :
    print (k,":", v)
    for find_file in v:
      print(find_file)
