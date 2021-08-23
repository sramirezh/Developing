#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 13:47:59 2019
Simple word document sorter
@author: sr802
"""
import textract
import re
import unidecode
import pandas as pd
import numpy as np


text = textract.process("read.docx")

splitted=text.split('\n\n\n')


def string_filtering(string):
    """
    Organises all the strings removing all the additional character
    """

    words = str.split(string)
    palabras=[]
    for word in words:
        word=word.decode('utf8')#To convert in unicode
        word=word.lower()
        
        word=unidecode.unidecode(word)
        
        word=re.sub('[^A-Za-z0-9]+', '', word) #Remove all the special characters
        
        palabras.append(word)
    
    palabras.sort()
    return palabras

pal=string_filtering(text)



def word_count(words):
    counts = dict()
    for word in words: 
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
            
    return counts

def dict_to_array(dictionary):
    dictlist=[]
    for key, value in dictionary.iteritems():
        temp = [key,value]
        dictlist.append(temp)
    array=np.array(dictlist)
    return array
    

dictionary=word_count(pal)

matrix=dict_to_array(dictionary)

matrix_sorted=matrix[np.array(matrix[:,1],dtype=float).argsort()]

#splitted.sort()
#
#
#f=open("1.sorted",'w')
#for line in splitted:
#    f.write(line)
#    f.write('\n\n\n')
#
#f.close()
#
#
#
#text = textract.process("read2.docx")
#
#splitted=text.split('\n\n\n')
#
#splitted.sort()
#
#
#f=open("2.sorted",'w')
#for line in splitted:
#    f.write(line)
#    f.write('\n\n\n')
#
#f.close()