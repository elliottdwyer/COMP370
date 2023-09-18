# Database Setup

The sequence of steps/commands required to set up a functioning database that is accessible from the public internet.

## Pre-Requisities: 

- You have an EC2 instance running on AWS.
- You are able to SSH into your EC2 instance.

# Steps: 

### SSH into your EC2 instance: 

  `ssh -i 'yourKey.pem' ubuntu@X.Y.Z.W`

  Or `ssh ubuntu@X.Y.Z.W` if `id_rsa` is set up in ~/.ssh

  > `X.Y.Z.W` is the public IP address of your EC2

### Update package list: 

  `sudo apt-get udpate`

### Install MariaDB Server:

  `sudo apt-get install mariadb-server`

### Configure MariaDB to Listen on Port 6002

  - Open the `50-server.cnf file`:

    `sudo vim /etc/mysql/mariadb.conf.d/50-server.cnf`

  - Find the `[mysqld]' section and add the following line to change the port:

    `port = 6002`

  - Edit the `bind-address` setting to listen for connections on all network interfaces

    `bind-address = 0.0.0.0`

### Update Security Group Rules in AWS to Allow Traffic on Port 6002

  Add a new rule:

  Type: `Custom TCP`, Protocol: `TCP`, Port Range: `6002`, Source: `Anwyhere IPv4`

### Open the Maria DB:

  `sudo mysql -u root`

### Create an empty database:

  `CREATE DATABASE comp370_test;`

### Create user with password protection:

  `CREATE USER 'comp370'@'%' IDENTIFIED BY '$ungl@ss3s';`

### Grant the user permission to access the COMP 370 server: 

  `GRANT ALL PRIVILEGES ON comp370_test.* TO 'comp370'@'%';`

### Restart MariaDB to apply the changes

  `sudo systemctl restart mariadb`

