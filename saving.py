import os
import shutil

downloads_dir = os.path.expanduser('~/Downloads')  
desktop_dir = os.path.expanduser('~/Desktop')  

praat_dir = os.path.join(desktop_dir, 'praat')
if not os.path.exists(praat_dir):
    os.makedirs(praat_dir)

roll_numbers = range(155, 232)

for filename in os.listdir(downloads_dir):
    for roll_number in roll_numbers:
        if filename.startswith(str(roll_number)):
            roll_dir = os.path.join(praat_dir, str(roll_number))
            if not os.path.exists(roll_dir):
                os.makedirs(roll_dir)
            src_path = os.path.join(downloads_dir, filename)
            dst_path = os.path.join(roll_dir, filename)
            shutil.move(src_path, dst_path)
            print(f"Moved {filename} to {roll_dir}")
            break 
