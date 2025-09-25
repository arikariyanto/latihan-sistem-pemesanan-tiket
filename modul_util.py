# Sorting dengan Bubble Sort
def bubble_sort(data):
    n = len(data)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data

# Searching dengan Linear Search
def linear_search(data, target):
    for i in range(len(data)):
        if data[i].lower() == target.lower():
            return i
    return -1