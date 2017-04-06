import os
import string

def rename_files():
    # get the file names from a folder
    file_list = os.listdir("/home/ievgen/images")
    print(file_list)

    saved_path = os.getcwd()
        
    print("Current Working Directory is " + saved_path)
    os.chdir("/home/ievgen/images")
    
    # for each file, rename filename
    for file_name in file_list:
        print("Old name - " + file_name)
        print("New name - " + file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)
      
rename_files()
