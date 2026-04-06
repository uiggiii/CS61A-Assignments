def two_of_four(a,b,c,d):
    return min(a,b,c,d)**2 + min(min(max(a,b),max(c,d)),max(min(a,b),min(c,d)))**2

while True:
    a, b, c, d = [int(input(f"input {i}'s number: ")) for i in range(4)]
    print(two_of_four(a,b,c,d))


'''
# from ai agent
# if you want to find the two smallest numbers in a list of four numbers, you can use the following function:
def find_two_smallest_manual(nums):
    """
    Find the two smallest numbers in a list without using any libraries.
    Time complexity: O(n) where n is the length of nums.
    """
    if len(nums) < 2:
        raise ValueError("List must have at least 2 elements")
    min1 = float('inf')
    min2 = float('inf')
    for num in nums:
        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num
    return [min1, min2]

# Example usage for find_two_smallest_manual
if __name__ == "__main__":
    nums = [3, 1, 4, 1, 5, 9, 2, 6]
    smallest_two = find_two_smallest_manual(nums)
    print(f"The two smallest numbers are: {smallest_two}")  # Output: [1, 1]'''

