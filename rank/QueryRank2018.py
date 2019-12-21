import requests
from bs4 import BeautifulSoup
import pymysql
import re


def DBQuery():
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='591586',
                           db='zs',
                           charset='utf8')
    cursor = conn.cursor()
    sql = 'select province, href from 2018href'
    try:
        cursor.execute(sql)
        data = cursor.fetchall()
    except Exception as e:
        print(e)
        conn.rollback()
    conn.close()
    return data


def Geturl():
    for row in DBQuery():
        res = requests.get(row[1])
        res.encoding = 'utf-8'
        html = res.text
        soup = BeautifulSoup(html, "html.parser").find_all("tr")
        info = []
        infos = []
        # print(row[0])
        # print(row[1])
        for tr in soup:
            tdList = []
            for j in tr:
                tdList.append(j.string)
            if tdList != []:
                if None not in tdList:
                    info.append(tdList)
        for i in range(0, len(info)):
            # print(' '.join(info[i]).replace('\t','').replace('\r','').replace('\n','').strip())
            infos.append(' '.join(info[i]).replace('\t', '').replace('\r', '').replace('\n', '').strip())
        # infos = [re.findall(r'\d+|[→]', infos[i]) for i in range(len(infos))]
        infos = [re.findall(r'\d+|[\d+][→][\d+]', infos[i]) for i in range(len(infos))]
        for info in infos:
            for j in info:
                if j == '2018':
                    info.remove(j)

        while [] in infos:
            infos.remove([])
        # if infos != [] and infos is not None:
        #     print(infos)
        rankList = []
        ranksList = []
        for info in infos:
            # print(info)
            if len(info) == 4:
                rankList.append(row[0])
                rankList.append(info[1])
                rankList.append(info[1])
                rankList.append(info[3])
            elif len(info) == 3 and infos[0][0] == '1':
                rankList.append(row[0])
                rankList.append(info[1])
                rankList.append(info[1])
                rankList.append(info[2])
            elif len(info) == 3:
                rankList.append(row[0])
                rankList.append(info[0])
                rankList.append(info[0])
                rankList.append(info[2])
            elif len(info) == 2:
                rankList.append(row[0])
                rankList.append(info[0])
                rankList.append(info[0])
                rankList.append(info[1])
            elif len(info) == 5:
                rankList.append(row[0])
                rankList.append(info[1])
                rankList.append(info[2])
                rankList.append(info[4])

        for i in range(0, len(rankList), 4):
            b = rankList[i:i + 4]
            ranksList.append(b)
        if ranksList != []:
            yield ranksList

def DBInsert(list):
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='591586',
                           db='zs',
                           charset='utf8')
    cursor = conn.cursor()
    try:
        for l in list:
            for i in l:
                sql = "insert into 2018Rank(province, highscore, lowscore, ranks) values('%s', '%s', '%s', '%s')"%(i[0], i[1], i[2], i[3])
                print(sql)
                cursor.execute(sql)
                conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()

if __name__ == '__main__':
    # print(Geturl())
    DBInsert(Geturl())
    # for l in Geturl():
    #     for i in l:
    #         print(','.join(i))