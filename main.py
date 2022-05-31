from flask import Flask, render_template, request
import sqlite3
from datetime import datetime
from database import Database
from calculator import *

app = Flask(__name__)
database = Database('database.db')

def setup_database():
    database.execute_query_from_file('event.sql')
    database.execute_query_from_file('ticket_type.sql')
    database.execute_query_from_file('ticket.sql')
        
@app.route('/')
def home():
    events = database.select('SELECT id, name FROM Event')
    return render_template("home.html", events = events)

@app.route('/event/<int:event_id>')
def event(event_id):
    event_info = database.select(f'SELECT * FROM Event WHERE id = {event_id}')
    return render_template("event.html", event_info = event_info[0])

@app.route('/return_ticket')
def return_ticket_form():
    return render_template("return_ticket.html")
    
@app.route('/check_ticket', methods = ['POST', 'GET'])
def check_ticket():
    if request.method == 'POST':
        try:
            ticket_id = request.form['ticket_id']            
            result = calculate_sum(ticket_id)

            if (not result.isnumeric()):
                return result

            if (result == 0):
                return "Too late. Can't return the ticket price!"
            
            database.execute(f"DELETE FROM ticket WHERE id = {ticket_id};")
            return "The ticket has been successfully returned. You can collect {result} from our office."
        
        except:
            return "Error: can't return the ticket!"

@app.route('/event/<int:event_id>/tickets_list')
def tickets_list(event_id):
    tickets = database.select(f'''SELECT * FROM ticket WHERE
                              event_id = {event_id}''')
    return render_template('tickets_list.html', tickets = tickets)

def main():
    setup_database()
    app.run(debug=True)

    

if __name__ == '__main__':
    main()
