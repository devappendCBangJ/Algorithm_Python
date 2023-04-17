input_coor = input()

# ---------------------------------------------------
# dictionary : zip 활용해서 호율성 증가
# ---------------------------------------------------
# alpha_to_num = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
# -> alpha_to_num = dict(zip('abcdefg', range(1, 9)))
# ---------------------------------------------------

small_itv_to_output = {'0':2, '1':4, '2':4}
big_itv_to_output = {'0':4, '1':6, '2':8}

# ---------------------------------------------------
# 알파벳 -> 숫자 : ord 활용
# ---------------------------------------------------
# coor = [alpha_to_num[input_coor[0]], int(input_coor[1])]
coor = [ord(input_coor[0]) - ord('a') + 1, int(input_coor[1])]
# ---------------------------------------------------
if (coor[0] - 1) + (coor[1] - 1) <= (8 - coor[0]) + (8 - coor[1]):
    ix, iy = (coor[0] - 1), (coor[1] - 1)
else:
    ix, iy = (8 - coor[0]), (8 - coor[1])
# print(ix, iy)

if ix+iy <= 2:
    output = small_itv_to_output[str(ix+iy)]
else:
    if min(ix, iy) <= 1:
        output = big_itv_to_output[str(min(ix, iy))]
    else:
        output = big_itv_to_output['2']

print(output)