from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df=pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    
        #Set the header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(0,0,254)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
        #Set lines
    for i in range(20,290,10):
        pdf.line(10,i, 200,i) #(x1,y1, x2,y2)
        
        #Set the footer
    pdf.ln(260) #added 261 mm break-lines
    pdf.set_font(family="Times", style="I", size=12)
    pdf.set_text_color(180,180,180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")
        
    for i in range(row["Pages"] - 1):
        pdf.add_page()
        
        #Set the footer
        pdf.ln(272)
        pdf.set_font(family="Times", style="I", size=12)
        pdf.set_text_color(180,180,180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")
        #Set lines
        for i in range(20,290,10):
            pdf.line(10,i, 200,i) #(x1,y1, x2,y2)
    
pdf.output("output.pdf")
