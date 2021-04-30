# **python-warmup**

Some helper codes to assit us in the dataset analysis task.


## **Description**

Our team received interesting challenges: 
*   Task \#1 Extract, Transform and Load pipeline without third party libraries
*   Task \#2 Create a recommendation system using the `ml-100k` dataset and our ETL framework

To spare our lives, we designed a ETL framework using python standard types, e.g. `dict`, `list`, `int`, `float`, etc... 

## **Usage**

To use the modules developed, clone this repo and, inside the directory `~/path_to_cloned_repo/python-warmup`, create every test file or script.

```python
from modules import DataFrame, mean, std #to use every function or class described in the module.py we need to import them


df = DataFrame(<path_to_dataset>, sep=<dataset_separator>, columns=<list_of_columns_names>)
```
There's a jupyer notebook with the first task completed as an example for better understanding of the funcionality of the modules.

## **Contributions**

If you want to add, remove or comment any new feature to the core code, please open an issue with a brief description of the feature and assigne it to whom will develop the new feature. We must follow the workflow patterns learned in the previous classes. This pratice helps us to improve in community-like development environment, also helps us to develop good pratices in code development. After opening an issue, to close it create a pull request to main.