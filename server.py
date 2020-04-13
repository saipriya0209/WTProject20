from flask import Flask, request, send_file, make_response
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
from json import dumps
import json
from flask_jsonpify import jsonify
import sqlite3
from sqlite3 import Error
import requests

app = Flask(__name__)
api = Api(app)

CORS(app)

def create_connection(db_file):
  conn = None
  conn = sqlite3.connect(db_file)
  return conn

def create_table(conn, create_table_sql):
  try:
      c = conn.cursor()
      c.execute(create_table_sql)
      conn.commit()
  except Error as e:
      print(e)

@app.route("/")
def hello():
    return jsonify({'text':'Hello World!'})

@app.route("/checkuser", methods=["POST"])
def check():
  email = request.get_json()["email"]
  password = request.get_json()["password"]
  table_name = request.get_json()["account_type"]
  if(table_name == "organiser"):
    query = "SELECT * FROM organisers WHERE email = '" + email + "' AND password  = '" + password + "';"
  else:
    query = "SELECT * FROM students WHERE email = '" + email + "' AND password  = '" + password + "';"
  database = r"pythonsqlite.db"
  conn = create_connection(database)
  c = conn.cursor()
  c.execute(query)
  rows = c.fetchall()
  if(len(rows) == 1 and table_name == "organiser"):
    return {'first_name': rows[0][1], 'email': email, 'o_id': rows[0][0]}
  elif(len(rows) == 1 and table_name == "student"):
    return {'first_name': rows[0][1], 'email': email, 's_id': rows[0][0]}
  else:
    return {'message':'Invalid credentials'}

@app.route("/newuser", methods=["POST"])
def new_user():
  try:
    first_name = request.get_json()["first_name"]
    last_name = request.get_json()["last_name"]
    email = request.get_json()["email"]
    password = request.get_json()["password"]
    phone_no = request.get_json()["phone_no"]
    query = "SELECT * FROM students WHERE email = '" + email + "';"
    database = r"pythonsqlite.db"
    conn = create_connection(database)
    c = conn.cursor()
    c.execute(query)
    rows = c.fetchall()
    d = dict()
    if(len(rows) == 0):
      query = "INSERT INTO students(first_name, last_name, email, password, phone_no) VALUES('" + first_name + "', '" + last_name + "', '" + email + "','" + password + "'," + phone_no + ");"
      c = conn.cursor()
      c.execute(query)
      d["result"] = "successful"
    else:
      d["result"] = "failed"
    conn.commit()
    return jsonify(d)
  except:
    d = dict()
    d["result"] = "failed"
    return jsonify(d)

@app.route("/newevent", methods=["POST"])
def new_event():
    event_name = request.get_json()["event_name"]
    event_type = request.get_json()["event_type"]
    max_par = request.get_json()["max_par"]
    fee = request.get_json()["fee"]
    max_teams = request.get_json()["max_teams"]
    venue = request.get_json()["event_venue"]
    event_date = request.get_json()["event_date"]
    o_id = request.get_json()['o_id']
    funds = request.get_json()['funds']
    database = r"pythonsqlite.db"
    conn = create_connection(database)
    c = conn.cursor()
    #change the value of o_id
    query = " INSERT INTO event(o_id, funds, e_name, o_id, e_type, e_date, e_venue, e_fee, e_tsize, e_maxpar) VALUES(" + str(o_id) + "," + str(funds) + ",'" + event_name + "', 1, '" + event_type + "','" + event_date + "','" + venue + "'," + str(fee) + "," + str(max_par) + "," + str(max_teams) + ");"
    c.execute(query)
    conn.commit()
    return jsonify({"done":"done"})

@app.route("/listevents", methods=["POST"])
def all_events():
  try:
    o_id = request.get_json()["o_id"]
    database = r"pythonsqlite.db"
    conn = create_connection(database)
    c = conn.cursor()
    query = " SELECT * FROM event WHERE o_id = " + str(o_id) + ";"
    c.execute(query)
    rows = c.fetchall()
    return jsonify(rows)
  except:
    return

@app.route('/allocatefunds', methods=["POST"])
def allocate_funds():
  o_id = request.get_json()["o_id"]
  e_id = request.get_json()["e_id"]
  amount = request.get_json()["amount"]
  reason = request.get_json()["reason"]
  database = r"pythonsqlite.db"
  conn = create_connection(database)
  c = conn.cursor()
  query = "SELECT * FROM event WHERE e_id = " + str(e_id) + ";"
  c.execute(query)
  rows = c.fetchall()
  total_amount = rows[0][1]
  query = "SELECT * FROM funds where e_id = " + str(e_id) + ";"
  c.execute(query)
  rows = c.fetchall()
  already_spent = 0
  for row in rows:
    already_spent += row[2]
  if(total_amount - already_spent >= int(amount)):
    query = "INSERT INTO funds(e_id, amount, reason) VALUES(" + str(e_id) + ", " + str(amount) + ", '" + reason + "');"
    c.execute(query)
    conn.commit()
    return jsonify({"message": "successful"})
  else:
    return jsonify({"message": "funds insufficient"})

@app.route('/fund_rem', methods=["POST"])
def fund_rem():
  e_id = request.get_json()["e_id"]
  database = r"pythonsqlite.db"
  conn = create_connection(database)
  c = conn.cursor()
  query = "SELECT * FROM event WHERE e_id = " + str(e_id) + ";"
  c.execute(query)
  rows = c.fetchone()
  funds_given = rows[1]
  query = "SELECT * FROM funds WHERE e_id = " + str(e_id) + ";"
  c.execute(query)
  rows = c.fetchall()
  spent = 0
  for row in rows:
    spent += row[2]
  send_back = {"rem_funds": funds_given - spent}
  return jsonify(send_back)

@app.route('/event_log', methods=["POST"])
def event_log():
  e_id = request.get_json()["e_id"]
  database = r"pythonsqlite.db"
  conn = create_connection(database)
  c = conn.cursor()
  query = "SELECT * FROM funds WHERE e_id = " + str(e_id) + ";"
  c.execute(query)
  rows = c.fetchall()
  if(rows):
    return jsonify({"data": rows})
  else:
    return jsonify({})

@app.route('/totalprofit', methods=["POST"])
def total_profit():
  o_id = request.get_json()["o_id"]
  database = r"pythonsqlite.db"
  conn = create_connection(database)
  c = conn.cursor()
  query = "SELECT * FROM event WHERE o_id = " + str(o_id) + ";"
  c.execute(query)
  rows = c.fetchall()
  total_profit_made = []
  rows.sort(key = lambda x : x[5])
  print(rows)
  objects = []
  for row in rows:
    req = requests.post("http://127.0.0.1:5000/eventprofit", json = {"e_id":row[0]}).json()
    profit = req["profit"]
    objects.append({"label":row[2], "y":profit})
  return jsonify(objects)

@app.route('/eventprofit', methods=["POST"])
def event_profit():
  e_id = request.get_json()["e_id"]
  database = r"pythonsqlite.db"
  conn = create_connection(database)
  c = conn.cursor()
  query = "SELECT * FROM event WHERE e_id = " + str(e_id) + ";"
  c.execute(query)
  rows = c.fetchall()
  cost_per_reg = rows[0][7]
  query = "SELECT * FROM registration WHERE e_id = " + str(e_id) + ";"
  c.execute(query)
  rows = c.fetchall()
  total_from_reg = cost_per_reg * len(rows)
  req = requests.post("http://127.0.0.1:5000/fund_rem", json = {"e_id":e_id}).json()
  total = total_from_reg + req["rem_funds"]
  return jsonify({"profit": total})

@app.route('/allocateprize', methods=["POST"])
def give_prize():
  r_id = request.get_json()["r_id"]
  prize = request.get_json()["prize"]
  e_id = request.get_json()["e_id"]
  database = r"pythonsqlite.db"
  conn = create_connection(database)
  c = conn.cursor()
  query = "SELECT * FROM registration WHERE r_id = " + str(r_id) + " AND e_id = " + str(e_id) + ";"
  c.execute(query)
  rows = c.fetchall()
  if(len(rows) != 0):
    query = "UPDATE registration SET prize = '" + prize + "' WHERE r_id = " + str(r_id) + ";"
    c.execute(query)
    conn.commit()
    return jsonify({"message":"successful"})
  else:
    return jsonify({"message":"unsuccessful"})

@app.route('/event_comp', methods=["POST"])
def event_complete():
  e_id = request.get_json()["e_id"]
  database = r"pythonsqlite.db"
  conn = create_connection(database)
  c = conn.cursor()
  query = "SELECT * FROM registration WHERE e_id = " + str(e_id) + ";"
  c.execute(query)
  rows = c.fetchall()
  if(len(rows) != 0):
    for row in rows:
      if(row[3] == '-'):
        query = "UPDATE registration SET prize = 'No Prize' WHERE r_id = " + str(row[0]) + ";"
        c.execute(query)
        conn.commit()
  return jsonify({})

@app.route('/show_reg', methods=['POST'])
def show_reg():
  e_id = request.get_json()["e_id"]
  database = r"pythonsqlite.db"
  conn = create_connection(database)
  c = conn.cursor()
  query = "SELECT * FROM registration WHERE e_id = " + str(e_id) + ";"
  c.execute(query)
  rows = c.fetchall()
  d = []

  r_id = []
  s_id = []
  person_registered = []
  team_mate_names = []
  prize = []
  i = 0
  if(rows):
    for row in rows:
      r_id.append(row[0])
      s_id.append(row[2])
      prize.append(row[3])
      query = "SELECT * FROM students WHERE s_id=" + str(row[2]) + ";"
      c.execute(query)
      row_x = c.fetchone()
      person_registered.append(row_x[1])
      query = "SELECT * FROM rteam WHERE id=" + str(row[0]) +";"
      c.execute(query)
      rows1 = c.fetchone()
      team_mate_names.append([])
      if(rows1):
        team_mate_id = eval(rows1[1])
        for id in team_mate_id:
          query = "SELECT * FROM students WHERE s_id=" + str(id) + ";"
          c.execute(query)
          row2 = c.fetchone()
          team_mate_names[i].append(str(row2[1]))
        i = i + 1
  for x in range(len(s_id)):
    d.append({"r_id": r_id[x], "s_id": s_id[x], "s_name": person_registered[x], "team_mates": team_mate_names[x], "prize": prize[x]})
  print(d)
  return jsonify({"data": d})

@app.route('/no_of_reg', methods=['POST'])
def showw_reg():
  o_id = request.get_json()["o_id"]
  database = r"pythonsqlite.db"
  conn = create_connection(database)
  c = conn.cursor()
  query = "SELECT * FROM event WHERE o_id = " + str(o_id) + ";"
  event_name = []
  no_of_reg = []
  c.execute(query)
  rows = c.fetchall()
  if(rows):
    rows.sort(key = lambda x : x[5])
    for row in rows:
      event_name.append(row[2])
      query = "SELECT * FROM registration WHERE e_id = " + str(row[0]) + ";"
      c.execute(query)
      rows = c.fetchall()
      no_of_reg.append(len(rows))
  objects = []
  if(len(event_name) != 0):
    for x in range(len(event_name)):
      objects.append({"label": event_name[x], "y": no_of_reg[x]})
  return jsonify(objects)




database = r"pythonsqlite.db"
# write queries for creating tables here
create_students_table = """CREATE TABLE IF NOT EXISTS students (
    s_id INTEGER PRIMARY KEY AUTOINCREMENT, first_name text NOT NULL, last_name text NOT NULL, email text NOT NULL UNIQUE, password text NOT NULL, phone_no int(10) NOT NULL, stream text); """
create_orgainsers_table = """CREATE TABLE IF NOT EXISTS organisers (o_id INTEGER PRIMARY KEY AUTOINCREMENT, first_name text NOT NULL, last_name text NOT NULL, email text NOT NULL UNIQUE, password text NOT NULL, phone_no int(10) NOT NULL); """
create_hobbies_table = """CREATE TABLE IF NOT EXISTS hobbies (id INTEGER PRIMARY KEY AUTOINCREMENT, student_id INTEGER, hobby text, FOREIGN KEY (student_id) REFERENCES students(s_id)) """
create_event_table = """ CREATE TABLE IF NOT EXISTS event( e_id INTEGER PRIMARY KEY AUTOINCREMENT, funds INTEGER NOT NULL, e_name VARCHAR(100) NOT NULL, o_id INTEGER NOT NULL, e_type VARCHAR(100) NOT NULL, e_date DATETIME NOT NULL, e_venue VARCHAR(300) NOT NULL, e_fee INTEGER, e_tsize INTEGER, e_maxpar INTEGER, FOREIGN KEY (o_id) REFERENCES organiser(id));"""
create_registration_table = """CREATE TABLE IF NOT EXISTS registration (r_id INTEGER PRIMARY KEY AUTOINCREMENT,  e_id INTEGER NOT NULL, s_id INTEGER NOT NULL, prize VARCHAR(100) DEFAULT '-', FOREIGN KEY (s_id) REFERENCES student(s_id), FOREIGN KEY (e_id) REFERENCES event(e_id));"""
create_registrationteam_table = """CREATE TABLE IF NOT EXISTS rteam (id INTEGER PRIMARY KEY, members VARCHAR(200) NOT NULL, FOREIGN KEY (id) REFERENCES registration(r_id));"""
create_funds_table = """CREATE TABLE IF NOT EXISTS funds (id INTEGER PRIMARY KEY AUTOINCREMENT, e_id INTEGER, amount INTEGER, reason TEXT, FOREIGN KEY (e_id) REFERENCES event(e_id));"""
#create_updates_table = """CREATE TABLE IF NOT EXISTS updates (id INTEGER PRIMARY KEY AUTOINCREMENT, o_id INTEGER, r_id INTEGER, FOREIGN KEY (o_id) REFERENCES organisers(id) , FOREIGN KEY (r_id) REFERENCES registration(r_id));"""
#create_create_event_table = """CREATE TABLE IF NOT EXISTS creates (id INTEGER PRIMARY KEY AUTOINCREMENT, o_id INTEGER, e_id INTEGER, FOREIGN KEY (o_id) REFERENCES organisers(o_id), FOREIGN KEY (e_id) REFERENCES event(e_id));"""

conn = create_connection(database)
if conn is not None:
  # execute queries for creating tables here
  create_table(conn, create_students_table)
  create_table(conn, create_orgainsers_table)
  create_table(conn, create_hobbies_table)
  create_table(conn, create_event_table)
  create_table(conn, create_registration_table)
  create_table(conn, create_registrationteam_table)
  create_table(conn, create_funds_table)
  #create_table(conn, create_updates_table)
  #create_table(conn, create_create_event_table)
else:
    print("Error! Cannot create the database connection")

if __name__ == "__main__":
  app.debug = True
  app.run()
