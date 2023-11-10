import os
import pandas as pd
import re


run_name = "tresmil"#input("What is the run name? ")
grd_name = "175-235"#input("The grid cell?lat-long ")
path_csv = f"/home/bianca/bianca/CAETE-DVM-alloc-allom/outputs/{run_name}/gridcell{grd_name}/csv"

# Get a list of all files with .csv extension in the directory
list_files = [file for file in os.listdir(path_csv) if file.endswith(".csv")]

# # Extract the final group of numbers from the file names
s = [re.search(r"_([0-9]+)\.csv", file).group(1) for file in list_files if re.search(r"_([0-9]+)\.csv", file)]

# # Create a DataFrame with the extracted numeric part
pls_id = pd.DataFrame({"pls_id": pd.to_numeric(s)})

# # Check the structure of pls_id to make sure it is as expected
print(pls_id.info())

# # Read file with all pls traits
pls_traits = pd.read_csv("/home/bianca/bianca/CAETE-DVM-alloc-allom/outputs/pls_attrs-3000.csv")

# # Select only data from living pls (those in the list of files)
new_pls_traits = pls_traits[pls_traits['PLS_id'].isin(pls_id['pls_id'])]

