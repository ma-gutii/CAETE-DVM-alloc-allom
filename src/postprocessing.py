import pktocsv_allspins as p 
import os
import joblib
import pandas as pd
import numpy as np

run_name = input('Run name: ')
grd = input('Which gridcell (lat-long): ')
print('GRDDDDD == ', grd)
path = f"../outputs/{run_name}/gridcell{grd}"
grd_name = f"gridcell{grd}"


start_year = 1979
end_year   = 2017

run_breaks_hist = []

for year in range(start_year, end_year, 1):
    #Crie as datas de início e fim no formato 'YYYYMMDD'
    start_date = f"{year}0101"
    end_date = f"{year}1231"
 
    # Obtenha o número do spin 
    spin_id = str((year - start_year) // 1 + 1).zfill(2)

    # Adicione a tupla à lista run_breaks_hist
    run_breaks_hist.append((start_date, end_date, spin_id))

# Exiba a lista resultante
# print(run_breaks_hist)

# # Process spins 1 to ..
for date_range in run_breaks_hist:

    start_date, end_date, spin_id = date_range
    file = p.read_pkz(int(spin_id), run_name, grd_name )
    p.pkz2csv(file, path, grd_name, run_name, int(spin_id), date_range)

