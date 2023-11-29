# Copyright 2017- LabTerra

#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.)

#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.

#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <http://www.gnu.org/licenses/>.

# AUTHOR: Bianca Fazio Rius


#This script is designed to process and concatenate Net Primary Productivity (NPP) 
#time series data from different spins in a run. It collects data from multiple spins, 
#organizes it into a pandas DataFrame, and saves the concatenated time series 
#into a CSV file. Additionally, the script generates a plot of the NPP time series 
#against dates and saves it as a PNG image. 

import numpy as np
import joblib
import os
import pandas as pd
import matplotlib.pyplot as plt

# Prompt the user to determine if the script is running on a server or not
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

# Input the run name
run_name = input('run name: ')

# Navigate to the specified folder
os.chdir(f'{main_path}outputs/{run_name}/gridcell175-235/')

# Initialize lists to store all time series, dates, and spins
all_series = []
all_series_ls = []
all_dates = []
all_spins = []

# Date intervals for each spin
run_breaks_hist = [('19790101', '19801231'),
                   ('19810101', '19821231'),
                   ('19830101', '19841231'),
                   ('19850101', '19861231'),
                   ('19870101', '19881231'),
                   ('19890101', '19901231'),
                   ('19910101', '19921231'),
                   ('19930101', '19941231'),
                   ('19950101', '19961231'),
                   ('19970101', '19981231'),
                   ('19990101', '20001231'),
                   ('20010101', '20021231'),
                   ('20030101', '20041231'),
                   ('20050101', '20061231'),
                   ('20070101', '20081231'),
                   ('20090101', '20101231'),
                   ('20110101', '20121231'),
                   ('20130101', '20141231'),
                   ('20150101', '20161231')]

# Iterate over all available spins
for spin, (start_date, end_date) in enumerate(run_breaks_hist, start=1):
    # Load data for the current spin
    with open(f"spin{spin:02d}.pkz", 'rb') as fh:
        dt = joblib.load(fh)

    # Get the NPP time series for the current spin and its dates
    npp_series = dt.get('npp', [])
    # ls_series  = dt.get('ls', [])
    date_index = pd.date_range(start=start_date, end=end_date, freq='D')

    # Add the time series, dates, and spin number to the lists
    all_series.extend(npp_series)
    # all_series_ls.extend(ls_series)

    all_dates.extend(date_index)
    all_spins.extend([spin] * len(date_index))

# Create a DataFrame with time series, dates, and spin numbers
df = pd.DataFrame({'Spin': all_spins, 'Date': all_dates, 'NPP': all_series}) #, 'ls': all_series_ls})

# Save the DataFrame to a CSV file
df.to_csv('concatenated_series_all_spins.csv', index=False)

# Print a small part of the data
print(df.head())

# Convert the 'Date' column to the datetime data type if it's not already
df['Date'] = pd.to_datetime(df['Date'])

# Plot the time series for 'NPP' against the 'Date' column
plt.plot(df['Date'], df['NPP'])
plt.xlabel('Date')
plt.ylabel('NPP')
plt.title('Time Series of NPP')

# Plot the time series for 'NPP' against the 'Date' column
# plt.plot(df['Date'], df['ls'])
# plt.xlabel('Date')
# plt.ylabel('ls')
# plt.title('Time Series of ls')

# Save the plot as an image
plt.savefig(os.path.join(f'{main_path}/outputs/{run_name}/gridcell175-235/', f'timeseries_{run_name}.png'))