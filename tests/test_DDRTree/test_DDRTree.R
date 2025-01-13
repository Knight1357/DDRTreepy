
library(devtools)

devtools::install("/mnt/ssd/geneplus/develop/liushen/projects/DDRTreepy")

library(DDRTree)

n_samples = 3000      # 样本数量（N）
n_features = 500    # 原始特征维度（D）
num_clusters = 100   # 聚类数量（K）
dimensions = 2      # 降维后的维度（d）
maxiter = 20        # 最大迭代次数
sigma = 1e-3        # 高斯核参数
lambda_ = 0.1       # 正则化参数
gamma = 10         # 权重参数
eps = 1e-3          # 收敛阈值
verbose = T      # 是否输出详细信息

# 指定CSV文件路径
R_X_path = "/mnt/ssd/geneplus/develop/liushen/projects/DDRTreepy/tests/data/R_X.csv"
R_Z_path = "/mnt/ssd/geneplus/develop/liushen/projects/DDRTreepy/tests/data/R_Z.csv"
R_Y_path = "/mnt/ssd/geneplus/develop/liushen/projects/DDRTreepy/tests/data/R_Y.csv"
R_W_path = "/mnt/ssd/geneplus/develop/liushen/projects/DDRTreepy/tests/data/R_W.csv"

# header = TRUE 表示文件包含列名，可根据实际情况修改
R_X <- as.matrix(read.csv(R_X_path, header = TRUE)) 
R_Z <- as.matrix(read.csv(R_Z_path, header = TRUE)) 
R_Y <- as.matrix(read.csv(R_Y_path, header = TRUE)) 
R_W <- as.matrix(read.csv(R_W_path, header = TRUE)) 


result <- DDRTree(
    R_X, maxIter = 1, verbose=T
)

print(result)
