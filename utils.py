from io import DEFAULT_BUFFER_SIZE
import numpy as np
from numpy.lib.format import dtype_to_descr 

class LoadDataset:
    def __init__(self, path: str, sep: str) -> None:
        
        self.data = np.genfromtxt(path, delimiter=sep, dtype=np.int)


