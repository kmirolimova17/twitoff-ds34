from flask import Flask, render_template
from .models import DB, User, Tweet 

def create_app():

    app = Flask(__name__)

    # configuration variable to our app
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Connect our database to the app object 
    DB.init_app(app)

    @app.route("/")
    def home_page():
        # query for all users in the database
        users = User.query.all()
        return render_template('base.html', title='Home', users=users)

    @app.route('/populate')
    # Test my database functionality 
    # by inserting some fake data into the DB
    def populate():

        # Reset the DB first 
        # remove everything from the DB
        DB.drop_all()
        # recreate User and Tweet tables
        # so that they're ready to be used (inserted into)
        DB.create_all()
        
        # Make two new users
        kamila = User(id=1, username='komilamirolimova')
        ryan = User(id=2, username='ryanallred')
        # Make two tweets
        tweet1 = Tweet(id=1, text="this is ryan's tweet", user=ryan)
        tweet2 = Tweet(id=2, text="this is kamila's tweet", user=kamila)

        # Inserting into the DB when working with SQLite directly
        DB.session.add(kamila)
        DB.session.add(ryan)
        DB.session.add(tweet2)
        DB.session.add(tweet1)

        # Commit the DB changes
        DB.session.commit()

        return render_template('base.html', title='Populate')
        # Make two tweets and attach the tweets to the users 

    @app.route('/reset')
    def reset():
        # Do some database stuff
        # Drop old DB Tables
        # Remake new DB Tables
        # remove everything from the DB
        DB.drop_all()
        # recreate User and Tweet tables
        # so that they're ready to be used (inserted into)
        DB.create_all()
        
        return render_template('base.html', title='Reset Database')
    
    return app
