n, m = map(int, input().split())
inputs = []

for _ in range(n*3):
    inputs.extend(input())

i = 0
while i < len(inputs):
    if inputs[i] not in ".*/":
        if i + 5 < len(inputs) and inputs[i+5] != ".":
            check = 1
            temp_result = str(int(inputs[i+4]) * 10 + int(inputs[i+5]))
            inputs[i+4] = temp_result[0]
            inputs[i+5] = temp_result[1] if len(temp_result) > 1 else ''
        else:
            check = 0
            temp_result = inputs[i+4]

        if int(inputs[i]) + int(inputs[i+2]) == int(temp_result):
            if check:
                inputs[i-1] = inputs[i+6] = '*'
                inputs[i-8*m:i-8*m+6] = ['*'] * 6
                inputs[i+8*m:i+8*m+6] = ['*'] * 6
            else:
                inputs[i-1] = inputs[i+5] = '*'
                inputs[i-8*m:i-8*m+5] = ['*'] * 5
                inputs[i+8*m:i+8*m+5] = ['*'] * 5
        else:
            inputs[i+1] = inputs[i-8*m+2] = inputs[i+8*m] = '/'

        i += 1 
        if check:
            i += 5
        else:
            i += 4

    i += 1 

for i in range(3*n):
    print(''.join(inputs[8*m*i:8*m*(i+1)]))
