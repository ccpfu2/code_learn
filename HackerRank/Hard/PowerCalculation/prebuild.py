result = []
# 0**n is 0, do not care about the 1st list
# 1**n is 1, do not care about the 2nd list
for i in range(2,10):
    temp_list = []
    for j in range(55):
        if j == 0:
            temp_list.append(i)
        else:
            temp = temp_list[j-1]
            temp_list.append((temp * temp) % 100)
    result.append(temp_list)

print('[')
for l in result:
    print(f'{l},')
print(']')