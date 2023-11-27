import joblib
import os
import matplotlib.pyplot as plt

# Get user input for the run name
run_name = input('run name: ')
# Get user input for the spin
spin = input('which spin?')


# Set the path to the data directory
path = '/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/{}/gridcell175-235'.format(run_name)

# Change the current working directory to the specified path
os.chdir(path)

# List the files and directories in the current path
contents = os.listdir()
for item in contents:
    print(item)



# Load data for the specified spin
with open("spin{}.pkz".format(spin), 'rb') as fh:
    dt = joblib.load(fh)
print(dt.keys())  # List the available keys for the outputs

# Specify the variables to be plotted
variables_to_plot = ['emaxm', 'tsoil', 'cleaf', 'cwood', 'croot', 'csap', 'cheart', 'csto', 'npp', 'photo', 'ar', 'ep', 'ev', 'lai', 'rm', 'rg', 'ls']

# Plot the specified variables in a 4x4 grid
fig, axs = plt.subplots(nrows=5, ncols=4, figsize=(20, 16))

for i, key in enumerate(variables_to_plot):
    values = dt[key]
    row = i // 4
    col = i % 4
    axs[row, col].plot(values)
    axs[row, col].set_title(key)
    axs[row, col].set_xlabel('Time')
    axs[row, col].set_ylabel(key)
    axs[row, col].grid(True)

# Adjust the layout to prevent title overlap
plt.tight_layout()

# Save the plot as a PNG file
plt.savefig('subplots_{}_{}.png'.format(run_name, spin))

# Display the subplots
plt.show()
