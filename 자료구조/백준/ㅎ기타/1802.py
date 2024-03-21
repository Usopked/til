def is_symmetric(binary_str):
    if len(binary_str) == 1: return 'YES'
    mid = len(binary_str) // 2
    flipped_right = ''.join('1' if digit == '0' else '0' for digit in binary_str[mid+1:])
    if binary_str[:mid] != flipped_right[::-1]:
        return 'NO'
    return is_symmetric(binary_str[:mid])

count = int(input())
for _ in range(count):
    print(is_symmetric(input()))
