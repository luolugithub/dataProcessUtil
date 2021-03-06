# -*- coding: utf-8 -*-
# @Time    : 12/3/19 6:54 PM
# @Author  : luolu
# @Email   : argluolu@gmail.com
# @File    : jpg2png.py
# @Software: PyCharm

import os
import sys
import platform
from PIL import Image as img

sysname = platform.system()
inpath = '/home/xkjs/PycharmProjects/pre_process/image/'
outpath = '/home/xkjs/PycharmProjects/pre_process/image/'

if sysname == 'Windows':

    os.system('cls')

elif sysname == 'Linux':

    os.system('clear')

else:

    print('Unsupported OS.')
    input('Press Enter to exit: ')
    sys.exit()

for i in os.listdir(inpath):
    print('[INFO] Saving ' + i + ' as PNG...')
    raw = img.open(inpath + i)
    raw.save(outpath + i[:-3] + 'png')

for i in os.listdir(outpath):
    print('[INFO] Converting ' + i + ' to RGBA...')
    pic = img.open(outpath + i).convert('RGBA')
    pic.save(outpath + i)