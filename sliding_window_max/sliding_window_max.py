'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

from collections import deque 

def sliding_window_max(nums, k):
    # Your code here
    """
    Creates a double ended queue that stores index of array elements
    Maintains decreasing order of values front to rear
    nums[que.front[]] && nums[que.rear()]
    """
    que = deque()
    arr = []
    length = len(nums)

    # returns the first window of the elements in the array
    for i in range(k):
        while que and nums[i] >= nums[que[-1]]:
            que.pop()
        que.append(i)
    #Process the rest of the elements wndows from k to n-1
    for i in range(k, length):
        #The element in at the front of the que is the largest so we add it to our external buffer array
        arr.append(nums[que[0]])
        #Remove elements that are outside of the current window
        while que and que[0] <= i-k:
            que.popleft()
        #Remove all emenets amsller then the currently being added element(Useless elements)
        while que and nums[i] >= nums[que[-1]]:
            que.pop()
        #Add the element at the rear of the que
        que.append(i)
    #Add the maximum element of the last window
    arr.append(nums[que[0]])

    return arr

    """
    array = []
    for i in range(len(nums) - k + 1):
        arr = nums[i:(k+i)]
        
        array.append(max(arr))
    return array
    """


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
