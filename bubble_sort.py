import pdb
from random import randint

def bubble_sort(list):
    list_len = len(list)
    if list_len <= 1:
        return
    index = 0
    while index < list_len:
        if list[index] > list[index+1]:
            temp = list[index]
            list[index] = list[index+1]
            list[index+1] = temp
        index += 1
        if index == list_len-1:
            index = 0
            list_len -= 1

if __name__ == '__main__':
    list = [8,7,6,5,4,3,2,1]
    bubble_sort(list)
    print list
    list = [2,7,9,3,4]
    bubble_sort(list)
    print list
    list = [6,5,3,1,8,7,2,4]
    bubble_sort(list)
    print list
    list = []
    for i in range(200):
        list.append(randint(1,200))
    print list
    bubble_sort(list)
    print list
