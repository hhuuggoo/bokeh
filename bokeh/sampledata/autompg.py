from os.path import dirname, join

try:
    import pandas as pd
except ImportError as e:
    raise RuntimeError("iris data requires pandas (http://pandas.pydata.org) to be installed")

autompg = pd.read_csv(join(dirname(__file__), 'auto-mpg.csv'))
