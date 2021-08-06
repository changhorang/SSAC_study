nums = [273, 103, 5, 32, 65, 9, 72, 800, 99]

# 홀/짝
# for num in nums:
#     if num % 2 == 0:
#         print("{}는 짝수".format(num))
#     else:
#         print("{}는 홀수".format(num))
# for num in nums:
#     if num % 2 != 0:
#         j = "홀수"
#     else:
#         j = "짝수"
#     print("{}는 {}".format(num, j))

# # 자릿 수
# for num in nums:
#     print("{}는 {}자릿수".format(num, len(str((num)))))

list_of_list = [
    [1, 2, 3],
    [4, 5, 6, 7],
    [8, 9]
]

for i in range(9):
    print(list_of_list.pop(i))