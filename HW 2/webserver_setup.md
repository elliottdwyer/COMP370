### Webserver Setup

The sequence of steps/commands required to set up a functioning webserver with a file named COMP370_hw2.txt being served from the wwww root.

## Pre-Requisities: 

- Ensure you have an EC2 instance running on AWS.
- Ensure that you are able to SSH into your EC2 instance.

## Steps: 

# SSH into your EC2 instance: 

  `ssh -i ~/Downloads/comp370_key.pem ubuntu@18.191.141.124`

  > (Or `ssh ubuntu@18.191.141.124` if id_rsa is set up in ~/.ssh)

# Update package list: 

  `sudo apt-get udpate`

# Install Apache Server: 

  `sudo apt-get install apache2`

# Change Apache Configuration To Listen on Desired Port

  `sudo vim /etc/apache2/ports.conf`

  Add the following line to make Apache listen on port `8008`:

  `Listen 8008`

# Update Security Group Rules in AWS to Allow Traffic on Port 8008

  Add a new rule:
  
  Type: `Custom TCP`, Protocol: `TCP`, Port Range: `8008`, Source: `Anwyhere IPv4`

# Create and write the COMP370_hw2 file:

 `sudo vim /var/www/html/comp370_hw2.txt`

## Testing

  Open a web browser and go to `http://X.Y.Z.W:8008/comp370_hw2.txt`

  > `X.Y.Z.W` is the public IP address of your EC2


