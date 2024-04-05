#!/usr/bin/env bash
# Bash script that sets up the web servers for the deployment of web_static.


# Install Nginx if it not already installed
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get install -y nginx


# Create the folder /data/web_static/ if it doesn’t already exist
mkdir -p /data/web_static/releases/

# Create the folder /data/web_static/releases/test/ if it doesn’t already exist
mkdir -p /data/web_static/releases/test/

# Create a fake HTML file /data/web_static/releases/test/index.html (with simple content, to test your Nginx configuration)
echo "Test file HTML" > /data/web_static/releases/test/index.html

# If the symbolic link already exists, it should be deleted and recreated every time the script is ran.
ln -sf /data/web_static/current /data/web_static/releases/test/


chown -R ubuntu:ubuntu /data/

sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

sudo service nginx start