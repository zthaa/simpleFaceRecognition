#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

path = r"D:\starlib"

list_dir = os.listdir(path)
for i in list_dir:
    filepath = os.path.join(path, i)
    newname = os.path.join(path, "fuck"+str(list_dir.index(i)))
    os.renames(filepath, newname)
print("alldone")
 