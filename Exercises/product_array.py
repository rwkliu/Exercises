# nums = [1, 2, 3, 4]
# prefix = [1, 1, 2, 6]
# suffix = [24, 12, 4, 1]
# output = [prefix[i] * suffix[i] for i in range(len(prefix))]
# print(output)


def product_array(nums):
    # Calculate prefix array
    prefix = [1] * len(nums)
    for i in range(1, len(nums)):
        prefix[i] = prefix[i - 1] * nums[i - 1]
    # print(prefix)
    # Calculate suffix array
    suffix = [1] * len(nums)
    for i in range(len(nums) - 2, -1, -1):
        suffix[i] = suffix[i + 1] * nums[i + 1]
    # print(suffix)
    # Calculate output
    output = [prefix[i] * suffix[i] for i in range(len(prefix))]
    return output


def optimized(nums):
    output = [1] * len(nums)

    curr = 1
    for i in range(1, len(nums)):
        output[i] *= curr
        curr *= nums[i]

    curr = 1
    for i in range(len(nums) - 1, -1, -1):
        output[i] *= curr
        curr *= nums[i]

    return output


nums = [1, 2, 3, 4]
print(product_array(nums))
print(optimized(nums))
