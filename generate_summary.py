from fpdf import FPDF

class SummaryPDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 16)
        self.cell(0, 10, "Executive Summary - CV Website Changes", new_x="LMARGIN", new_y="NEXT", align="C")
        self.set_font("Helvetica", "", 9)
        self.set_text_color(100, 100, 100)
        self.cell(0, 6, "Session: March 2026 | Repository: galavashubhang.github.io", new_x="LMARGIN", new_y="NEXT", align="C")
        self.set_text_color(0, 0, 0)
        self.ln(4)

    def section_title(self, title):
        self.set_font("Helvetica", "B", 13)
        self.set_fill_color(235, 235, 235)
        self.cell(0, 9, title, new_x="LMARGIN", new_y="NEXT", fill=True)
        self.ln(2)

    def sub_heading(self, text):
        self.set_font("Helvetica", "B", 10)
        self.cell(0, 7, text, new_x="LMARGIN", new_y="NEXT")

    def body_text(self, text):
        self.set_font("Helvetica", "", 10)
        self.multi_cell(0, 5.5, text)
        self.ln(1)

    def bullet(self, text):
        self.set_font("Helvetica", "", 10)
        x = self.get_x()
        self.cell(6, 5.5, "-")
        self.multi_cell(0, 5.5, text)
        self.ln(0.5)

pdf = SummaryPDF()
pdf.set_auto_page_break(auto=True, margin=20)
pdf.add_page()

# Section 1: New Files
pdf.section_title("1. New Files Created")

pdf.sub_heading("projects.html")
pdf.body_text("Dedicated Projects page containing Ongoing Projects, Projects, and Competitions sections. Content copied from cv.html using the same cv-style.css template.")

pdf.sub_heading("competitions.html")
pdf.body_text("Dedicated Competitions page with the SAE ADDC 2026 entry. Uses the same cv-style.css template as the CV.")

pdf.sub_heading("blogs.html")
pdf.body_text("Technical Blogs page using index-style.css (same styling as Home page). Lists IEEE NITK Virtual Expo project reports:")
pdf.bullet("Multiscale Materials Analysis (ieee.nitk.ac.in/virtual_expo/report/68)")
pdf.bullet("Pathfinder MPC: Charting the Way! (ieee.nitk.ac.in/virtual_expo/report/110)")
pdf.ln(2)

# Section 2: CV Changes
pdf.section_title("2. CV (cv.html) Changes")
pdf.bullet('New "Competitions" section added with SAE ADDC 2026 (Runners Up) entry - 3 bullet points about Team AeroNITK, drone fabrication, and the runners-up prize with Certificate link.')
pdf.bullet("All external links given target=\"_blank\" (previously most opened in the same tab).")
pdf.bullet("Navbar updated with new buttons (detailed below).")
pdf.bullet("No content was removed - everything that existed before remains intact.")
pdf.ln(2)

# Section 3: Navbar
pdf.section_title("3. Navbar Updated Across All Pages")
pdf.body_text("Updated consistently on: index.html, cv.html, projects.html, competitions.html, blogs.html")
pdf.ln(1)

pdf.sub_heading("Before:")
pdf.set_font("Courier", "", 10)
pdf.cell(0, 6, "Home | CV | Projects (dropdown) | Blogs (dropdown) | GitHub", new_x="LMARGIN", new_y="NEXT")
pdf.ln(2)

pdf.sub_heading("After:")
pdf.set_font("Courier", "", 10)
pdf.cell(0, 6, "Home | CV | Projects | Competitions | Blogs (dropdown) | GitHub | LinkedIn", new_x="LMARGIN", new_y="NEXT")
pdf.ln(3)

pdf.sub_heading("Key changes:")
pdf.bullet("Projects - No longer a dropdown; now a direct link to projects.html.")
pdf.bullet("Competitions - New button linking to competitions.html.")
pdf.bullet('Blogs - Dropdown now has two sub-items: "Technical Blogs" (blogs.html) and "Medium.com" (external link).')
pdf.bullet("LinkedIn - New button next to GitHub, linking to linkedin.com/in/galavashubhang (opens in new tab).")
pdf.ln(2)

# Section 4: CSS
pdf.section_title("4. CSS Changes (navbar-style.css)")
pdf.bullet('Added "flex-wrap: wrap" to .navbar-menu so the navbar wraps gracefully on smaller screens with the additional buttons.')
pdf.ln(2)

# Section 5: Files modified
pdf.section_title("5. Files Modified / Created")

pdf.set_font("Courier", "", 9)
files = [
    ("MODIFIED", "index.html"),
    ("MODIFIED", "cv.html"),
    ("CREATED",  "projects.html"),
    ("CREATED",  "competitions.html"),
    ("CREATED",  "blogs.html"),
    ("MODIFIED", "assets/css/navbar-style.css"),
]
for status, name in files:
    color = (0, 128, 0) if status == "CREATED" else (0, 0, 180)
    pdf.set_text_color(*color)
    pdf.cell(22, 6, f"[{status}]")
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 6, name, new_x="LMARGIN", new_y="NEXT")

output_path = r"d:\shubh\Old C Drive\galavashubhang Github Repos\galavashubhang\Executive_Summary.pdf"
pdf.output(output_path)
print(f"PDF saved to: {output_path}")
