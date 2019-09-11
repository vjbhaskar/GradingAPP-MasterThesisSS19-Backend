from fpdf import FPDF


head_valk = ""

class PDF(FPDF):


    def Val(self,f):
        global head_valk
        self.head_valk = f

    def header(self):
        # Logo
        # Arial bold 15
        global head_valk
        self.set_font('Arial', 'B', 9)
        # Text color in gray
        self.set_text_color(128)
        # Move to the right
        # Title

        self.cell(40, 10, self.head_valk)
        # Line break
        self.ln(20)

