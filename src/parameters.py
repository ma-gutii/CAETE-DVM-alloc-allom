"""DEFINE SOME PARAMETERS FOR CAETÊ EXPERIMENTS"""
from pathlib import Path

# Name of the base historical observed run.
# gridcell_name = input('Acronym for your gridcell [ALP, FEC, MAN, CAX, NVX]')
# gridcell_name = input("lat-long")
BASE_RUN = f'init_condi_186239_2' 
ATTR_FILENAME = "pls_attrs-3000.csv"
START_COND_FILENAME = f"CAETE_STATE_START_{BASE_RUN}_.pkz"

run_path = Path(f"../outputs/{BASE_RUN}/{START_COND_FILENAME}")
pls_path = Path(f"../outputs/base_run/{ATTR_FILENAME}")
