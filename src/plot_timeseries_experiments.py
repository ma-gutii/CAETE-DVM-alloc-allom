import pandas as pd
import os


path_csv_allfreq = f'/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/AFL/experiments/20perc_reduction/concatenated_series_AFL_20prec_allfreq.csv'

#verify if the table with all frequencies for this experiment 
    #already exists
if os.path.exists(path_csv_allfreq):
    #load
    print('\n !!!!!!!!! The csv with all frequencies for this experiment already exists !!!!!!!!! \n')
    csv_allfreq = pd.read_csv(path_csv_allfreq)

else:
    print('\n !!!!!!!!! Creating the csv with all frquencies for this experiment !!!!!!!!! \n')

    #Lista para armazenar os dataframes
    list = []

    #Path to dir
    path = "/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/AFL/experiments/20perc_reduction/"

    #Path reg clim
    path_regclim = "/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/AFL/experiments/AFL_regularclimate/gridcell199-248/concatenated_series_AFL_regularclimate.csv"
    df_regclim = pd.read_csv(path_regclim)
    df_regclim['frequency'] = 0
    df_regclim['prec_red_perc'] = 0.0


    # obtain list of files
    files = os.listdir(path)

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

            # Add df to the list
            list.append(df)

    #include csv regular climate in the list
    list.append(df_regclim)

    #concatenate the sheets
    csv_allfreq = pd.concat(list, ignore_index=True)

    #save the csv with all frequencies + regular climate
    csv_allfreq.to_csv(f"{path}/concatenated_series_AFL_20prec_allfreq.csv",index=False)

