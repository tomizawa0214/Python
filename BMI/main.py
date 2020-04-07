"""
BMI ボディマス指数計算
"""

import tkinter as tk

# import tkinter;print(tkinter.TkVersion)

class App(tk.Frame):
    """tkinterのFrameクラスを継承して作成"""

    def __init__(self, master=None):
        """コンストラクタ"""
        # Frameクラスのコンストラクタを呼ぶ
        super().__init__(master, padx=10, pady=10)
        # root (masterはrootを代入) にpackして配置
        # packはウィジェットを行または列に配置
        # この場合rootの真ん中にFrameウィジェットが配置された状態
        self.pack()

        # 最初とリセットを押した時に表示する文字列
        self.initial = "身長と体重を入力して\nボタンを押してください\n"
        # self.lab6で使う文字列変数を設定
        self.var1 = tk.StringVar()
        # self.var2 = tk.StringVar()
        # 最初はself.initialを代入
        self.var1.set(self.initial)
        # self.var2.set(self.initial)

        # 以降、Frameにウィジェットをgridで配置
        self.lab1 = tk.Label(self, text="BMI ボディマス指数計算")
        self.lab1.grid(row=0, column=0, columnspan=4)

        self.lab2 = tk.Label(self, text="身長")
        self.lab2.grid(row=1, column=0)

        # Entryウィジェットはテキスト入力 justify=tk.RIGHTで右寄せにしている
        self.ent1 = tk.Entry(self, justify=tk.RIGHT)
        self.ent1.grid(row=1, column=1, columnspan=2)
        # 最初にent1にフォーカスさせる
        self.ent1.focus()
        # bindメソッドでEnterボタンを押したときにもself.calcを呼び出す
        self.ent1.bind("<Return>", self.calc)

        self.lab4 = tk.Label(self, text="cm")
        self.lab4.grid(row=1, column=3)

        self.lab3 = tk.Label(self, text="体重")
        self.lab3.grid(row=2, column=0)

        self.ent2 = tk.Entry(self, justify=tk.RIGHT)
        self.ent2.grid(row=2, column=1, columnspan=2)
        # bindメソッドでEnterボタンを押したときにもself.calcを呼び出す
        self.ent2.bind("<Return>", self.calc)

        self.lab5 = tk.Label(self, text="kg")
        self.lab5.grid(row=2, column=3)

        # ボタンを押したときにself.calcメソッドを呼ぶ
        self.btn1 = tk.Button(self, text="計算", command=self.calc)
        self.btn1.grid(row=3, column=1)

        # ボタンを押したときにself.clearメソッドを呼ぶ
        self.btn2 = tk.Button(self, text="リセット", command=self.clear)
        self.btn2.grid(row=3, column=2)

        # textvariableでself.var1が変わればLabelのテキストも変わる
        self.lab6 = tk.Label(self, textvariable=self.var1, fg="black")
        # self.lab6 = tk.Label(self, textvariable=self.var1, fg="red")
        self.lab6.grid(row=4, column=0, columnspan=4)
        # self.lab9 = tk.Label(self, textvariable=self.var2, fg="red")
        # self.lab9.grid(row=4, column=0, columnspan=4)

        # PhotoImageのオブジェクトを作成
        self.img = tk.PhotoImage(file="BMI/img/measurement.png")

        # image=self.imgでPhotoImageのオブジェクトを表示させる
        self.lab7 = tk.Label(self, image=self.img)
        self.lab7.grid(row=5, column=0, columnspan=4)

    def calc(self, _=None):
        """計算ボタンが押されたら発動
        Buttonのcommandとbindから呼ばれる
        bindの場合event引数も受けなければいけないが
        このメソッドでは使わないので_=Noneにしている
        何が入力されるかわからないのでtry～exceptで例外処理"""
        try:
            # Entryの内容を取得
            height = float(self.ent1.get())
            weight = float(self.ent2.get())
            # BMIを計算
            bmi = round(weight / ((height / 100) * (height / 100)), 1)
            # 適正体重を計算
            right_weight = round(((height / 100) * (height / 100)) * 22, 1)

            # if文で分岐
            if bmi < 18.5:
                result = "痩せすぎだよ"
                # PhotoImageのオブジェクトのfileを変えて
                self.img["file"] = "BMI/img/thin.png"
                # self.lab7のimageを変える
                self.lab7["image"] = self.img

            elif 18.5 <= bmi < 25:
                result = "標準体型ですね！"
                self.img["file"] = "BMI/img/normal.png"
                self.lab7["image"] = self.img

            elif 25 <= bmi < 30:
                result = "ちょっと肥満"
                self.img["file"] = "BMI/img/obesity.png"
                self.lab7["image"] = self.img
            
            elif 30 <= bmi < 35:
                result = "肥満体型ね…"
                self.img["file"] = "BMI/img/obesity.png"
                self.lab7["image"] = self.img

            elif 35 <= bmi < 40:
                result = "や、やばい…"
                self.img["file"] = "BMI/img/obesity.png"
                self.lab7["image"] = self.img

            elif 40 <= bmi:
                result = "これはもはや才能？"
                self.img["file"] = "BMI/img/obesity.png"
                self.lab7["image"] = self.img

            self.lab6["fg"] = "black"
            ans = f"あなたのBMIは{bmi}です。\n{result}\n適正体重は{right_weight}kgです。"

            # self.var1に文字列をセット
            self.var1.set(ans)

        except ValueError:
            # エラーメッセージ
            # self.var1.set("半角の数字を入力してください")
            # return("\033[31m" + "半角の数字を入力してください" + "\033[0m")
            # self.lab6 = tk.Label(self, text="半角の数字を入力してください", fg="red")
            # self.var1.set = tk.Label(self, text="半角の数字を入力してください", fg="red")
            # self.var1.set(tk.Label(text="半角の数字を入力してください", fg="red"))
            self.lab6["fg"] = "red"
            self.var1.set("半角の数字を入力してください")
        except ZeroDivisionError:
            # エラーメッセージ
            # self.var1.set("正しい数値を入力してください")
            # self.lab6 = tk.Label(self, text="正しい数値を入力してください", fg="red")
            # self.var1.set = tk.Label(self, text="正しい数値を入力してください", fg="red")
            # self.var1.set(tk.Label(text="正しい数値を入力してください", fg="red"))
            self.lab6["fg"] = "red"
            self.var1.set("正しい数値を入力してください")

    def clear(self):
        """リセットボタンが押されたら発動"""
        self.img["file"] = "BMI/img/measurement.png"
        self.lab7["image"] = self.img
        self.lab6["fg"] = "black"
        self.var1.set(self.initial)
        # self.var2.set(self.initial)
        # Entryに書いている文字の最初[0]から最後まで消すという意味
        self.ent1.delete(0, tk.END)
        self.ent2.delete(0, tk.END)
        self.ent1.focus()

# Tkクラスをインスタンス化
root = tk.Tk()
# ウィンドウのタイトル指定
root.title("BMI計算アプリ")
# すべてのウィジェットのフォント指定
root.option_add("*Font", "メイリオ 12")
# Appクラスをインスタンス化
app = App(master=root)
# mainloopメソッドでメインループを呼び出しイベントを待つ
root.mainloop()