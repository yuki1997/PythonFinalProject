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
    sql = 'select href from 2016href'
    try:
        cursor.execute(sql)
        data = cursor.fetchall()
    except Exception as e:
        print(e)
        conn.rollback()
    conn.close()
    return data


def DBQuery2():
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='591586',
                           db='zs',
                           charset='utf8')
    cursor = conn.cursor()
    sql = 'select province from 2016href'
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
        res = requests.get(row[0])
        res.encoding = 'utf-8'
        html = res.text
        soup = BeautifulSoup(html, "html.parser").find_all("tr")
        info = []
        infos = []
        print(row[0])
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
                if j == '2016':
                    info.remove(j)

        while [] in infos:
            infos.remove([])
        # if infos is not None:
        #     print(infos)
        # for i in range(0, len(info)):
        # print(info[i])
        # if info[i] == '→':

        # info = [j.strip() for i in info for j in i if j.strip() != '']
        # info = [re.findall(r'\d+|[→]', info[i]) for i in range(len(info))]
        # info = [j.strip() for i in info for j in i if j.strip() != '2017']
        # print(info)
        # if info[0] == '1':
        #     print('error')
        # i = 0
        # s1 = []
        # for i in info:
        #     if i == '→':

        # if int(info[0]) > 100 and int(info[2]) < 100:
        #     for i in range(0, len(info), 3):
        #         b = info[i: i + 3]
        #         s1.append(b)
        # elif int(info[0]) > 100:
        #     for i in range(0, len(info), 2):
        #         b = info[i: i + 2]
        #         s1.append(b)
        # elif info[0] == '1' and info[3] == '2':
        #     for i in range(0, len(info), 3):
        #         b = info[i:i + 3]
        #         s1.append(b)
        # elif info[0] == '1':
        #     for i in range(0, len(info), 4):
        #         b = info[i:i + 4]
        #         s1.append(b)
        # else:
        #     for i in range(0, len(info), 3):
        #         b = info[i:i + 3]
        #         s1.append(b)
        # if s1 is not None:
        #     print(s1)
        print(infos)
if __name__ == '__main__':
    print(Geturl())
