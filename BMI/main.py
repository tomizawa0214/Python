"""
BMI ボディマス指数計算
"""

from tkinter import *

class App(Frame):
    """tkinterのFrameクラスを継承して作成"""

    def __init__(self, master=None):
        # Frameクラスのコンストラクタを呼ぶ
        super() .__init__(master, padx=10, pady=10)
        # root (masterはrootを代入) にpackして配置
        # packはウィジェットを行または列に配置
        # この場合rootの真ん中にFrameウィジェットが配置された状態
        self.pack()

        # 最初とリセットを押した時に表示する文字列
        self.initial = "身長と体重を入力して\nボタンを押してください"
        # self.lab6で使う文字列変数を設定
        self.var1 = StringVar()
        # 最初はself.initialを代入
        self.var1.set(self.initial)

        # 以降、Frameにウィジェットをgridで配置
        self.lab1 = Label(self, text="BMI ボディマス指数計算")
        self.lab1.grid(row=0, column=0, columnspan=4)

        self.lab2 = Label(self, text="身長")
        self.lab2.grid(raw=1, column=0)

        # Entryウィジェットはテキスト入力 justify=RIGHTで右寄せにしている
        self.ent1 = Entry(self, justify=RIGHT)
        self.ent1.grid(row=1, column=1, columnspan=2)
        # 最初にent1にフォーカスされる
        self.ent1.focus()
        # bindメソッドでEnterボタンを押したときにもself.calcを呼び出す
        self.ent1.bind("<Return>", self.calc)

        self.lab4 = Label(self, text="cm")
        self.lab4.grid(row1, column=3)

        self.lab3 = Label(self, text="体重")
        self.lab3.grid(row=2, column=0)

        self.ent2 = Entry(self, justify=RIGHT)
        self.ent2.grid(row=2, column=1, columnspan=2)
        # bindメソッドでEnterボタンを押したときにもself.calcを呼び出す
        self.ent2.bind("<Return>", self.calc)

        self.lab5 = Label(self, text="kg")
        self.lab5.grid(row=2, column=3)

        #ボタンを押したときにself.calcメソッドを呼ぶ
        self.btn1 = Button(self, text="計算", command=self.calc)
        self.btn1.grid(row=3, column=2)

        # textvariableでself.var1が変わればLabelのテキストも変わる
        self.lab6 = Label(self, textvariable=self.var1)
        self.lab6.grid(row4, column=0, columnspan=4)

        # PhotoImageのオブジェクトを作成
        self.img = PhotoImage(file="img/measurement.jpg")

        # image=self.imgでPhotoImageのオブジェクトを表示させる
        self.lab7 = Label(self, image=self.img)
        self.lab7.grid(row=5, column=0, columnspan=4)

    def calc(self, _=None):
        """計算ボタンが押されたら発動
        Buttonのcommandとbindから呼ばれる
        bindの場合event引数も受けなければいけないが
        このメソッドでは使わないので_Noneにしている
        何が入力されるかわからないのでtry～exceptで例外処理"""