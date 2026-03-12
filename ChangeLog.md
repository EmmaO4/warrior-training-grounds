ENTRY FORMATTING
    Timestamp (current day) - name/sig:    
    list files touched by explicit file name:
        main.login():    
            change made
        ...
        optimization made
        yada yada                                                       
######################################################################
!!!!!! The following is the first entry to serve as an example. Entries are inputed top -> down!!!!!!

3.1.26 -r:
    static/style.css:
        created css file for future development
    templates/index.html:
        created rudimentary html file for testing flask wsgi get
    app.py:
        created runner file for entrypoint of app to run 
    ChangeLog.md:
        created this file and entry for 3.1.26
    flask-setup.md:
        created flask setup file to help people run flask on vscode specifically
    StanStant CSClub Hackathon Flyer:
        Hackathon flyer showing relevant info and initial project ideations
    pgAdmin4-notes.txt:
        created notes for navigation of PostgreSQL pgAmin GUI to view tables created by db
    README.md
        Full project overview 
    requirements.txt
        app dependencies    
######################################################################
3.12.26 -r:
    app.py:
        imported module: datetime
        [].signout():
            added session clearing for app n MS account when signing out to properly sign out due to inactivity or by choice
        [].inactivity_signout():
            template render for inactivity-signout.html file
    inactivity-signout.html:
        created file to handle sign out due to inactivity
        [].check_inactivity():
            function to check user inactivity. Inactivity works by checking the last HTTP request sent by interaction 
    dashboard.html:
        added refresh button to send HTTP request for testing inactivity. could've just refreshed the page but added this just cause fuq it    
    TODO.txt:
        added compartmentalizing config.py for configuration of app to agenda. Marked some stuff as done    

3.3.26 -r:
    made comments to understand backend logic in app.py 
    notes/signin-auth-workflow.txt:
        created note to help understand auth workflow from backend engineering perspective
    dashboard.html:
        injected username to display from passed argument from dashboard backend for page personalization
    [].dashboard():
        created login logic for unique users for personalized dashboards
    []._build_msal_app(cache=None):
        passed in addtional argumenbt, cache, to store user session state
    sandbox.py:
        created file for testing stuff
    
3.2.26 -r:
    TODO.txt:
        created file and added some stuff to agenda for bookkeeping
    .gitignore:
        created ignore file to prevent pushing sensitive creds to github
    .env:
        created .env file to store secrets and credentials
    requirements.txt:
        added dependencies:
            msal
            dotenv
            + affiliated dependencies that came with them
    tempalates/dashboard.html:
        created file for user after signing in through SSO sim
    notes/:
        created folder to record notes on some processes to streamline interaction
    app.py:
        imported dependencies: os, uuid, msal, dotenv
        added MS Azure secrets and api calling
        [].signin():
            create user session for api logic 
        [].dashboard():
            dashboard html template render 
        [].signout():
            implem req. will terminate user session to prevent manual URLing page 
        [].callback():
            api logic. understand this with more fidelity
        []._build_msal_app():
            api logic. understand this with more fidelity
    notes/secrets-sharing.txt:
        created file for info and directions on accessing secret keys needed for Azure SSO API