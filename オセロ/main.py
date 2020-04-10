import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super(App, self).__init__()
        self.title("オセロゲーム")
        self.geometry("{}x{}+{}+{}".format(550, 550, 300, 100))
        self.resizable(0, 0)
        self.iconbitmap("オセロ/img/othello.ico")
        self.configure(bg="white")
        self.set_widgets()

    def set_widgets(self):
        # Label
        self.turn = 1
        self.info = tk.Canvas(self, bg="white", width=300, height=100)
        self.info.pack(pady=(30,0))
        self.var = tk.StringVar()
        self.update_label()
        self.label = tk.Label(self.info, bg="white", font=("Helvetica", 15), textvariable=self.var)
        self.label.pack()

        # オセロ盤
        self.board = tk.Canvas(self, bg="lime green", width=350, height=350)
        self.board.pack(pady=(30, 0))

        # オセロ盤の設定
        self.board2info = [-1] * 10 + [[0, -1][i in [0, 9]] for i in range(10)] * 8 + [-1] * 10
        # tag
        self.numstr = '12345678'
        self.alpstr = "abcdefgh"
        # tagからクリックされたtagの位置を得る
        self.tag2pos = {}
        # 1次元の座標からtagを得る
        self.z2tag = {}
        # 長方形を配置する
        for i, y in zip(self.numstr, range(15, 336, 40)):
            for j, x in zip(self.alpstr, range(15, 336, 40)):
                pos = x, y, x+40, y+40
                tag = i + j
                self.tag2pos[tag] = pos
                self.board.create_rectangle(*pos, fill="lime green", tags=tag)
                self.z2tag[self.z_coordinate(tag)] = tag
        # 初期設定
        for p, i in zip([1, 2], "45"):
            for q, j in zip([2, 1], "de"):
                color = ["black", "white"][p-q]
                tag = i + j
                self.board2info[self.z_coordinate(tag)] = [1, 2][p-q]
                self.board.create_oval(*self.tag2pos[tag], fill=color, tags=tag)
        self.get_board_info()

    def z_coordinate(self, tag):
        x = self.alpstr.index(tag[1])+1
        y = self.numstr.index(tag[0])+1
        return y*10 + x

    def get_board_info(self):
        board_format = " {:2d} " * 10
        print("", *[board_format.format(*self.board2info[i:i+10]) \
            for i in range(0, 100, 10)], sep='\n')

    def update_label(self):
        self.var.set("{}のターン".format(["コンピューター", "あなた"][self.turn]))

    def run(self):
        self.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()