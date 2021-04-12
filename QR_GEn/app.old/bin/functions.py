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
from os.path import join as pjoin
import json


def keygen(dic, number, process):
    curr_lot = number
    dic[curr_lot] = process
    return 0

def add_plot(img, count, bat, offset):
    print(f"工序 = {count},  任务 = {bat}")
    plt.gcf().subplot(8, 11, int(count) + 2)
    plt.imshow(img)
    plt.axis('off')
    #plt.imshow(img)
    plt.title(str(bat)+","+str(count), fontsize = 'x-small')
    return 0
    
def qrgen(msg):
    qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_Q,
    box_size=50,
    border=4,
    )
    qr.add_data(msg)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img
    


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