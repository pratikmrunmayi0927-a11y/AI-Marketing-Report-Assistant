from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import pandas as pd

def generate_pdf(report_text):
    file_name = "Marketing_Report.pdf"

    pdf = SimpleDocTemplate(file_name)
    styles = getSampleStyleSheet()

    story = [
        Paragraph("<b>AI Marketing Report</b>", styles["Title"]),
        Paragraph(report_text.replace("\n", "<br/>"), styles["BodyText"])
    ]

    pdf.build(story)

    return file_name


def generate_excel(df):
    file_name = "Marketing_Report.xlsx"
    df.to_excel(file_name, index=False)
    return file_name