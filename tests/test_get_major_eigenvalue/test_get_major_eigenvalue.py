
import sys
import os

# 将drr_tree.py文件所在目录添加到系统路径
module_path = '/mnt/ssd/geneplus/develop/liushen/projects/DDRTreepy/DDRTree'  # ddr_tree.py所在的目录
if module_path not in sys.path:
    sys.path.append(module_path)

# 导入ddr_tree模块
from ddr_tree import * # 现在可以导入ddr_tree.py文件

import pandas as pd

    

# 指定CSV文件路径
csv_file_path = '/mnt/ssd/geneplus/develop/liushen/projects/DDRTreepy/tests/data/random_matrix.csv'

# 使用pandas读取CSV文件
df = pd.read_csv(csv_file_path, header=None)  # header=None表示不将第一行作为列名

# 将DataFrame转换为NumPy数组（二维矩阵）
matrix = df.values  # 或使用 df.to_numpy()

# 打印导入的矩阵
# print(matrix)

C = matrix

L = 5  # 设置要检索的前 5 个特征值
top_eigenvalue = get_major_eigenvalue_python(C, L)  # 调用函数获取特征值
print(top_eigenvalue)  # 输出最大特征值

