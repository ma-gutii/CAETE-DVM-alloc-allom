import pandas as pd
import os
import matplotlib.pyplot as plt

while True:
    grd_acro = input('Gridcell acronym [AFL, ALP, FEC, MAN, CAX, NVX]: ')

    if grd_acro == 'ALP':
        grd = '188-213'
        break
    elif grd_acro == 'FEC':
        grd = '200-225'
        break
    elif grd_acro == 'MAN':
        grd = '186-239'
        break
    elif grd_acro == 'CAX':
        grd = '183-257'
        break
    elif grd_acro == 'NVX':
        grd = '210-249'
        break
    elif grd_acro == 'AFL':
        grd = '199-248'
        break
    else:
        print('This acronym does not correspond')
        break



path_regclim = f"/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/{grd_acro}/experiments/{grd_acro}_regularclimate/gridcell{grd}/concatenated_series_{grd_acro}_regularclimate.csv"

path = f"/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/{grd_acro}/experiments/20perc_reduction/"

path_csv_allfreq = f'/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/{grd_acro}/experiments/20perc_reduction/concatenated_series_{grd_acro}_20prec_allfreq.csv'

#verify if the table with all frequencies for this experiment 
    #already exists
if os.path.exists(path_csv_allfreq) and os.path.exists(path_regclim):
    #load
    print('\n !!!!!!!!! The csv with all frequencies for this experiment already exists !!!!!!!!! \n')
    csv_allfreq = pd.read_csv(path_csv_allfreq)
    
    df_regclim = pd.read_csv(path_regclim)

else:
    print('\n !!!!!!!!! Creating the csv with all frquencies for this experiment !!!!!!!!! \n')

    #Lista para armazenar os dataframes
    list = []

    #Path to dir
    path = f"/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/{grd_acro}/experiments/20perc_reduction/"

    #Path reg clim
    path_regclim = f"/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/{grd_acro}/experiments/{grd_acro}_regularclimate/gridcell{grd}/concatenated_series_{grd_acro}_regularclimate.csv"
    df_regclim = pd.read_csv(path_regclim)
    df_regclim['frequency'] = 0
    df_regclim['prec_red_perc'] = 0.0

    df_regclim['total_carbon'] = (
        df_regclim['cleaf'] +
        df_regclim['cwood'] +
        df_regclim['croot'] +
        df_regclim['csap'] +
        df_regclim['cheart'] +
        df_regclim['csto']
        )


    # obtain list of files
    files = os.listdir(path)
    print(files)

    #iterates on csv files
    for file in files:
        if file.endswith('y.csv'):
            # Extrats the frequency of disturbance (1, 3, 5, 7 years)
            frequency = int(file.split('_')[-1][0])
            # print(frequency)

            # Load csv in a DataFrame e add the colunm 'frequency'
            df = pd.read_csv(os.path.join(path, file))
            df['frequency'] = frequency
            df['prec_red_perc'] = 20.
            df['total_carbon'] = (
            df['cleaf'] +
            df['cwood'] +
            df['croot'] +
            df['csap'] +
            df['cheart'] +
            df['csto']
            )
        # else:

            # Add df to the list
            list.append(df)

    #include csv regular climate in the list
    list.append(df_regclim)

    #concatenate the sheets
    csv_allfreq = pd.concat(list, ignore_index=True)

    csv_allfreq['date_dateformat'] = pd.to_datetime(csv_allfreq['Date'])


    #save the csv with all frequencies + regular climate
    csv_allfreq.to_csv(f"{path}/concatenated_series_{grd_acro}_20prec_allfreq.csv",index=False)

# #Plotting the time series:
plt.figure(figsize=(13,9))

# Iterate over the frequencies
for freq in [0, 1, 3, 5, 7]:
    if freq == 0:
        file_path = path_regclim
    else: 
        # File name for the current frequency
        file_name = f'concatenated_series_{grd_acro}_20prec_{freq}y.csv'

        # Full path of the file
        file_path = os.path.join(path, file_name)


    # Check if the file exists
    if os.path.exists(file_path):
        if freq == 0:
            print(f'\nPlotting time series for regular climate...\n')
            df = pd.read_csv(file_path)
            # Convert the 'Date' column to the date format
            df['date_dateformat'] = pd.to_datetime(df['Date'])
            # Plot the time series
            plt.plot(df['date_dateformat'], df['npp'], label=f'Regular climate', linewidth = 0.6, alpha=0.8, color = 'black', zorder = 5)

        else:
            print(f'\nPlotting time series for frequency {freq} years...\n')
            # Load the DataFrame from the CSV file
            df = pd.read_csv(file_path)
            # Convert the 'Date' column to the date format
            df['date_dateformat'] = pd.to_datetime(df['Date'])
            # Plot the time series
            plt.plot(df['date_dateformat'], df['npp'], label=f'Frequency {freq} years', linewidth = 0.8, alpha=0.8)

# # Add labels to the axes and legend
plt.xlabel('Date')
plt.ylabel('NPP')
plt.title('Time series - 20% precipitation reduction')
plt.legend()

# Save the plot as a PNG file
plt.savefig(os.path.join(path, f'{grd_acro}_timeseries_allfreq_20perc.png'))

# Show the plot
plt.show()

# Plot freq X regular climate:
# Frequencies to iterate over
frequencies = [1, 3, 5, 7]

# Create subplots
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 8), sharex=True)

# Iterate over the frequencies
for idx, freq in enumerate(frequencies, 1):
    # File name for the current frequency
    file_name = f'concatenated_series_{grd_acro}_20prec_{freq}y.csv'
    
    # Full path of the file
    file_path = os.path.join(path, file_name)

    # Check if the file exists
    if os.path.exists(file_path) and os.path.exists(path_regclim):
        print(f'\nPlotting time series for frequency {freq} years...\n')
        
        # Load the DataFrame from the CSV file
        df = pd.read_csv(file_path)
        df['date_dateformat'] = pd.to_datetime(df['Date'])
        df_regclim = pd.read_csv(path_regclim)
        df_regclim['date_dateformat'] = pd.to_datetime(df_regclim['Date'])


        # Plot the time series for the current frequency
        axes[(idx-1)//2, (idx-1)%2].plot(df['date_dateformat'], df['npp'], label=f'Frequency {freq} years', linewidth=0.2, color = 'coral', alpha = 0.8)
        
        # Plot the time series for regular climate
        axes[(idx-1)//2, (idx-1)%2].plot(df_regclim['date_dateformat'], df_regclim['npp'], label='Regular Climate', linewidth=0.2, color = 'black', alpha = 0.8)

#         # Add labels to the axes and legend
        axes[(idx-1)//2, (idx-1)%2].set_xlabel('Date')
        axes[(idx-1)//2, (idx-1)%2].set_ylabel('NPP')
        axes[(idx-1)//2, (idx-1)%2].set_title(f'Time series - {freq} years precipitation reduction')
        axes[(idx-1)//2, (idx-1)%2].legend()

# # Adjust layout
plt.tight_layout()

# # Save the plot as a PNG file
plt.savefig(os.path.join(path, f'{grd_acro}_timeseries_allfreq_x_regclim_20perc.png'))

# # Show the plot
plt.show()