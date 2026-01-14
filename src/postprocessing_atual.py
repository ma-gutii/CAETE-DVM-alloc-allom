import pktocsv_allspins as p
import os
import joblib
import pandas as pd
import numpy as np
import re

main_path = f'/home/amazonfaceme/marcelagutierrez/novas_rodadas/CAETE-DVM-alloc-allom'
run_names = ['simulacao_normal']
grd_name = "gridcell186-239"
grd_acro = "MAN"
path = f'/home/amazonfaceme/marcelagutierrez/novas_rodadas/CAETE-DVM-alloc-allom/outputs/simulacao_normal/gridcell186-239/'


for run_name in run_names:
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
        print("spin id", spin_id)

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
        file = p.read_pkz(int(spin_id), run_name, grd_name, grd_acro)
        p.pkz2csv(file, path, grd_name, run_name, int(spin_id), date_range, grd_acro)

    # # Navigate to the specified folder to access spins
    #print("path", os.chdir(f'{main_path}/{run_name}/{grd_name}/'))
    os.chdir(path)
    #print(os.chdir(f'{main_path}/{run_name}/{grd_name}/'))

    for date_range in run_breaks_hist2:
        print('Joining together all time series, dates, and spins =====',date_range)

#erro possivelmente a partir daqui
# Get a list of all files with .csv extension in the directory(there is one csv for each alive PLS)
path_csv = f"{path}/csv/"
list_files = [file for file in os.listdir(path_csv) if file.endswith(".csv")]

print(list_files)

# # Extract the final group of numbers from the file names(get the PLS id)
s = [re.search(r"_([0-9]+)\.csv", file).group(1) for file in list_files if re.search(r"_([0-9]+)\.csv", file)]

# # Create an empty DataFrame to store the merged and sorted data
final_merged_df = pd.DataFrame()

# # Extract the final group of numbers from the file names and group the files (group each PLS considering all spins)
for file in list_files:
    match = re.search(r"EV_([0-9]+)\.csv", file)
    if match:
        group_number = match.group(1)
        file_path = os.path.join(path_csv, file)
        df = pd.read_csv(file_path)
#       Add a column to store the group number for reference
        df['GroupNumber'] = group_number
        # Merge the current group into the final DataFrame
        final_merged_df = pd.concat([final_merged_df, df], ignore_index=True)
		
       
# # Create a DataFrame with all combinations of years and group numbers

merged_data = final_merged_df.copy()

#start_year = int(start_date[:4])
#end_year = int(end_date[:4])+1

print(f"Start year: {start_year}, End year: {end_year}")

all_years = range(start_year, end_year)
print(list(all_years))

# #Select the PLS ID for the alives
all_group_numbers = merged_data['GroupNumber'].unique()
print(all_group_numbers.size)

print(merged_data.columns)
all_combinations = pd.DataFrame([(year, group_number) for year in all_years for group_number in all_group_numbers],
                                 columns=['YEAR', 'GroupNumber'])


# Merge all_combinations with final_merged_df to fill gaps
merged_data = pd.merge(all_combinations, merged_data, on=['YEAR', 'GroupNumber'], how='left')


# Fill NaN values in 'PID' with 'GroupNumber' and convert back to int
merged_data['PID'] = merged_data['PID'].fillna(merged_data['GroupNumber']).astype(int)



# Fill NaN values in 'OC' with 0
merged_data['OC'] = merged_data['OC'].fillna(0.0)  




# Sort the final DataFrame by the "YEAR" column in ascending order
merged_data.sort_values(by=["GroupNumber", "YEAR"], inplace=True)



# Drop the temporary group number column
merged_data.drop(columns=['GroupNumber'], inplace=True)



# Save the final merged and sorted DataFra  prinme to a new CSV file
final_file_path = os.path.join(path_csv, "final_merged_sorted_data.csv")

merged_data.to_csv(final_file_path, index=False)

print("Your file has been created! Find it in:", path_csv)

# #Now get the trait values from attrs (without considering the occupation)
# # Read file with all pls traits
pls_traits = pd.read_csv(f"{main_path}/pls_attrs-6000.csv")

table_merged_data = pd.read_csv(f"{path_csv}/final_merged_sorted_data.csv")
print(table_merged_data)

# Get the PIDs, that is, the alive PLSs
pids = table_merged_data['PID'].unique()

# # Filtrar pls_traits com base nos PIDs
selected_PLS_traits = pls_traits[pls_traits['PLS_id'].isin(pids)]

# #PLS id, year and occupation
PLS_ocp_year = table_merged_data 

# # Realiza a agregação
ocp_traits = pd.merge(PLS_ocp_year, selected_PLS_traits[['PLS_id', 'g1','sla_random','wd_random']], left_on='PID', right_on='PLS_id', how='left')
# # Remove a coluna 'PLS_id' da nova tabela
ocp_traits = ocp_traits.drop('PLS_id', axis=1)

# #Calculates the value for a trait multiplying it by the PLS occupation (mesmo que a gente 
# não use, é bom ter o valor dos traits ponderados pela ocupação)
ocp_traits['sla_ocp'] = ocp_traits['OC']*ocp_traits['sla_random']
ocp_traits['wd_ocp'] = ocp_traits['OC']*ocp_traits['wd_random']
ocp_traits['g1_ocp'] = ocp_traits['OC']*ocp_traits['g1']

ocp_traits.to_csv(f"{path_csv}/PLS_alive_traits_{run_name}.csv", index=False)

