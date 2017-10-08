#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify, send_file
import base64
import json
import os
import keras
from keras.models import load_model
from PIL import Image
app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route('/')
@app.route('/image', methods=['GET', 'POST'])
def imageFunction():
    if request.method == 'GET':
        return ''
    elif request.method == 'POST':
        target = os.path.join(APP_ROOT, 'images/')
        if not os.path.isdir(target):
            os.mkdir(target)

        data=request.data
        # print(data)
        newFile=data[10:]
        newFile= newFile.replace('%2F','/')
        newFile = newFile.replace('%0A','')
        newFile = newFile.replace('%2B','+')
        newFile = newFile.replace('%3D&','=')
        # print(newFile)

        imgdata = base64.b64decode(newFile)

        filename = '/home/Aaditya21396/mysite/images/some_image.jpg'
        with open(filename, 'wb') as f:
            f.write(imgdata)

        img = Image.open('bookpage.jpg')
        img = img.convert('1')
        resized = im.resize((64, 64), Image.ANTIALIAS)

        resized = np.asarray(resized)
        resized = resized/255

        model = load_data('/home/Aaditya21396/mysite/models/model-digits.h5')
        pred = model.predict(resized)
        print('true value' + pred)
        print "Got Image"
        return "Success"

if __name__ == '__main__':
    app.debug = False

