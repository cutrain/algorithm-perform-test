import os
import sys
__module_path='../visual-analysis-platform'
sys.path.append(__module_path)

from algorithm.image.image_monorec import *
from algorithm.image.image_process import *
from test_tool import Timer

size_list = ['1tb']

def test_monorec():
    for size in size_list:
        kwargs = {
            'class_':'people,car',
        }
        result_file = 'report/test_image_monorec_{}.txt'.format(size)
        if os.path.exists(result_file):
            print('skip {}'.format(result_file))
            continue
        import cv2
        data_in = [[cv2.imread('data/1.png')], ['1.png']]
        filesize = 2690941
        totalsize = 1024*1024*1024*1024 #gb*mb*kb*b
        multip = totalsize // filesize
        timer = Timer()
        print('running {}'.format(result_file))
        image_monorec(data_in, **kwargs)
        while timer.count < 20:
            timer(image_monorec, data_in, **kwargs)
        cost = timer.avg_cost * multip
        with open(result_file, 'w') as f:
            f.write('total,each,number\n')
            f.write(str(cost)+","+str(timer.avg_cost)+","+str(multip))

def test_resolution():
    for size in size_list:
        kwargs = {
            'width':"960",
            "height":"540",
        }
        result_file = 'report/test_image_resolution_{}.txt'.format(size)
        if os.path.exists(result_file):
            print('skip {}'.format(result_file))
            continue
        import cv2
        data_in = [[cv2.imread('data/1.png')], ['1.png']]
        filesize = 2690941
        totalsize = 1024*1024*1024*1024 #gb*mb*kb*b
        multip = totalsize // filesize
        timer = Timer()
        print('running {}'.format(result_file))
        while timer.count < 20 or timer.total_cost < 2:
            timer(image_resolution, data_in, **kwargs)
        cost = timer.avg_cost * multip
        with open(result_file, 'w') as f:
            f.write('total,each,number\n')
            f.write(str(cost)+","+str(timer.avg_cost)+","+str(multip))

def test_channel():
    for size in size_list:
        kwargs = {
            'method':'BGR2GRAY',
        }
        result_file = 'report/test_image_channel_{}.txt'.format(size)
        if os.path.exists(result_file):
            print('skip {}'.format(result_file))
            continue
        import cv2
        data_in = [[cv2.imread('data/1.png')], ['1.png']]
        filesize = 2690941
        totalsize = 1024*1024*1024*1024 #gb*mb*kb*b
        multip = totalsize // filesize
        timer = Timer()
        print('running {}'.format(result_file))
        while timer.count < 20 or timer.total_cost < 2:
            timer(image_channel, data_in, **kwargs)
        cost = timer.avg_cost * multip
        with open(result_file, 'w') as f:
            f.write('total,each,number\n')
            f.write(str(cost)+","+str(timer.avg_cost)+","+str(multip))

def test_small():
    for size in size_list:
        kwargs = {
        }
        result_file = 'report/test_image_small_{}.txt'.format(size)
        if os.path.exists(result_file):
            print('skip {}'.format(result_file))
            continue
        import cv2
        data_in = [[cv2.imread('data/1.png')], ['1.png']]
        filesize = 2690941
        totalsize = 1024*1024*1024*1024 #gb*mb*kb*b
        multip = totalsize // filesize
        timer = Timer()
        print('running {}'.format(result_file))
        while timer.count < 20 or timer.total_cost < 2:
            timer(image_small, data_in, **kwargs)
        cost = timer.avg_cost * multip
        with open(result_file, 'w') as f:
            f.write('total,each,number\n')
            f.write(str(cost)+","+str(timer.avg_cost)+","+str(multip))

def test_cut():
    for size in size_list:
        kwargs = {
            'left':"0",
            'width':'960',
            'top':'0',
            'height':'540',
        }
        result_file = 'report/test_image_cut_{}.txt'.format(size)
        if os.path.exists(result_file):
            print('skip {}'.format(result_file))
            continue
        import cv2
        data_in = [[cv2.imread('data/1.png')], ['1.png']]
        filesize = 2690941
        totalsize = 1024*1024*1024*1024 #gb*mb*kb*b
        multip = totalsize // filesize
        timer = Timer()
        print('running {}'.format(result_file))
        while timer.count < 20 or timer.total_cost < 2:
            timer(image_cut, data_in, **kwargs)
        cost = timer.avg_cost * multip
        with open(result_file, 'w') as f:
            f.write('total,each,number\n')
            f.write(str(cost)+","+str(timer.avg_cost)+","+str(multip))

def test_blur():
    for size in size_list:
        kwargs = {
            'method':'gaussian',
            'kernel_size':'3,3',
        }
        result_file = 'report/test_image_blur_{}.txt'.format(size)
        if os.path.exists(result_file):
            print('skip {}'.format(result_file))
            continue
        import cv2
        data_in = [[cv2.imread('data/1.png')], ['1.png']]
        filesize = 2690941
        totalsize = 1024*1024*1024*1024 #gb*mb*kb*b
        multip = totalsize // filesize
        timer = Timer()
        print('running {}'.format(result_file))
        while timer.count < 20 or timer.total_cost < 2:
            timer(image_blur, data_in, **kwargs)
        cost = timer.avg_cost * multip
        with open(result_file, 'w') as f:
            f.write('total,each,number\n')
            f.write(str(cost)+","+str(timer.avg_cost)+","+str(multip))

def test_dilate():
    for size in size_list:
        kwargs = {
            'kernel_size':'3,3',
            'iterations':1,
        }
        result_file = 'report/test_image_dilate_{}.txt'.format(size)
        if os.path.exists(result_file):
            print('skip {}'.format(result_file))
            continue
        import cv2
        data_in = [[cv2.imread('data/1.png')], ['1.png']]
        filesize = 2690941
        totalsize = 1024*1024*1024*1024 #gb*mb*kb*b
        multip = totalsize // filesize
        timer = Timer()
        print('running {}'.format(result_file))
        while timer.count < 20 or timer.total_cost < 2:
            timer(image_dilate, data_in, **kwargs)
        cost = timer.avg_cost * multip
        with open(result_file, 'w') as f:
            f.write('total,each,number\n')
            f.write(str(cost)+","+str(timer.avg_cost)+","+str(multip))

def test_close():
    for size in size_list:
        kwargs = {
            'kernel_size':'3,3',
        }
        result_file = 'report/test_image_close_{}.txt'.format(size)
        if os.path.exists(result_file):
            print('skip {}'.format(result_file))
            continue
        import cv2
        data_in = [[cv2.imread('data/1.png')], ['1.png']]
        filesize = 2690941
        totalsize = 1024*1024*1024*1024 #gb*mb*kb*b
        multip = totalsize // filesize
        timer = Timer()
        print('running {}'.format(result_file))
        while timer.count < 20 or timer.total_cost < 2:
            timer(image_close, data_in, **kwargs)
        cost = timer.avg_cost * multip
        with open(result_file, 'w') as f:
            f.write('total,each,number\n')
            f.write(str(cost)+","+str(timer.avg_cost)+","+str(multip))

def test_brightness_contrast():
    for size in size_list:
        kwargs = {
            'brightness_shift':10,
            'contrast_shift':1.2,
        }
        result_file = 'report/test_image_brightness_contrast_{}.txt'.format(size)
        if os.path.exists(result_file):
            print('skip {}'.format(result_file))
            continue
        import cv2
        data_in = [[cv2.imread('data/1.png')], ['1.png']]
        filesize = 2690941
        totalsize = 1024*1024*1024*1024 #gb*mb*kb*b
        multip = totalsize // filesize
        timer = Timer()
        print('running {}'.format(result_file))
        while timer.count < 20 or timer.total_cost < 2:
            timer(image_brightness_contrast, data_in, **kwargs)
        cost = timer.avg_cost * multip
        with open(result_file, 'w') as f:
            f.write('total,each,number\n')
            f.write(str(cost)+","+str(timer.avg_cost)+","+str(multip))

