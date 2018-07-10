# Database creation code. Use the relevant part of the code for creating the
# required table and comment out the code for the tables which are not required

import sqlite3
import settings

# Database initialzion

dB = sqlite3.connect(settings.db)
cur = dB.cursor()

# Table creation code

# Users table

cur.execute('''CREATE table users (id INTEGER AUTO INCREMENT, cpf INTEGER \
	PRIMARY KEY, first_name TEXT REQUIRED, surname TEXT REQUIRED, email TEXT\
	 REQUIRED, contact NUMBER REQUIRED, department TEXT REQUIRED)''')

dB.commit()

# Complaints table

cur.execute(''' CREATE table complaints (id INTEGER AUTO INCREMENT, num TEXT\
 PRIMARY KEY, cpf INTEGER REQUIRED, from_deptt TEXT REQUIRED, for_deptt TEXT\
  REQUIRED, content TEXT REQUIRED, comp_time time REQUIRED)''')

dB.commit()

# Complaint status table

cur.execute('''CREATE table status (id INTEGER AUTO INCREMENT, comp_num TEXT\
 PRIMARY KEY, created_on time REQUIRED, approved_on time, under_process_on\
  time, resolved_on time)''')

dB.commit()

# Session table

cur.execute('''CREATE table sessions (id INTEGER AUTO INCREMENT, sess_id TEXT\
 PRIMARY KEY, cpf NUMBER REQUIRED, role INTEGER REQUIRED, log_in time\
  REQUIRED, active INTEGER REQUIRED)''')

dB.commit()

# Department heads table

cur.execute('''CREATE table dheads (id INTEGER AUTO INCREMENT, cpf INTEGER \
	PRIMARY KEY, first_name TEXT REQUIRED, surname TEXT REQUIRED, email TEXT\
	 REQUIRED, contact NUMBER REQUIRED, department TEXT REQUIRED)''')

dB.commit()

# Complaint heads table

cur.execute('''CREATE table cheads (id INTEGER AUTO INCREMENT, cpf INTEGER \
	PRIMARY KEY, first_name TEXT REQUIRED, surname TEXT REQUIRED, email TEXT\
	 REQUIRED, contact NUMBER REQUIRED, department TEXT REQUIRED)''')

dB.commit()




