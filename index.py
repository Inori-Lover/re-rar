#!/usr/bin/env python
# coding=utf-8

from zipfile import ZipFile
with ZipFile("./sample/text.zip") as f:
    print(f.filelist)
