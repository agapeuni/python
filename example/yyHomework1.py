def min_member(dic):
    max_value = max(dic.values())
    key_list = list(dic.keys())
    for key, val in dic.items():
        if val == max_value:
            return key, val


first_list = [1, 5, 6, 8, 10, 7, 4, 9, 4, 8, 4]
result_list = []
result_dic = {}


for val in first_list:
    if val not in result_list:
        result_list.append(val)
    else:
        if val in result_dic:
            result_dic[val] = result_dic[val] + 1
        else:
            result_dic[val] = 2

key, cnt = min_member(result_dic)

print("처음 리스트 :", first_list)
print("중복 제거 후 리스트 : ", result_list)
print("가장 많이 중복된 멤버중 최소멤버", key, ", 중복횟수:", cnt)