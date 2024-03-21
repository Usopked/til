sum = 0
score = 0
for _ in range(20):
    a, b, c = map(str, input().split())
    sum += float(b)
    match c:
        case 'A+':
            score += 4.5 * float(b)
        case 'A0':
            score += 4.0 * float(b)
        case 'B+':
            score += 3.5 * float(b)
        case 'B0':
            score += 3.0 * float(b)
        case 'C+':
            score += 2.5 * float(b)
        case 'C0':
            score += 2.0 * float(b)
        case 'D+':
            score += 1.5 * float(b)
        case 'D0':
            score += 1.0 * float(b)
        case 'F':
            score += 0.0 * float(b)
        case 'P':
            sum -= float(b)
            
print(round(score/sum, 6))