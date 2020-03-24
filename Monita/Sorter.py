#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 13:47:59 2019
Simple word document sorter
@author: sr802
"""
import textract

text = textract.process("read.docx")

splitted=text.split('\n\n\n')

splitted.sort()


f=open("1.sorted",'w')
for line in splitted:
    f.write(line)
    f.write('\n\n\n')

f.close()



text = textract.process("read2.docx")

splitted=text.split('\n\n\n')

splitted.sort()


f=open("2.sorted",'w')
for line in splitted:
    f.write(line)
    f.write('\n\n\n')

f.close()