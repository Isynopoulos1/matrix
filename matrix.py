from functools import reduce

matrix_example =[
    [3,8,5,4],
    [5,3,1,9],
    [9,8,4,7],
    [7,4,2,1]
]
   
# DEFINITIONS 

def process_matrix(matrix):
    proxies = []
    averages = []
    for row_index, row in enumerate(matrix):
        for column_index, column in enumerate(row):
            proxies.append(process_element(matrix, [row_index, column_index], row))
    for proxy in proxies:
        averages.append(reduce_element(proxy))

    return averages


def get_element(matrix, indexes):
    return matrix[indexes[0]][indexes[1]] if indexes != None else None

def proxy_filter(proxy_list):
    return list(filter(lambda item: item is not None, proxy_list))

def reduce_element(proxy):
    total = reduce(lambda a, b: a + b, proxy)
    proxy_average = round(total / len(proxy), 2)
    return proxy_average


def process_element(matrix, indexes, row):
   # DEFINE INDEXES
    row_index = indexes[0]
    column_index = indexes[1]

    # DEFINE ELEMENTS AND PROXIES
    element = get_element(matrix, [row_index, column_index])
    left_element =  get_element(matrix, [row_index, column_index - 1]) if (column_index - 1) >= 0 else None
    right_element =  get_element(matrix, [row_index, column_index + 1])  if (column_index + 1) < len(row) else None
    top_element =  get_element(matrix, [row_index - 1, column_index])  if (row_index - 1) >= 0 else None
    bottom_element =  get_element(matrix, [row_index + 1, column_index]) if (row_index + 1) < len(matrix) else None

    # RETURN PROXY ARRAY
    return proxy_filter([element, left_element, right_element, top_element, bottom_element])


# INVOCATION
results = process_matrix(matrix_example)
print(results)