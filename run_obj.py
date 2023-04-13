import os

# Activate the trash_can environment in Anaconda
# os.system('conda activate trash_can')

# Activate trash_can in conda
# command=command = "conda activate trash_can"
# # Run command
# os.system(command)

# Change directory to the desired location
# os.chdir(r'D:\Programs\python\TF2\models\research\object_detection')

# Define the command to be executed
command = "python .\detect_from_webcam.py -m .\inference_graph\saved_model\ -l .\labelmap.pbtxt"

# Run the command in the Anaconda prompt
os.system(command)
