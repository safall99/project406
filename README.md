# project406


This project is a Flask-based web application that allows users to view and book tickets for various concerts. It utilizes a MySQL database to store information about the available concerts, including the artist, venue, and number of tickets. 

The application consists of two main routes:
1. The homepage ("/") displays a list of available concerts fetched from the MySQL database. Users can see the artist, venue, and the number of remaining tickets for each concert.
2. The confirmation route ("/confirm/<int:concert_id>") allows users to select a specific concert and confirm their ticket booking. The route handles both GET and POST requests. GET requests display a confirmation page with details about the concert. POST requests process the ticket booking, reducing the available tickets if there are enough available.

It uses Flask's templating system to render HTML templates for the different routes. The templates are designed to display the concert information and provide a form for users to enter the number of tickets they want to book. Once the booking is submitted, appropriate feedback messages are displayed based on the availability of tickets.

Overall, this project provides a simple and interactive web interface for users to browse and book concert tickets, while also demonstrating the integration of Flask with a MySQL database for data storage and retrieval.
