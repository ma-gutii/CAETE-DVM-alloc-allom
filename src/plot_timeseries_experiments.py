import pandas as pd
import os
import matplotlib.pyplot as plt
import glob

while True:
    grd_acro = input('Gridcell acronym [AFL, ALP, FEC, MAN, CAX]: ')

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


# Consolidate file paths
base_path = "/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs"
path_regclim = os.path.join(base_path, grd_acro, f"experiments/{grd_acro}_regularclimate/gridcell{grd}/concatenated_series_{grd_acro}_regularclimate.csv")
path_csv_allfreq = os.path.join(base_path, grd_acro, "experiments/20perc_reduction", f"concatenated_series_{grd_acro}_20prec_allfreq.csv")
path = os.path.join(base_path, grd_acro, "experiments/20perc_reduction/")

# Use a function for frequency logic
def get_file_path(freq):
    if freq == 0:
        return path_regclim
    return os.path.join(base_path, grd_acro, f'experiments/20perc_reduction/concatenated_series_{grd_acro}_20prec_{freq}y.csv')

# Avoid using reserved words
dfs_list = []

# Verify if the table with all frequencies for this experiment already exists
if os.path.exists(path_csv_allfreq) and os.path.exists(path_regclim):
    print('\n !!!!!!!!! The csv with all frequencies for this experiment already exists !!!!!!!!! \n')
    csv_allfreq = pd.read_csv(path_csv_allfreq)
    df_regclim = pd.read_csv(path_regclim)
    
else:
    print('\n !!!!!!!!! Creating the csv with all frequencies for this experiment !!!!!!!!! \n')
    df_regclim = pd.read_csv(path_regclim)
    df_regclim['frequency'] = 0
    df_regclim['prec_red_perc'] = 0.0
    df_regclim['total_carbon'] = df_regclim[['cleaf', 'cwood', 'croot', 'csap', 'cheart', 'csto']].sum(axis=1)

    path = os.path.join(base_path, grd_acro, "experiments/20perc_reduction/")
    files = glob.glob(os.path.join(path, '*y.csv'))

    for file in files:
        frequency = int(file.split('_')[-1][0])
        df = pd.read_csv(file)
        df['frequency'] = frequency
        df['prec_red_perc'] = 20.0
        df['total_carbon'] = df[['cleaf', 'cwood', 'croot', 'csap', 'cheart', 'csto']].sum(axis=1)
        dfs_list.append(df)

    dfs_list.append(df_regclim)
    csv_allfreq = pd.concat(dfs_list, ignore_index=True)
    csv_allfreq['date_dateformat'] = pd.to_datetime(csv_allfreq['Date'])
    csv_allfreq.to_csv(os.path.join(path, f'concatenated_series_{grd_acro}_20prec_allfreq.csv'), index=False)

# # Plotting the time series
# plt.figure(figsize=(13, 9))

# for freq in [0, 1, 3, 5, 7]:
#     file_path = get_file_path(freq)
#     if os.path.exists(file_path):
#         if freq == 0:
#             print(f'\nPlotting time series for regular climate...\n')
#             df = pd.read_csv(file_path)
#             df['date_dateformat'] = pd.to_datetime(df['Date'])
#             plt.plot(df['date_dateformat'], df['npp'], label='Regular climate', linewidth=0.6, alpha=0.8, color='black', zorder=5)
#         else:
#             print(f'\nPlotting time series for frequency {freq} years...\n')
#             df = pd.read_csv(file_path)
#             df['date_dateformat'] = pd.to_datetime(df['Date'])
#             plt.plot(df['date_dateformat'], df['npp'], label=f'Frequency {freq} years', linewidth=0.8, alpha=0.8)

# # Add labels to the axes and legend
# plt.xlabel('Date')
# plt.ylabel('NPP')
# plt.title('Time series - 20% precipitation reduction')
# plt.legend()

# # Save the plot as a PNG file
# plt.savefig(os.path.join(path, f'{grd_acro}_timeseries_allfreq_20perc.png'))

# # Show the plot
# plt.show()

# # Plot freq X regular climate
# fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 8), sharex=True)

# frequencies = [1, 3, 5, 7]

# for idx, freq in enumerate(frequencies, 1):
#     file_path = get_file_path(freq)
#     if os.path.exists(file_path) and os.path.exists(path_regclim):
#         print(f'\nPlotting time series for frequency {freq} years...\n')
#         df = pd.read_csv(file_path)
#         df['date_dateformat'] = pd.to_datetime(df['Date'])
#         df_regclim = pd.read_csv(path_regclim)
#         df_regclim['date_dateformat'] = pd.to_datetime(df_regclim['Date'])

#         axes[(idx-1)//2, (idx-1)%2].plot(df['date_dateformat'], df['npp'], label=f'Frequency {freq} years', linewidth=0.2, color='coral', alpha=0.8)
#         axes[(idx-1)//2, (idx-1)%2].plot(df_regclim['date_dateformat'], df_regclim['npp'], label='Regular Climate', linewidth=0.2, color='black', alpha=0.8)

#         axes[(idx-1)//2, (idx-1)%2].set_xlabel('Date')
#         axes[(idx-1)//2, (idx-1)%2].set_ylabel('NPP')
#         axes[(idx-1)//2, (idx-1)%2].set_title(f'Time series - {freq} years precipitation reduction')
#         axes[(idx-1)//2, (idx-1)%2].legend()

# plt.tight_layout()
# plt.savefig(os.path.join(path, f'{grd_acro}_timeseries_allfreq_x_regclim_20perc.png'))
# plt.show()

# Plotting other variables with 3 year frequency
df = pd.read_csv(f'/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/{grd_acro}/experiments/20perc_reduction/concatenated_series_{grd_acro}_20prec_allfreq.csv')
df['date_dateformat'] = pd.to_datetime(df['Date'])

# Filter DataFrame for the desired frequency

df_3y = df[df['frequency'] == 3]

df_regclim = pd.read_csv(path_regclim)
df_regclim['frequency'] = 0
df_regclim['prec_red_perc'] = 0.0
df_regclim['total_carbon'] = df_regclim[['cleaf', 'cwood', 'croot', 'csap', 'cheart', 'csto']].sum(axis=1)
df_regclim['date_dateformat'] = pd.to_datetime(df_regclim['Date'])


plt.figure(figsize=(15, 10))
variables_to_plot = ['npp', 'photo', 'ls', 'evapm']
freq = 3

# Number of subplots
num_subplots = len(variables_to_plot)

# Create subplots
fig, axes = plt.subplots(2, 2, figsize=(15,10), sharex=True)

# Plot each variable in a separate subplot
for idx, variable in enumerate(variables_to_plot):
    row = idx // 2
    col = idx % 2
    axes[row, col].plot(df_3y['date_dateformat'], df_3y[variable],  linewidth=0.8, alpha=0.8, color = 'coral', label = '20% reduction (3 years)')
    # Plot reg clim
    axes[row, col].plot(df_regclim['date_dateformat'], df_regclim[variable], linewidth=0.8, alpha=0.8, color = 'blue', label = 'Regular climate')

    axes[row, col].set_ylabel(f'{variable.upper()}')

# Add labels to the common x-axis and legend
axes[-1, 0].set_xlabel('Date')
axes[-1, 1].set_xlabel('Date')
plt.suptitle(f'Time series - {freq} years precipitation reduction', y=1.02)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

# Adjust layout for better spacing
plt.tight_layout()

# Save the plot as a PNG file
plt.savefig(os.path.join(path, f'{grd_acro}_timeseries_freq{freq}_20perc_subplots.png'))

# Show the plot
plt.show()
