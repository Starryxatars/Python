class Report:
    def generate(self):
        print("Generating a generic report.")


class PDFReport(Report):
    def generate(self):
        print("Generating report in PDF format (report.pdf).")


class ExcelReport(Report):
    def generate(self):
        print("Generating report in Excel format (report.xlsx).")


class HTMLReport(Report):
    def generate(self):
        print("Generating report in HTML format (report.html).")


def generate_report(report):
    report.generate()


for r in (PDFReport(), ExcelReport(), HTMLReport()):
    generate_report(r)
