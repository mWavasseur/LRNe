# INTRODUCTION

This jupyter notebook automates the process of modifying input parameters for the MESA (Modules for Experiments in Stellar Astrophysics) code and running the corresponding models. We are using a loop where first the 
new parameters are implemented, by modifing their value in the "inlist files" and then, the routine opens a terminal and initiates the MESA run. Once this is completed, in a new iteration the input values are replaced 
again and MESA executed in the same terminal than before, etc...

# Requirements: 
MESA, version: mesa-r11.55.4 or mesa-r23.05.1

Python, version: 3.11.4

Python packages: (subprocess, numpy, os)

# Usage
## Setting Up Input Files

In the code, select the range of parameters you want to test (initial_mass, initial_ratio and bin_sep) :

    initial_mass = [k for k in np.arange(21.5, 23.5, 0.5)]
    initial_ratio = [np.round(k,2) for k in np.arange(3.2, 3.8, 0.2)]
    bin_sep = [k for k in np.arange(1100, 1200, 100)]

Pay attention that in your inlist files, the initial values must be similar to those that are stored in the following variables:

    init = [18,4,400]# the global array of target initial parameters
    init1 = 18 # related to initial_mass
    init2 = 4 # related to initial_ratio
    init3 = 400 # related to binary separation

The function change_txt(file,init, m,r=None,s=None) takes in argument the following:
  - file (string): the file that must be modified, 
  - init (float array): the values initially displayed in the file
  - m,r and s (int): variables that control which string sequence we want to replace
    
This function allows to modify both parameters values and directory paths for storing the MESA outputs. More precisely the variables for each inlist file are the following: 
   - inlist1: LOGS, png, save_model_filename
   - star_job_extra: m2, initial_separation_in_Rsuns
   - inlist_extra_binary: saved_model_name
    
The function also displays some message confirming the modification of the desired values or indicating that the strings have not been founded within the file.

Inside the loop, we need to compute the accretor mass (ac_m) from the initial_mass and initial_ratio because MESA requires this information rather than the mass ratio for the binary system.

    ac_m = np.round(d_m/rat,3)

MESA is called and executed in a terminal with the following command:

    process = subprocess.run(['./clean; ./mk; ./rn', dir_path], stdout=subprocess.PIPE, text=True, shell=True, check=True)
    output = process.stdout.splitlines()
    for line in output[:10]:
    print(line)

Here, we just print the 10 first lines of the run to ensure that the code is executing correctly and avoiding to saturate the display capacity of the jupyter notebook as the run generate a large quantity of information.

## Run

To run the routine, just execute the jupyter notebook.
