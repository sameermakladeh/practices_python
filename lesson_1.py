'''

#open a video on Youtube 3 times every 10 seconds

import webbrowser
import time

total_break=3
break_count=1

print ('this program started at:'+time.ctime())
while break_count<=total_break:
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=daQJiRyZc8k")
    break_count=break_count+1

'''

'''
#change name files

import os
import string

def rename_files():
# 1. get files names from a folder
    files_list = os.listdir(r"C:\Users\Sameer\Desktop\prank")
    #print (files_list)
    saved_path=os.getcwd()
    print ("current working directory is:"+saved_path)
    os.chdir(r"C:\Users\Sameer\Desktop\prank")
# 2. for each file, rename file name
    for file_name in files_list:
        translation_table = string.maketrans("0123456789","          ")
        os.rename(file_name,file_name.translate(translation_table))

rename_files()

'''

# make a movie program!!

def show_trailer():
    # open a browser and play trailer

def show_info():
    # print movie information



