
import sys
import os

# 将drr_tree.py文件所在目录添加到系统路径
module_path = '/mnt/ssd/geneplus/develop/liushen/projects/DDRTreepy/DDRTree'  # ddr_tree.py所在的目录
if module_path not in sys.path:
    sys.path.append(module_path)

# 导入ddr_tree模块
from ddr_tree import * # 现在可以导入ddr_tree.py文件

import pandas as pd


n_samples = 3000      # 样本数量（N）
n_features = 500    # 原始特征维度（D）
num_clusters = 100   # 聚类数量（K）
dimensions = 2      # 降维后的维度（d）
maxiter = 20        # 最大迭代次数
sigma = 1e-3        # 高斯核参数
lambda_ = 0.1       # 正则化参数
gamma = 10         # 权重参数
eps = 1e-3          # 收敛阈值
verbose = True      # 是否输出详细信息

# 指定CSV文件路径
R_X_path = "/mnt/ssd/geneplus/develop/liushen/projects/DDRTreepy/tests/data/R_X.csv"

# 使用pandas读取CSV文件
df = pd.read_csv(R_X_path, header=None)  # header=None表示不将第一行作为列名
X_R = df.values  # 或使用 df.to_numpy()

result = DDRTree_python(X_R, maxIter = 1, verbose=True)
print(result)

