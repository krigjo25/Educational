# Importing responsories
import sys
from PIL import Image
from fpdf import FPDF

class PDF(FPDF):

  def MetaConfiguration(self, title, creator, author):

    #   Set the title of the document
    self.set_title(title)

    #   Set the document creator
    self.set_creator(creator)

    # Set the author of the document
    self.set_author(author)

    return

  def PageConfigurations(self):

    #   Initializing margins
    left, top, right = 10, 30, 10

    self.set_margins(left, top, right)

    return

  def PDFHeader(self):

    self.set_font('Arial', 'B', 16)

    return

  def ChapterTitle(self, label):

    #   Set the font for the title
    self.set_font('Arial', 'B', 50)

    #   Fill the background for the title
    self.set_fill_color(255, 255, 255)

    #   Line break
    self.ln(4)

    #   Set the text for the chapter
    self.cell(0, 25, f'{label}', 0, 1, 'C', 1)

    #   Line break
    self.ln(4)

    return

  def ChapterBody(self, name, file):

    #   Add a image
    if file:

      img = Image.open(file)

      width, height = img.size

      self.image(file, x = 0, type = img.format, link = 'https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png')

      height =-abs(height // 2)

    #   Add text
    self.set_font('Helvetica', '', 20)

    self.set_text_color(255,255,255)
    self.cell(0, height, f'{name} took CS50', align='C')


    return

  def PDFChapter(self, title, name, file = None):

    self.add_page()
    self.ChapterTitle(title)
    self.ChapterBody(name, file)

    return

  def PDFFooter(self):

    self.output('shirtificate.pdf')

    return

def CS50Certificate(name):

  '''
      #   Author : @krigjo25
      #   Date :    11-22

      1. Prompts the user for their name and outputs, using fpdf2, a CS50 shirtificate in a file called shirtificate.pdf, with these specifications:

- The orientation of the PDF should be Portrait.
- The format of the PDF should be A4.
- The top of the PDF should “CS50 Shirtificate” as text, centered horizontally.

- The shirt’s image should be centered horizontally.
- The user’s name should be on top of the shirt, in white text.

  '''
  #   Initializing classes to variables
  pdf = PDF(orientation = 'Portrait', format ='A4')

  # Configuring the PDF file

  pdf.MetaConfiguration('CS50 Shirtificate', '@krigjo25', name)
  pdf.PageConfigurations()

  #   Pages
  pdf.PDFChapter('CS50 Shirtificate', name, 'shirtificate.png')

  #   Footer information
  pdf.PDFFooter()

  return

if __name__ == '__main__':
  CS50Certificate(input('Name : '))