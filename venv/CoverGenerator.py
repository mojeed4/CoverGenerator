from fpdf import FPDF
from SizeCalculator import SizeCalculator as SC

class CoverGenerator:
    def __init__(self, trim_width, trim_height, number_of_pages, interior_type):
        # creating new size calculator based on trim size, number of pages and code for paper type
        self.new_page = SC((trim_width, trim_height), number_of_pages, interior_type)

    def create_cover_template(self):
        # checks to confirm if all works well
        print(self.new_page.get_spine_size())
        print(self.new_page.get_cover_size())

        # creating pdf document for the cover using generated cover size
        pdf = FPDF('P', 'in', self.new_page.get_cover_size())
        pdf.add_page()

        # setting fill color to background pink of the bleed area
        pdf.set_fill_color(248, 170, 143)

        # confirming self.new_page object workflow
        print(self.new_page.get_cover_width())

        # painting the background bleed color all over the entire cover page
        pdf.rect(0, 0, self.new_page.get_cover_width(), self.new_page.get_cover_height(), 'F')

        # setting fill color for the working areas
        pdf.set_fill_color(255, 255, 255)

        # applying white fill to the back cover area
        pdf.rect(0.25, 0.25, self.new_page.get_trim_width() - 0.25, self.new_page.get_trim_height() - 0.25, 'F')

        # applying white fill to the spine area of the cover
        start_x = 0.0625 + 0.125 + self.new_page.get_trim_width()
        pdf.rect(start_x, 0.25, self.new_page.get_spine_size() - (2 * 0.0625), self.new_page.get_trim_height() - 0.25, 'F')

        # applying white fill to the front cover area of the cover
        start_x = 0.25 + self.new_page.get_trim_width() + self.new_page.get_spine_size()
        pdf.rect(start_x, 0.25, self.new_page.get_trim_width() - 0.25, self.new_page.get_trim_height() - 0.25, 'F')

        # left most vertical line for book trim (actual trim area)
        pdf.dashed_line(0.125, 0.125, 0.125, self.new_page.get_trim_height() + 0.125, 0.05, 0.05)

        # Right most vertical line for book trim (actual trim area)
        start_x = self.new_page.get_cover_width() - 0.125
        pdf.dashed_line(start_x, 0.125, start_x, self.new_page.get_trim_height() + 0.125, 0.05, 0.05)

        # Top horizontal line for book trim (actual trim area)
        end_x = self.new_page.get_cover_width() - 0.125
        pdf.dashed_line(0.125, 0.125, end_x, 0.125, 0.05, 0.05)

        # Bottom horizontal line for book trim (actual trim area)
        start_y = self.new_page.get_cover_height() - 0.125
        end_x = self.new_page.get_cover_width() - 0.125
        pdf.dashed_line(0.125, start_y, end_x, start_y, 0.05, 0.05)

        # Spine vertical lines
        start_x = 0.125 + self.new_page.get_trim_width()
        print('start x', start_x)
        pdf.dashed_line(start_x, 0, start_x, self.new_page.get_trim_height() + 0.25, 0.05, 0.05)

        start_x = self.new_page.get_cover_width() - (self.new_page.get_trim_width() + 0.125)
        print('start x', start_x)
        pdf.dashed_line(start_x, 0, start_x, self.new_page.get_trim_height() + 0.25, 0.05, 0.05)

        # Additional text on the cover
        pdf.set_font('helvetica', 'B', 25)
        start_x = 0.25 + self.new_page.get_trim_width()
        pdf.cell(start_x, self.new_page.get_trim_height() - 1, '             Created by Majid!', 'C')

        #setting fill color for barcode and drawing the barcode
        pdf.set_fill_color(255, 242, 0)
        start_x = self.new_page.get_trim_width() - 2 - 0.125
        start_y = self.new_page.get_trim_height() - 1.2 - 0.125
        end_x = self.new_page.get_trim_width() - 0.125
        end_y = self.new_page.get_trim_height() - 0.125
        pdf.rect(start_x, start_y, 2, 1.2,'F')

        # cover output
        pdf.output('Cover Irregular.pdf')


