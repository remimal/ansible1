import base64

# user_data_node_manager = base64.b64encode("""#!/bin/bash
# echo "userdata-start"
# apt update
# apt install -y python3-pip
# pip3 install ansible
# ssh-keygen -t rsa -b 2048 -f ~/.ssh/node_manager_key -N '' -q <<< y
# echo "userdata-end"
# """.encode("ascii")).decode("ascii")

# import base64

# Read the contents of labsuser.pem
with open('../../../../../.aws/labsuser.pem', 'r') as file:
    labsuser_pem = file.read()

# Base64 encode the user data script
user_data_node_manager = base64.b64encode(f"""#!/bin/bash
echo "userdata-start"
apt update
apt install -y python3-pip
pip3 install ansible

# Create the .ssh directory
mkdir -p /home/ubuntu/.ssh

# Write the labsuser.pem file
cat << 'EOF' > /home/ubuntu/.ssh/labsuser.pem
{labsuser_pem}
EOF

# Set the correct permissions
chmod 600 /home/ubuntu/.ssh/labsuser.pem
chown ubuntu:ubuntu /home/ubuntu/.ssh/labsuser.pem

echo "userdata-end"
""".encode("ascii")).decode("ascii")


user_data_http1 = base64.b64encode("""#!/bin/bash
echo "userdata-start"
apt update
apt install -y python3-pip
echo "userdata-end"
""".encode("ascii")).decode("ascii")

user_data_bdd1 = base64.b64encode("""#!/bin/bash
echo "userdata-start"
apt update
apt install -y python3-pip
echo "userdata-end"
""".encode("ascii")).decode("ascii")

