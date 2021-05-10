class _Datasettype(list):
    """Wrapper mimics the functionality of Series in the pandas package. 
    
    Data struct wraps the loaded dataset into a customized container.

    Example:
        >>>ds = _Datasettype([[1,2,3,4,5,6],
                              [4,3,2,4,5,1]] 
                            )
        >>>ds[0, 2]
        >>>ds=modules._Datasettype(    [[1,2,3,4,5,6],
                                        [4,3,2,4,5,1],
                                        [4,3,2,4,5,1],
                                        [4,3,2,4,5,1],
                                        [4,3,2,4,5,1],
                                        [4,3,2,4,5,1],
                                        [4,3,2,4,5,1]])
        >>>ds[0,2]
        >>>[3]
        >>>ds[0:4,2]
        >>>[3, 2, 2, 2]
        >>>ds[0,2:4]
        >>>[[3, 4]]

        ..note:
            This wrapper implements `in`, `len(.)`, `==`, `[idx]`, `[idx1, idx2]`, `[start1:stop1, start2:stop2]`
    """
    def __init__(self, data: list):
        self._data=data
        super().__init__(self)
        
    def __contains__(self, obj):
        return [obj in "".join(x) for x in self._data]

    def __eq__(self, obj):
        if isinstance(obj, list):
            obj = list(map(lambda x: "".join(x),obj))
            return [x in obj  for x in self._data]
        return [x == obj  for x in self._data]

    def __iter__(self):
        #return iter([self[idx] for idx in range(len(self))])
        return iter(self._data)
    
    def __len__(self) -> int:
        return len(self._data)
           
    def __getitem__(self, idx: int) -> int:

        if isinstance(idx, tuple):
            _slice1=idx[0]
            _slice2=idx[1]

            if isinstance(_slice1, int):
                return _Datasettype([self._data[_slice1][_slice2]])
            if isinstance(_slice2, int):
                return _Datasettype(list(map(lambda x: x[_slice2], self._data[_slice1])))
            
                
            return _Datasettype([x[_slice2] for x in self._data[_slice1]])

        elif isinstance(idx, list):

            _selected_content=[]

            for i, boolean in enumerate(idx):
                if boolean:
                    _selected_content.append(self._data[i])

            return _Datasettype(_selected_content)
        else:    
            return _Datasettype(self._data[idx])


class DataFrame(_Datasettype):
    """Handler class trying to mimic DataFrame class

    Args:
        path (string): path to where the dataset is saved.

    Properties:
        loc (_Datatype): raw data in _Datatype type.
    
    """
    def __init__(self, path: str, separator: str, columns: list):
        
        self._path=path
        self._separator=separator
        self._columns=columns
        self._raw_data=self.load()
        self._data=self._set_header()
        
    @property
    def loc(self) -> _Datasettype:
        return self._raw_data
    
    def __len__(self) -> int:
        return len(self._raw_data)

    def _set_header(self) -> dict:
        return {key: self._raw_data[:,i] for i, key in enumerate(self._columns)}

    def load(self) -> _Datasettype:
        data=[]
        with open(self._path, encoding = "ISO-8859-1") as f:
            for line in  f.readlines():
                data.append(
                    tuple(
                            map(lambda x: x.replace('\n', ''), line.split(sep=self._separator))
                        )
                    )
        return _Datasettype(data)



def flat(dataset: list) -> list:
    return list(map(float,[x for y in dataset for x in y]))

def mean(dataset: list) -> float:
    sigma = sum(dataset)
    N = len(dataset)
    return sigma / N

def std(dataset: list) -> float:
    sqrt = lambda x: x**(1/2)
    mu = mean(dataset)
    sigma = sum([x - mu for x in dataset])
    N = len(dataset)

    return sqrt(sigma**2/(N-1))