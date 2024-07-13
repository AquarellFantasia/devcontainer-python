
from zdrive import Uploader

input_directory = "/home/abhinav/Downloads"
u = Uploader()

# creating a folder in Drive where we want to upload the folder
parent_folder_id = u.createFolder(name="Data")
result = u.uploadFolder(input_directory, max_depth=3,
                        parentId=parent_folder_id)
print(result)
