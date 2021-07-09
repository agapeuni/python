import matplotlib.pyplot as plt

plt.rc('font', family='gulim')

sido = ['서울', '부산', '대구', '인천', '광주', '대전', '울산', '세종',
        '경기', '강원', '충북', '충남', '전북', '전남', '경북', '경남', '제주']
count = [9911088, 3438710, 2446144, 3010476, 1471385, 1480777, 1153901, 360907,
         13807158, 1560172, 1637897, 2185575, 1835392, 1884455, 2691891, 3407455, 697578]

plt.figure(figsize=(10, 5))
xtick_label_position = list(range(len(sido)))
plt.xticks(xtick_label_position, sido)

plt.bar(xtick_label_position, count, color='blue')

plt.title('시도별 인구수', fontsize=15)
plt.xlabel('시도')
plt.ylabel('인구수')
plt.show()
