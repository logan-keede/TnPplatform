import json
import click
from fpdf import FPDF

@click.command()
@click.option('-i', '--input-file', type=click.Path(exists=True), help='Input JSON file path', required=True)
@click.option('-o', '--output-file', type=click.Path(), default='output.pdf', help='Output PDF file path')
def generate_pdf(input_file, output_file):
    pdf = FPDF('P', 'mm', 'Letter')
    pdf.add_page()
    json_file = open(input_file, 'r')
    data = json.load(json_file)
    pdf.set_auto_page_break(True, margin=7)
    pdf.add_font('cmr','', './fonts/cmr12.ttf', uni=True)
    pdf.add_font('cmbx','', './fonts/cmbx12.ttf', uni=True)
    pdf.add_font('cmsl','', './fonts/cmsl12.ttf', uni=True)
    pdf.set_font("cmr", "", 24)
    pdf.cell(0, 7, data["Name"] , ln=1, align="C")
    pdf.set_font("times", "", 10)

    pdf.set_font("cmr", "", 10)
    if data.get('mobile'):
        pdf.set_x(pdf.get_x() + 60)
        pdf.image('./phone-flip-solid.png', x=pdf.get_x(), y=pdf.get_y()+1, w=3.5, h=3.2)
        pdf.set_x(pdf.get_x() + 4)
        width = pdf.get_string_width(data['mobile'])
        pdf.cell(width + 2, 5, data['mobile'])

        
    pdf.set_font("cmr", "U", 10)
    if data.get('email'):  
        pdf.set_x(pdf.get_x() + 2)
        pdf.image('./envelope-solid.png', x=pdf.get_x(), y=pdf.get_y()+1, w=3.5, h=3.5)      
        pdf.set_x(pdf.get_x() + 4)
        pdf.set_link(link=f"mailto:{data['email']}")
        width = pdf.get_string_width(data['email'])
        pdf.cell(width+2, 5, data['email'], ln=1)
        pdf.set_link(link='')

    if data.get('linked'):
        pdf.set_x(pdf.get_x() + 50)
        pdf.image('./linkedin.png', x=pdf.get_x(), y=pdf.get_y()+1, w=3.5, h=3.5)
        pdf.set_x(pdf.get_x() + 4)
        width = pdf.get_string_width(data['linked'])
        linkedin = f"https://{data['linked']}"
        pdf.cell(width + 2, 5, data['linked'],link=linkedin)
        
        
    if data.get('github'):
        pdf.set_x(pdf.get_x() + 2)
        pdf.image('./github.png', x=pdf.get_x(), y=pdf.get_y()+1, w=3.5, h=3.5)
        pdf.set_x(pdf.get_x() + 4)
        width = pdf.get_string_width(data['github'])
        github = f"https://{data['github']}"
        pdf.cell(width + 2, 5, data['github'], ln=1,link=github)
        # pdf.set_link(link='')

    if data.get('CareerSum'):
        pdf.set_font("cmbx", "", 14)
        pdf.cell(0, 7, "Career summary so far", ln=1)
        pdf.set_line_width(0.2)
        pdf.line(10, pdf.get_y(), 204, pdf.get_y())
        pdf.set_font("cmr", "", 10)

        remain_space = 204 - pdf.get_x()
        lines = pdf.multi_cell(remain_space, 5, data['CareerSum'][0].get('data'))

        for line in lines:
            pdf.cell(0, 5, line)

        pdf.cell(0, 6, data['CareerSum'][1].get("date"), ln=1)
        pdf.set_y(pdf.get_y() + 2)

    # Check if 'education' key exists
    if data.get('education'):
        pdf.set_font("cmbx", "", 14)
        pdf.cell(0, 7, 'Education', ln=1)
        pdf.line(10, pdf.get_y(), 204, pdf.get_y())
        pdf.set_font("cmbx", "", 11)
        pdf.cell(0, 7, data['education'].get("Education-clg"))
        pdf.cell(0, 7, data['education'].get("ed-date"), ln=1, align="R")
        pdf.set_font("cmsl", "", 10)
        remain_space = 204 - pdf.get_x()
        lines = pdf.multi_cell(remain_space, 4, data['education'].get("edu-details"))

        for line in lines:
            pdf.cell(0, 5, line)
        pdf.set_y(pdf.get_y() + 2)

    # Check if 'achievement' key exists
    if data.get('achievement'):
        pdf.set_font("cmbx", "", 14)
        pdf.cell(0, 7, "Achievements", ln=1)
        pdf.line(10, pdf.get_y(), 204, pdf.get_y())
        pdf.set_font("cmr", "", 10)
        p = 0
        for i in range(len(data["achievement"])):
            pdf.cell(5)
            pdf.cell(5, 6, "-")
            pdf.cell(0, 6, data["achievement"][i].get("ach-details"), ln=1)
        pdf.set_y(pdf.get_y() + 2)

    # Check if 'experience' key exists
    if data.get('experience'):
        pdf.set_font("cmbx", "", 14)
        pdf.cell(0, 7, "Experience", ln=1)
        pdf.line(10, pdf.get_y(), 204, pdf.get_y())
        for i in range(len(data['experience'])):
            pdf.set_font("cmbx", "", 11)
            pdf.cell(0, 6, data['experience'][i].get("exp-company"))
            pdf.cell(0, 6, data['experience'][i].get("exp-date"), ln=1, align="R")
            pdf.set_font("cmr", "", 10)
            pdf.cell(0, 5, data['experience'][i].get("exp-details1"))
            pdf.cell(0, 5, data['experience'][i].get("exp-details2"), ln=1, align="R")
            for j in range(len(data['experience'][i].get("exp-details3"))):
                pdf.cell(5)
                pdf.cell(5, 5, "-")
                pdf.cell(0, 5, data['experience'][i].get("exp-details3")[j].get("exp_details"), ln=1)
        pdf.set_y(pdf.get_y() + 2)

    # Check if 'Internships' key exists
    if data.get('Internships'):
        pdf.set_font("cmbx", "", 14)
        pdf.cell(0, 7, "Internships", ln=1)
        pdf.line(10, pdf.get_y(), 204, pdf.get_y())
        for i in range(len(data['Internships'])):
            pdf.set_font("cmbx", "", 11)
            pdf.cell(0, 6, data['Internships'][i].get("intern-company"))
            pdf.cell(0, 6, data['Internships'][i].get("intern-date"), ln=1, align="R")
            pdf.set_font("cmr", "", 10)
            pdf.cell(0, 5, data['Internships'][i].get("intern-details1"))
            pdf.cell(0, 5, data['Internships'][i].get("intern-details2"), ln=1, align="R")
            for j in range(len(data['Internships'][i].get("intern-details3"))):
                pdf.cell(5)
                pdf.cell(5, 5, "-")
                pdf.cell(0, 5, data['Internships'][i].get("intern-details3")[j].get("intern_details"), ln=1)
        pdf.set_y(pdf.get_y() + 2)

    # Check if 'Hackathon' key exists
    if data.get('Hackathon'):
        pdf.set_font("cmbx", "", 14)
        pdf.cell(0, 7, "Hackathons Won", ln=1)
        pdf.line(10, pdf.get_y(), 204, pdf.get_y())
        for i in range(len(data['Hackathon'])):
            pdf.set_font("cmbx", "", 11)
            pdf.cell(0, 6, data['Hackathon'][i].get("hack-title"))
            pdf.cell(0, 6, data['Hackathon'][i].get("hack-date"), ln=1, align="R")
            pdf.set_font("cmr", "", 10)
            for j in range(len(data['Hackathon'][i].get("hack-details"))):
                pdf.cell(5)
                pdf.cell(5, 5, "-")
                lines = pdf.multi_cell(remain_space, 4, data['Hackathon'][i].get("hack-details")[j].get("hack_details1"))
                for line in lines:
                    pdf.cell(0, 5, line)
        pdf.set_y(pdf.get_y() + 2)

    # Check if 'Gitproj' key exists
    if data.get('Gitproj'):
        pdf.set_font("cmbx", "", 14)
        pdf.cell(0, 7, "Notable Github Projects", ln=1)
        pdf.line(10, pdf.get_y(), 204, pdf.get_y())
        for i in range(len(data['Gitproj'])):
            pdf.set_font("cmbx", "", 11)
            lines = pdf.multi_cell(remain_space, 6, data['Gitproj'][i].get("gitproj-title"))

            for line in lines:
                pdf.cell(0, 5, line)

            pdf.set_font("cmr", "", 10)
            for j in range(len(data['Gitproj'][i].get("gitproj-details"))):
                pdf.cell(5)
                pdf.cell(5, 5, "-")
                lines = pdf.multi_cell(remain_space, 4, data['Gitproj'][i].get("gitproj-details")[j].get("gitproj_details1"))

                for line in lines:
                    pdf.cell(0, 5, line)

    pdf.output(output_file)

def main():
    generate_pdf()

if __name__ == '__main__':
    main()
