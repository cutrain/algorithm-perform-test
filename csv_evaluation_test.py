import os
import sys
__module_path='../visual-analysis-platform'
sys.path.append(__module_path)

from algorithm.dataframe.evaluation import *
from maker import LabelDataMaker
from test_tool import Timer

size_list = ['1tb']
filesize_list = ['1mb', '30mb', '1gb']

def test_fone():
    for size in size_list:
        for file_size in filesize_list:
            kwargs = {
                'true_posi':'right',
                'average':'binary',
                'truth_column':'label',
                'pred_column':'label',
            }
            result_file = 'report/test_fone_{}_{}.txt'.format(size, file_size)
            if os.path.exists(result_file):
                print('skip {}'.format(result_file))
                continue
            dfmaker = LabelDataMaker(size, file_size, 100, 2)
            multip = len(dfmaker)
            if multip == 0:
                continue
            timer = Timer()
            print('running {}'.format(result_file))
            new_data = next(dfmaker)
            timer(fone, new_data, new_data, **kwargs)
            cost = timer.avg_cost * multip
            with open(result_file, 'w') as f:
                f.write('total,each,number\n')
                f.write(str(cost)+","+str(timer.avg_cost)+","+str(multip))

def test_recall():
    for size in size_list:
        for file_size in filesize_list:
            kwargs = {
                'true_posi':'right',
                'average':'binary',
                'truth_column':'label',
                'pred_column':'label',
            }
            result_file = 'report/test_recall_{}_{}.txt'.format(size, file_size)
            if os.path.exists(result_file):
                print('skip {}'.format(result_file))
                continue
            dfmaker = LabelDataMaker(size, file_size, 100, 2)
            multip = len(dfmaker)
            if multip == 0:
                continue
            timer = Timer()
            print('running {}'.format(result_file))
            new_data = next(dfmaker)
            timer(recall, new_data, new_data, **kwargs)
            cost = timer.avg_cost * multip
            with open(result_file, 'w') as f:
                f.write('total,each,number\n')
                f.write(str(cost)+","+str(timer.avg_cost)+","+str(multip))

def test_accuracy():
    for size in size_list:
        for file_size in filesize_list:
            kwargs = {
                'true_posi':'right',
                'average':'binary',
                'truth_column':'label',
                'pred_column':'label',
            }
            result_file = 'report/test_accuracy_{}_{}.txt'.format(size, file_size)
            if os.path.exists(result_file):
                print('skip {}'.format(result_file))
                continue
            dfmaker = LabelDataMaker(size, file_size, 100, 2)
            multip = len(dfmaker)
            if multip == 0:
                continue
            timer = Timer()
            print('running {}'.format(result_file))
            new_data = next(dfmaker)
            timer(accuracy, new_data, new_data, **kwargs)
            cost = timer.avg_cost * multip
            with open(result_file, 'w') as f:
                f.write('total,each,number\n')
                f.write(str(cost)+","+str(timer.avg_cost)+","+str(multip))

