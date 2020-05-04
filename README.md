# pyrootUtil

Open a root file within a python context:  
'
from pyrootUtil import open_root   
with open_root(filename, opt) as rf:
  \# your code   
  rf.ls()   
'         
Automatically cleanup when finish reading the file.  

