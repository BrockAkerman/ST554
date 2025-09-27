import pandas as pd
import time
import os

'''
INSTRUCTIONS FOR DEMO:

>> cd ./Project_Final/                #Change Director
>> python Loop.py                     #Initiate Loop
CTRL+C                                #to break the loop. 

'''

# Define paths
source_file = "power_streaming_data.csv"  # Path to the full dataset
output_folder = "Streaming_Data/"  # Folder where streaming data will be saved

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Read the full dataset
df = pd.read_csv(source_file)

# Streaming loop
for i in range(50):  # 50 iterations
    # Randomly sample 3 rows
    sampled_df = df.sample(n=3)

    # Format the file name with leading zeros for numbers 1-9
    if i < 9:
        file_path = f"{output_folder}/stream_sample_0{i+1}.csv"
    else:
        file_path = f"{output_folder}/stream_sample_{i+1}.csv"

    # Write sample to a CSV file (exclude indices)
    sampled_df.to_csv(file_path, index=False)

    print(f"Generated: {file_path}")  # Print confirmation

    time.sleep(10)  # Pause for 10 seconds before the next file