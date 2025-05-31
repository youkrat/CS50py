# Replace problematic en dash and other unicode characters with ASCII equivalents

def sanitize_text(text):
    return text.replace("–", "-").replace("’", "'")

# Rebuild the resume with sanitized content
class CleanPDFResume(FPDF): # type: ignore
    def header(self):
        self.set_font("Helvetica", "B", 16)
        self.set_text_color(30, 30, 30)
        self.cell(0, 10, sanitize_text("Ben Mwangi Kimani"), ln=True, align="C")
        self.set_font("Helvetica", "", 12)
        self.set_text_color(100, 100, 100)
        self.cell(0, 8, sanitize_text("bkimani@wesleyan.edu | +254 792 651 507"), ln=True, align="C")
        self.cell(0, 8, sanitize_text("linkedin.com/in/ben-mwangi-b650bb266"), ln=True, align="C")
        self.ln(10)

    def section_title(self, title):
        self.set_font("Helvetica", "B", 14)
        self.set_text_color(0, 102, 204)
        self.cell(0, 10, sanitize_text(title), ln=True)
        self.set_text_color(0, 0, 0)

    def add_bullet(self, text):
        self.set_font("Helvetica", "", 11)
        self.multi_cell(0, 8, f"- {sanitize_text(text)}")

    def add_text(self, text):
        self.set_font("Helvetica", "", 11)
        self.multi_cell(0, 8, sanitize_text(text))

pdf = CleanPDFResume()
pdf.add_page()

# Education Section
pdf.section_title("Education")
pdf.set_font("Helvetica", "B", 12)
pdf.cell(0, 8, sanitize_text("Wesleyan University - Middletown, CT"), ln=True)
pdf.set_font("Helvetica", "", 11)
pdf.cell(0, 8, sanitize_text("Bachelor of Arts in Computer Science & IDEAS Major (Computing Track), Class of 2029"), ln=True)
pdf.cell(0, 8, sanitize_text("Wesleyan African Scholar"), ln=True)
pdf.ln(4)

pdf.set_font("Helvetica", "B", 12)
pdf.cell(0, 8, sanitize_text("Alliance High School - Kikuyu, Kenya"), ln=True)
pdf.set_font("Helvetica", "", 11)
pdf.cell(0, 8, sanitize_text("KCSE (Kenyan Certificate of Secondary Education), Class of 2022"), ln=True)
pdf.cell(0, 8, sanitize_text("Ranked 12th nationally"), ln=True)
pdf.ln(6)

# Experience Section
pdf.section_title("Experience")
pdf.set_font("Helvetica", "B", 12)
pdf.cell(0, 8, sanitize_text("Peer Mentor - Equity College Counselling Program"), ln=True)
pdf.set_font("Helvetica", "I", 11)
pdf.cell(0, 8, sanitize_text("May 2024 - November 2024"), ln=True)
pdf.set_font("Helvetica", "", 11)
pdf.add_bullet("Helped 5 students with essays, brainstorming, and timelines.")
pdf.add_bullet("Guided students to Stanford, Princeton, Amherst, and UBC.")
pdf.add_bullet("Focused on helping students reflect and present their authentic stories.")
pdf.ln(2)

pdf.set_font("Helvetica", "B", 12)
pdf.cell(0, 8, sanitize_text("Corporate Bank Teller & Assistant TFO - Equity Bank, Murang'a"), ln=True)
pdf.set_font("Helvetica", "I", 11)
pdf.cell(0, 8, sanitize_text("Feb 2023 - Sept 2023"), ln=True)
pdf.set_font("Helvetica", "", 11)
pdf.add_bullet("Handled 150+ customers and $200,000+ in daily transactions.")
pdf.add_bullet("Maintained branch server room.")
pdf.add_bullet("Won the Equity Tech Hub Hackathon for a digital finance solution.")
pdf.ln(6)

# Awards Section
pdf.section_title("Awards & Recognition")
pdf.add_bullet("King-Morgridge Scholar, University of Wisconsin-Madison")
pdf.add_bullet("Top 15 Student Nationwide in the 2022 KCSE exams")
pdf.ln(6)

# Skills Section
pdf.section_title("Skills")
pdf.add_bullet("Essay Advising & Mentorship: Narrative development, authentic voice, structure")
pdf.add_bullet("Programming: Python, HTML, CSS, JavaScript")
pdf.add_bullet("Web Tools: Git, GitHub, React.js")
pdf.add_bullet("Strengths: Clear communication, collaboration, problem solving, follow-through")
pdf.ln(6)

# References Section
pdf.section_title("References")
pdf.set_font("Helvetica", "B", 11)
pdf.cell(0, 8, sanitize_text("Dr. Martha Oigo - General Manager, Equity Leaders Program"), ln=True)
pdf.set_font("Helvetica", "", 11)
pdf.cell(0, 8, sanitize_text("martha.oigo@equitybank.co.ke | +254 724 613 995"), ln=True)
pdf.ln(1)

pdf.set_font("Helvetica", "B", 11)
pdf.cell(0, 8, sanitize_text("David Bett Kimeli - Program Manager, Equity College Counselling Program"), ln=True)
pdf.set_font("Helvetica", "", 11)
pdf.cell(0, 8, sanitize_text("david.bett@equitybank.co.ke | +254 764 026 213"), ln=True)
pdf.ln(1)

pdf.set_font("Helvetica", "B", 11)
pdf.cell(0, 8, sanitize_text("George Kamau - Operations Manager, Equity Bank, Murang'a"), ln=True)
pdf.set_font("Helvetica", "", 11)
pdf.cell(0, 8, sanitize_text("george.kamau@equitybank.co.ke | +254 720 826 629"), ln=True)

# Save the PDF
output_path = "/mnt/data/Ben_Mwangi_Kimani_Resume.pdf"
pdf.output(output_path)

output_path
