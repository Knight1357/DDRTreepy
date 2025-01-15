import time
from loguru import logger
import datetime
import scanpy as sc
import numpy as np

def time_func(func):
    """
    便捷的记录函数运行时间
    """

    def wrapper(*args, **kwargs):
        start_time = time.time()  # 记录开始时间
        result = func(*args, **kwargs)  # 执行函数
        end_time = time.time()  # 记录结束时间
        start_time_fmt = datetime.datetime.fromtimestamp(start_time).strftime(
            "%Y-%m-%d %H:%M:%S"
        )
        run_time = str(round((end_time - start_time) / 60, 2))

        logger.info(
            f"函数 {func.__name__} 开始时间： {start_time_fmt}，"
            f"整体运行时间: {run_time} min"
        )
        return result

    return wrapper


def memory_usage(step="此处"):
    memory_usage = sc.logging.get_memory_usage()
    logger.info(
        f"代码运行到{step}内存共使用：{memory_usage[0]:.2f} GB，相比前一次记录，内存变化：{memory_usage[1]:.2f} GB"
    )

def print_matrix_elements(matrix, num_elements = 10):
    """
    打印给定矩阵的前 num_elements 个元素。

    参数:
    matrix: 二维数组或矩阵
    num_elements: 要打印的元素数量
    """
    # 确保 matrix 是一个 NumPy 数组
    if not isinstance(matrix, (np.ndarray)):
        logger.error("Provided matrix is not a valid NumPy array.")
        return

    # 检查矩阵的维度
    if matrix.ndim != 2:
        logger.error("Provided matrix is not a 2D array.")
        return

    # 记录矩阵大小
    logger.info(f"Matrix size: ({matrix.shape[0]} x {matrix.shape[1]})")
    logger.info(f"Matrix (first {num_elements} elements):")
    
    count = 0
    for i in range(min(num_elements, matrix.shape[0])):  # 对于行数
        for j in range(min(num_elements, matrix.shape[1])):  # 对于列数
            print(f"Matrix[{i}, {j}] = {matrix[i, j]} ")
            count += 1
            if count >= num_elements:  # 只打印到指定数量的元素
                return  # 退出函数
        if count >= num_elements:
            return  # 退出函数
    print('')

# 使用示例
# print_matrix_elements(B, 10)  # 确保 B 是一个 NumPy 的 2D 数组