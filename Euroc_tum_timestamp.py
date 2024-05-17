import os

# Specify the directory containing the .txt files
directory_path = '/home/ziwen/ORBSLAM3/common_results_correct_timestamp/'

# Loop over each file in the directory
for filename in os.listdir(directory_path):
    if filename.endswith('.txt'):  # Check if the file is a .txt file
        file_path = os.path.join(directory_path, filename)
        print(f"Processing file: {file_path}")
        # Read and process the file
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        # Process each line
        with open(file_path, 'w') as file:
            for line in lines:
                parts = line.split()  # Split the line into parts
                parts[0] = parts[0].split('.')[0]  # Remove the '.000000' from the first element
                new_line = ' '.join(parts) + '\n'  # Rejoin the parts into a new line
                file.write(new_line)  # Write the new line to the file

print("All files have been modified in place.")
