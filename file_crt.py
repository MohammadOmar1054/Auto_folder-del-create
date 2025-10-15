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

