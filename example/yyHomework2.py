list = [91, -60, -32, -77, 5, -75, 70, 22, 19, -97]

avr = sum(list) / len(list)
print("평균", avr)

list2 = [i for i in list]

list2.sort()
newList1 = [x for x in list2 if x < avr]
print("작은 멤버 모음", newList1)

list2.sort(reverse=True)
newList2 = [x for x in list2 if x > avr]
print("큰 멤버 모음", newList2)

print("처음 리스트", list)