from fpdf import FPDF


pdf = FPDF()
pdf.add_page()

# Input name from user, raise exception if no name entered
name = input("Name: ")
if not name:
    raise ValueError("Missing name")

# Set font and print header
pdf.set_font("helvetica", "B", 35)
pdf.cell(0, 60, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")

# Open image
pdf.image("shirtificate.png", x=0, y=70)

# Set new font and color for shirt print
pdf.set_font("helvetica", "B", 25)
pdf.set_text_color(255, 255, 255)

pdf.cell(0, 140, f"{name} took CS50", align="C")

# Save image
pdf.output("shirtificate.pdf")
