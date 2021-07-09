import pandas as pd

data = {
'No': ['01', '02', '03', '04'],
'Code': ['A1', 'B2', 'C3', 'D4'],
'Name': ['connector', 'battery', 'motor', 'button']
}

# data를 DataFrame으로 변환
df = pd.DataFrame(data, index=['0', '1', '2', '3'])
print(df)
print()
"""
No Code Name
0 01 A1 connector
1 02 B2 battery
2 03 C3 motor
3 04 D4 button
"""

# CSV 저장 ('output1.csv')
df.to_csv('output1.csv', sep=',', columns = ['No', 'Code', 'Name'], index=False, header=True)
'''
No,Code,Name
01,A1,connector
02,B2,battery
03,C3,motor
04,D4,button
'''

# CSV 저장 ('output2.csv')
df.to_csv('output2.csv', sep='\t', columns = ['No', 'Code', 'Name'], index=True, header=False)
'''
0 01 A1 connector
1 02 B2 battery
2 03 C3 motor
3 04 D4 button
'''