import pyqrcode as qrcode
import pickle as pk
import time
import os,glob

def generate_QR(data, pin):
    key = sk_to_data(data,pin)
    qr = qrcode.QRCode(version=1,box_size=10,border=4)
    qr.add_data(key)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    cleardata()
    qr = "qr"+str(time.time())+".png"
    img.save('static/'+qr)
    return qr

def cleardata():
    for filename in glob.glob("static/qr*"):
        os.remove(filename)


def sk_to_data(privatekey,pin):
    key = pk._dumps(privatekey)
    key = str(key)[2:-1]
    ls = [str(pin),key]
    data = '****'.join(element for element in ls)
    return data


if __name__ == '__main__':
    generate_QR('sdfvds','ghbjjcg')
