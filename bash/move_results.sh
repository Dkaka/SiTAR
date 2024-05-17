#!/bin/bash
resultsPath='/home/ziwen/ORBSLAM3/results' # Path where the iteration folders are located
commonFolder='/home/ziwen/ORBSLAM3/common_results' # Path for the common folder to store the copied files

mkdir -p $commonFolder # Create the common folder if it doesn't exist

# Assuming the iterations are numbered from 1 to 101
for i in $(seq 1 101); do
    iterationFolder="$resultsPath/iteration_$i"
    if [ -d "$iterationFolder" ]; then # Check if the iteration folder exists
        fileName="f_dataset-V103_monoi_iteration_$i.txt" # New file name with iteration number
        cp "$iterationFolder/f_dataset-V103_monoi.txt" "$commonFolder/$fileName" # Copy and rename the file
        echo "Copied $iterationFolder/f_dataset-V103_monoi.txt to $commonFolder/$fileName"
    else
        echo "Skipping $iterationFolder, directory does not exist."
    fi
done

echo "All files have been copied to $commonFolder"