# Create session on login
import random
import string
import sqlite3
import time
import sys
import settings

cpf = sys.argv[1]
role = sys.argv[2]
def id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

# Database

dB = sqlite3.connect(settings.db)
cur = dB.cursor()

# Enter the login details into database

sess_id = id_generator()
log_in = time.strftime('%Y-%m-%d %H:%M;%S')
cur.execute('''INSERT INTO sessions (sess_id, cpf, role, log_in, active) VALUES (?,?,?,?,?)''', (sess_id, cpf, role, log_in, 1))
dB.commit()

print(sess_id)