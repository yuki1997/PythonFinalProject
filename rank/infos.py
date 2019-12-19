import requests, xlwt
from bs4 import BeautifulSoup


def Geturl(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print("请求成功！")
        return r.text
    except:
        print("请求失败，请检查网络.....")


def GetInfo(html1, html2):
    soup1 = BeautifulSoup(html1, "html.parser").find_all("tr")
    soup2 = BeautifulSoup(html2, "html.parser").find_all("tr")
    info1 = []
    info2 = []
    # 拿理科一份一段表存入列表
    for i in soup1:
        l = []
        for j in i:
            l.append(j.string)
        if l != []:
            info1.append(l)
    # 拿文科一分一段表
    for i in soup2:
        l = []
        for j in i:
            l.append(j.string)
        if l != []:
            info2.append(l)
    file = xlwt.Workbook(encoding='urf-8')
    print("正在写入Excel四川省理科一分一段表.....")
    table1 = file.add_sheet("四川省2017年理科一分一段表")
    for i in range(len(info1)):
        for j in range(len(info1[i])):
            table1.write(i, j, info1[i][j])
    print("正在写入Excel四川省文科一分一段表.....")
    table2 = file.add_sheet("四川省2017年文科一分一段表")
    for i in range(len(info2)):
        for j in range(len(info2[i])):
            table2.write(i, j, info2[i][j])
    file.save("四川省一分一段表.xls")
    print("数据写入成功！")


def main():
    url = "http://www.creditsailing.com/GaoKaoZhiYuan/666259.html"
    url2 = "http://www.creditsailing.com/GaoKaoZhiYuan/666260.html"
    html1 = Geturl(url)
    html2 = Geturl(url2)
    GetInfo(html1, html2)


if __name__ == '__main__':
    main()
