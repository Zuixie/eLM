#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import os
from flask import Flask, request, url_for, render_template, jsonify, send_from_directory
from werkzeug import secure_filename
from importlib import import_module
import json

UPLOAD_FLOAD = './temp'
app = Flask(__name__)
app.config['UPLOAD_FLOAD'] = UPLOAD_FLOAD
app.secret_key = 'dasjkhldhskjdnkjsanj'
app.config['CONFIG_PATH'] = "./script/scriptconfig.json"
app.config['CONFIG_CONTENT'] = None 
app.config['CONFIG_CHANGE_TIME'] = None

# 获取配置文件,当网页载入的时候使用,通过判断配置的的更新时间判断是否需要重新载入
def get_script_config():
    config_change_time = os.path.getctime(app.config['CONFIG_PATH'])
    if config_change_time == app.config['CONFIG_CHANGE_TIME']:
        return
    app.config['CONFIG_CHANGE_TIME'] = config_change_time
    with open(app.config['CONFIG_PATH'], 'r') as f:
        print("loading config json file")
        app.config['CONFIG_CONTENT'] = json.load(f)


@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        pass
    get_script_config()
    scriptlist = app.config['CONFIG_CONTENT']['scriptlist']
    return render_template('index.html', scriptlist = scriptlist)

@app.route('/upload/', methods = ['GET','POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        scriptid = request.form['scriptid']
        # filename = secure_filename(file.filename)
        filename = file.filename
        # TODO confirm filename is exist 
        print('file name', filename, 'script:',scriptid )
        file.save(os.path.join(app.config['UPLOAD_FLOAD'], filename))
        
        detailjson = app.config["CONFIG_CONTENT"]
        return jsonify(uploadfilename = filename, 
            scriptname = scriptid, 
            detail = detailjson)

@app.route('/runscript/<scriptname>/', methods = ['GET', 'POST'])
def run_script(scriptname):
    if request.method == 'POST':
        print("start run script:" + scriptname)
        # uploadfilename = request.form['uploadfilename']
        
        uploadfilename = 'daily' # for test
        print(uploadfilename)

        print(request.form)

        # run python script with filename dynamic 
        scriptmd = import_module("script." + scriptname)
        outfile = scriptmd.run(uploadfilename, "./temp/")
        print ("down load fiel name :" + outfile)
        return jsonify(status = 200, msg = 'run success ' + uploadfilename, data = outfile)


@app.route('/download/<filename>/', methods = ['GET', 'POST'])
def download_file(filename):
    print ("start download " + filename)
    return send_from_directory(app.config['UPLOAD_FLOAD'], filename)

if __name__ == '__main__':
    app.debug = True
    app.run()
