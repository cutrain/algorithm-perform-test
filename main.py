import time
import inspect

def test_group(module):
    obj = inspect.getmembers(module)
    test_case = []
    for name, value in obj:
        if inspect.isfunction(value) and name[:4]=="test":
            test_case.append((name, value))
    print('\033[0;33mStart\033[0m Module: {}, Total {} cases'.format(module.__name__, len(test_case)))
    cnt = 0
    for name, value in test_case:
        cnt += 1
        print('\033[0;33mRunning\033[0m case {}:'.format(cnt), name)
        start = time.time()
        value()
        end = time.time()
        diff = end - start
        print('\033[0;32mComplete\033[0m case {}:'.format(cnt), name, 'cost:%.2fs'% diff)
    print('\033[0;32mFinish\033[0m Module: {}'.format(module.__name__))



def test_basic():
    import basic_test
    test_group(basic_test)

def test_csv():
    import csv_test
    test_group(csv_test)

def test_csv_cluster():
    import csv_cluster_test
    test_group(csv_cluster_test)

def test_csv_evaluation():
    import csv_evaluation_test
    test_group(csv_evaluation_test)

def test_process():
    import csv_process_test
    test_group(csv_process_test)

def test_outlier():
    import csv_outlier_test
    test_group(csv_outlier_test)

def test_image():
    import image_test
    test_group(image_test)

def test_video():
    import video_test
    test_group(video_test)

def test_graph():
    import graph_test
    test_group(graph_test)

if __name__ == "__main__":
    test_basic()
    test_csv()
    test_csv_cluster()
    test_process()
    test_csv_evaluation()
    test_outlier()
    test_image()
    test_video()
    test_graph()
