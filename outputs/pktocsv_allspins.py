import os
import joblib
import pandas as pd
import numpy as np

def read_pkz(spin):
    with open(f"/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/{run_name}/{grd_name}/spin{spin:02d}.pkz", 'rb') as fh:
        dt = joblib.load(fh)
    print(f"Loaded data for spin {spin:02d}")
    return dt

def pkz2csv(file, path, grd_name, spin_id, date_range) -> pd.DataFrame:
    assert date_range[2] == f"{spin_id:02d}", f"ID do spin {spin_id} não corresponde ao ID no date_range: {date_range[2]}"


    CT1 = pd.read_csv("/home/bianca/bianca/CAETE-DVM-alloc-allom/src/code_table_allom.csv")

    MICV = ['year', 'pid', 'ocp']

    area = file['area']
    area_dim = area.shape

    
    
    idx1 = np.where(area[:, 0] > 0.0)[0]
    cols = CT1.VariableCode.__array__()

    # Get the date range for the current spin
    idxT1 = pd.date_range(date_range[0], date_range[1], freq='D')

    fname = f"{run_name}_spin{spin_id:02d}"
    folder_path = f"./csv/{fname}"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    folder_path2 = f"/home/bianca/bianca/CAETE-DVM-alloc-allom/outputs/{run_name}/{grd_name}/csv"
    if not os.path.exists(folder_path2):
        os.makedirs(folder_path2)

    for lev in idx1:
        area_TS = area[lev, :]
        area_TS = pd.Series(area_TS, index=idxT1)

        # Use the date range specified for the current spin
        idxT2 = pd.date_range(date_range[0], date_range[1], freq='Y')
        YEAR = []
        PID = []
        OCP = []

        for i in idxT2:
            YEAR.append(i.year)
            PID.append(int(lev))
            OCP.append(float(area_TS.loc[[i.date()]].iloc[0]))
            print(f"lev: {lev}, PID: {int(lev)}")

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

        # Save the CSV file with spin information in the name
        csv_filename = f"{run_name}_{grd_name}_spin{spin_id:02d}_EV_{int(lev)}.csv"
        dt1.to_csv(f"/home/bianca/bianca/CAETE-DVM-alloc-allom/outputs/{run_name}/{grd_name}/csv/{csv_filename}", index=False)

# User inputs
run_name = input('Run name: ')
grd = input('Which gridcell (lat-long): ')
path = f"../outputs/{run_name}/gridcell{grd}"
grd_name = f"gridcell{grd}"

# List of date ranges for spins 1 to 19 with corresponding IDs
run_breaks_hist = [('19790101', '19801231', '01'),
                   ('19810101', '19821231', '02'),
                   ('19830101', '19841231', '03'),
                   ('19850101', '19861231', '04'),
                   ('19870101', '19881231', '05'),
                   ('19890101', '19901231', '06'),
                   ('19910101', '19921231', '07'),
                   ('19930101', '19941231', '08'),
                   ('19950101', '19961231', '09'),
                   ('19970101', '19981231', '10'),
                   ('19990101', '20001231', '11'),
                   ('20010101', '20021231', '12'),
                   ('20030101', '20041231', '13'),
                   ('20050101', '20061231', '14'),
                   ('20070101', '20081231', '15'),
                   ('20090101', '20101231', '16'),
                   ('20110101', '20121231', '17'),
                   ('20130101', '20141231', '18'),
                   ('20150101', '20161231', '19')]

# Process spins 1 to 19
for date_range in run_breaks_hist:
    start_date, end_date, spin_id = date_range
    file = read_pkz(int(spin_id))
    pkz2csv(file, path, grd_name, int(spin_id), date_range)

# import os
# import joblib
# import pandas as pd
# import numpy as np

# def read_pkz(spin):
#     with open(f"/home/bianca/bianca/CAETE-DVM-alloc-allom/outputs/{run_name}/{grd_name}/spin{spin:02d}.pkz", 'rb') as fh:
#         dt = joblib.load(fh)
#     print(f"Loaded data for spin {spin:02d}")
#     return dt

# def pkz2csv(file, path, grd_name, spin, date_range) -> pd.DataFrame:
#     print(grd_name)

#     CT1 = pd.read_csv("/home/bianca/bianca/CAETE-DVM-alloc-allom/src/code_table_allom.csv")

#     MICV = ['year', 'pid', 'ocp']

#     area = file['area']
#     area_dim = area.shape
    
#     idx1 = np.where(area[:, 0] > 0.0)[0]
#     cols = CT1.VariableCode.__array__()

#     # Get the date range for the current spin
#     idxT1 = pd.date_range(date_range[0], date_range[1], freq='D')
#     print('Shape idxT1', idxT1.shape)

#     fname = f"{run_name}_spin{spin:02d}"
#     folder_path = f"./{fname}"
#     if not os.path.exists(folder_path):
#         os.makedirs(folder_path)

#     folder_path2 = f"/home/bianca/bianca/CAETE-DVM-alloc-allom/outputs/{run_name}/{grd_name}/csv"
#     if not os.path.exists(folder_path2):
#         os.makedirs(folder_path2)

#     for lev in idx1:
#         area_TS = area[lev, :]
#         area_TS = pd.Series(area_TS, index=idxT1)

#         # Use the date range specified for the current spin
#         idxT2 = pd.date_range(date_range[0], date_range[1], freq='Y')
#         YEAR = []
#         PID = []
#         OCP = []

#         for i in idxT2:
#             YEAR.append(i.year)
#             PID.append(int(lev))
#             OCP.append(float(area_TS.loc[[i.date()]].iloc[0]))

#         ocp_ts = pd.Series(OCP, index=idxT2)
#         pid_ts = pd.Series(PID, index=idxT2)
#         y_ts = pd.Series(YEAR, index=idxT2)

#         series = []
#         for i, var in enumerate(MICV):
#             if var == 'year':
#                 series.append(y_ts)
#             elif var == 'pid':
#                 series.append(pid_ts)
#             elif var == 'ocp':
#                 series.append(ocp_ts)
#             else:
#                 pass
#         dt1 = pd.DataFrame(dict(list(zip(cols, series))))

#         # Save the CSV file with spin information in the name
#         csv_filename = f"{run_name}_{grd_name}_spin{spin:02d}_EV_{int(lev)}.csv"
#         dt1.to_csv(f"/home/bianca/bianca/CAETE-DVM-alloc-allom/outputs/{run_name}/{grd_name}/csv/{csv_filename}", index=False)

# # User inputs
# run_name = input('Run name: ')
# grd = input('Which gridcell (lat-long): ')
# path = f"../outputs/{run_name}/gridcell{grd}"
# grd_name = f"gridcell{grd}"

# run_breaks_hist = [('20130101', '20141231'),
#                    ('20150101', '20161231')]

# # Adiciona um ID de 01 a 19 a cada tupla
# # run_breaks_hist_with_id = [(f"{i + 1:02d}", start_date, end_date) for i, (start_date, end_date) in enumerate(run_breaks_hist)]

# # Exibe a nova lista
# # for item in run_breaks_hist_with_id:
#     # print(item)

# # Process spins 18 and 19
# for spin, date_range in zip([18, 19], run_breaks_hist):
#     file = read_pkz(spin)
#     pkz2csv(file, path, grd_name, spin, date_range)