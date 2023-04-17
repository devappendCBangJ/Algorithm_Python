N = int(input())
output = 0

for i in range(N+1):
    for j in range(60):
        for k in range(60):
            if ('3' in str(i)) or ('3' in str(j)) or ('3' in str(k)):
                output += 1

print(output)