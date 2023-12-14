"""

Code documentation:

The clean_run function performs the following actions:

    1. Save Current Conditions:
Before starting a new round or experiment, the function saves the current conditions associated with a save_id identifier.
    2. Check Output Directory Existence:
Checks if the output directory associated with the new experiment already exists. If the directory already exists, the code takes measures to avoid overwriting.
    3. Revert Changes in Case of Failure:
If the attempt to create the directory fails due to its preexistence, the code reverts the changes made earlier (restoring self.out_dir to its original value) and raises an exception.
    4. Record Current Conditions:
Adds a pair (save_id, self.outputs.copy()) to the realized_runs list, thus recording the current state of the simulation.
    5. Clear Attributes for the New Round:
Resets relevant attributes for the simulation, such as self.outputs and self.run_counter, preparing for a new simulation round.

This function appears prepare for a new round of simulation, ensuring the integrity of saved data and avoiding accidental overwriting of previous results.


The variable run_breaks_hist contains the data in which the code will be run

Function zip_gridtime enables to acces the intervals defined in the run_breaks_hist
"""
import os
import shutil
import multiprocessing as mp
from pathlib import Path
import joblib
import numpy as np

from parameters import BASE_RUN, ATTR_FILENAME, run_path, pls_path

assert run_path.exists(), "Wrong path to initial conditions"
assert pls_path.exists(), "Wrong path to Attributes Table"

# Open the binary file at 'run_path' for reading ('rb')
with open(run_path, 'rb') as fh:
    # Load data from the file using the joblib library
    init_conditions = joblib.load(fh)
    #init_conditions contais all the attributes and methods of caete.grd


# new outputs folder
run_name = input(f"Give a name to this output: ")
dump_folder = Path(f"{run_name}")

for gridcell in init_conditions:
    gridcell.clean_run(dump_folder, "init_cond")
    # gridcell.pr = gridcell.pr * 0.1
    # gridcell.rsds = gridcell.rsds * 0.0
    # prevent negative values
    gridcell.pr[np.where(gridcell.pr < 0.0)[0]] = 0.0
    assert np.all(gridcell.pr >= 0.0)


# from caete import run_breaks_hist as rb

rb = [('19790101', '19801231'),
      ('19810101', '19821231')]

def zip_gridtime(grd_pool, interval):
    res = []
    for i, j in enumerate(grd_pool):
        res.append((j, interval[i % len(interval)]))
    return res



def apply_funX(grid, brk):
    grid.run_caete_allom(brk[0], brk[1])
    return grid


n_proc = mp.cpu_count()

for i, brk in enumerate(rb):
    print(f"Applying model to the interval {brk[0]}-{brk[1]}")
    init_conditions = zip_gridtime(init_conditions, (brk,))
    with mp.Pool(processes=n_proc) as p:
        init_conditions = p.starmap(apply_funX, init_conditions)

