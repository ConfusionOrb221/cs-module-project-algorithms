'''
Input: an integer
Returns: an integer
'''
"""
1	|	1 I realized the number is just the combination of the previous 3 numbers	
2	|	2 i started doing them manually after 3 
3	|	4
4	|	7
5	|	13	
6	|	24
7	|	44
"""
def eating_cookies(n):
    # Your code here
    if n == 2:
        return 2
    elif n == 1:
        return 1
    elif n == 0: #this test case doesnt make sense
        return 1
    elif n > 2:
        arr = [1, 1, 2]
        for i in range(n - 2):
            arr.append(sum(arr))
            arr.pop(0)
        return arr[2]
    
    pass

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
