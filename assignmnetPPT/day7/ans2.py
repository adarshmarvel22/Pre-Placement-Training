def is_strobogrammatic(num):
    left, right = 0, len(num) - 1
    strobogrammatic_pairs = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}

    while left <= right:
        left_char = num[left]
        right_char = num[right]

        if left_char not in strobogrammatic_pairs or strobogrammatic_pairs[left_char] != right_char:
            return False

        left += 1
        right -= 1

    return True

num = "69"
print(is_strobogrammatic(num))  # Output: True
