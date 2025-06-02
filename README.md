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

netfetch-automation/
│
├── app.py
├── nohup.out
├── poll_fortinet.py
├── polling.py
├── __pycache__
│   ├── poll_fortinet.cpython-38.pyc
│   └── polling.cpython-38.pyc
├── static
│   ├── cisco.png
│   ├── f5.png
│   ├── favicon1.png
│   ├── fortinet.png
│   ├── NetFetch_logo.png
│   ├── wget-log
│   └── wget-log.1
└── templates
    ├── cisco.html
    ├── fortinet.html
    └── home.html

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

<img width="949" alt="image" src="https://github.com/user-attachments/assets/6e173380-68d9-41ca-a665-789e748cd6b1" />

<img width="964" alt="image" src="https://github.com/user-attachments/assets/635839a0-7bd5-40fb-8796-3429267f1af1" />

<img width="964" alt="image" src="https://github.com/user-attachments/assets/a18efeb1-9820-4940-a385-82c00af53e91" />

---

## 🙏 Acknowledgments

Thanks to the maintainers of Netmiko and Flask for enabling such automation.

```
