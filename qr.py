# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 11:19:27 2021

@author: asus
"""
import qrcode
import matplotlib.pyplot as plt
from PIL import Image


def build_qr():
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)#設定qrcode參數
    qr.add_data('Image Test')
    qr.make(fit=True)
    img = qr.make_image()
    img = img.convert('RGBA')
    img = qr.make_image(fill_color="blue", back_color="yellow")
    #設定qrcode顏色
    
    icon = Image.open('01.png')
    img_w, img_h = img.size
    factor = 4
    size_w = int(img_w/factor)
    size_h = int(img_h/factor)
    
    icon_w, icon_h = icon.size
    if icon_w > size_w:
        icon_w = size_w
        
    if icon_h > size_h:
        icon_h = size_h
    
    icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)
    
    w = int((img_w - icon_w)/ -20)
    h = int((img_h - icon_h)/ -20)
    icon = icon.convert('RGBA')
    img.paste(icon, (w,h), icon)
    img.save("logoQR.png")
    #設定圖片qrcode

def show_image():
    img=Image.open('logoQR.png')
    plt.figure("a")
    plt.imshow(img)
    plt.show()
    

  
    
if __name__ == '__main__':
    build_qr()
    show_image()


