# クラスのインポート
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
import reportlab.lib.units as unit
import reportlab.lib.pagesizes as pagesizes

# フォントの登録
pdfmetrics.registerFont(UnicodeCIDFont("HeiseiKakuGo-W5"))

# PDFを作る
pdf = canvas.Canvas("example.pdf", pagesize=pagesizes.A4)
moji = "あ"

# フォントの大きさは用紙横幅と同じ210mmとする
pdf.setFont("HeiseiKakuGo-W5", 210 * unit.mm)
# 高さ
h = (297 - 210) / 2 * unit.mm
pdf.drawString(0 * unit.mm, h, moji)
pdf.save()
