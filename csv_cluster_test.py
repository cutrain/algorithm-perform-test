import os
import sys
__module_path='../visual-analysis-platform'
sys.path.append(__module_path)

from algorithm.dataframe.cluster import *
from maker import DataFrameMaker
from test_tool import Timer

size_list = ['1tb']
filesize_list = ['1mb', '30mb', '1gb']

def test_dbscan():
    for size in size_list:
        for file_size in filesize_list:
            kwargs = {
                'eps':0.5,
                'minpts':5,
                'predict_labels':'label',
                'store_origin':'False',
            }
            result_file = 'report/test_dbscan_{}_{}.txt'.format(size, file_size)
            if os.path.exists(result_file):
                print('skip {}'.format(result_file))
                continue
            dfmaker = DataFrameMaker(size, file_size, 100)
            multip = len(dfmaker)
            if multip == 0:
                continue
            timer = Timer()
            print('running {}'.format(result_file))
            timer(dbscan, next(dfmaker), **kwargs)
            cost = timer.avg_cost * multip
            with open(result_file, 'w') as f:
                f.write('total,each,number\n')
                f.write(str(cost)+","+str(timer.avg_cost)+","+str(multip))

def test_kmeans():
    for size in size_list:
        for file_size in filesize_list:
            kwargs = {
                'n_cluster':8,
                'max_iter':300,
                'predict_labels':'label',
                'store_origin':'False',
            }
            result_file = 'report/test_kmeans_{}_{}.txt'.format(size, file_size)
            if os.path.exists(result_file):
                print('skip {}'.format(result_file))
                continue
            dfmaker = DataFrameMaker(size, file_size, 100)
            multip = len(dfmaker)
            if multip == 0:
                continue
            timer = Timer()
            print('running {}'.format(result_file))
            timer(kmeans, next(dfmaker), **kwargs)
            cost = timer.avg_cost * multip
            with open(result_file, 'w') as f:
                f.write('total,each,number\n')
                f.write(str(cost)+","+str(timer.avg_cost)+","+str(multip))
