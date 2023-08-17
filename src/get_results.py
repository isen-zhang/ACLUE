#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from categories import zh2en,taskno
from utils import get_results
import os
if __name__ == "__main__":
    result_dirs = os.listdir("../results")
    subjects = list(zh2en.keys())
    print("0 shot")
    for result_dir in result_dirs:
        if result_dir[0]!='.':
            if result_dir.split('_')[1] == '0':
                print(f"|[{result_dir.split('_')[0]}]")
                r=get_results(subjects,"../results/" + result_dir)
    print("5 shot")
    for result_dir in result_dirs:
        if result_dir[0]!='.':
            if result_dir.split('_')[1] == "5":
                print(f"|[{result_dir.split('_')[0]}]")
                r=get_results(subjects,"../results/" + result_dir)
