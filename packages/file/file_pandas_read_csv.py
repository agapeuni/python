# https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html#pandas.read_csv

import pandas as pd

# Pandas는 파이썬에서 사용하는 데이터분석 라이브러리로,
# 행과 열로 이루어진 데이터 객체를 만들어 다룰 수 있으며
# 데이터들을 보다 편리하게 처리할 수 있습니다.

# input.csv 파일 내용
'''
No, Code, Name
01, A1, connector
02, B2, battery
03, C3, motor
04, D4, button
'''

# to_csv 함수를 사용하여 파일읽어 DataFrame으로 전달한다.
# 구분자는 기본으로 ',' (sep=',')
cvs_data = pd.read_csv('input.csv')
print(cvs_data)
print()
'''
No Code Name
0 1 A1 connector
1 2 B2 battery
2 3 C3 motor
3 4 D4 button
'''

# 구분자를 공백으로 지정
cvs_data = pd.read_csv('input.csv', sep=' ')
print(cvs_data)
print()
'''
No, Code, Name
0 01, A1, connector
1 02, B2, battery
2 03, C3, motor
3 04, D4, button
'''

# 헤더 None으로 설정하면 열이름으로 자동으로 만든다.
cvs_data = pd.read_csv('input.csv', header=None)
print(cvs_data)
print()
'''
0 1 2
0 No Code Name
1 01 A1 connector
2 02 B2 battery
3 03 C3 motor
4 04 D4 button
'''

# 헤더를 0로 지정
cvs_data = pd.read_csv('input.csv', header=0)
print(cvs_data)
print()
'''
No Code Name
0 1 A1 connector
1 2 B2 battery
2 3 C3 motor
3 4 D4 button
'''

# 헤더를 1로 지정
cvs_data = pd.read_csv('input.csv', header=1)
print(cvs_data)
print()
'''
01 A1 connector
0 2 B2 battery
1 3 C3 motor
2 4 D4 button
'''

# 열이름을 지정
# CVS 파일에 헤더행이 포함 된 경우 명시적으로 header=0으로 설정하여 열이름을 재정의할 수 있다.
cvs_data = pd.read_csv('input.csv', header=0, names=['번호', '문자', '메모'])
print(cvs_data)
print()
'''
번호 문자 메모
0 1 A1 connector
1 2 B2 battery
2 3 C3 motor
3 4 D4 button
'''