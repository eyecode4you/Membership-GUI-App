"""	extract_from_pdf.py - Create list from fields of membership.pdf, 
	requires pdf structure of membership form I created with 
	LibreOffice Draw """
import PyPDF2 as pypdf
def extract(filename):
	"""Extract member details from filename passed by members_gui.py"""
	mem_info_list = [] #List to contain info
	pdfobject=open(filename,'rb')
	pdf=pypdf.PdfFileReader(pdfobject)
	data = pdf.getFormTextFields()
	for k, v in data.items():
		#print(k, ' ',v)
		mem_info_list.append(v) #append the values to list
	#print(mem_info_list)
	return mem_info_list
