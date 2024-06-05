import base64

user_data = base64.b64encode("""#!/bin/bash
echo "userdata-start"
apt update
apt install -y python3-pip
echo y | sudo apt install python3.11-venv sshpass
git clone https://github.com/remimal/ansible1.git
# cd Ensai-CloudComputingLab1
# pip3 install -r requirements.txt
# python3 app.py
echo "userdata-end"
""".encode("ascii")).decode("ascii")