# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import lightgbm as lgb
from pandas import DataFrame
from sklearn.model_selection import train_test_split
from io import StringIO
import gc
import sys
import os



hive_cmd = "hive -f ./sql/sql.sql"
output = os.popen(hive_cmd)
data_cart_prop = pd.read_csv(StringIO(np.unicode(output.read(), 'utf-8')), sep="\t", header=0)