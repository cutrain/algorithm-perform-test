import os
import sys
__module_path='../visual-analysis-platform'
sys.path.append(__module_path)

from algorithm.dataframe.process import *
from maker import LabelDataMaker
from test_tool import Timer

size_list = ['1tb']
filesize_list = ['1mb', '30mb', '1gb']

def test_random():
    for size in size_list:
        for file_size in filesize_list:
            kwargs = {
            }
            result_file = 'report/test_random_{}_{}.txt'.format(size, file_size)
            if os.path.exists(result_file):
                print('skip {}'.format(result_file))
                continue
            dfmaker = LabelDataMaker(size, file_size, 100, 2)
            multip = len(dfmaker)
            if multip == 0:
                continue
            timer = Timer()
            print('running {}'.format(result_file))
            timer(random, next(dfmaker), **kwargs)
            cost = timer.avg_cost * multip
            with open(result_file, 'w') as f:
                f.write('total,each,number\n')
                f.write(str(cost)+","+str(timer.avg_cost)+","+str(multip))


def test_sort():
    for size in size_list:
        for file_size in filesize_list:
            kwargs = {
                'columns':'1',
                'ascending':'True',
                'na_position':'last',
            }
            result_file = 'report/test_sort_{}_{}.txt'.format(size, file_size)
            if os.path.exists(result_file):
                print('skip {}'.format(result_file))
                continue
            dfmaker = LabelDataMaker(size, file_size, 100, 2)
            multip = len(dfmaker)
            if multip == 0:
                continue
            timer = Timer()
            print('running {}'.format(result_file))
            timer(sort, next(dfmaker), **kwargs)
            cost = timer.avg_cost * multip
            with open(result_file, 'w') as f:
                f.write('total,each,number\n')
                f.write(str(cost)+","+str(timer.avg_cost)+","+str(multip))

def test_normalization():
    for size in size_list:
        for file_size in filesize_list:
            kwargs = {
                'method':'min-max',
                'columns':'1',
            }
            result_file = 'report/test_normalization_{}_{}.txt'.format(size, file_size)
            if os.path.exists(result_file):
                print('skip {}'.format(result_file))
                continue
            dfmaker = LabelDataMaker(size, file_size, 100, 2)
            multip = len(dfmaker)
            if multip == 0:
                continue
            timer = Timer()
            print('running {}'.format(result_file))
            timer(normalization, next(dfmaker), **kwargs)
            cost = timer.avg_cost * multip
            with open(result_file, 'w') as f:
                f.write('total,each,number\n')
                f.write(str(cost)+","+str(timer.avg_cost)+","+str(multip))

