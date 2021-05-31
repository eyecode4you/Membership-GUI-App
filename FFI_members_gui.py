""" FFI_members_gui.py
	Forest Friends Ireland Membership Management System
	Author: EyeCode4You
	Date: 16/05/2021
	Version: 1.0
"""
#Imports: tkinter - GUI, sqlite3 - Database
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import sqlite3, export_members_pdf, extract_from_pdf

def update(rows):
	""" Display rows in app from db """
	trv.delete(*trv.get_children())
	for i in rows:
		trv.insert('', 'end', values=i)

#Wrapper 2 button functions	
def search():
	""" Allow searching by member name """
	q2 = q.get()
	query = "SELECT * FROM members WHERE name LIKE '%"+q2+"%'"
	cursor.execute(query)
	rows = cursor.fetchall()
	update(rows)

def clear():
	""" Reset app row view to initial """
	q.set('') #Clear search input
	query = "SELECT * FROM members"
	cursor.execute(query)
	rows = cursor.fetchall()
	update(rows)

def export():
	""" Export db data to pdf file """
	query = "SELECT * FROM members"
	cursor.execute(query)
	db_data = cursor.fetchall()
	export_members_pdf.export_to_docx(db_data)
	messagebox.showinfo("Note", "File exported as: FFI-member-list.pdf")
	
def import_member():
	""" Import member details from pdf and add to wrapper 3 fields """
	try:
		filename = filedialog.askopenfilename(initialdir='./', \
		title='Select Member PDF to Open', \
		filetypes=(('PDF Files', '*.pdf'), ))
		mem_data = extract_from_pdf.extract(filename)
		t1.set(mem_data[3])
		t2.set(mem_data[1])
		t3.set(mem_data[0])
		t4.set(mem_data[2])
		t5.set(mem_data[6])
		t6.set(mem_data[15])
		t7.set(mem_data[4])
		t8.set(mem_data[5])
		t9.set(mem_data[12])
		t10.set(mem_data[10])
		t11.set(mem_data[9])
	except:
		messagebox.showerror("Error!", "Could not open selected file. Ensure the file is a valid membership PDF!")

#Wrapper 3 button functions
def update_memberdata():
	""" Update currently selected member data entry """
	mId = t0.get()
	name = t1.get()
	phone = t2.get()
	email = t3.get()
	address = t4.get()
	nationality = t5.get()
	category = t6.get()
	company = t7.get()
	position = t8.get()
	accountname = t9.get()
	IBAN = t10.get()
	BIC = t11.get()
	if messagebox.askyesno("Warning!", "Are you sure you want to update this entry?"):
		query = "UPDATE members SET name = ?, phone = ?, email = ?, address = ?, nationality = ?, category = ? , company = ?, position = ?, accountname = ?, IBAN = ?, BIC = ? WHERE id = ?"
		cursor.execute(query, (name, phone, email, address, \
		nationality, category, company, position, accountname, \
		IBAN, BIC, mId))
		clear()
	else:
		return True

def add_new_member():
	""" Add new member data entry """
	name = t1.get()
	phone = t2.get()
	email = t3.get()
	address = t4.get()
	nationality = t5.get()
	category = t6.get()
	company = t7.get()
	position = t8.get()
	accountname = t9.get()
	IBAN = t10.get()
	BIC = t11.get()
	query = "INSERT INTO members(id, name, phone, email, address, nationality, category, company, position, accountname, IBAN, BIC, expiry) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
	#Check all fields are filled
	if '' in {name, phone, email, address, nationality, category}:
		messagebox.showerror("ERROR!", "Please ensure fields are filled! (ID, created, and expiry are not required)")
	else:
		#Auto assign expiry based on member category
		category = category.upper()
		if category == 'A':
			expiry = 'n/a'
		elif category == 'B':
			expiry = '5 Years'
		elif category == 'C':
			expiry = '5 Years'
		elif category == 'D':
			expiry = 'n/a'
		elif category == 'E':
			expiry = '5 Years'
		elif category == 'F':
			expiry = 'n/a'
		cursor.execute(query, (None, name, phone, email, address, \
		nationality, category, company, position, accountname, IBAN, \
		BIC, expiry))
		clear()

def delete_memberdata():
	""" Delete member data entry """
	mId = t0.get()
	if messagebox.askyesno("Confirm Deletion?", \
	"Are you sure you want to delete this member?"):
		try:
			query = "DELETE FROM members WHERE id = "+mId
			cursor.execute(query)
			clear()
		except sqlite3.OperationalError as e:
			messagebox.showerror('Error in ID Selection!', str(e) + \
			' (Ensure you have the correct Member ID inserted!)')
	else:
		return True
		
def clearWrap3Fields():
	""" Clear all wrapper 3 input data """
	e = ''
	t0.set(e)
	t1.set(e)
	t2.set(e)
	t3.set(e)
	t4.set(e)
	t5.set(e)
	t6.set(e)
	t7.set(e)
	t8.set(e)
	t9.set(e)
	t10.set(e)
	t11.set(e)
	t12.set(e)
	t13.set(e)

def save_db_changes():
	""" Commit changes to members database """
	if messagebox.askyesno("Warning!", \
	"Are you sure you want to commit changes? This cannot be undone!"):
		conn.commit() #Save changes to database
	else:
		return True

def getrow(event):
	""" Populate wrapper 3 entries with data """
	rowid = trv.identify_row(event.y)
	item = trv.item(trv.focus())
	t0.set(item['values'][0])
	t1.set(item['values'][1])
	t2.set(item['values'][2])
	t3.set(item['values'][3])
	t4.set(item['values'][4])
	t5.set(item['values'][5])
	t6.set(item['values'][6])
	t7.set(item['values'][7])
	t8.set(item['values'][8])
	t9.set(item['values'][9])
	t10.set(item['values'][10])
	t11.set(item['values'][11])
	t12.set(item['values'][12])
	t13.set(item['values'][13])

#START - Setup
conn = sqlite3.connect('members.db')
cursor = conn.cursor() #create database cursor object
cursor.execute('SELECT * FROM members')
root = Tk()

style = ttk.Style() #Will be used for styling our treeview

wrapper1 = LabelFrame(root, text='Members Database')
wrapper2 = LabelFrame(root, text='Options')
wrapper3 = LabelFrame(root, text='Member Data')
wrapper1.pack(fill='both', expand='no', padx=20, pady=10)
wrapper2.pack(fill='both', expand='no', padx=20, pady=1)
wrapper3.pack(fill='both', expand='yes', padx=20, pady=10)

"""***MEMBER-LIST-WRAPPER1-SECTION***"""
trv = ttk.Treeview(wrapper1, columns=(1,2,3,4,5,6,7,8,9,10,11,12,13,14)\
, show='headings', height='10')
trv.pack(side=TOP)
#Selected entries highlighted green
style.map('Treeview', background=[('selected', 'green')])

#TRV Wrapper 1 Headings
trv.heading(1, text='ID')
trv.heading(2, text='Member Name')
trv.heading(3, text='Phone')
trv.heading(4, text='Email')
trv.heading(5, text='Address')
trv.heading(6, text='Nationality')
trv.heading(7, text='Category')
trv.heading(8, text='Company')
trv.heading(9, text='Position')
trv.heading(10, text='AccountName')
trv.heading(11, text='IBAN')
trv.heading(12, text='BIC')
trv.heading(13, text='Est.')
trv.heading(14, text='Expiry')
trv.column(1, width=15, minwidth=50)
trv.column(2, width=100, minwidth=125)
trv.column(3, width=100, minwidth=125)
trv.column(4, width=100, minwidth=175)
trv.column(5, width=100, minwidth=200)
trv.column(6, width=50, minwidth=75)
trv.column(7, width=100, minwidth=75)
trv.column(8, width=100, minwidth=175)
trv.column(9, width=100, minwidth=175)
trv.column(10, width=100, minwidth=125)
trv.column(11, width=100, minwidth=175)
trv.column(12, width=100, minwidth=75)
trv.column(13, width=100, minwidth=125)
trv.column(14, width=100, minwidth=125)

trv.bind('<Double 1>', getrow) #When double clicking entry getrow()

#Vertical Scrollbar
yscrollbar = ttk.Scrollbar(wrapper1, orient='vertical', \
command=trv.yview)
yscrollbar.pack(side=RIGHT, fill='y')

#Horizontal Scrollbar
xscrollbar = ttk.Scrollbar(wrapper1, orient='horizontal', \
command=trv.xview)
xscrollbar.pack(side=BOTTOM, fill='x')

trv.configure(yscrollcommand=yscrollbar.set, \
xscrollcommand=xscrollbar.set)

#Pop. Member List Wrapper
query = 'SELECT * FROM members'
cursor.execute(query)
rows = cursor.fetchall()
update(rows)

"""***OPTIONS-WRAPPER2-SECTION***"""
#Search functionality
q = StringVar() #Search Term
lbl = Label(wrapper2, text='Search:')
lbl.pack(side=tk.LEFT, padx=10, pady=20)
ent = Entry(wrapper2, textvariable=q)
ent.pack(side=tk.LEFT, padx=6)
btn = Button(wrapper2, text='Search', command=search)
btn.pack(side=tk.LEFT, padx=6)
clrbtn = Button(wrapper2, text='Clear', command=clear)
clrbtn.pack(side=tk.LEFT, padx=6)

#export as pdf
lbl = Label(wrapper2, text='Options:')
lbl.pack(side=tk.LEFT, padx=10)
expbtn = Button(wrapper2, text='Export as\n PDF', command=export)
expbtn.pack(side=tk.LEFT, padx=6)

#import member details from pdf
impbtn = Button(wrapper2, text='Import Member\n from PDF', \
command=import_member)
impbtn.pack(side=tk.LEFT, padx=6)

"""***BOOKDATA-WRAPPER3-SECTION***"""
t0, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13 = \
StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), \
StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), \
StringVar(), StringVar(), StringVar(), StringVar()
lbl0 = Label(wrapper3, text='Member ID:')
lbl0.grid(row=0, column=0, padx=5, pady=5)
ent0 = Entry(wrapper3, textvariable=t0)
ent0.grid(row=0, column=1, padx=5, pady=5)
lbl1 = Label(wrapper3, text='Member Name:')
lbl1.grid(row=1, column=0, padx=5, pady=5)
ent1 = Entry(wrapper3, textvariable=t1)
ent1.grid(row=1, column=1, padx=5, pady=5)
lbl2 = Label(wrapper3, text='Member Phone:')
lbl2.grid(row=2, column=0, padx=5, pady=5)
ent2 = Entry(wrapper3, textvariable=t2)
ent2.grid(row=2, column=1, padx=5, pady=5)
lbl3 = Label(wrapper3, text='Member Email:')
lbl3.grid(row=3, column=0, padx=5, pady=5)
ent3 = Entry(wrapper3, textvariable=t3)
ent3.grid(row=3, column=1, padx=5, pady=5)
lbl4 = Label(wrapper3, text='Member Address:')
lbl4.grid(row=4, column=0, padx=5, pady=5)
ent4 = Entry(wrapper3, textvariable=t4)
ent4.grid(row=4, column=1, padx=5, pady=5)
lbl5 = Label(wrapper3, text='Member Nationality:')
lbl5.grid(row=5, column=0, padx=5, pady=5)
ent5 = Entry(wrapper3, textvariable=t5)
ent5.grid(row=5, column=1, padx=5, pady=5)
lbl6 = Label(wrapper3, text='Member Category:')
lbl6.grid(row=6, column=0, padx=5, pady=5)
ent6 = Entry(wrapper3, textvariable=t6)
ent6.grid(row=6, column=1, padx=5, pady=5)

lbl7 = Label(wrapper3, text='Member Company:')
lbl7.grid(row=0, column=2, padx=5, pady=5)
ent7 = Entry(wrapper3, textvariable=t7)
ent7.grid(row=0, column=3, padx=5, pady=5)
lbl8 = Label(wrapper3, text='Member Position:')
lbl8.grid(row=1, column=2, padx=5, pady=5)
ent8 = Entry(wrapper3, textvariable=t8)
ent8.grid(row=1, column=3, padx=5, pady=5)
lbl9 = Label(wrapper3, text='Member AccountName:')
lbl9.grid(row=2, column=2, padx=5, pady=5)
ent9 = Entry(wrapper3, textvariable=t9)
ent9.grid(row=2, column=3, padx=5, pady=5)
lbl10 = Label(wrapper3, text='Member IBAN:')
lbl10.grid(row=3, column=2, padx=5, pady=5)
ent10 = Entry(wrapper3, textvariable=t10)
ent10.grid(row=3, column=3, padx=5, pady=5)
lbl11 = Label(wrapper3, text='Member BIC:')
lbl11.grid(row=4, column=2, padx=5, pady=5)
ent11 = Entry(wrapper3, textvariable=t11)
ent11.grid(row=4, column=3, padx=5, pady=5)
lbl12 = Label(wrapper3, text='Member Created:')
lbl12.grid(row=5, column=2, padx=5, pady=5)
ent12 = Entry(wrapper3, textvariable=t12)
ent12.grid(row=5, column=3, padx=5, pady=5)
lbl13 = Label(wrapper3, text='Member Expiry:')
lbl13.grid(row=6, column=2, padx=5, pady=5)
ent13 = Entry(wrapper3, textvariable=t13)
ent13.grid(row=6, column=3, padx=5, pady=5)

#Clear all input fields
clr_btn = Button(wrapper3, text='Clear All', command=clearWrap3Fields)
clr_btn.grid(row=6, column=4, padx=5, pady=5)

upd_btn = Button(wrapper3, text='Update', command=update_memberdata)
add_btn = Button(wrapper3, text='Add New', command=add_new_member)
del_btn = Button(wrapper3, text='Delete', command=delete_memberdata)
sav_btn = Button(wrapper3, text='Save Changes', command=save_db_changes)
upd_btn.grid(row=8, column=0, padx=5, pady=3)
add_btn.grid(row=8, column=1, padx=5, pady=3)
del_btn.grid(row=8, column=2, padx=5, pady=3)
sav_btn.grid(row=8, column=3, padx=5, pady=3)

#tkinter window setup and run
root.title('FFIreland Membership Management System')
root.geometry('750x750')
root.mainloop()
