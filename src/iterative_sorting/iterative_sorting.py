# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        tracker = cur_index

        while tracker < (len(arr)):

            if arr[tracker] < arr[smallest_index]:
                smallest_index = tracker
            tracker += 1

        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    # Your code here
    i = 0
    while i <= len(arr) - 1:

        cur_index = 0
        next_index = cur_index + 1

        while next_index < len(arr):

            if arr[cur_index] > arr[next_index]:
                arr[cur_index], arr[next_index] = arr[next_index], arr[cur_index]
            cur_index += 1
            next_index += 1
        i += 1
    return arr


'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''


def counting_sort(arr, maximum=None):
    # Your code here

    return arr


# # Add up and print the sum of the all of the minimum elements of each inner array:
# # The expected output is given by:
# # 4 + -1 + 9 + -56 + 201 + 18 = 175
# # You may use whatever programming language you'd like.
# # Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.

# arr = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
# sum_total = 0

# for sub_arr in arr:

#     for i in len(sub_arr) - 1:


# print(sum_total)
