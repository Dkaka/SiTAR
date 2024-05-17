#!/bin/bash
pathDatasetEuroc='/home/ziwen/ORBSLAM3/' # Update this with your actual dataset path
resultsPath='/home/ziwen/ORBSLAM3/results' # Update this with your desired results directory path

mkdir -p $resultsPath # Create the results directory if it doesn't exist

# Change the number 101 to the number of iterations you want to run
for i in $(seq 1 101); do
    resultFolder="$resultsPath/iteration_$i"
    mkdir -p $resultFolder # Create a directory for this iteration's results
    echo "Launching V102 with Monocular-Inertial sensor, Iteration $i"

    # Change directory to the result folder for this iteration
    cd $resultFolder
    
    # Execute the SLAM and evaluation commands
    $pathDatasetEuroc/ORB_SLAM3/Examples/Monocular-Inertial/mono_inertial_euroc $pathDatasetEuroc/ORB_SLAM3/Vocabulary/ORBvoc.txt $pathDatasetEuroc/ORB_SLAM3/Examples/Monocular-Inertial/EuRoC.yaml $pathDatasetEuroc/V103 $pathDatasetEuroc/ORB_SLAM3/Examples/Monocular-Inertial/EuRoC_TimeStamps/V103.txt dataset-V103_monoi

    echo "------------------------------------"
    echo "Evaluation of V103 trajectory with Monocular-Inertial sensor, Iteration $i"
    python $pathDatasetEuroc/ORB_SLAM3/evaluation/evaluate_ate_scale.py $pathDatasetEuroc/ORB_SLAM3/V103/mav0/state_groundtruth_estimate0/data.csv f_dataset-V103_monoi.txt --plot V103_monoi.pdf

    # Return to the original directory
    cd -
done