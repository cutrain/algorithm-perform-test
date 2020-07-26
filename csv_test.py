import os
import sys
__module_path='../visual-analysis-platform'
sys.path.append(__module_path)

from algorithm.dataframe import *
from maker import LabelDataMaker
from test_tool import Timer

size_list = ['1tb']
filesize_list = ['1mb', '30mb', '1gb']

def test_knn():
    kwargs = {
        'label_columns':'label',
    }
    for size in size_list:
        for file_size in filesize_list:
            result_file = 'report/test_knn_{}_{}.txt'.format(size, file_size)
            if os.path.exists(result_file):
                print('skip {}'.format(result_file))
                continue
            dfmaker = LabelDataMaker(size, file_size, 100, 2)
            multip = len(dfmaker)
            if multip == 0:
                continue
            print('running {}'.format(result_file))
            timer = Timer()
            timer(classify_knn, next(dfmaker), **kwargs)
            cost = timer.avg_cost * multip
            with open(result_file, 'w') as f:
                f.write('total,each,number\n')
                f.write(str(cost)+","+str(timer.avg_cost)+","+str(multip))

def test_adaboost():
    for size in size_list:
        for file_size in filesize_list:
            kwargs = {
                'label_columns': 'label'
            }
            result_file = 'report/test_adaboost_{}_{}.txt'.format(size, file_size)
            if os.path.exists(result_file):
                print('skip {}'.format(result_file))
                continue
            dfmaker = LabelDataMaker(size, file_size, 100, 2)
            multip = len(dfmaker)
            if multip == 0:
                continue
            print('running {}'.format(result_file))
            timer = Timer()
            timer(classify_adaboost, next(dfmaker), **kwargs)
            cost = timer.avg_cost * multip
            with open(result_file, 'w') as f:
                f.write('total,each,number\n')
                f.write(str(cost)+","+str(timer.avg_cost)+","+str(multip))

def test_svm():
    for size in size_list:
        for file_size in filesize_list:
            kwargs = {
                'label_columns': 'label',
                'kernel': 'linear'
            }
            result_file = 'report/test_svm_{}_{}.txt'.format(size, file_size)
            if os.path.exists(result_file):
                print('skip {}'.format(result_file))
                continue
            dfmaker = LabelDataMaker(size, file_size, 100, 2)
            multip = len(dfmaker)
            if multip == 0:
                continue
            print('running {}'.format(result_file))
            timer = Timer()
            timer(classify_svm, next(dfmaker), **kwargs)
            cost = timer.avg_cost * multip
            with open(result_file, 'w') as f:
                f.write('total,each,number\n')
                f.write(str(cost)+","+str(timer.avg_cost)+","+str(multip))

def test_neural_network():
    for size in size_list:
        for file_size in filesize_list:
            kwargs = {
                'label_columns': 'label',
                'solver': 'adam',
                'alpha': '0.0001',
                'activation': 'relu'
            }
            result_file = 'report/test_neural_network_{}_{}.txt'.format(size, file_size)
            if os.path.exists(result_file):
                print('skip {}'.format(result_file))
                continue
            dfmaker = LabelDataMaker(size, file_size, 100, 2)
            multip = len(dfmaker)
            if multip == 0:
                continue
            print('running {}'.format(result_file))
            timer = Timer()
            timer(classify_neural_network, next(dfmaker), **kwargs)
            cost = timer.avg_cost * multip
            with open(result_file, 'w') as f:
                f.write('total,each,number\n')
                f.write(str(cost)+","+str(timer.avg_cost)+","+str(multip))

def test_naive_bayes():
    for size in size_list:
        for file_size in filesize_list:
            kwargs = {
                'label_columns': 'lable'
            }
            result_file = 'report/test_naive_bayes_{}_{}.txt'.format(size, file_size)
            if os.path.exists(result_file):
                print('skip {}'.format(result_file))
                continue
            dfmaker = LabelDataMaker(size, file_size, 100, 2) 
            multip = len(dfmaker)
            if multip == 0:
                continue
            print('running {}'.format(result_file))
            timer = Timer()
            timer(classify_naive_bayes, next(dfmaker), **kwargs)
            cost = timer.avg_cost * multip
            with open(result_file, 'w') as f:
                f.write('total,each,number\n')
                f.write(str(cost)+","+str(timer.avg_cost)+","+str(multip))

def test_decision_tree():
    for size in size_list:
        for file_size in filesize_list:
            kwargs = {
                'label_columns': 'label'
            }
            result_file = 'report/test_decision_tree_{}_{}.txt'.format(size, file_size)
            if os.path.exists(result_file):
                print('skip {}'.format(result_file))
                continue
            dfmaker = LabelDataMaker(size, file_size, 100, 2)
            multip = len(dfmaker)
            if multip == 0:
                continue
            print('running {}'.format(result_file))
            timer = Timer()
            timer(classify_decision_tree, next(dfmaker), **kwargs)
            cost = timer.avg_cost * multip
            with open(result_file, 'w') as f:
                f.write('total,each,number\n')
                f.write(str(cost)+","+str(timer.avg_cost)+","+str(multip))

