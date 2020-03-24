#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May 19 23:47:06 2018
Learining multiprocessing pythons
@author: simon
"""
from multiprocessing import Process


print multiprocessing.cpu_count()
import os


def info(title):
    print title
    print 'module name:', __name__
    if hasattr(os, 'getppid'):  # only available on Unix
        print 'parent process:', os.getppid()
    print 'process id:', os.getpid()

def f(name):
    info('function f')
    print 'hello', name

if __name__ == '__main__':
    info('main line')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()