import subprocess
import numpy as np
import os
import time


def change_txt(file,init, m,r=None,s=None):
        with open(os.path.join(dir_path, file), 'r') as template_file:
            template = template_file.read()
        if r is None and s is None:
            if '_{0}d{1}_'.format(int(init), int((init-int(init))*10)) in template:
               modified_template = template.replace('{0}d{1}'.format(int(init), int((init-int(init))*10)),
                                                    '{0}d{1}'.format(int(m), int((m-int(m))*10))) 
               print('{0}d{1} replaced by {2}d{3}'.format(int(init), int((init-int(init))*10), int(m), int((m-int(m))*10)))
            elif '{0}d0'.format(init) in template:
               modified_template = template.replace('{0}d0'.format(init),
                                                    '{0}d0'.format(m)) 
               print('{0}d0 replaced by {1}d0'.format(init, m))
            else:
               print('{0}d{1} not found !!!'.format(int(init), int((init-int(init))*10)))
        elif s is not None and r is not None:
            if '{0}d{1}_{2}d{3}_{4}d{5}'.format(int(init[0]), int((init[0]-int(init[0]))*10), int(init[1]), int((init[1]-int(init[1]))*10), int(init[2]), int((init[2]-int(init[2]))*10)) in template:
               modified_template = template.replace('{0}d{1}_{2}d{3}_{4}d{5}'.format(int(init[0]), int((init[0]-int(init[0]))*10), int(init[1]), int((init[1]-int(init[1]))*10),  int(init[2]), int((init[2]-int(init[2]))*10)),
                                                    '{0}d{1}_{2}d{3}_{4}d{5}'.format(int(m), int((m-int(m))*10),int(r),int((r-int(r))*10),int(s),int((s-int(s))*10))) 
               print('{0}d{1}_{2}d{3}_{4}d{5} replaced by {6}d{7}_{8}d{9}_{10}d{11}'.format(int(init[0]), int((init[0]-int(init[0]))*10), int(init[1]), int((init[1]-int(init[1]))*10), int(init[2]), int((init[2]-int(init[2]))*10),
                                                                                            int(m), int((m-int(m))*10),int(r),int((r-int(r))*10),int(s),int((s-int(s))*10)))  
            else:
               print('{0}d{1}_{2}d{3}_{4}d{5} not found !!!'.format(int(init[0]), int((init[0]-int(init[0]))*10), int(init[1]), int((init[1]-int(init[1]))*10), int(init[2]), int((init[2]-int(init[2]))*10)))
        else:
            print('check your inlist files')
        with open(os.path.join(dir_path, file), 'w') as modified_file:
           modified_file.write(modified_template)

dir_path = '/home/maxwav/Software/MESA/mesa-r11554/star/test_suite/KLENCKI_models/NGC45_Nadia/'

initial_mass = [k for k in np.arange(21, 22, 0.5)]
initial_ratio = [k for k in np.arange(3.7, 4.1, 0.15)]
bin_sep = [k for k in np.arange(1100, 1250, 100)]
combinations = [(i, np.round(i/j,2), k) for i in initial_mass for j in initial_ratio for k in bin_sep]

print(combinations)
init = [18,4,400]
init1 = 18
init2 = 4
init3 = 400
count=1
dir_path = '/home/maxwav/Software/MESA/mesa-r11554/star/test_suite/KLENCKI_models/NGC45_Nadia/'

for m,r,s in combinations:
        print(m,r,s)
        
        change_txt('star_job_extra', init1, m, None, None)
        # change_txt('star_job_extra', init, m, r, s)
        change_txt('inlist1', init, m, r, s)
        change_txt('inlist_extra_binary', init2, r, None, None)
        change_txt('inlist_extra_binary', init3, s, None, None)
        init = [m,r,s]
        init1 = m
        init2 = r
        init3 = s

        subprocess.run(['cd', dir_path], shell=True, check=True)
        subprocess.run(['pwd'], shell=True, check=True)
        print("we are located in {0}".format(dir_path))
    
        print("Environment:",os.environ.get('MESA_DIR'), "\n",os.environ.get('MESASDK_ROOT'))
    
        # Run clean and mk executables
        print(os.chdir(dir_path))
        print(" \n ****************************** \n **Software/MESA/mesa-r11554/star/** \n ****************************** \n \n \n  /!\ /!\ /!\ Run {0}/{1} with mass_donor={2} mass_accretor={3} bin_sep={4}  /!\ /!\ /!\ \n \n \n ****************************** \n ****************************** \n ".format(count, len(combinations),m,r,s))
        print(" Time: {0}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        print("start cleaning, making and running")
        process = subprocess.run(['./clean; ./mk; ./rn', dir_path], stdout=subprocess.PIPE, text=True, shell=True, check=True)
        print("clean, make and run done")
        output = process.stdout.splitlines()
        for line in output[:10]:
            print(line)
        count+=1
    
subprocess.Popen('Jakub', shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)