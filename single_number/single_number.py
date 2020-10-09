'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    res = arr[0]
    for i in range(1,len(arr)):
        res = res ^ arr[i] #xor operator will cancel out all repeating numbers to 0 leaving only the odd number out
    return res


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")