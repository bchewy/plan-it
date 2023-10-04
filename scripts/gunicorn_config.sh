[Unit]
Description=Gunicorn instance to serve backend
After=network.target

[Service]
User=ubuntu
Group=ubuntu
WorkingDirectory=/home/ubuntu/sustainable-singapore/backend
ExecStart=/usr/bin/gunicorn -w 4 -b 0.0.0.0:8888 app:app # no more /local/ its in /bin

[Install]
WantedBy=multi-user.target
