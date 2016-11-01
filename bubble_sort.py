import pdb
def bubble_sort(list):
    list_len = len(list)
    if list_len <= 1:
        return
    index = 0
    while(list[index] > list[index+1]):
        temp = list[index]
        list[index] = list[index+1]
        list[index+1] = temp
        index += 1
        if index == list_len-1:
            index = 0

if __name__ == '__main__':
    list = [8,7,6,5,4,3,2,1]
    bubble_sort(list)
    print list
