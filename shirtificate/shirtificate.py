from fpdf import FPDF

def main():
    fpdf = FPDF()
    name = input('Name: ')
    fpdf.set_font('arial', size=20)
    fpdf.add_page()
    fpdf.cell(70)
    fpdf.cell(30, 10, 'CS50 Shirtificate', align="C")
    fpdf.image('shirtificate.png', 5, 40, 200)
    fpdf.set_font('Times', size=30)
    fpdf.set_text_color(250, 250, 250)
    fpdf.cell( 1, 230, f'{name} took CS50', align="C")
    fpdf.output('shirtificate.pdf')

if __name__ == '__main__':
    main()