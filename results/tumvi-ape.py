import numpy as np

from evo.tools.settings import SETTINGS
from evo.tools import file_interface
from evo.core import metrics
from evo.tools import log
from evo.core import sync
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import pprint
import copy
import pandas as pd
import itertools
import os
import time
import subprocess
import math
import glob
# import shutil
import matplotlib.pyplot as plt
import evo.common_ape_rpe as common

groundtruth = "/home/ziwen/ORBSLAM3//V103/mav0/state_groundtruth_estimate0/data.csv"

trajectory = "/home/ziwen/ORBSLAM3/common_results_correct_timestamp/f_dataset-V103_monoi_iteration_1.txt"

traj_ref = file_interface.read_euroc_csv_trajectory(groundtruth)
# traj_ref.timestamps = traj_ref.timestamps / 1e3 # Convert timestamps to seconds for TUM as Euroc/TUM-VI are in nanoseconds.
print(traj_ref.timestamps[0])
traj_est = file_interface.read_tum_trajectory_file(trajectory)
traj_est.timestamps = traj_est.timestamps / 1e9
print(traj_est.timestamps[0])

file_interface.write_tum_trajectory_file("V103TUM_GT.txt", traj_ref)

file_interface.write_tum_trajectory_file("V103TUM.txt", traj_est)

max_diff = 0.1     
traj_ref, traj_est = sync.associate_trajectories(traj_ref, traj_est, max_diff)        
traj_est_aligned = copy.deepcopy(traj_est)
traj_est_aligned.align(traj_ref, correct_scale=False, correct_only_scale=False)         
ape_metric = metrics.APE(metrics.PoseRelation)
ape_metric.process_data((traj_ref, traj_est))
ape_result = ape_metric.get_result("groundtruth", "Orb-SLAM3-Monoi")
ape_result.info["title"] = "Groundtruth vs. Orb-SLAM3-Monoi"

ape_result.add_trajectory("groundtruth", traj_ref)
ape_result.add_trajectory("Orb-SLAM3-Monoi", traj_est)

common.plot_result()
