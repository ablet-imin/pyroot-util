# pyrootUtil

Open a root file within a python context:  
```python
from pyrootUtil import open_root      
with open_root(filename, opt) as rf:  
    #read objects from rf              
```     
Automatically cleanup when finish reading the file.  

