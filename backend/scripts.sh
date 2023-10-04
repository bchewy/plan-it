sudo nano /etc/systemd/system/backend.service

```
[Unit]
Description=Gunicorn instance to serve backend.service
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/path/to/your/project
ExecStart=/path/to/your/venv/bin/gunicorn --workers=3 --bind unix:your_project_name.sock -m 007 wsgi:app

[Install]
WantedBy=multi-user.target
```

sudo systemctl start your_project_name
sudo systemctl enable your_project_name
sudo nano /etc/nginx/sites-available/backend.service

# Use this command to run the gunicorn server
gunicorn -w 4 -b 0.0.0.0:8888 app:app

# Mongo on AWS:
# $ python3 -m pip install "pymongo[aws]"

