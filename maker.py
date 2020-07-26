import pandas as pd
import numpy as np

class BaseMaker:
    def __init__(self, size, unit_size, generator, batch_size, drop_last, repeat):
        if type(size) == str:
            if size[-2:].upper()=='TB':
                #      KB   MB   GB   TB
                base=1024*1024*1024*1024
            elif size[-2:].upper()=='GB':
                #      KB   MB   GB
                base=1024*1024*1024
            elif size[-2:].upper()=='MB':
                #      KB   MB
                base=1024*1024
            elif size[-2:].upper()=='KB':
                #      KB
                base=1024
            else:
                raise NotImplementedError
            size = int(size[:-2])*base
        if type(unit_size) == str:
            if unit_size[-2:].upper()=='TB':
                #      KB   MB   GB   TB
                base=1024*1024*1024*1024
            elif unit_size[-2:].upper()=='GB':
                #      KB   MB   GB
                base=1024*1024*1024
            elif unit_size[-2:].upper()=='MB':
                #      KB   MB
                base=1024*1024
            elif unit_size[-2:].upper()=='KB':
                #      KB
                base=1024
            else:
                raise NotImplementedError
            unit_size = int(unit_size[:-2])*base
        self._size = size
        self._unit_size = unit_size
        self._generator = generator
        self._batch_size = batch_size
        self._drop_last = drop_last
        self._repeat = repeat

        self._len = size // unit_size
        self._count = 0
        if self._repeat:
            self._data = lambda :self._generator()
        else:
            self._data = self._generator

    def __iter__(self):
        self._count = 0
        if self._repeat:
            self._data = lambda :self._generator()
        else:
            self._data = self._generator
        return self

    def __next__(self):
        if self._count >= self._len:
            raise StopIteration
        if self._count + self._batch_size > self._len and self._drop_last:
            raise StopIteration
        ret = []
        for i in range(self._count, min(self._count+self._batch_size, self._len)):
            ret.append(self._data())
        self._count += self._batch_size
        if self._batch_size == 1:
            return ret[0]
        return ret

    def __len__(self):
        return self._len


class DataFrameMaker(BaseMaker):
    def __init__(self, size, file_size, dimension, batch_size=1, drop_last=True, repeat=True, seed=None, mode='uniform_float'):
        """set dataset size & dimension
        size: total dataset size (B)
        dimension: column number
        repeat: True, will generate new data every iter if False
        seed: generate new data with random seed
        """
        if mode != 'uniform_float':
            raise NotImplementedError
        if type(file_size) == str:
            if file_size[-2:].upper()=='TB':
                #      KB   MB   GB   TB
                base=1024*1024*1024*1024
            elif file_size[-2:].upper()=='GB':
                #      KB   MB   GB
                base=1024*1024*1024
            elif file_size[-2:].upper()=='MB':
                #      KB   MB
                base=1024*1024
            elif file_size[-2:].upper()=='KB':
                #      KB
                base=1024
            else:
                raise NotImplementedError
            file_size = int(file_size[:-2])*base
        self.__rowsize = 19*dimension # 18 floatchar + ',' + '\n'
        row = file_size // self.__rowsize
        super().__init__(size, file_size, self.__gen_csv(row, dimension, seed), batch_size, drop_last, repeat)

    def __gen_csv(self, row, dimension, seed):
        columns = [str(i) for i in range(dimension)]
        random_generator = np.random.RandomState(seed)
        def gen_row():
            return pd.DataFrame(random_generator.rand(row, dimension), columns=columns)
        return gen_row

class LabelDataMaker(BaseMaker):
    def __init__(self, size, file_size, dimension, class_, batch_size=1, drop_last=True, repeat=True, seed=None):
        if type(file_size) == str:
            if file_size[-2:].upper()=='TB':
                #      KB   MB   GB   TB
                base=1024*1024*1024*1024
            elif file_size[-2:].upper()=='GB':
                #      KB   MB   GB
                base=1024*1024*1024
            elif file_size[-2:].upper()=='MB':
                #      KB   MB
                base=1024*1024
            elif file_size[-2:].upper()=='KB':
                #      KB
                base=1024
            else:
                raise NotImplementedError
            file_size = int(file_size[:-2])*base
        self.__rowsize = 19*dimension + 2
        row = file_size // self.__rowsize
        super().__init__(size, file_size, self.__gen_label(row, dimension, class_, seed), batch_size, drop_last, repeat)

    def __gen_label(self, row, dimension, class_, seed):
        random_generator = np.random.RandomState(seed)
        columns = [str(i) for i in range(dimension)]+['label']
        def gen_label():
            df = pd.DataFrame(np.hstack((random_generator.rand(row, dimension), random_generator.randint(0, class_, (row, 1), dtype='int'))), columns=columns)
            df['label']=df['label'].astype(int)
            return df
        return gen_label




