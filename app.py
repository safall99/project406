from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Connect to MySQL database
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Changeme22@',
    database='concert_booking'
)

# Sample data for available concerts
# Remove the sample data since we'll be fetching it from the database

@app.route('/')
def index():
    # Fetch concerts from the database
    cursor = db.cursor()
    cursor.execute('SELECT * FROM concerts')
    concerts = cursor.fetchall()
    cursor.close()
    
    return render_template('index.html', concerts=concerts)

@app.route('/confirm/<int:concert_id>', methods=['GET', 'POST'])
def confirm(concert_id):
    # Fetch concert details from the database
    cursor = db.cursor()
    cursor.execute('SELECT * FROM concerts WHERE id = %s', (concert_id,))
    concert = cursor.fetchone()
    cursor.close()

    if not concert:
        return 'Concert not found'

    if request.method == 'POST':
        # Process ticket booking
        tickets_requested = int(request.form.get('tickets'))
        if tickets_requested <= concert[3]:  # Assuming tickets column is at index 3
            # Update the tickets available in the database
            updated_tickets = concert[3] - tickets_requested
            cursor = db.cursor()
            cursor.execute('UPDATE concerts SET tickets = %s WHERE id = %s', (updated_tickets, concert_id))
            db.commit()
            cursor.close()
            return 'Your tickets have been booked successfully!'
        else:
            return 'Insufficient tickets available'
    else:
        return render_template('confirmation.html', concert=concert)

if __name__ == '__main__':
    app.run(debug=True)

