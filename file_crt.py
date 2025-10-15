# import os 


    

# print("file we are working on : " , os.getcwd())


# for i in range(10): 
#     ex_fle = f"auto_created{i}"
#     os_maker = os.system("mkdir auto_created{}".format(i))
#     if os.path.exists(ex_fle): 
#         print("file already exist in the system")

import os

print("file we are working on: ", os.getcwd())


for i in range(4):
    folder_name = f"auto_created{i}"
    if os.path.exists(folder_name):
        print(f"Folder '{folder_name}' already exists!")
    else:
        try:
            os.mkdir(folder_name)
            print(f"Folder '{folder_name}' created successfully.")
        except:
            print(f"An unexpected error occurred while creating {folder_name}:")
