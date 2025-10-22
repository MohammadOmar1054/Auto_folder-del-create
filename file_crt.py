import os 

class folder_create:
    print("File we are working on : ", os.getcwd())
    def __init__(self, folder_name): 
        self.folder_name = folder_name
        
    def create(self): 
        for i in range(10): 
            if os.path.exists(self.folder_name):
                print(f"Folder '{self.folder_name}' already exists!")
                
            else :
                try:
                    os.mkdir(self.folder_name)
                    print('creating file.......')
                    print(f"Folder '{self.folder_name}' created successfully.")
                except:
                    print(f"An unexpected error occurred while creating {self.folder_name}:")

            ask_more = str(input('Do you wish to create more (y/n) : ')) 
            if ask_more=="y":
                self.foler_name = str(input('Enter the new folder name : '))
                
            elif ask_more=="n": 
                break 
if __name__ ==  "__main__":          
    nm_fl= str(input("Enter the name of the folder : "))
    folder = folder_create(nm_fl)
    folder.create()
