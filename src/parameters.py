"""DEFINE SOME PARAMETERS FOR CAETÊ EXPERIMENTS"""
from pathlib import Path 

# Choose the sampling mode:
ATTR_FILENAME = ""
pls_path = None

while True:
    sample_type = input('Choose the sampling mode [uniform, normal]: ')

    if sample_type == 'uniform':
        ATTR_FILENAME = 'pls_attrs-6000.csv'
        pls_path = Path(f"../outputs/rodada_uniforme/{{ATTR_FILENAME}}")
        break

    elif sample_type == 'normal':
        ATTR_FILENAME = 'pls_attrs-6000.csv'
        pls_path = Path(f"../outputs/rodada_normal/{{ATTR_FILENAME}}")
        break

    else:
        print('Invalid option, try again')

ATTR_FILENAME = "pls_attrs-6000.csv"
START_COND_FILENAME = f"CAETE_STATE_START_MAN_save_spin_2_.pkz"

run_path = Path(f"../outputs/MAN/state_start/{START_COND_FILENAME}")

