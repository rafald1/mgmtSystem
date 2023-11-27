from io import BytesIO

from fpdf import FPDF
from pypdf import PdfReader, PdfWriter


def insert_values_to_pdf_template(agreement):
    data = {
        "agreement_date": {"position": (32, 41), "value": str(agreement.agreement_date)},
        "name": {"position": (17, 76), "value": agreement.name},
        "company_name": {"position": (37, 80), "value": agreement.company_name},
        "tax_number": {"position": (35, 84), "value": agreement.tax_number},
        "agreement_length": {"position": (42, 159), "value": agreement.agreement_length[:-1]},
        "price_and_no_of_items": {"position": (57, 163), "value": f"{agreement.price} * {agreement.no_of_items}"}
    }
    pdf = FPDF("P", "mm", "A4")
    pdf.add_page()
    pdf.set_font("helvetica", "B", 9)
    for element in data.values():
        pdf.text(*element["position"], element["value"])

    buffer = BytesIO(pdf.output())
    generated_text = PdfReader(buffer).pages[0]
    writer = PdfWriter(clone_from="./agreement/utils/pdf_templates/agreement_template_v1.1.pdf")
    writer.pages[0].merge_page(generated_text, over=True)
    writer.write(buffer)
    return buffer
