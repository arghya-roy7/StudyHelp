from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors


def generate_pdf(request, name, id, payslip_number, courses):
    response = HttpResponse(content_type='application/pdf')
    
    response['Content-Disposition'] = f'attachment; filename=payslip_{id}.pdf'
    pdf_canvas = canvas.Canvas(response, pagesize=letter)

    title_text = "Pay Slip"
    title_x = 250
    title_y = 760
    pdf_canvas.setFillColor(colors.blue)
    pdf_canvas.setFont("Helvetica-Bold", 16)
    pdf_canvas.drawString(title_x, title_y, title_text)
    

    
    # Draw a box
    box_x = 50
    box_y = 550
    box_width = 500
    box_height = 25
    pdf_canvas.setFillColor(colors.black)
    pdf_canvas.setFont("Helvetica", 10)
    name_width = len(name) + 120
    pdf_canvas.rect(420, 680 ,name_width , 30)
    pdf_canvas.line(420, 695, 420 + name_width , 695)
    pdf_canvas.drawString(50, 700, f"Payslip Number: {payslip_number}")
    pdf_canvas.drawString(425, 700, f"Name: {name}")
    pdf_canvas.drawString(425, 685, f"Student ID: {id}")
    pdf_canvas.setFont("Helvetica", 12)
    total_price = sum([i.course_fee for i in courses])
    for course in courses:
        pdf_canvas.drawString(box_x + 5, box_y+8, f"({course.course_id}) {course.course_name}")
        pdf_canvas.drawString(box_x + 410, box_y+8, f"{course.course_fee}/= BDT")
        pdf_canvas.rect(box_x, box_y, box_width, box_height)
        box_y+=25
    pdf_canvas.rect(box_x, box_y-(25 * len(courses)+25) , box_width, box_height)
    pdf_canvas.drawString(box_x + 375, box_y-(25 * len(courses)+17), F"Total: {total_price}/= BDT")
    pdf_canvas.line(box_x + 400, box_y, box_x + 400, box_y-(25 * len(courses)) )
    pdf_canvas.save()

    return response

