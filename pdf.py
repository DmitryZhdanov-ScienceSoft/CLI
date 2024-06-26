from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'CLI Applications Research', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page %s' % self.page_no(), 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(10)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

pdf = PDF()
pdf.add_page()

pdf.chapter_title("Introduction")
pdf.chapter_body("- Welcome and Introduction\n- Purpose and Scope of the Research")

pdf.chapter_title("Typical CLI Application Structure")
pdf.chapter_body("- Entry Point\n- Argument Parsing\n- Main Logic\n- Error Handling\n- Output Results\n- Example Libraries: click, argparse, typer")

pdf.chapter_title("Integration with External Services")
pdf.chapter_body("- Interacting with APIs\n- Example: MidJourney API\n- Displaying Images in Terminal")

pdf.chapter_title("Best Practices for CLI Development")
pdf.chapter_body("- Clear Error Messages\n- Documentation and Help\n- Compatibility with Pipelines (pipe)\n- Using Colors and Formatting\n- Progress Bars for Long Operations")

pdf.chapter_title("Application Examples")
pdf.chapter_body("- CLI Task Manager\n- Snake Game")

pdf.chapter_title("Demonstration")
pdf.chapter_body("- Video or Live Demo\n- Example Use Cases")

pdf.chapter_title("Questions and Answers")
pdf.chapter_body("Feel free to ask any questions!")

pdf.chapter_title("Conclusion")
pdf.chapter_body("- Summary of Key Findings\n- Next Steps\n- Thank You and Contact Information")

pdf_path = "./CLI_Applications_Research_Report.pdf"
pdf.output(pdf_path)
