#2와 5가 들어있지 않은 정수 n
#11, 111, 1111, 11111... 중 n의 배수를 찾아야 함
#1부터 + 10*i
while 1:
    try:
        num = int(input())
        i = 1; j = 1;
        while 1:
            if i%num==0: break;
            else: j = 10*j;
            i += j
        print(len(str(i)))
    except EOFError:
        break
    