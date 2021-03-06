# coding:utf-8
import tkinter as tk

# 円をリストで用意する
balls = [
    {"x" : 400, "y": 300, "dx" : 1, "dy" : 1, "color" : "red"},
    {"x" : 200, "y": 100, "dx" : -1, "dy" : 1, "color" : "green"},
    {"x" : 100, "y": 200, "dx" : 1, "dy" : -1, "color" : "blue"},
]

def move():
    global balls
    for b in balls:
        # いまの円を消す
        canvas.create_oval(b["x"] -20, b["y"] - 20, b["x"] + 20, b["y"] + 20, fill="white", width=0)
        # X座標を動かす
        b["x"] = b["x"] + b["dx"]
        # Y座標も動かす
        b["y"] = b["y"] + b["dy"]
        # 次の位置に円を描く
        canvas.create_oval(b["x"] - 20, b["y"] - 20, b["x"] + 20, b["y"] + 20, fill=b["color"], width=0)
        # 端を超えていたら反対向きにする
        if b["x"] >= canvas.winfo_width() - 20:
            b["dx"] = -1
        if b["x"] <= 20:
            b["dx"] = +1
        # Y座標についも同様
        if b["y"] >= canvas.winfo_height() - 20:
            b["dy"] = -1
        if b["y"] <= 20:
            b["dy"] = +1
        # 再びタイマー
        root.after(10, move)

# ウィンドウを描く
root = tk.Tk()
root.geometry("600x400")

# キャンバスを置く
canvas =tk.Canvas(root, width=600, height=400, bg="white")
canvas.place(x=0, y=0)

# タイマーを設定する
root.after(10, move)

root.mainloop()
