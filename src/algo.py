# algos to find possible peak values (spike/pulse/apex) from discrete 2-Dimension data
# input data format: List[Tuple[float, float]], **kwargs
# output data format: List[Tuple[float, float]]


from typing import List, Tuple


def algo_threshold_v1(data: List[Tuple[float, float]], **kwargs) -> List[Tuple[float, float]]:
    value_threshold = kwargs.get("value_threshold", 0.55)

    return [
        data[i] for i in range(1, len(data) - 1)
        if data[i][1] > value_threshold and data[i][1] > data[i-1][1] and data[i][1] > data[i+1][1]
    ]


def algo_threshold_v2(data: List[Tuple[float, float]], **kwargs) -> List[Tuple[float, float]]:
    slope_threshold = kwargs.get("slope_threshold", 0.1)

    return [
        data[i] for i in range(1, len(data) - 1)
        if min(data[i][1] - data[i-1][1], data[i][1] - data[i+1][1]) > slope_threshold
    ]


algo_l = [algo_threshold_v1]
