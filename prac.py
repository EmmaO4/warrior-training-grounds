from flask import Flask, session, render_template, request, url_for, redirect
import msal
import os
import uuid

app = Flask(__name__)

# secrets here 
app.secret_key = os.environ.get("FLASK_SECRET_KEY")
CLIENT_ID = os.environ.get("AZURE_CLIENT_ID")
CLIENT_SECRET = os.environ.get("AZURE_CLIENT_SECRET")
TENANT_ID = os.environ.get("AZURE_TENANT_ID")

AUTHORITY = f'https://login.microsoftonline.com/{TENANT_ID}'
SCOPE = ["User.Read"]

@app.route('/')
def home():
    return redirect(url_for('index.html'))

@app.route('/signin')
def signin():
    session["state"] = str(uuid.uuid4())
    auth_url = _build_msal_auth_url().get_authorization_request_url(
        SCOPE, 
        state = session["state"],
        redirect_uri=url_for("callback")
    )
    return redirect(auth_url)

@app.route('/dashboard')
def dashboard():
    if session['user'] not in session:
        return redirect(url_for('signin'))
    user = session['user']
    username = session.get("name")
    return render_template('dashboard.html', username=username)

@app.route("/callback")
def callback():
    if request.args.get("state") != session.get("state"):
        return "state mismatch", 400
    code = request.args.get("code")
    result = _build_msal_auth_url().acquire_token_by_authorization_code(
        code,
        scopes=SCOPE,
        redirect_uri=url_for("callback")
    )
    if "if_token_claims" in result:
        session["user"] = result["token_id_claims"]
        return redirect(url_for('dashboard'))
    return "login failed"

def _build_msal_auth_url(cache=None):
    return msal.ConfidentialClientApplication(
        client_credential=CLIENT_SECRET,
        authority=AUTHORITY,
        token_cache=cache,
        client_id=CLIENT_ID
    )