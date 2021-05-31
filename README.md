# Membership-GUI-App
Simple TKinter GUI for managing sqlite3 membership database in Python

### High Level Information
The “Members GUI App” was developed with Python with the aim of creating a comprehensive and easy-to-use management interface for our Membership services.

***Python Dependencies:
- tkinter
- sqlite3 (Intrinsic)
- docxtpl
- docx2pdf

The main structure of the app is as follows:
- Member data (Name, Phone, Email, Address, Nationality, Member Category ) is contained within SQLite3 local database file
- This database is loaded into Python GUI app (TKinter)
- Python GUI app displays database entries with functionality to:
- Search through database
- Update, Add, and Delete entries
- Export data from database to PDF file for sharing (Web, email, etc...)

Program consists of various Python scripts and resource files:
- members_gui.py (Main Program): Displays Python GUI for interacting with database
- init_member_db.py: Creates the initial database file for use within main program.
- export_members_pdf.py: Convert members database to pdf
- schema.sql: SQL structure of database
- member-list-template.docx: Word doc template for formatting PDF created
- members.db: Members database
