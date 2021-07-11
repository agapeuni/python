import datetime
import pandas as pd
import requests
from bs4 import BeautifulSoup

main_url = "https://www.dhlottery.co.kr/gameResult.do?method=byWin" # 마지막 회차를 얻기 위한 주소
basic_url = "https://www.dhlottery.co.kr/gameResult.do?method=byWin&drwNo=" # 임의의 회차를 얻기 위한 주소

# 마지막 회차 정보를 가져옴
def GetLast():     
    resp = requests.get(main_url)    
    soup = BeautifulSoup(resp.text, "lxml")
    result = str(soup.find("meta", {"id" : "desc", "name" : "description"})['content'])
    s_idx = result.find(" ")
    e_idx = result.find("회")    
    return int(result[s_idx + 1 : e_idx])

'''
text: 웹 데이터 문자형(string)
ranking: 찾을 등수
startIndex: 시작 위치
'''
def getMoney(text, ranking, startIndex):
    rankingTag = '{}등'.format(ranking)    
    s_idx = text.find(rankingTag, startIndex) + 2
    e_idx = text.find("원", s_idx) + 1
    e_idx = text.find("원", e_idx)

    # '원'과 ',' 는 제거
    splitItem = text[s_idx:e_idx].strip().replace(',','').replace('원','').split()
    # 첫번째 총 당첨금액
    totalMoney = splitItem[0]
    # 두번째 당첨자 수
    totalNumber = splitItem[1]
    # 세번째 1인당 당첨금액
    money = splitItem[2] 
    return (totalMoney, totalNumber, money, e_idx)

# 지정된 파일에 지정된 범위의 회차 정보를 기록함
def Crawler(s_count, e_count, fp):
    title = '회차,번호1,번호2,번호3,번호4,번호5,번호6,보너스,1등당첨총금액,1등당첨금액,1등당첨자수,2등당첨총금액,2등당첨금액,2등당첨자수,3등당첨총금액,3등당첨금액,3등당첨자수,4등당첨총금액,4등당첨금액,4등당첨자수,5등당첨총금액,5등당첨금액,5등당첨자수'
    title += '\n'
    fp.write(title)
    for i in range(s_count , e_count + 1):
        '''
        https://www.dhlottery.co.kr/gameResult.do?method=byWin&drwNo=1
        https://www.dhlottery.co.kr/gameResult.do?method=byWin&drwNo=2
        https://www.dhlottery.co.kr/gameResult.do?method=byWin&drwNo=3
        ...        
        https://www.dhlottery.co.kr/gameResult.do?method=byWin&drwNo=850
        https://www.dhlottery.co.kr/gameResult.do?method=byWin&drwNo=851
        '''
        crawler_url = basic_url + str(i)
        # 페이지 얻기
        resp = requests.get(crawler_url)
        # 파싱!
        soup = BeautifulSoup(resp.text, "html.parser")
        # 텍스트 가져오기
        text = soup.text
        # 텍스트에서 '당첨결과'라는 문자를 찾아 위치를 반환한다.
        s_idx = text.find(" 당첨결과")        
        # '당첨결과' 위치부터 '당첨번호' 위치를 찾고 거기에 + 4를 한다.
        s_idx = text.find("당첨번호", s_idx) + 4
        # '당첨번호'위치 + 4 즉, '당첨번호' 끝 위치부터 '보너스'를 위치를 찾는다.
        e_idx = text.find("보너스", s_idx)
        # 담청번호 끝지점부터 보너스 위치안에 있는 문자열을 찾는다.
        '''
        10
        23
        29
        33
        37
        40 

        '''
        # 위와 같은 데이터를 공백을 제거후 자른다.
        numbers = text[s_idx:e_idx].strip().split()
        # '보너스' 시작점을 가지고 있는 e_idx에서 + 3 '보너스' 끝 위치를 s_idx로
        s_idx = e_idx + 3
        # s_idx 부터 + 3을 e_idx로
        e_idx = s_idx + 3
        # 이것을 공백제거하면 보너스 숫자
        bonus = text[s_idx:e_idx].strip()

        # 등수별 당첨금액 정보 가져오기
        totalMoney =  [None] * 5
        totalNumber =  [None] * 5
        money =  [None] * 5    
        for idx in range(5):
            ranking = idx + 1
            totalMoney[idx], totalNumber[idx], money[idx], e_idx = getMoney(text, ranking, e_idx)

        # 파일에 저장하기 위해 문자열로 만듬
        line = str(i) + ',' + numbers[0] + ',' + numbers[1] + ',' + numbers[2] + ',' + numbers[3] + ',' + numbers[4] + ',' + numbers[5] + ',' + bonus + ','         
        for idx in range(5):            
            line += totalMoney[idx] + ',' +  money[idx] + ',' + totalNumber[idx]
            if idx != 4:
                line += ','
        print(line) # 디버깅용        
        line += '\n'
        fp.write(line)

last = GetLast() # 마지막 회차를 가져옴
file_name = '{}_lotto_1_to_{}_data.csv'.format(datetime.datetime.now().strftime('%Y-%m-%d'), last)
print(file_name)

with open(file_name, 'w', encoding='utf-8') as fp:
    # 처음부터 마지막 회차까지 저장
    Crawler(1, last, fp)