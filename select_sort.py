# 从数组中返回最小元素索引，为选择排序pop出该元素
def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    # 因为第一个元素已经取出，从下一个索引开始遍历
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


print(selectionSort([5, 3, 6, 2, 10]))
