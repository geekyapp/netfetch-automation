from flask import Flask, render_template, request
from polling import get_device_info
from poll_fortinet import get_fortinet_info

app = Flask(__name__)
 
@app.route("/")
def home():
    return render_template("home.html")
 
@app.route("/cisco", methods=["GET", "POST"])
def cisco():
    data = {}
    if request.method == "POST":
        ip = request.form["device_ip"]
        data = get_device_info(ip)
    return render_template("cisco.html", data=data)

@app.route('/fortinet', methods=['GET', 'POST'])
def fortinet():
    data = None
    if request.method == 'POST':
        ip = request.form['device_ip']
        data = get_fortinet_info(ip)
    return render_template('fortinet.html', data=data)

# Placeholder routes (for future)
@app.route("/f5")
def f5():
    return "<div style=\"color: #504e91; font-size: 12px; font-family: 'Courier New', monospace;\">NetFetch for F5 : coming soon -- Stay Tuned !! </div>"

 
#@app.route("/fortinet")
#def fortinet():
#    return "<h2>Fortinet Polling Page Coming Soon...</h2>"
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
