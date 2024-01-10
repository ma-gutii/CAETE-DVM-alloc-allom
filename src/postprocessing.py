import pktocsv_allspins as p 
import time_series as t
import os
import joblib
import pandas as pd
import numpy as np

while True:
    server = input('Are you running in the server? y/n ')

    if server == 'y':
        # Set the main_path accordingly for server
        main_path = '/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/'
        break
    elif server == 'n':
        # Set the main_path accordingly for local machine
        main_path = '/home/bianca/bianca/CAETE-DVM-alloc-allom/'
        break

run_name = input('Run name: ')
grd = input('Which gridcell (lat-long): ')
print('GRDDDDD == ', grd)
path = f"../outputs/{run_name}/gridcell{grd}"
grd_name = f"gridcell{grd}"


start_year = 1979
end_year   = 2017

run_breaks_hist1 = []
run_breaks_hist2 = []


for year in range(start_year, end_year, 1):
    #Crie as datas de início e fim no formato 'YYYYMMDD'
    start_date = f"{year}0101"
    end_date = f"{year}1231"
 
    # Obtenha o número do spin 
    spin_id = str((year - start_year) // 1 + 1).zfill(2)

    # Adicione a tupla à lista run_breaks_hist
    run_breaks_hist1.append((start_date, end_date, spin_id))


for year in range(start_year, end_year, 1):
    #Crie as datas de início e fim no formato 'YYYYMMDD'
    start_date = f"{year}0101"
    end_date = f"{year}1231"
 

    # Adicione a tupla à lista run_breaks_hist
    run_breaks_hist2.append((start_date, end_date))


# # Process spins 1 to ..
for date_range in run_breaks_hist1:

    start_date, end_date, spin_id = date_range
    file = p.read_pkz(int(spin_id), run_name, grd_name )
    p.pkz2csv(file, path, grd_name, run_name, int(spin_id), date_range)

# # Navigate to the specified folder to access spins
os.chdir(f'{main_path}outputs/{run_name}/{grd_name}/')

for date_range in run_breaks_hist2:
    print('Joining together all time series, dates, and spins =====',date_range)
    
print('Plotting')
t.join_plot(start_date, end_date, run_breaks_hist2, main_path, run_name, grd_name)



