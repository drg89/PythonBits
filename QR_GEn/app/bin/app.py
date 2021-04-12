#  -*-  coding:utf-8  -*-
"""
Created on Tue Jul  2 21:15:35 2019

@author: JACKEY
"""
import sys
import f2
import numpy as np
import json
from datetime import date
import os
print("按 CTRL+C 或直接关闭窗口退出\n")
def main():
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
        input_string=input("输入工序名，用空格键分开，输入完按回车键： ")
        process = input_string.replace(" "," ").split()
        f2.keygen(dic, order, process)
        f2.write_log(dic, file_name)
        for i in dic[order]:
            f2.qrgen(order, f"{dic[order].index(i)}_{i}")
    return main()

if __name__ == "__main__":
    main()
    
    
    
    
    
    