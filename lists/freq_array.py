arr = [100, 200, 300, 110, 210, 200, 110, 110, 100]

freq_num = []

for num in arr:

    occ = 0

    for num1 in arr:

        if num == num1:
            occ += 1

        if occ > 1 and num not in freq_num:
            freq_num.append(num)
            break


    # if num not in freq_num:

    #     if arr.count(num) > 1:
    #         freq_num.append(num)
        

print(freq_num)