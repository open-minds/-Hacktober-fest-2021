# Retail Agency web app

### Heroku link: (https://sagemodeboy.herokuapp.com/)
#### Warning:
 for security purposes, admin and manager access have been disabled which means you cannot add, update or delete any entities within the app, if you want to try, contact me after signing up to the app and i'll give you temporary access.
 * Current login access:
   mail: admin@mail.io
   password: Capstone2020

### Landing page screenshot:
<img src="screenshots/landing page.png" width="720"/>

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

```
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

## Running the server

To run the server, execute:

```
source setup.sh
```

## Retail Agency Description

The Retail Agency models a company that is responsible for selling clients' houses and managing and assigning agents to those houses. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

## Models

House with attributes contain name, rooms, price, picture
Agent with attributes name, age and picture
Job with attributes agent_id, house_id

## Environment Variables

In the `setup.sh` file, you will find:
- DATABASE_URL
- TEST_TOKEN
- AUTH0_DOMAIN
- API_AUDIENCE
- LOGIN_URL: the auth0 login(to handle local and heroku logins)

## Roles

### USER

- get:agents
- get:houses
- get:jobs

### MANAGER

#####  All permissions a user has
- post:houses
- post:jobs
- put:agents
- put:houses
- put:jobs
- delete:jobs

### ADMIN

##### All permissions a manager has
- delete:agents
- delete:houses
- post:agents

## Endpoints

### Login
`````bash
GET '/login'
 
this endpoint will help you login in an easy and fast way
`````

### Agents
`````bash
GET '/get-agents'

reponse = {
"success": true,
"agents": [
        {
            "age": 24,
            "id": 80,
            "name": "another agent",
            "picture": ""
        },
        {
            "age": 27,
            "id": 76,
            "name": "some agent",
            "picture": ""
        },
    ]
}

GET '/get-agent/<id>'

params = <id>

reponse = {
"success": true,
"agents": [
        {
            "age": 24,
            "id": 80,
            "name": "another agent",
            "picture": ""
        }
    ]
}


POST '/create-agent'

payload = {
    "age": 24,
    "name": "some agent",
    "picture": ""
}
response = {
"success": true,
"agents": [
        {
            "age": 24,
            "id": 80,
            "name": "another agent",
            "picture": ""
        },
        {
            "age": 27,
            "id": 76,
            "name": "some agent",
            "picture": ""
        },
    ]
}

PUT '/update-agent/<id>'

params = <id>

payload = {
    "age": 24,
    "name": "some agent",
    "picture": ""
}
response = {
"success": true,
"agents": [
        {
            "age": 24,
            "id": 80,
            "name": "another agent",
            "picture": ""
        },
        {
            "age": 27,
            "id": 76,
            "name": "some agent",
            "picture": ""
        },
    ]
}

DELETE '/delete-agent/<id>'

params = <id>

response = {
"success": true,
"agents": [
        {
            "age": 24,
            "id": 80,
            "name": "another agent",
            "picture": ""
        },
        {
            "age": 27,
            "id": 76,
            "name": "some agent",
            "picture": ""
        },
    ]
}
`````
### Houses
`````bash
GET '/get-houses'

reponse = {
"success": true,
"houses": [
        {
            "id": 62,
            "name": "some house",
            "picture": "",
            "price": 120,
            "rooms": 7
        },
        {
            "id": 61,
            "name": "another house",
            "picture": "",
            "price": 999,
            "rooms": 7
        },
    ]
}

GET '/get-house/<id>'

params = <id>

reponse = {
"success": true,
"house": {
        "id": 61,
        "name": "some house",
        "picture": "",
        "price": 999,
        "rooms": 7
    },
}

POST '/create-house'

payload = {
    "name": "some house",
    "picture": "",
    "price": 999,
    "rooms": 7
}
response = {
"success": true,
"houses": [
        {
            "id": 62,
            "name": "some house",
            "picture": "",
            "price": 120,
            "rooms": 7
        },
        {
            "id": 61,
            "name": "another house",
            "picture": "",
            "price": 999,
            "rooms": 7
        },
    ]
}

PUT '/update-house/<id>'

params = <id>

payload = {
            "name": "another house",
            "picture": "",
            "price": 999,
            "rooms": 7
        },
response = {
"success": true,
"houses": [
        {
            "id": 62,
            "name": "some house",
            "picture": "",
            "price": 120,
            "rooms": 7
        },
        {
            "id": 61,
            "name": "another house",
            "picture": "",
            "price": 999,
            "rooms": 7
        },
    ]
}

DELETE '/delete-house/<id>'

params = <id>

response = {
"success": true,
"houses": [
        {
            "id": 62,
            "name": "some house",
            "picture": "",
            "price": 120,
            "rooms": 7
        },
        {
            "id": 61,
            "name": "another house",
            "picture": "",
            "price": 999,
            "rooms": 7
        },
    ]
}
`````
### Jobs
`````bash
GET '/get-jobs'

reponse = {
"success": true,
"jobs": [
        {
            "agent_id": 80,
            "house_id": 62
        },
        {
            "agent_id": 79,
            "house_id": 61
        }
    ],
}

GET '/get-job/<agent_id>&<house_id>'

params = <agent_id>&<house_id>

reponse = {
"success": true,
 "job": {
        "agent_id": 80,
        "house_id": 62
    }
}

POST '/create-job'

payload = {
        "agent_id": 80,
        "house_id": 62
    }

response = {
"success": true,
"jobs": [
        {
            "agent_id": 80,
            "house_id": 62
        },
        {
            "agent_id": 79,
            "house_id": 61
        }
    ]
}

PUT '/update-job/<agent_id>&<house_id>'

params = <agent_id>&<house_id>

payload = {
    "agent_id": 80,
    "house_id": 63
}
response = {
"success": true,
"jobs": [
        {
            "agent_id": 80,
            "house_id": 63
        },
        {
            "agent_id": 79,
            "house_id": 61
        }
    ],
}

DELETE '/delete-job/<agent_id>&<house_id>'

params = <agent_id>&<house_id>

response = {
"success": true,
"jobs": [
        {
            "agent_id": 80,
            "house_id": 63
        },
        {
            "agent_id": 79,
            "house_id": 61
        }
    ]
}
`````

## Testing

To run the tests:

`````bash

python test_app.py

`````

## Frontend
### Why?:
    I added a frontend to the flask app to test my newly acquired skills!

### How to navigate the website?:
    The home page contains the emails and passwords for premade accounts with different roles.
    Write them into the (mail/password) fields in the auth0 login page
    * You can login using the login button on the main page
    * You can refresh the token using the refresh token button in case it expires
    * You can logout using the logout button on the main page
    * You can perform all actions using the fronent (provided that you use the correct account role)

### Weird specifications:
    Due to my limited ability to handle frontend calls using AJAX, each page has 2 endpoints:
    * One loader page (requires no auth and it calls instantly the actual page)
    * The actual page (contains the correct data and requires proper auth)
    This was done due to certain issues with JWT storage in the local storage.

## Backend
### What is a Job (model)?
    A job is the representation that a sales agent is currently trying to sell a house to potential clients.
    A job is a direct relationship between one specific agent and one specific house.
    An agent can sell multiple houses but a house can be sold by many agents.
### Why a many to many relationship?
    I used a many to many relationship in order to be able to extend the Job model to include (in the future) many data attributes that has no relation with the house or the agent models, and since each house can be handled by an agent, it would seem appropriate to use a one to one relationship but this would not allow to extend the app's functions in a smooth way (data architecture speaking).
    Also a job has no id, the primary keys in a job are the id of the agent and the house.
