import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np


df = pd.read_csv("/home/bianca/bianca/CAETE-DVM-alloc-allom/scripts/EWS/results_csv/MAN_30prec_allfreq_timeseries_ews.csv")

freq = df['frequency']

fig, axs = plt.subplots(5, 1, figsize=(8, 4 * 5), sharex=True)

for i,f in enumerate(freq.unique()):
    subset_df = df[df['frequency'] == f]
    axs[i].plot(subset_df['timeindex'], subset_df['ar1'], label=f'Frequency {f}', color = 'black')
    # Adicionar linha tracejada vertical quando a frequência é "regularclimate" e o timeindex é 362
    if f == 'regularclimate':
        axs[i].axvline(x=362, linestyle='--', color='grey', label='break point')
    if f == '1':
        axs[i].axvline(x = 99, linestyle='--', color='grey', label='break point')
        axs[i].axvline(x = 167, linestyle='--', color='grey', label='break point')
        axs[i].axvline(x = 244, linestyle='--', color='grey', label='break point')
        axs[i].axvline(x = 334, linestyle='--', color='grey', label='break point')
    if f == '3':
        axs[i].axvline(x = 154, linestyle='--', color='grey', label='break point')
        axs[i].axvline(x = 222, linestyle='--', color='grey', label='break point')
        axs[i].axvline(x = 374, linestyle='--', color='grey', label='break point')
    if f == '5':
        axs[i].axvline(x = 202, linestyle='--', color='grey', label='break point')
        axs[i].axvline(x = 298, linestyle='--', color='grey', label='break point')
        axs[i].axvline(x = 366, linestyle='--', color='grey', label='break point')
    if f == '7':
        axs[i].axvline(x = 300, linestyle='--', color='grey', label='break point')
        axs[i].axvline(x = 368, linestyle='--', color='grey', label='break point')
        
    axs[i].legend()
plt.suptitle('AR(1) Time series - 30%prec reduction - Manaus', y=1.02)
plt.tight_layout()
plt.show()

print(df['timeindex'])