from tkinter import *
import pymysql
import numpy
from sklearn import linear_model
import matplotlib


class Query(Frame):
    def __init__(self, window):
        frame = Frame(window)
        frame.pack()
        self.lab1 = Label(frame, text="省份:")
        self.lab1.grid(row=0, column=0, sticky=W)
        self.ent1 = Entry(frame)
        self.ent1.grid(row=0, column=1, sticky=W)
        self.lab2 = Label(frame, text="专业:")
        self.lab2.grid(row=1, column=0)
        self.ent2 = Entry(frame)
        self.ent2.grid(row=1, column=1, sticky=W)
        self.lab3 = Label(frame, text="分数")
        self.lab3.grid(row=2, column=0)
        self.ent3 = Entry(frame)
        self.ent3.grid(row=2, column=1, sticky=W)
        self.lab4 = Label(frame, text="科类")
        self.lab4.grid(row=3, column=0)
        self.ent4 = Entry(frame)
        self.ent4.grid(row=3, column=1, sticky=W)
        self.button = Button(frame, text="查询", command=self.Submit)
        self.button.grid(row=4, column=1, sticky=E)
        self.lab5 = Label(frame, text="")
        self.lab5.grid(row=5, column=0, sticky=W)
        self.button2 = Button(frame, text="退出", command=frame.quit)
        self.button2.grid(row=5, column=3, sticky=E)

    def getProvince(self):
        province = self.ent1.get()
        return province + self.getSubject()

    def getMajor(self):
        major = self.ent2.get()
        return major

    def getScore(self):
        score = self.ent3.get()
        return score

    def getSubject(self):
        subject = self.ent4.get()
        return subject

    def QueryMajor(self):
        conn = pymysql.connect(host='localhost',
                               user='root',
                               password='591586',
                               db='zs',
                               charset='utf8')
        cursor = conn.cursor()
        sql = "select year, score from zsinfo where province = " + "\"" + self.ent1.get() + "\"" + "and major = " + "\"" + self.getMajor() + "\"; "
        try:
            cursor.execute(sql)
            data2016 = cursor.fetchall()
            return data2016
        except Exception as e:
            print(e)
            conn.rollback()
        conn.close()


    def Query2016(self):
        conn = pymysql.connect(host='localhost',
                               user='root',
                               password='591586',
                               db='zs',
                               charset='utf8')
        cursor = conn.cursor()
        sql = "select highscore, lowscore, ranks from 2016Rank where province = " +"\"" + self.getProvince() + "\"" + " and (highscore >= %s and lowscore <= %s);"%(self.getScore(), self.getScore())
        try:
            cursor.execute(sql)
            data2016 = cursor.fetchall()
            return data2016
        except Exception as e:
            print(e)
            conn.rollback()
        conn.close()


    def Query2017(self):
        conn = pymysql.connect(host='localhost',
                               user='root',
                               password='591586',
                               db='zs',
                               charset='utf8')
        cursor = conn.cursor()
        sql = "select highscore, lowscore, ranks from 2017Rank where province = " +"\"" + self.getProvince() + "\"" + " and (highscore >= %s and lowscore <= %s);"%(self.getScore(), self.getScore())
        try:
            cursor.execute(sql)
            data2017 = cursor.fetchall()
            return data2017
        except Exception as e:
            print(e)
            conn.rollback()
        conn.close()


    def Query2018(self):
        conn = pymysql.connect(host='localhost',
                               user='root',
                               password='591586',
                               db='zs',
                               charset='utf8')
        cursor = conn.cursor()
        sql = "select highscore, lowscore, ranks from 2018Rank where province = " +"\"" + self.getProvince() + "\"" + " and (highscore = %s or lowscore = %s);"%(self.getScore(), self.getScore())
        try:
            cursor.execute(sql)
            data2018 = cursor.fetchall()
            return data2018
        except Exception as e:
            print(e)
            conn.rollback()
        conn.close()


    def Forecast(self):
        rank = []
        mininumScore = []
        if len(self.Query2016()) > 0 and len(self.Query2017()) > 0 and len(self.Query2018()) > 0:
            rank.append(self.Query2016()[0][2])
            rank.append(self.Query2017()[0][2])
            rank.append(self.Query2018()[0][2])
        mininumScore.append(self.QueryMajor()[0][1])
        mininumScore.append(self.QueryMajor()[1][1])
        mininumScore.append(self.QueryMajor()[2][1])
        print(self.Query2016Rank())
        print(self.Query2017Rank())
        print(self.Query2018Rank())


    def Query2016Rank(self):
        conn = pymysql.connect(host='localhost',
                               user='root',
                               password='591586',
                               db='zs',
                               charset='utf8')
        cursor = conn.cursor()
        sql = "select ranks from 2016Rank where province = " +"\"" + self.getProvince() + "\"" + " and (highscore >= %s and lowscore <= %s);"%(self.QueryMajor()[2][1], self.QueryMajor()[2][1])
        print(sql)
        try:
            cursor.execute(sql)
            rank2016 = cursor.fetchall()
            return rank2016
        except Exception as e:
            print(e)
            conn.rollback()
        conn.close()

    def Query2017Rank(self):
        conn = pymysql.connect(host='localhost',
                               user='root',
                               password='591586',
                               db='zs',
                               charset='utf8')
        cursor = conn.cursor()
        sql = "select ranks from 2017Rank where province = " +"\"" + self.getProvince() + "\"" + " and (highscore >= %s and lowscore <= %s);"%(self.QueryMajor()[1][1], self.QueryMajor()[1][1])
        print(sql)
        try:
            cursor.execute(sql)
            rank2017 = cursor.fetchall()
            return rank2017
        except Exception as e:
            print(e)
            conn.rollback()
        conn.close()

    def Query2018Rank(self):
        conn = pymysql.connect(host='localhost',
                               user='root',
                               password='591586',
                               db='zs',
                               charset='utf8')
        cursor = conn.cursor()
        sql = "select ranks from 2018Rank where province = " +"\"" + self.getProvince() + "\"" + " and (highscore = %s or lowscore = %s);"%(self.QueryMajor()[0][1], self.QueryMajor()[0][1])
        print(sql)
        try:
            cursor.execute(sql)
            rank2018 = cursor.fetchall()
            return rank2018
        except Exception as e:
            print(e)
            conn.rollback()
        conn.close()

    def Submit(self):
        s1 = self.ent1.get()
        s2 = self.ent2.get()
        s3 = self.ent3.get()
        if s1 == '' or s2 == '' or s3 == '':
            self.lab5['text'] = '请检查是否有空'
        else:
            db = pymysql.connect(host='localhost',
                                 user='root',
                                 password='591586',
                                 database='zs',
                                 port=3306,
                                 charset='utf8'
                                 )
            cursor = db.cursor()
            sql = "select year, score from zsinfo where province = " + "\"" + s1 + "\"" + "and major = " + "\"" + s2 + "\"; "
            rows = []
            try:
                cursor.execute(sql)
                result = cursor.fetchall()
                for row in result:
                    rows.append(row)
            except Exception as e:
                print(e)
                db.rollback()

            self.lab5["text"] = '您被录取的概率为：'
            self.Forecast()


if __name__ == '__main__':
    root = Tk()
    root.title("大连东软信息学院报考小助手")
    root.geometry('480x240')
    app = Query(root)
    root.mainloop()
