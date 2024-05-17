#!/bin/bash
pathDatasetEuroc='/home/ziwen/ORBSLAM3/' # Update this with your actual dataset path
resultsPath='/home/ziwen/ORBSLAM3/results2' # Update this with your desired results directory path

mkdir -p $resultsPath # Create the results directory if it doesn't exist

# Change the number 101 to the number of iterations you want to run
for i in $(seq 1 101); do
    echo "-------------------------------------------------------------------------------------------------------------------------------------------------------------"

    echo "Launching V102 with Monocular-Inertial sensor, Iteration $i"
    resultFolder="$resultsPath/iteration_$i"
    mkdir -p $resultFolder # Create a directory for this iteration's results

    ./Examples/Monocular-Inertial/mono_inertial_euroc ./Vocabulary/ORBvoc.txt ./Examples/Monocular-Inertial/EuRoC.yaml "$pathDatasetEuroc"/V103 ./Examples/Monocular-Inertial/EuRoC_TimeStamps/V103.txt "$resultFolder"/dataset-V103_monoi

    ./Examples/Monocular-Inertial/mono_inertial_euroc ./Vocabulary/ORBvoc.txt ./Examples/Monocular-Inertial/EuRoC.yaml "$pathDatasetEuroc"/V103 ./Examples/Monocular-Inertial/EuRoC_TimeStamps/V103.txt dataset-V103_monoi

        ./Examples/Monocular-Inertial/mono_inertial_euroc ./Vocabulary/ORBvoc.txt ./Examples/Monocular-Inertial/EuRoC.yaml /home/ziwen/ORBSLAM3/V103 ./Examples/Monocular-Inertial/EuRoC_TimeStamps/V103.txt /home/ziwen/ORBSLAM3/dataset-V103_monoi



    echo "-----------------------------------------------------------------------------------------"

    echo "Evaluation of V103 trajectory with Monocular-Inertial sensor, Iteration $i"
    python evaluation/evaluate_ate_scale.py "$pathDatasetEuroc"/V103/mav0/state_groundtruth_estimate0/data.csv "$resultFolder/f_dataset-V103_monoi.txt" --plot "$resultFolder"/V103_monoi.pdf
    sleep 1
done