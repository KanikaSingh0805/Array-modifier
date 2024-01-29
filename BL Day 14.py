def move_zeroes(nums):
    non_zero_count = 0

    # Move all non-zero elements to the front
    for num in nums:
        if num != 0:
            nums[non_zero_count] = num
            non_zero_count += 1

    # Fill the remaining positions with zeroes
    while non_zero_count < len(nums):
        nums[non_zero_count] = 0
        non_zero_count += 1

    return nums

# Ask the user for input
input_array = input("Enter the numbers separated by commas: ").strip().split(',')
input_array = [int(num) for num in input_array]

# Call the function and print the result
output_array = move_zeroes(input_array)
print("Array after moving zeroes to the end:", output_array)
