import os
import joblib
import pandas as pd
import numpy as np
import re


start_date = '19790101'
end_date = '20161231'

main_path = f'/home/amazonfaceme/marcelagutierrez/novas_rodadas/CAETE-DVM-alloc-allom/'

run_names = ['simulacao_uniforme']

for run_name in run_names:
	with open(f"{main_path}outputs/{run_name}/gridcell186-239/spin38.pkz", 'rb') as fh:
		file = joblib.load(fh)

	CT1 = pd.read_csv(f"{main_path}code_table_allom.csv")

	MICV = ['year', 'pid', 'ocp']

	area = file['area']

	area_dim = area.shape
	print(area_dim)

	idx1 = np.where(area[:, 0] > 0.0)[0]
	print(idx1.shape)

	cols = CT1.VariableCode.__array__()
	print(cols)

	fname = f"{run_name}_spin38"

	folder_path = f"{main_path}outputs/{run_name}/gridcell186-239/csv/{fname}"
	

	if not os.path.exists(folder_path):
		os.makedirs(folder_path)

	for lev in idx1:
		area_TS = area[lev, :]
		print(f"lev: {lev}, area_TS length: {len(area_TS)}")
		idxT1 = pd.date_range(start=start_date, end=end_date, freq='D')    
		print('idxt1', idxT1)
		# print('')
		print(f'len area_TS {len(area_TS)} len idxT1 {len(idxT1)}')

		assert len(area_TS) == len(idxT1), "Length mismatch between area_TS and idxT1"

		# Se o assert não levantou um erro, significa que a condição é True
		#print("Success!!!! Length match between area_TS and idxT1")

		area_TS = pd.Series(area_TS, index=idxT1)
		idxT2 = pd.date_range(start=start_date, end=end_date, freq='D')

		YEAR = []
		PID = []
		OCP = []

		for i in idxT2:
			YEAR.append(i.year)
			PID.append(int(lev))
			OCP.append(float(area_TS.loc[[i.date()]].iloc[0]))

		ocp_ts = pd.Series(OCP, index=idxT2)
		pid_ts = pd.Series(PID, index=idxT2)
		y_ts = pd.Series(YEAR, index=idxT2)


		series = []
		for i, var in enumerate(MICV):
			if var == 'year':
				series.append(y_ts)
			elif var == 'pid':
				series.append(pid_ts)
			elif var == 'ocp':
				series.append(ocp_ts)
			else:
				pass
		dt1 = pd.DataFrame(dict(list(zip(cols, series))))

		csv_filename = f"{run_name}_gridcell186-239_spin38_EV_{int(lev)}.csv"
		dt1.to_csv(f"{main_path}outputs/{run_name}/gridcell186-239/csv/{csv_filename}", index=False)

# Get a list of all files with .csv extension in the directory(there is one csv for each alive PLS)
path_csv = f"{main_path}outputs/{run_name}/gridcell186-239/csv/"
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

start_year = int(start_date[:4])
end_year = int(end_date[:4])+1

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
pls_traits = pd.read_csv(f"{main_path}pls_attrs-6000.csv")

table_merged_data = pd.read_csv(f"{path_csv}final_merged_sorted_data.csv")
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

ocp_traits.to_csv(f"{path_csv}PLS_alive_traits_{run_name}.csv", index=False)

