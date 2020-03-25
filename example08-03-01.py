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
pdf.setFont("HeiseiKakuGo-W5", 14)
pdf.drawString(10 * unit.mm, 270 * unit.mm, "はじめてのPDF")
pdf.save()
