import pandas as pd
from fpdf import FPDF

# Load data from CSV
data = pd.read_csv("data.csv")

# Calculate basic statistics
average_marks = data["Marks"].mean()
highest_marks = data["Marks"].max()
lowest_marks = data["Marks"].min()

# Create PDF report
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=14)

pdf.cell(200, 10, txt="STUDENT PERFORMANCE REPORT", ln=True, align="C")
pdf.ln(10)

pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt=f"Average Marks: {average_marks:.2f}", ln=True)
pdf.cell(200, 10, txt=f"Highest Marks: {highest_marks}", ln=True)
pdf.cell(200, 10, txt=f"Lowest Marks: {lowest_marks}", ln=True)

pdf.ln(10)
pdf.set_font("Arial", style="B", size=12)
pdf.cell(200, 10, txt="Detailed Data:", ln=True)

pdf.set_font("Arial", size=12)

# Add table contents
for index, row in data.iterrows():
    pdf.cell(200, 10, txt=f"{row['Name']} - {row['Marks']}", ln=True)

# Save PDF
pdf.output("sample_report.pdf")

print("PDF Generated Successfully!")
