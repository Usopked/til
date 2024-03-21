a = input()
num = input()
nnum = [num[i:i+6] for i in range(0, len(num), 6)]
arr = []
for i in nnum:
    if i == '000000' or i == '100000' or i == '010000' or i == '001000' or i == '000100' or i == '000010' or i == '000001':
        arr.append('A')
    elif i == '001111' or i == '101111' or i == '011111' or i == '000111' or i == '001011' or i == '001101' or i == '001110':
        arr.append('B')
    elif i == '010011' or i == '110011' or i == '000011' or i == '011011' or i == '010111' or i == '010001' or i == '010010':
        arr.append('C')
    elif i == '011100' or i == '111100' or i == '001100' or i == '010100' or i == '011000' or i == '011110' or i == '011101':
        arr.append('D')
    elif i == '100110' or i == '000110' or i == '110110' or i == '101110' or i == '100010' or i == '100100' or i == '100111':
        arr.append('E')
    elif i == '101001' or i == '001001' or i == '111001' or i == '100001' or i == '101101' or i == '101011' or i == '101000':
        arr.append('F')
    elif i == '110101' or i == '010101' or i == '100101' or i == '111101' or i == '110001' or i == '110111' or i == '110100':
        arr.append('G')
    elif i == '111010' or i == '011010' or i == '101010' or i == '110010' or i == '111110' or i == '111000' or i == '111011':
        arr.append('H')
    else:
        arr.append('Z')
        break
if 'Z' in arr:
    print(len(arr))
else:
    arr = ''.join(map(str, arr))
    print(arr)