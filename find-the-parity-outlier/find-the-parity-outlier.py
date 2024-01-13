def find_outlier(integers):
    odd_nums = [num for num in integers if num % 2 != 0]
    even_nums = [num for num in integers if num % 2 == 0]

    if len(odd_nums) == 1:
        return odd_nums[0]
    elif len(even_nums) == 1:
        return even_nums[0]


    return None
