#  -*-  coding:utf-8  -*-
"""
Created on Tue Jul  2 21:15:35 2019

@author: JACKEY
"""
import sys
import functions
import matplotlib.pyplot as plt
import numpy as np
import json
from datetime import date
import os
print("按 CTRL+C 或直接关闭窗口退出\n")
def main():
    fig, ax = plt.subplots(6, 6, sharex=True, sharey=True, figsize=(11.69, 16.54))
    fig.tight_layout()
    [axi.set_axis_off() for axi in ax.ravel()]
    fig.subplots_adjust(hspace=2, wspace=2)
    j = k = 0
    file_name = f"{date.today().isoformat()}.json"
    path = "log/"
    if '''bin\log''' not in os.getcwd():
        os.chdir(path)
    if file_name not in os.listdir():
        fp = open(file_name, 'w')
        fp.write("{}")
        fp.close()
        
    with open(file_name) as log:
            dic = json.load(log)
    
    print("今日发出任务数: ",len(list(dic.keys())))
    log.close()
    order = input("输入order number: ")
    if order == 'exit()' or order == 'Exit()':
        sys.exit()
    if (order in dic.keys() ):
        print(f"{order} 任务工序如下：{dic[order]}")
        return main()
    else:    
        #plt.title("B"+str(batch))
        input_string=input("输入工序名，用空格键分开，输入完按回车键： ")
        process = input_string.replace(" "," ").split()
        functions.keygen(dic, order, process)
        functions.write_log(dic, file_name)
        for i in dic[order]:
            plt.rcParams["figure.figsize"] = (2,2)
            img = functions.qrgen(f"单号: {order}，工序: {i}")
            plt.sca(ax[j, k])          # set the current axes instance
            ax[j, k].imshow(img)
            ax[j, k].axis('off')
            k+=1
            if k >= 6:
                j += 1
                k = 0
    plt.savefig(f"{order}.png", dpi = 300, orientation='portrait', format='png')
    return main()

if __name__ == "__main__":
    main()
    
    
    
    
    
    