import os
import sys
__module_path='../visual-analysis-platform'
sys.path.append(__module_path)

from algorithm.basic import *
from maker import DataFrameMaker
from test_tool import Timer

# I/O密集任务，无测试必要
test_size = ['1tb']
test_filesize = ['1mb', '30mb', '1gb']

def test_data_instream():
    for file_size in test_filesize:
        newfile = False
        for size in test_size:
            result_file = 'report/test_data_instream_{}_{}.txt'.format(size, file_size)
            if os.path.exists(result_file):
                print('skip {}'.format(result_file))
                continue
            test_file = 'testfile.csv'
            dfmaker = DataFrameMaker(size, file_size, 100)
            multip = len(dfmaker)
            if multip == 0:
                continue
            print('testing {}'.format(result_file))
            if not newfile:
                df = next(dfmaker)
                df.to_csv('data/'+test_file)
                newfile = True

            timer = Timer()
            kwargs = {
                'read_number':'0',
                'header':'True',
                'path':test_file,
            }
            while timer.total_cost < 2:
                timer(data_instream, **kwargs)
            cost = timer.avg_cost * multip
            with open(result_file, 'w') as f:
                f.write('total,each,number\n')
                f.write(str(cost)+","+str(timer.avg_cost)+","+str(multip))

def test_data_outstream():
    pass
def test_sql_instream():
    pass
def test_sql_outstream():
    pass
def test_model_instream():
    pass
def test_model_oustream():
    pass
def test_image_instream():
    pass
def test_image_outstream():
    pass
def test_graph_instream():
    pass
def test_graph_outsream():
    pass
def test_video_instream():
    pass
def test_video_oustream():
    pass
def test_seq_instream():
    pass
def test_seq_outstream():
    pass
def test_text_instream():
    pass
def test_text_oustream():
    pass
