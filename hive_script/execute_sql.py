# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from io import StringIO
import os


hive_cmd = 'hive -e "create table default.test(id int);"'
output = os.popen(hive_cmd)
data_cart_prop = pd.read_csv(StringIO(np.unicode(output.read(),'utf-8')), sep="\t",header=0)