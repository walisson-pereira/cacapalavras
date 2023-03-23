# importing modules
from reportlab.lib import pagesizes
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors

from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table, TableStyle, SimpleDocTemplate


def gera_pdf(palavras: list, str_mapa: list, fileName='sample.pdf'):

    # initializing variables with values
    documentTitle = 'caça-palavras'
    title = 'Caça-palavras'
    subTitle = 'Encontre as seguintes palavras:'
    
    #image = 'image.jpg'

    # creating a pdf object
    pdf = canvas.Canvas(fileName)
    
    # setting the title of the document
    pdf.setTitle(documentTitle)

    # creating the title by setting it's font
    # and putting it on the canvas
    pdf.setFillColor(colors.black)
    pdf.setFont("Courier-Bold", 24)
    pdf.drawCentredString(300, 770, title)

    # creating the subtitle by setting it's font,
    # colour and putting it on the canvas
    #pdf.setFillColor(colors.black)
    #pdf.setFont("Courier-Bold", 18)
    #pdf.drawCentredString(290, 720, subTitle)

    # drawing a line
    #pdf.line(30, 710, 550, 710)



    # drawing a line
    #pdf.line(30, 710, 550, 710)
    ponto_superior_esquerdo = (30, 695)
    ponto_superior_direito = (555, 695)
    ponto_inferior_esquerdo = (30, 305)
    ponto_inferior_direito = (555, 305)
    pdf.line( 30, 695, 555, 695)
    pdf.line( 30, 695,  30, 305)
    pdf.line(555, 695, 555, 305)
    pdf.line( 30, 305, 555, 305)

    # creating a multiline text using
    # textline and for loop
    text = pdf.beginText(40, 680)
    text.setFont("Courier", 18)
    text.setFillColor(colors.black)
    for line in str_mapa:
        text.textLine(line)
    pdf.drawText(text)

    # creating a multiline text using
    # textline and for loop
    #text = pdf.beginText(40, 680)
    
    #text.setFont("Courier", 18)
    #text.setFillColor(colors.black)
    #for line in palavras:
#        text.textLine(line)
    #for i in range(len(palavras) // 2):
    #    text.textLine(palavras[i * 2 - 1] + '   ' + palavras[i * 2])
 #   pdf.drawText(text)

    data = [
        [palavras[0], palavras[1], palavras[2]],
        [palavras[3], palavras[4], palavras[5]],
        [palavras[6], palavras[7], palavras[8]],
        [palavras[9], palavras[10], palavras[11]],
    ]
        
    text.textLine(' ')
    text.textLine(subTitle)
    text.textLine(' ')
    for i in range(4):
        linha = f'{data[i][0]:<15} {data[i][1]:<15} {data[i][2]:<15}'
        text.setFont("Courier", 18)
        text.setFillColor(colors.black)
        text.textLine(linha)
        pdf.drawText(text)
    
    # saving the pdf
    pdf.save()
