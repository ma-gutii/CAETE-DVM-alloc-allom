"""DEFINE SOME PARAMETERS FOR CAETÊ EXPERIMENTS"""
from pathlib import Path

# Name of the base historical observed run.
while True:
    grd_acro = input('Gridcell acronym [ALP, FEC, MAN, CAX, NVX]: ')

    if grd_acro == 'ALP':
        grd = '188-213'
        base_run = 'ALP_save_spin_1'

        break

    elif grd_acro == 'FEC':
        grd = '200-225'
        break
    elif grd_acro == 'MAN':
        grd = '186-239'
        base_run = 'MAN_save_spin_2'
        break
    elif grd_acro == 'CAX':
        grd = '183-257'
        break
    elif grd_acro == 'NVX':
        grd = '210-249'
        break
    else:
        print('This acronym does not correspond')
        break

ATTR_FILENAME = "pls_attrs-6000.csv"
START_COND_FILENAME = f"CAETE_STATE_START_{base_run}_.pkz"

run_path = Path(f"../outputs/{grd_acro}/state_start/{base_run}/{START_COND_FILENAME}")
pls_path = Path(f"../outputs/baserun_6000pls_attrs_table/{ATTR_FILENAME}")
