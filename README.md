# NetFetch - Network Device Command Automation

**NetFetch** is a lightweight web-based tool built using **Flask**, **Netmiko**, and **Jinja2** templating. It allows network engineers to connect to Cisco, F5, and Fortinet devices, run predefined commands, and display the output in a user-friendly web interface.

---

## 🔧 Features

- Connects to network devices over SSH using Netmiko
- Supports Cisco, F5 BIG-IP, and Fortinet platforms
- Runs common diagnostic/monitoring commands
- Displays output neatly in the browser
- Modular and easily extensible

---

## 📁 Project Structure

```

netfetch/
│
├── app.py                 # Main Flask application
├── templates/             # Jinja2 HTML templates
│   └── index.html         # Main interface
├── static/                # Images, favicon, CSS
│   └── NetFetch\_logo.png
├── requirements.txt       # Required Python packages
└── README.md              # Project overview

````

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/geekyapp/netfetch-automation.git
cd netfetch-automation
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
python app.py
```

Then open your browser and go to:
`http://localhost:80`

---

## ✅ Requirements

* Python 3.x
* Flask
* Netmiko

Install with:

```bash
pip install flask netmiko
```

---

## 🖼️ Screenshot

*(Add a screenshot here if you'd like)*

---

## 📜 License

This project is licensed under the MIT License.

---

## 🙏 Acknowledgments

Thanks to the maintainers of Netmiko and Flask for enabling such automation.

```
