""" export_members_pdf.py - Export db data to PDF file using .docx 
	template (Requires Microsoft Word)"""
from docxtpl import DocxTemplate
from time import time, localtime, asctime
from docx2pdf import convert

def export_to_docx(db_data):
	""" Create docx before pdf for formating """
	db_table = []
	for i in db_data:
		db_table.append({
		'index':i[0],
		'name':i[1],
		'number':i[2],
		'email':i[3],
		'address':i[4],
		'nationality':i[5],
		'category':i[6],
		'company':i[7],
		'position':i[8],
		'accountname':i[9],
		'IBAN':i[10],
		'BIC':i[11],
		'created':i[12],
		'expiry':i[13]
		})
	date = asctime(localtime(time())) #nice time format
	#import docx template
	template = DocxTemplate('member-list-template.docx')
	#Create template variables
	template_data = {
		'datetime': date,
		'table_contents': db_table
		}
	#render + save book list docx and create pdf
	template.render(template_data)
	template.save('member-list.docx')
	convert('member-list.docx', r'.\\') #Create pdf file in dir
