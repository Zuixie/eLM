#! /usr/bin/env python3
# -*- coding:utf-8 -*-
import openpyxl

# TODO 参数使用键值对传递
# 未来上传的路径和输出的路径要通过类进行设置
def run(filename, outpath='../temp/'):
    print ("script start run", filename)
    # TODO judje filename is endswith .xlsx
    fnlist = filename.split('.')
    outfilename = None
    if len(fnlist) > 1:
        fnlist[-2] = fnlist[-2] + '-out'
        outfilename = '.'.join(fnlist)
    else:
        outfilename = filename + "-out"
    text = "this is good things + " + filename
    with open(outpath + outfilename, 'w') as f:
        f.write(text)
    return outfilename

def utils_create_outfilenmae(filename):
    if filename.find('\\') > filename.find('/'):
        filename = filename.split('\\')[-1];        
    else:
        filename = filename.split('/')[-1];
    fnlist = filename.split('.')
    outfilename = None
    if len(fnlist) > 1:
        fnlist[-2] = fnlist[-2] + '-out'
        outfilename = '.'.join(fnlist)
    else:
        outfilename = filename + "-out"
    return outfilename
    

def run_main(args_dict):
    if not isinstance(args_dict, dict):
        raise Exception('run_main args type must be args')
    print ("srcipt run :", args_dict)
    input_filename = args_dict['inputfilename']
    output_path = args_dict['outputpath']
    # other args
    out_filename = utils_create_outfilenmae(input_filename)
    with open(input_filename,'r') as fin, open(output_path + out_filename, 'w') as fout:
        fout.write(fin.read())
    return out_filename


if __name__ == "__main__":
    # rets = run('test-file.xls')
    rets = run_main({'inputfilename':'../test.py','outputpath':''})
    print (rets)
