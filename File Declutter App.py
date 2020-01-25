'''
@author: ROHAN TRIX
'''

import os
mydir='<CHANGE THIS TO YOUR WORKING DIRECTORY>'
os.chdir(mydir)
for root_path,sub_dir,files in os.walk(os.getcwd()):
    for i in files:
        if not 'en.srt' in str(i) and '.srt' in str(i) :
            os.remove(os.path.join(root_path,str(i)))
            