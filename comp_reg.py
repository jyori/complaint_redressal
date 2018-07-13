# Code for creation of a new complaint

import sys
import sqlite3
import settings
import time
import random

dB = sqlite3.connect(settings.db)
cur = dB.cursor()

# Obtain user details using session ID

session = sys.argv[1]
cpf_data = cur.execute('''SELECT cpf FROM sessions where sess_id = ?''',\
 (session,))
cpf = str(cpf_data.fetchone()[0])
user_data = cur.execute('''SELECT department from users where cpf = ?''',\
 (cpf,))
from_department = user_data.fetchone()[0]

# Obtain infromation regarding the complaint

to_department = sys.argv[2]
i = 3
content = ''
try:
	content += sys.argv[i]
	content += ' '
	i += 1
except:
	pass
time = time.strftime('%Y-%m-%d %H:%M;%S')
comp_id = from_department[0] + to_department[0] + str(random.randint(10000, 99999))

# Register complaint

cur.execute('''INSERT into complaints (num, cpf, from_deptt, for_deptt,\
 content, comp_time) VALUES (?,?,?,?,?,?)''', (comp_id, cpf, from_department,\
  to_department, content, time,))

cur.execute('''INSERT into status (comp_num, created_on) VALUES (?,?)''',\
 (comp_id, time, ))

dB.commit()

print(1)