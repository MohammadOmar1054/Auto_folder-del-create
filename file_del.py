import os 
path_working = os.getcwd()
print('Path we are working on : ', path_working)

for i in range(90): 
    del_fle = os.system("rmdir auto_created{}".format(i))