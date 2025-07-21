# GENERAL DESCRIPTION
# This script consolidates the initial data extraction and conversion steps
# from PKZ (Pickle) simulation outputs with the subsequent post-processing
# and trait-merging functionalities.


#
## OUTPUTS:
# - 'concatenated_series_{run_name}.csv': Daily time series of core biogeochemical
#    variables (NPP, Photo, LAI, etc.) for all spins.
# - 'timeseries_{run_name}_all_variables.png': Plots of the above time series.
# - 'final_merged_sorted_data.csv': Consolidated PLS occupation data across all spins.
# - 'PLS_alive_traits.csv': Consolidated PLS occupation data (only PLSs with area > 0.0, i.e. ALIVE PLSs) merged with
#    occupation-weighted trait values.


#
## DETAILED DESCRIPTION:
#
# Pipeline Flow:
# 1. User Input & Configuration: Gathers necessary simulation parameters to access the folder of interest
#    (gridcell, run type, etc.).
# 2. PKZ to CSV Conversion: Iterates through all specified simulation 'spins' (years),
#    loads the raw PKZ data, and converts key variables into CSV format:
#    - Individual CSVs for 'Plant Life Stage (PLS)' occupation data per spin
#      (e.g., '{run_name}_{grd_name}_spinXX_EV_{int(lev)}.csv').
#    - A single, concatenated CSV for main biogeochemical time series
#      (e.g., 'photo', 'npp', 'lai') across all spins
#      (saved as 'concatenated_series_{run_name}.csv').
#    - Generates and saves time series plots for these biogeochemical variables.
# 3. PLS Occupation Data Consolidation: Reads all individual PLS occupation CSVs,
#    consolidates them into a unified DataFrame, ensuring data completeness
#    across all years and PLSs, filling gaps with zeros where necessary.
#    Temporary individual PLS CSVs are then removed for tidiness (this can be removed if there
#    is an interest in having the csv for each PLS).
# 4. Trait Data Merging & Calculation: Merges the consolidated PLS occupation
#    data with an external PLS trait table ('pls_attrs-6000.csv') to integrate
#    trait information. It then calculates occupation-weighted trait values.


#
# Author: Bianca Rius (some functionalities adapted from J.P. Darela scripts os post processing)


# IMPORTANT: if any change in the script is made, please put your name initials in front of the implementation


# import general libraries
import os
import joblib
import pandas as pd
import numpy as np
import re


# import functions created from other python files


# pktocsv_allspins.py
import pktocsv_allspins as p
# This module serves as the core conversion engine for your raw simulation output data.
# Its primary function is to read .pkz files (a binary file format) and extract specific information,
# converting it into CSV files. It focuses on the 'area' variable, which represents the
# occupation of different Plant Life Stages (PLS) over time. For each PLS that has a recorded area
# in a given "spin" (i.e., a simulation year), it generates a separate CSV file detailing
# the year, PLS ID, and its daily occupation.


# time_series.py
import time_series as t
# This module acts as the time series compiler and visualizer. It's designed to collect
# data for various biogeochemical variables (such as Net Primary Productivity (NPP),
# photosynthesis, Leaf Area Index (LAI), carbon in different pools, etc.) from
# all "spins" (years) of a simulation. It then concatenates this data into a single,
# comprehensive dataset. Finally, it saves the consolidated time series into a CSV
# file (named concatenated_series_*.csv) and also generates plots of these variables over time,
# offering a quick and insightful overview of the model's dynamics.    


# IMPORTANT: if you are not using the Manaus gridcell you have to change the two following variables
grd_acro = 'MAN'
grd = '186-239'


main_path = "/home/amazonfaceme/marcelagutierrez/novas_rodadas/CAETE-DVM-alloc-allom/outputs/" 
#(if you want determine a basis path that will be used later) o caminho ate os outputs


run_name = input('Run name: ')


# Use this instead if you want to process more than one run at the same time
run_names = [run_name]


# Loop through the run_names (if it is a list)
for run_name in run_names:
   print(f'Processing run: {run_name}')
  
   # ATTENTION: the path is relative to the your execution diretory (i.e. the folder where the model outputs are)
   # If you want, determine a main_path before run_name, that will save as a basis path
   # Also, ajust the 'path' to be the diretory where the CSVs will be saved inside the main_path
   output_base_path = os.path.join(main_path, run_name, f"gridcell{grd}")
   path_csv_output = os.path.join(output_base_path, "csv")


   # Garantuee the output directory for the CSVs exists
   if not os.path.exists(path_csv_output):
       os.makedirs(path_csv_output)


   # Adjust according to the period you used to run the mode (1st and last year of simulation)
   start_year = 1979
   end_year   = 2017
  
   # Initialize an empty list to store metadata for each simulation spin (year).
   # Each entry in this list will be a tuple containing the start date, end date,
   # and a unique string identifier for the spin.
   run_breaks_hist1 = []


   # Loop through each year from the defined 'start_year' up to and including 'end_year'.
   # The '+ 1' in the range ensures that 'end_year' is included in the iteration.
   for year in range(start_year, end_year + 1):
       # Format the start date for the current year as a string 'YYYYMMDD' (e.g., '19790101').
       start_date = f"{year}0101"
       # Format the end date for the current year as a string 'YYYYMMDD' (e.g., '19791231').
       end_date = f"{year}1231"
       # Calculate a sequential spin ID based on the year.
       # This converts the year into a 1-based index (e.g., 1979 becomes spin 1, 1980 becomes spin 2).
       # .zfill(2) ensures the spin ID is zero-padded to two digits (e.g., '01', '02', '10').
       spin_id = str((year - start_year) // 1 + 1).zfill(2)
       # Append the tuple (start_date, end_date, spin_id) to the list.
       run_breaks_hist1.append((start_date, end_date, spin_id))


   # This section processes each defined spin (year) by converting its raw PKZ data into CSV files.
   # It iterates through the 'run_breaks_hist1' list, which contains the metadata for each spin.
   # Process spins 1 to N, converting PKZ to CSV
   for date_range in run_breaks_hist1:
       # Unpack the tuple 'date_range' into its individual components:
       # - start_date_range: The start date string for the current spin.
       # - end_date_range: The end date string for the current spin.
       # - spin_id_str: The two-digit string identifier for the current spin (e.g., '01', '35').
       start_date_range, end_date_range, spin_id_str = date_range
       # Convert the string 'spin_id_str' to an integer 'spin_id_int'.
       # This integer format is often required by functions that need a numeric spin identifier.
       spin_id_int = int(spin_id_str)


       # Print a message to the console indicating which spin is currently being processed.
       # This provides real-time feedback to the user about the script's progress.
       print(f'Converting spin {spin_id_str} to CSV for {run_name}...')
      
       # Call the 'read_pkz' function from the 'pktocsv_allspins' module (aliased as 'p').
       # This function loads the raw simulation data from the PKZ file corresponding to the current spin.
       # Parameters: spin_id_int (numeric spin ID), run_name, gridcell name, gridcell acronym.
       file_data = p.read_pkz(spin_id_int, run_name, f"gridcell{grd}", grd_acro)
      
       # Call the 'pkz2csv' function from the 'pktocsv_allspins' module ('p').
       # This function takes the loaded PKZ data ('file_data') and converts specific parts
       # (primarily the 'area' variable for each PLS) into individual CSV files.
       # The 'output_base_path' is passed to ensure the CSVs are saved in the correct,
       # predefined output directory for the current run and gridcell.
       # Parameters: loaded PKZ data, base output path, gridcell name, run name,
       #             numeric spin ID, full date range tuple, gridcell acronym.
       p.pkz2csv(file_data, output_base_path, f"gridcell{grd}", run_name, spin_id_int, date_range, grd_acro)


   # Print a final message to the console indicating that the conversion process
   # for all spins of the current run has been successfully completed.
   print(f"Finished converting all spins to CSV for {run_name}.")
  


   ##############################################
   # --- Post processing and selecting alive PLSs ---
  
   print(f"\nStarting post-processing for {run_name}...")


   # path_csv is the same as path_csv_output defined above
   path_csv = path_csv_output


   # List all .csv files in the directory, excluding any that start with "concatenated" to get every EV file
   list_files = [file for file in os.listdir(path_csv) if file.endswith(".csv") and not file.startswith("concatenated")]


   # Create an empty DataFrame to store the merged and sorted data
   final_merged_df = pd.DataFrame()


   # Extract the PLS ID from the filenames and group the files
   for file in list_files:
       # Use regex to find the numeric PLS ID (e.g., '0', '1', '123') before '.csv'
       match = re.search(r"EV_([0-9]+)\.csv", file)
       if match:
           # Extract the captured group (the PLS ID)
           group_number = match.group(1)
           # Construct the full path to the current CSV file
           file_path = os.path.join(path_csv, file)
           # Read the CSV file into a temporary DataFrame
           df = pd.read_csv(file_path)


           # Add a column to store the group number (PLS ID) for reference during merging
           df['GroupNumber'] = group_number
           # Concatenate the current DataFrame to the final DataFrame, ignoring index issues
           final_merged_df = pd.concat([final_merged_df, df], ignore_index=True)


   # Create a DataFrame containing all possible combinations of years and unique group numbers (PLS IDs).
   # This ensures that even if a PLS had zero occupation in certain years, those years are included.
   all_years = range(start_year, end_year + 1) # Note: 'end_year' here is exclusive; adjust if needed for your range.
   all_group_numbers = final_merged_df['GroupNumber'].unique()


   # Create a DataFrame from all year-group number combinations
   all_combinations = pd.DataFrame([(year, group_number) for year in all_years for group_number in all_group_numbers],
                                    columns=['YEAR', 'GroupNumber'])


   # Merge 'all_combinations' with 'final_merged_df' using a left merge.
   # This fills in any missing year-PLS combinations, creating gaps (NaNs) where data was absent.
   final_merged_df = pd.merge(all_combinations, final_merged_df, on=['YEAR', 'GroupNumber'], how='left')


   # Fill NaN values in the 'PID' (Plant ID) column with their corresponding 'GroupNumber'.
   # This assigns the PLS ID where it might be missing due to the merge, then converts to integer type.
   final_merged_df['PID'] = final_merged_df['PID'].fillna(final_merged_df['GroupNumber']).astype(int)


   # Fill NaN values in the 'OC' (Occupation) column with 0.0.
   # This ensures that years/PLSs without recorded occupation are treated as zero.
   final_merged_df['OC'] = final_merged_df['OC'].fillna(0.0)


   # Sort the final DataFrame first by 'GroupNumber' (PLS ID) and then by 'YEAR' in ascending order.
   # This organizes the data logically for time series analysis per PLS.
   final_merged_df.sort_values(by=["GroupNumber", "YEAR"], inplace=True)


   # Remove the temporary 'GroupNumber' column as it's no longer needed after merging and sorting.
   final_merged_df.drop(columns=['GroupNumber'], inplace=True)


   # Construct the full file path for the consolidated and sorted data.
   final_file_path = os.path.join(path_csv, "final_merged_sorted_data.csv")
   # Save the consolidated DataFrame to a CSV file without the DataFrame index.
   final_merged_df.to_csv(final_file_path, index=False)


   # Inform the user that the consolidated file has been created and where to find it.
   print("Great!! Your consolidated file has been created! \nFind it in:", path_csv)


   # Delete the individual PLS CSVs that were used for consolidation to keep the directory tidy
   # ATTENTION: this can be turned off if you need.
   temp_files = os.listdir(path_csv)
   for file in temp_files:
       # Ensure only the original individual PLS CSVs are deleted,
       # and not the newly created consolidated file.
       if file.startswith(f'{run_name}') and file.endswith('.csv') and not file.startswith("final_merged_sorted_data"):
           file_path2 = os.path.join(path_csv, file)
           os.remove(file_path2) # Delete the file
   print("Temporary individual PLS CSVs have been removed.")


   # Assign the consolidated PLS occupation data to a new variable for further processing.
   PLS_ocp_year = final_merged_df


   # Inform the user about the next step: merging with trait data.
   print('\nNow getting trait values from attrs and calculating occupation-weighted traits.')
   # Read the CSV file containing trait data for all possible PLSs.
   # Ensure this path is correct for your environment.
   pls_traits = pd.read_csv("/home/amazonfaceme/marcelagutierrez/novas_rodadas/CAETE-DVM-alloc-allom/outputs/rodada_uniforme/pls_attrs-6000.csv")


   # Get the unique PIDs (Plant IDs) from the consolidated occupation data.
   # These are the PLSs that were identified as 'alive' (i.e., had occupation > 0) at some point.
   pids_to_select = final_merged_df['PID'].unique()


   # Filter the full trait table ('pls_traits') to include only traits for the 'alive' PLSs.
   selected_PLS_traits = pls_traits[pls_traits['PLS_id'].isin(pids_to_select)]


   # Perform the merge operation: combine the PLS occupation data with their selected traits.
   # Merge 'PLS_ocp_year' with 'selected_PLS_traits' using 'PID' and 'PLS_id' as keys.
   ocp_traits = pd.merge(PLS_ocp_year, selected_PLS_traits[['PLS_id', 'sla_random']], left_on='PID', right_on='PLS_id', how='left')
   # Remove the redundant 'PLS_id' column that resulted from the merge.
   ocp_traits = ocp_traits.drop('PLS_id', axis=1)


   # Calculate a new trait value ('sla_ocp') by multiplying the PLS's occupation ('OC')
   # by its random specific leaf area ('sla_random'). This creates an occupation-weighted trait.
   ocp_traits['sla_ocp'] = ocp_traits['OC'] * ocp_traits['sla_random']
   # **Note**: Leave it here Even if you won't use the trait weighted by the area (the original value won't be deleted) 


   # Construct the full file path for the final merged data with traits.
   final_merged_path = os.path.join(path_csv, "PLS_alive_traits.csv")
   # Save this final DataFrame to a CSV file without the DataFrame index.
   ocp_traits.to_csv(final_merged_path, index=False)


   # Inform the user that the PLS_alive_traits.csv file has been created and its location.
   print("PLS_alive_traits.csv has been created! \nFind it in:", path_csv)
   # Print a final completion message for the current run.
   print(f"Processing completed for run_name: {run_name}")
   # Print a separator for clarity between runs (if processing multiple runs).
   print("====================================")

