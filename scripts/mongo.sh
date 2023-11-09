# Config file lives:
cat /etc/mongod.conf

# # Start mongo
sudo systemctl start mongod
# # Check status
sudo systemctl status mongod
# # Enable mongo
sudo systemctl enable mongod


# Mongo admin script
```
use admin
db.createUser(
  {
    user: "admin",
    pwd: "T=5T1i+iWUMac4sWAj!9", # this password doesn't work.. plz dont try
    roles: [ { role: "userAdminAnyDatabase", db: "admin" }, "readWriteAnyDatabase" ]
  }
)
```