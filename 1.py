'''
Дан массив чисел, состоящий из некоторого количества подряд идущих единиц, за которыми
следует какое-то количество подряд идущих нулей: 111111111111111111111111100000000.
Найти индекс первого нуля (то есть найти такое место, где заканчиваются единицы, и
начинаются нули)

Какова сложность вашего алгоритма?
'''

#import time
#start = time.time()
def task(array, desire_val='0'):
    first = 0
    last = len(array)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if array[mid] == desire_val and array[mid-1] == '1':
            index = mid
        else:
            if array[mid-1] == '0':
                last = mid -1
            else:
                first = mid +1
    return index

print(task("111111111111111111111111100000000"))
#finish = time.time()
#print("elapsed time: ", finish-start)
