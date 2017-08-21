#!/usr/bin/env bash
# sets up server for deployment

sudo mkdir -p /data/web_static/releases/test/
wget https://raw.githubusercontent.com/glyif/AirBnB_clone_v2/master/deploy/test_index.html
sudo mv test_index.html /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown ubuntu:ubuntu /data -R
wget https://raw.githubusercontent.com/glyif/AirBnB_clone_v2/master/deploy/config
sudo mv config /etc/nginx/sites-available/default
sudo ln -sf /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default
sudo service nginx restart
