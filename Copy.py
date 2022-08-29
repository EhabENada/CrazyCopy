import shutil
import progressbar
import time
from tkinter import Tk, filedialog
import glob
import os
import tqdm
import readchar
def animated_marker():
    widgets = ['Please Wait while starting program :) : ', progressbar.AnimatedMarker()]
    bar = progressbar.ProgressBar(widgets=widgets).start()
    for i in range(20):
        time.sleep(0.1)
        bar.update(i)

print('')

print('''
                                            Welcome to Crazy Copy V 1.0
                                            Copyright (c) \x1b[6;30;42mEhab Nada\x1b[0m 2022
''')


root = Tk()
root.withdraw()
root.attributes('-topmost', True)

animated_marker()


copy_from = filedialog.askdirectory()
copy_to = filedialog.askdirectory()
sap_num = filedialog.askopenfilename()
dir_count = 0
with open(sap_num, "r") as file:
    for sap_count in file:
        dir_count += 1

progress_bar = tqdm.tqdm(range(dir_count),  colour="YELLOW", desc='Please Wait while the program Copying Folders')


with open(sap_num , "r") as file:
    
    for i, sap in zip(progress_bar,file):
        sap = sap.strip()
        src_file = os.path.join(copy_from, sap)
        dst_file = os.path.join(copy_to, sap)
        try:
            if os.path.exists(dst_file):
                pass
            else:
                shutil.copytree(src_file, dst_file)
        except:
            pass
        
file.close()


print("Press Any Key To Exit")
readchar.readchar()
