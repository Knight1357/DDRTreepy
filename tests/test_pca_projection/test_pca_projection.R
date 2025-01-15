
library(devtools)

# uninstall(DDRTree)

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
R_X_path = "/mnt/ssd/geneplus/develop/liushen/projects/DDRTreepy/tests/data/random_matrix.csv"


# header = TRUE 表示文件包含列名，可根据实际情况修改
X <- as.matrix(read.csv(R_X_path, header = FALSE)) 



result <- pca_projection_R(
    X, dimensions
)

print(result)
