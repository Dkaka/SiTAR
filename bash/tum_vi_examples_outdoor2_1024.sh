#!/bin/bash
pathDatasetTUM_VI='/home/ziwen/ORBSLAM3/' #Example, it is necesary to change it by the dataset path


echo "Launching Outdoor 2 with Monocular-Inertial sensor"
./Examples/Monocular-Inertial/mono_inertial_tum_vi Vocabulary/ORBvoc.txt Examples/Monocular-Inertial/TUM_1024_far.yaml "$pathDatasetTUM_VI"/dataset-corridor5_1024_16/mav0/cam0/data Examples/Monocular-Inertial/TUM_TimeStamps/dataset-corridor5_512.txt Examples/Monocular-Inertial/TUM_IMU/dataset-corridor5_512.txt dataset-corridor5_1024_monoi

#echo "Launching Outdoor 2 with Stereo-Inertial sensor"
#./Examples/Stereo-Inertial/stereo_inertial_tum_vi Vocabulary/ORBvoc.txt Examples/Stereo-Inertial/TUM_512_outdoors.yaml "$pathDatasetTUM_VI"/dataset-outdoors2_512_16/mav0/cam0/data "$pathDatasetTUM_VI"/dataset-outdoors2_512_16/mav0/cam1/data Examples/Stereo-Inertial/TUM_TimeStamps/dataset-outdoors2_512.txt Examples/Stereo-Inertial/TUM_IMU/dataset-outdoors2_512.txt outdoors2_512_stereoi
