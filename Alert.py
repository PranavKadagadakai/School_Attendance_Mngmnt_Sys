import mysql.connector as a
import smtplib
import database

# Establish the database connection
con = a.connect(host='localhost', password='', user='') # Enter username, password, and host of your MySQL

# Create cursor
c = con.cursor()
database.create_DB(con)


def send_email():
    # Set up the SMTP server
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    email_ = ''# Add your email id here
    pass_ = '' # Enter your email's app password
    s.login(email_, pass_)

    # Execute the SQL query
    c.execute('''
    SELECT p.email, s.student_name,s.student_id
    FROM student s 
    JOIN parent p ON s.parent_id = p.parent_id 
    WHERE s.student_id IN (
        SELECT student_id 
        FROM attendance 
        WHERE status = 'A'
    )
    ''')
    emails = c.fetchall()

    # Loop through the fetched emails and send notifications
    for e in emails:
        email_address = e[0]
        student_name = e[1]
        subj = "In regards to your ward's absence"
        msg = f'Dear Sir/Madam,\n\nYour ward {student_name} is absent for today\'s classes.\n\nFMS Team'
        msg = "Subject: {}\n\n{}".format(subj, msg)

        s.sendmail(email_, email_address, msg)

        c.execute('''
        INSERT INTO alert (message, sent_to, student_name, student_id) 
        VALUES (%s, %s, %s, %s)
        ''', (msg, e[0], e[1], e[2]))
        con.commit()

    # Check SMTP status
    chk = s.ehlo()
    s.quit()
    if chk[0] == 250:
        return 's'
    else:
        return 'f'




# Call the function
send_email()
