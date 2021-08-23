#!/usr/bin/env python
# coding=utf-8

def func():
    try:
        from zipfile import ZipFile

        with ZipFile("./sample/text.zip") as f:
            print(f.filelist)
    except ImportError:
        print('')
    except:
        print('')
