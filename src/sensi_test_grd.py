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

# Loop para executar para cada ano de '19790101' a '20161231'
for year in range(1979, 2017):
    start_date = f"{year}0101"
    end_date = f"{year}1231"

    # Aplica gridcell.pr * 0.5 a cada 3 anos
    if (year % 3 == 0) and (start_date != '19790101'):  # Garante que o primeiro ano não seja afetado
        print(year)
        gridcell.pr = gridcell.pr * 0.5
    
    # Execute o método para o intervalo de datas atual
    gridcell.run_caete_allom(start_date, end_date)

# gridcell.run_caete_allom('19790101','19791231')
# gridcell.run_caete_allom('19800101','19801231')

# gridcell.run_caete_allom('20000101','20050101')
# gridcell.pr = gridcell.pr * 0.5
# gridcell.run_caete_allom('20050101','20060101')
# gridcell.rsds = gridcell.rsds
# gridcell.run_caete_allom('20070101','20150101')

# def apply_funX(grid, brk):
#     grid.run_caete_allom(brk[0], brk[1])
#     return grid


# n_proc = mp.cpu_count()

# # for i, brk in enumerate(rb):
# #     print(f"Applying model to the interval {brk[0]}-{brk[1]}")
# #     init_conditions = zip_gridtime(init_conditions, (brk,))
# #     with mp.Pool(processes=n_proc) as p:
# #         init_conditions = p.starmap(apply_funX, init_conditions)




# # Defina os intervalos de tempo desejados
# time_intervals = [
#     ('19790101', '19801231'),
#     ('19810101', '19821231'),
#     ('19830101', '19841231'),
#     ('19850101', '19861231'),
#     ('19870101', '19881231'),
#     ('19890101', '19901231'),
#     ('19910101', '19921231'),
#     # Adicione mais intervalos conforme necessário
# ]

# # Defina os intervalos de tempo desejados
# time_intervals = [
#     ('19790101', '19801231'),
#     ('19810101', '19821231'),
#     # Adicione mais intervalos conforme necessário
# ]

# # Número de rodadas desejado
# num_rounds = 3

# # Loop para realizar múltiplas rodadas
# for round_num in range(1, num_rounds + 1):
#     # Escolha um intervalo de tempo para a rodada atual
#     selected_interval = time_intervals[round_num - 1]
    
#     print(f"Round {round_num}: Applying model to the interval {selected_interval[0]}-{selected_interval[1]}")
    
#     # Crie uma cópia das condições iniciais para cada rodada e intervalo
#     init_conditions_copy = init_conditions.copy()

#     # Atualize o nome do diretório de saída para a pasta run_name
#     dump_folder = Path(f"{run_name}")

#     # Loop para aplicar o modelo em paralelo ou sequencial, conforme desejado
#     with mp.Pool(processes=n_proc) as p:
#         init_conditions_copy = p.starmap(apply_funX, zip_gridtime(init_conditions_copy, (selected_interval,)))

#     # Após a rodada, execute as ações de limpeza para salvar resultados, etc.
#     for gridcell in init_conditions_copy:
#         # Salve os resultados na mesma pasta run_name sem criar subpastas round_name
#         gridcell.clean_run(dump_folder, f"round{round_num}_init_cond")

#     # Se você quiser realizar alguma ação específica após cada rodada, faça aqui
#     # Exemplo: Salvar resultados agregados ou fazer alguma análise pós-rodada
