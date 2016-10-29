#!/usr/bin/env python
#                      
# -*- coding: utf-8 -*-
# wu.wu@hisilicon.com 
# 2015-03-26 14:28:18

import re
import string
import pdb

def peripheral_parser(content, outfp, flag):
    score = -1

    string = flag + ' test succeed'
    if re.search(string, content):
        score = 1
    else:
        score = 0
    outfp.write('%s:  \n%s\n' % (flag, string))
    return score

def basic_parser(content, outfp):
    score = -1

    if re.search('test succeed', content):
        flag = 1
    else:
        flag = 0
    outfp.write('Test:  \n%s\n' % content)
    #print flag
    return flag

def sata_parser(content, outp):
    dic_sata = {}
    if re.search("SATA test succeed", content):
        dic_sata["status"] = 1
    else:
        dic_sata["status"] = 0

        dic_sata["UUID"]={}
        for item in re.findall("the sata disk (.*?)\sworks\spass", content):
            dic_sata["UUID"][item] = 1
        for item in re.findall("the sata disk (.*?)\sworks\spass", content):
            dic_sata["UUID"][item] = 0
    return dic_sata

def d05_PCIE_parser(content, outfp):
    dic_pcie = {}
    dic_pcie["link"] = {}
    if re.findall("pcie1\slink\sstatus.*succeed\n", content):
        dic_pcie["link"]["pcie1"] = 1
    else:
        dic_pcie["link"]["pcie1"] = 0

    #if re.findall("pcie2\slink\sstatus.*succeed\n", content):
    #    dic_pcie["link"]["pcie2"] = 1
    #else:
    #    dic_pcie["link"]["pcie2"] = 0

    dic_pcie["speed"]={}
    if re.findall("\sPCIE\sconnection.*succeed\n", content):
        dic_pcie["speed"]["status"]=1
    else:
        dic_pcie["speed"]["status"]=0
        
        for item in re.findall("iperf.*pcie\s(.*?)\s.*transfer", content):
            dic_pcie["speed"][item] = 0
        for item in re.findall("ping.*pcie\s(.*?)\s.*", content):
            dic_pcie["speed"][item] = 0
        for item in re.findall("iper.*pcie\s(.*?)\s.*transfer.*succeed", content):
            dic_pcie["speed"][item] = 1

    return dic_pcie

def d05_GE_parser(content, outfp):
    dic_GE={}
    dic_GE["speed"]={}
    if re.findall("MAC\sconfiguration.*succeed", content):
        dic_GE["MAC"] = 1
    else:
        dic_GE["MAC"] = 0

    dic_GE["speed"]["GE"]={}
    if re.findall("\sGE\sconnection.*succeed\n", content):
        dic_GE["speed"]["GE"]["status"]=1
    else:
        dic_GE["speed"]["GE"]["status"]=0
        for item in re.findall("iperf.*\sGE\s(.*?)\s.*transfer", content):
            dic_GE["speed"]["GE"][item] = 0
        for item in re.findall("ping.*\sGE\s(.*?)\s.*", content):
            dic_GE["speed"]["GE"][item] = 0
        for item in re.findall("iperf.*\sGE\s(.*?)\s.*transfer.*succeed", content):
            dic_GE["speed"]["GE"][item] = 1

    dic_GE["speed"]["XGE"]={}
    if re.findall("\sXGE\sconnection.*succeed\n", content):
        dic_GE["speed"]["XGE"]["status"]=1
    else:
        dic_GE["speed"]["XGE"]["status"]=0
        for item in re.findall("iperf.*\sXGE\s(.*?)\s.*transfer", content):
            dic_GE["speed"]["XGE"][item] = 0
        for item in re.findall("ping.*\sXGE\s(.*?)\s.*", content):
            dic_GE["speed"]["XGE"][item] = 0
        for item in re.findall("iperf.*\sXGE\s(.*?)\s.*transfer.*succeed", content):
            dic_GE["speed"]["XGE"][item] = 1

    dic_GE["speed"]["NON_XGE"]={}
    if re.findall("NON_XGE\sconnection.*succeed\n", content):
        dic_GE["speed"]["NON_XGE"]["status"]=1
    else:
        dic_GE["speed"]["NON_XGE"]["status"]=0
        for item in re.findall("iperf.*\sNON_XGE\s(.*?)\s.*transfer", content):
            dic_GE["speed"]["NON_XGE"][item] = 0
        for item in re.findall("ping.*\sNON_XGE\s(.*?)\s.*", content):
            dic_GE["speed"]["NON_XGE"][item] = 0
        for item in re.findall("iperf.*\sNON_XGE\s(.*?)\s.*transfer.*succeed", content):
            dic_GE["speed"]["NON_XGE"][item] = 1

    dic_GE["speed"]["RISER"]={}
    if re.findall("RISER\sconnection.*succeed\n", content):
        dic_GE["speed"]["RISER"]["status"]=1
    else:
        dic_GE["speed"]["RISER"]["status"]=0
        for item in re.findall("iperf.*\sRISER\s(.*?)\s.*transfer", content):
            dic_GE["speed"]["RISER"][item] = 0
        for item in re.findall("ping.*\sRISER\s(.*?)\s.*", content):
            dic_GE["speed"]["RISER"][item] = 0
        for item in re.findall("iperf.*\sRISER\s(.*?)\s.*transfer.*succeed", content):
            dic_GE["speed"]["RISER"][item] = 1

    return dic_GE

def memtester_parser(content, outfp):
    flag = -1

    if re.search('memory test succeed', content):
        flag = 1
    else:
        flag = 0

    outfp.write('memtester:  %s\n' % flag)
    return flag

def rtc_test_parser(content, outfp):
    score = -1
    score = peripheral_parser(content, outfp, 'rtc')
    return  score

if __name__=="__main__":
    infp = open("1.txt", "r")
    outfp = open("2.txt", "a+")
    contents = infp.read()
    for content in re.findall("%%%\s*test_start\s*\n(.*?)\n%%%\s*test_end", contents, re.DOTALL):
        basic_parser(content, outfp)

    outfp.close()
    infp.close()


