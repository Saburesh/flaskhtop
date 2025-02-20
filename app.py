from flask import Flask
import os
import getpass
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    try:
        import pwd
        full_name = pwd.getpwuid(os.getuid()).pw_gecos.split(',')[0]
        if not full_name:
            full_name = "Saburesh"
    except:
        full_name = "Saburesh"

    username = getpass.getuser()

    ist_time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=5, minutes=30)))
    ist_time_str = ist_time.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

    try:
        top_output = subprocess.check_output(['top', '-b', '-n', '1'], text=True)
    except:
        top_output = "Could not retrieve top output"

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>System Information</title>
        <style>
            body {{ font-family: monospace; padding: 20px; }}
            pre {{ background-color: #f5f5f5; padding: 10px; overflow-x: auto; }}
        </style>
    </head>
    <body>
        <h3>Name: {full_name}</h3>
        <h3>user: {username}</h3>
        <h3>Server Time (IST): {ist_time_str}</h3>
        <h3>TOP output:</h3>
        <pre>{top_output}</pre>
    </body>
    </html>
    """

    return html

if __name__ == "__main__":  
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
