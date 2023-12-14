import os
import shutil
import multiprocessing as mp
from pathlib import Path
import joblib
import numpy as np

from parameters import BASE_RUN, ATTR_FILENAME, run_path, pls_path

assert run_path.exists(), "Wrong path to initial conditions"
assert pls_path.exists(), "Wrong path to Attributes Table"

with open(run_path, 'rb') as fh:
    init_conditions = joblib.load(fh)

# new outputs folder
run_name = input(f"Give a name to this output")
dump_folder = Path(f"{run_name}")

for gridcell in init_conditions:
    gridcell.clean_run(dump_folder, "init_cond")
    gridcell.pr -= gridcell.pr * 0.0
    gridcell.ipar
    # prevent negative values
    gridcell.pr[np.where(gridcell.pr < 0.0)[0]] = 0.0
    assert np.all(gridcell.pr >= 0.0)


from caete import run_breaks_hist as rb


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

