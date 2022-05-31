import sqlite3
from datetime import datetime
from database import Database

def calculate_sum(ticket_id):
    database = Database('database.db')
    
    if (not ticket_id.isnumeric()):
        return "Error: can't find the ticket!"

    if (int(ticket_id) < 0 or int(ticket_id) > 35):
        return "Error: can't find the ticket!"

    
    ticket_data = database.select(f'SELECT * from ticket WHERE id = {ticket_id}')[0]

    if (not ticket_data):
        return "Error: can't find the ticket!"

    if (ticket_data[-1] == 1):
        return "Error: you can't return an unpurchased ticket!"
    
    event_date_time = database.select(f'SELECT date, time FROM event WHERE id = {ticket_data[1]}')[0]

    fmt = "%d-%m-%Y %H:%M:%S"
    event_date = str(event_date_time[0]) + " " + str(event_date_time[1] + ":00")
    event_date = datetime.strptime(event_date, fmt)
    print(event_date)
    now_date = datetime.today().strftime(fmt)
    now_date = datetime.strptime(now_date, fmt)
    
    date_diff = event_date - now_date
    date_diff_m = (date_diff.days * 24 * 60) + (date_diff.seconds / 60)
    
    if (date_diff_m <= 0):
        return 0
    
    ticket_type = int(ticket_data[2])
    ticket_price = float(ticket_data[3])
    
    month_m = 31 * 24 * 60
    two_week_m = 14 * 24 * 60
    week_m = 7 * 24 * 60
    day_m = 24 * 60
    
    coef = {1: [1, 0.75, 0.5, 0.25],
              2: [1, 0.5, 0.25, 0.1],
              3: [1, 0.25, 0.1, 0.05]}

    result = 0
    
    if (date_diff_m > month_m):
        return ticket_price * coef[ticket_type][0]
    if (date_diff_m > two_week_m):
        return ticket_price * coef[ticket_type][1]
    if (date_diff_m > week_m):
        return ticket_price * coef[ticket_type][2]
    if (date_diff_m > day_m):
        return ticket_price * coef[ticket_type][3]

    return 0
