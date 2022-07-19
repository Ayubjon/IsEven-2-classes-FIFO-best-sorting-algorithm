# ---------------------------------------
# THIRD PROBLEM
# ---------------------------------------

# Merge Sort works in O(n * log(n)) anyway, no matter is array sorted or not.
# If array's length is 1 it's sorted if not we divide it into 2 arrays sort them. And mergeSort 2 sorted arrays.
def mergeSort(array: list) -> list:
    length = len(array)
    if length == 1:
        return array
    left = array[:(length // 2)]
    right = array[(length // 2):]
    left = mergeSort(left)
    right = mergeSort(right)
    i = 0
    j = 0
    newArray = []
    while i != len(left) and j != len(right):
        if left[i] < right[j]:
            newArray.append(left[i])
            i += 1
        else:
            newArray.append(right[j])
            j += 1
    while i != len(left):
        newArray.append(left[i])
        i += 1
    while j != len(right):
        newArray.append(right[j])
        j += 1
    return newArray


def testMergeSort():
    print(mergeSort([4, 1, 2, 3]))
    print(mergeSort([1, 2, 3, 4]))
    print(mergeSort([3]))
    print(mergeSort([10331, 1231222, 55011]))
    print("Enter list of numbers to sort them: ", end="")
    print(mergeSort(list(map(int, input().split()))))


# Hello, here I will code and test problems that
# I got like a test for Junior Python Programmer position.
if __name__ == '__main__':
    testMergeSort()
