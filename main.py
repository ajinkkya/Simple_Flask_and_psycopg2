from config import *


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# Create - 'Crud'
# Endpoint for "Insert Record"
@app.route('/insert/<int:emp_id>/<string:emp_name>/<string:Emp_Phone_no>/<string:emp_email>/<string:cration_date>/<string:is_active>', methods=['GET', 'POST'])
def insert(emp_id, emp_name, Emp_Phone_no, emp_email, cration_date, is_active):
    # 121/ganesh chudhari/1243548798/ganesh@gmail.com/2019-01-05/TRUE
    
    try:
        with psycopg2.connect(
                host=hostname,
                dbname=database,
                user=username,
                password=password,
                port=port_id) as conn:

            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                if emp_id and emp_name and Emp_Phone_no and emp_email and cration_date and is_active:
                    cur.execute('INSERT INTO employees(EMP_ID, EMP_NAME, emp_phone_no, EMP_EMAIL_ID, CREATION_DATE, IS_ACTIVE) VALUES (%s, %s, %s, %s, %s, %s)',
                                (emp_id, emp_name, Emp_Phone_no, emp_email, cration_date, is_active))
                    
                    
                    conn.commit()

    except Exception as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return f'For EMP ID - "{emp_id}", named - "{emp_name}". Record is submitted in Database successfully!'

# Read - 'cRud'
# Endpoint for "Read Record"
@app.route('/read/<int:emp_id>', methods=['GET', 'POST'])
def read(emp_id):

    try:
        with psycopg2.connect(
                host=hostname,
                dbname=database,
                user=username,
                password=password,
                port=port_id) as conn:

            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:

                cur.execute(f"SELECT * FROM employees WHERE emp_id = {emp_id}")
                for record in cur.fetchall():
                    recordDict = {
                        "Emp_Id": record['emp_id'],
                        "Emp_Name": record['emp_name'],
                        "Emp_Phone_no": record['emp_phone_no'],
                        "Emp_Email_ED": record['emp_email_id'],
                        "Creation Date": record['creation_date'],
                        "Is_Active": record['is_active']
                    }

    except Exception as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return jsonify(recordDict)

# Update - 'crUd'
# Endpoint for "Update Record"
@app.route('/update/<int:emp_id>/<string:Emp_Phone_no>/<string:emp_email>', methods=['GET', 'POST'])
def update(emp_id, Emp_Phone_no, emp_email):
    
    try:
        with psycopg2.connect(
                    host = hostname,
                    dbname = database,
                    user = username,
                    password = password,
                    port = port_id) as conn:

            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                
                if emp_id and Emp_Phone_no and emp_email:
                    update_script = f"UPDATE employees SET emp_phone_no = {Emp_Phone_no}, EMP_EMAIL_ID = {emp_email} WHERE emp_id = {emp_id}"
                    cur.execute(update_script)
                    
                    conn.commit()
                
    except Exception as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return f'''For EMP ID - "{emp_id}",\n
            Record is Updated in Database successfully!\n
            For Phone No - "{Emp_Phone_no},\n
            For Email Address "{emp_email}".'''
    
# Delete - 'cruD'
# Endpoint for "Delete Record"
@app.route('/delete/<int:emp_id>>', methods=['GET', 'POST'])
def delete(emp_id):
    
    try:
        with psycopg2.connect(
                    host = hostname,
                    dbname = database,
                    user = username,
                    password = password,
                    port = port_id) as conn:

            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                
                if emp_id:
                    cur.execute(f'DELETE FROM employees WHERE emp_id = {emp_id}')
                    
                    conn.commit() 
                
    except Exception as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return f'For EMP ID - "{emp_id}", Record is Deleted from Database successfully!'

if __name__ == "__main__":
    app.run(debug=True)