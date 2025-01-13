library(irlba)

#' Get the top L eigenvalues
#' @param C data matrix used for eigendecomposition
#' @param L number for the top eigenvalues
#' @import irlba irlba
#' @export
get_major_eigenvalue <- function(C, L) {
    if (L >= min(dim(C))){
        return (base::norm(C, '2')^2);
    }else{
        #message("using irlba")
        initial_v <- as.matrix(qnorm(1:(ncol(C) + 1)/(ncol(C) + 1))[1:ncol(C)])
        eigen_res <- irlba(C, nv = L, v = initial_v)
        return (max(abs(eigen_res$v)))
    }
    #     eig_sort <- sort(V, decreasing = T, index.return = T)
    #     eig_idx <- eig_sort$ix
    #
    #     W <- U[, eig_idx[1:L]]
}


# 指定CSV文件路径
csv_file_path = '/mnt/ssd/geneplus/develop/liushen/projects/DDRTreepy/tests/data/random_matrix.csv'

data <- read.csv(csv_file_path, header = TRUE)  # header = TRUE 表示文件包含列名，可根据实际情况修改

# 将数据框转换为矩阵
matrix_data <- as.matrix(data)

C = matrix_data



L = 5  # 设置要检索的前 5 个特征值
top_eigenvalue = get_major_eigenvalue(C, L)  # 调用函数获取特征值
print(top_eigenvalue)  # 输出最大特征值
