from tkinter import *
import pymysql
import numpy
from sklearn.linear_model import LinearRegression

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
        self.button = Button(frame, text="查询", command=self.Submit)
        self.button.grid(row=3, column=1, sticky=E)
        self.lab4 = Label(frame, text="")
        self.lab4.grid(row=4, column=0, sticky=W)
        self.button2 = Button(frame, text="退出", command=frame.quit)
        self.button2.grid(row=4, column=3, sticky=E)

    def Submit(self):
        s1 = self.ent1.get()
        s2 = self.ent2.get()
        s3 = self.ent3.get()
        if s1 == '' or s2 == '' or s3 == '':
            self.lab4['text'] = '请检查是否有空'
        else:
            db = pymysql.connect(host='localhost',
                                 user='root',
                                 password='591586',
                                 database='zs',
                                 port=3306,
                                 charset='utf8'
                                 )
            cursor = db.cursor()
            sql = "select year, province, major, score from zsinfo where province = " + "\"" + s1 + "\"" + "and major = " + "\"" +s2 + "\";"
            print(sql)
            try:
                cursor.execute(sql)
                result = cursor.fetchall()
                for row in result:
                    print(row)
                    print(type(row))
            except Exception as e:
                print(e)
                db.rollback()
            self.lab4["text"] = [row for row in result]


root = Tk()
root.title("大连东软信息学院报考小助手")
root.geometry('800x480')
app = Query(root)
root.mainloop()
