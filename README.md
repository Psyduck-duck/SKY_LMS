# LMS API Service

A RESTful API service for Learning Management System (LMS) built with DRF and PostgreSQL.

## Features

- User authentication (JWT)
- Course management
- Lesson management
- User management (automatic blocking of inactive users)
- Payment service
- Courses subscription feature (be aware of all updates of a course you're interested at)
- API documentation with Swagger

## Server Setup
1. Connect to your server
```commandline
ssh user_name@your_server_ip
```
2. Run necessary updates
```commandline
sudo apt update && sudo apt upgrade
```
3. Set up firewall and open necessary ports
```commandline
sudo ufw status
sudo ufw enable #if case firewal is turned off
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw allow 22/tcp
```

## Installation

1. Clone the repository:
```commandline
git clone https://github.com/Psyduck-duck/SKY_LMS.git
```
2. Go to project directory and set up env variables according to .env.sample:
```commandline
cd lms_api/
nano .env
```
3. Start the container:
```commandline
docker-compose up
```

## API Documentation

After starting the container, access the API documentation at:

Swagger UI: http://localhost:8000/api/swagger/
Redoc UI: http://localhost:8000/api/redoc/

## server ip
`158.160.136.146`