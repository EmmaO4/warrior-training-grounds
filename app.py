from flask import Flask, render_template, redirect, url_for, session, request
import os
import uuid
import msal
from dotenv import load_dotenv

app = Flask(__name__)

# MS Azure login info
app.secret_key = os.environ.get("FLASK_SECRET_KEY")
CLIENT_ID = os.environ.get("AZURE_CLIENT_ID")
CLIENT_SECRET = os.environ.get("AZURE_CLIENT_SECRET")
TENANT_ID = os.environ.get("AZURE_TENANT_ID")

AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
REDIRECT_PATH = "/callback"  
SCOPE = ["User.Read"]


# home page
@app.route('/')
def home():
    return render_template('index.html')

"""
 using single-tenant-only option to sim school SSO since they have a db of all student
 logins. This means only recognized n manually inserted users will be allowed on this
 app. For testing, Azure Active Directory owner will add specific test user to Directory
 -- make a testing MS acc for this for security of personal MS accounts.

 FOR NOW USE: warriortesteruser1@raulesquerra18gmail.onmicrosoft.com. credentials in .env 

 API MESSAGE SHOWS WHEN NOT ADDED TO DIR: 'AADSTS50020: User account '<user email>' from identity provider 'live.com' does not exist 
  in tenant 'Default Directory' and cannot access the application 'fe0e0a8f-50e2-47e6-a8a3-17489660c3d0'(warrior-training-grounds) in 
  that tenant.The account needs to be added as an external user in the tenant first. Sign out and sign in again with a different Azure 
  Active Directory user account.
"""
# signin page using personal MS Azure Entra ID
@app.route('/signin')
def signin():
    session["state"] = str(uuid.uuid4())  
    auth_url = _build_msal_app().get_authorization_request_url(
        SCOPE,
        state=session["state"],
        redirect_uri=url_for("callback", _external=True)
    )
    return redirect(auth_url)

# user dashboard ONLY after signing in
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# implem req -- terminate user session
@app.route('/signout')
def signout():
    return "signed out implementation goes here. should only be accessed from signed in session. currently can manually url this page"

@app.route(REDIRECT_PATH)
def callback():
    if request.args.get("state") != session.get("state"):
        return "State mismatch"

    code = request.args.get("code")
    result = _build_msal_app().acquire_token_by_authorization_code(
        code,
        scopes=SCOPE,
        redirect_uri=url_for("callback", _external=True)
    )

    if "id_token_claims" in result:
        session["user"] = result["id_token_claims"]
        return redirect(url_for("dashboard"))

    return "Login failed"

def _build_msal_app():
    return msal.ConfidentialClientApplication(
        CLIENT_ID,
        authority=AUTHORITY,
        client_credential=CLIENT_SECRET
    )