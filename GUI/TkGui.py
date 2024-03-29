import webbrowser
from tkinter import *
import tkinter.messagebox
import pymysql
from pyecharts.globals import ThemeType
from sklearn import linear_model
from pyecharts.charts import Line, Bar
from pyecharts import options as opts


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
        self.button = Button(frame, text="排名预测", command=self.show)
        self.button.grid(row=4, column=1, sticky=E)
        self.button2 = Button(frame, text="退出程序", command=frame.quit)
        self.button2.grid(row=7, column=1, sticky=E)
        self.button3 = Button(frame, text="查看分数", command=self.showScore)
        self.button3.grid(row=6, column=1, sticky=E)
        self.button4 = Button(frame, text="查看排名", command=self.showRank)
        self.button4.grid(row=5, column=1, sticky=E)

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
        sql = "select ranks from 2016Rank where province = " + "\"" + self.getProvince() + "\"" + " and (highscore >= %s and lowscore <= %s);" % (
            self.getScore(), self.getScore())
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
        sql = "select ranks from 2017Rank where province = " + "\"" + self.getProvince() + "\"" + " and (highscore >= %s and lowscore <= %s);" % (
            self.getScore(), self.getScore())
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
        sql = "select ranks from 2018Rank where province = " + "\"" + self.getProvince() + "\"" + " and (highscore = %s or lowscore = %s);" % (
            self.getScore(), self.getScore())
        try:
            cursor.execute(sql)
            data2018 = cursor.fetchall()
            return data2018
        except Exception as e:
            print(e)
            conn.rollback()
        conn.close()

    def Forecast(self):
        x = [[2016], [2017], [2018]]
        y = [[self.Query2016Rank()[0][0]], [self.Query2017Rank()[0][0]], [self.Query2018Rank()[0][0]]]
        model = linear_model.LinearRegression()
        model.fit(x, y)
        rank2019 = model.predict([[2019]])
        print("预测2019年被录取的最低名次为：{:.2f}".format(rank2019[0][0]))
        return rank2019

    def Forecast2(self):
        x = [[2016], [2017], [2018]]
        y = [[self.Query2016()[0][0]], [self.Query2017()[0][0]], [self.Query2018()[0][0]]]
        model = linear_model.LinearRegression()
        model.fit(x, y)
        rank2019 = model.predict([[2019]])
        print("预计您2019年的名次为：{:.2f}".format(rank2019[0][0]))
        return rank2019

    def Query2016Rank(self):
        conn = pymysql.connect(host='localhost',
                               user='root',
                               password='591586',
                               db='zs',
                               charset='utf8')
        cursor = conn.cursor()
        sql = "select ranks from 2016Rank where province = " + "\"" + self.getProvince() + "\"" + " and (highscore >= %s and lowscore <= %s);" % (
            self.QueryMajor()[2][1], self.QueryMajor()[2][1])
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
        sql = "select ranks from 2017Rank where province = " + "\"" + self.getProvince() + "\"" + " and (highscore >= %s and lowscore <= %s);" % (
            self.QueryMajor()[1][1], self.QueryMajor()[1][1])
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
        sql = "select ranks from 2018Rank where province = " + "\"" + self.getProvince() + "\"" + " and (highscore >= %s and lowscore <= %s);" % (
            self.QueryMajor()[0][1], self.QueryMajor()[0][1])
        try:
            cursor.execute(sql)
            rank2018 = cursor.fetchall()
            return rank2018
        except Exception as e:
            print(e)
            conn.rollback()
        conn.close()

    def show(self):
        s1 = self.ent1.get()
        s2 = self.ent2.get()
        s3 = self.ent3.get()
        if s1 == '' or s2 == '' or s3 == '':
            tkinter.messagebox.askretrycancel('格式非法', '请检查是否有未输入数据')
        else:
            self.Forecast()
            self.Forecast2()
            tkinter.messagebox.askokcancel('排名预测', '预计2019年被录取的最低名次为：' + str(
                '{:.2f}'.format(self.Forecast()[0][0])) + '\n预计您2019年的名次为：' + str(
                '{:.2f}'.format(self.Forecast2()[0][0])))
            self.draw()
            self.drawRank()

    def draw(self):
        columns = [self.QueryMajor()[2][0], self.QueryMajor()[1][0], self.QueryMajor()[0][0]]
        data1 = [int(self.QueryMajor()[2][1]), int(self.QueryMajor()[1][1]), int(self.QueryMajor()[0][1])]
        bar = (
            Line(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
                .add_xaxis(columns)
                .add_yaxis('分数', data1)
                .set_global_opts(title_opts=opts.TitleOpts(title="心仪专业的分数线以及排名"))
        )
        bar.render(path='./score.html')

    def drawRank(self):
        columns = [self.QueryMajor()[2][0], self.QueryMajor()[1][0], self.QueryMajor()[0][0]]
        data2 = [int(self.Query2016Rank()[0][0]), int(self.Query2017Rank()[0][0]), int(self.Query2018Rank()[0][0])]
        bar = (
            Line(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
                .add_xaxis(columns)
                .add_yaxis('排名', data2)
                .set_global_opts(title_opts=opts.TitleOpts(title="心仪专业的分数线以及排名"))
        )
        bar.render(path='./rank.html')

    def showScore(self):
        webbrowser.open_new_tab('score.html')
    def showRank(self):
        webbrowser.open_new_tab('rank.html')


if __name__ == '__main__':
    root = Tk()
    root.title("大连东软信息学院报考小助手")
    root.geometry('480x240')
    app = Query(root)
    root.mainloop()
