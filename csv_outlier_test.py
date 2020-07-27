
import os
import sys
__module_path='../visual-analysis-platform'
sys.path.append(__module_path)

from algorithm.dataframe.outlier import *
from maker import LabelDataMaker
from test_tool import Timer

size_list = ['1tb']
filesize_list = ['1mb', '30mb', '1gb']

def test_iforest():
    for size in size_list:
        for file_size in filesize_list:
            kwargs = {
                'contamination':'0.1',
                'n_jobs':'10',
            }
            result_file = 'report/test_iforest_{}_{}.txt'.format(size, file_size)
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
            timer(outlier_iforest, new_data, **kwargs)
            cost = timer.avg_cost * multip
            with open(result_file, 'w') as f:
                f.write('total,each,number\n')
                f.write(str(cost)+","+str(timer.avg_cost)+","+str(multip))


