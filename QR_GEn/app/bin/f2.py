#  -*-  coding:utf-8  -*-
"""
Spyder Editor

This contains functions needed to run the app
"""
#global var DIC
#text generation
#qr generation from text, store generated vals in JSON
#tesselate for printing on A4 sheet
#gui

#counter app for every worker ID
import matplotlib.pyplot as plt
import qrcode
import os
from os.path import join as pjoin
import json
from pathlib import Path


def keygen(dic, number, process):
    curr_lot = number
    dic[curr_lot] = process
    return 0
    
def qrgen(order, process):
    qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_Q,
    box_size=50,
    border=4,
    )
    filename = f"{(Path(__file__).absolute().parent)}\\QRCODE\\{order}\\{process}.png"
    dirname = os.path.dirname(filename)
    if not os.path.exists(dirname):
        os.makedirs(dirname)
#    with open(f"{(Path(__file__).absolute().parent)}\\QRCODE\\{order}\\{process}.png", 'w') as fp:
    qr.add_data(process)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
#        fp.write(img)
#        fp.close()
    return 0
    


def write_log(dic, file_name):
    name_emb = dic
    fr = open(pjoin(file_name)) 
    model=json.load(fr)
    fr.close()
    
    for i in name_emb:
        model[i] = name_emb[i]
 
    jsObj = json.dumps(model)    
 
    with open(file_name, "w") as fw:  
        fw.write(jsObj)  
        fw.close()
    return 0
    print("logged: ",jsObj)
        
if __name__ == '__main__':
    print("请运行app.py")