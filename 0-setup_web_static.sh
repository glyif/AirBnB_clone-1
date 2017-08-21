#!/usr/bin/env bash
# sets up server for deployment

mkdir -p /data/web_static/releases/test/
echo "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown ubuntu:ubuntu /data -R
wget https://raw.githubusercontent.com/glyif/AirBnB_clone_v2/master/config
sudo cp config /etc/nginx/sites-available/default
sudo ln -sf /etc/nginx/sites-available/default /etc/nginx/sites-enable/default
sudo service nginx restart
