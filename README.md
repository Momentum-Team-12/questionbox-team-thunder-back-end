## Base URL

All endpoints begin with `https://questionbox-team-thunder-api.herokuapp.com/api/`

NOTE: API Root is /api/


## Create a new user

Go to url: /api/auth/users/
method: POST
Required fields: username, password
Optional fields: email
Response: same info you provided means successful

### request

Username and password are required.

```json
POST auth/users

{
  "username": "Luke",
  "password": "Momentum"
}
```

### response

```json
201 Created

{
  "id": 4,  
  "email": "",
  "username": "Luke",
}

```

## Login user

POST /api/auth/token/login/
Required fields: username, password
Response: auth_token
NOTE: use auth token from now on

### request

```
POST auth/token/login
```

```json
{
    "username": "Luke",
    "password": "Momentum1"
}
```

### response

```json
200 OK
400 Bad Request

{
    "auth_token": "d99a2de1b0a09db0fc2da23c9fdb1fc2447fff5d"
}
``` 



## User's info

GET /api/auth/users/me/
Fields you can see: id, username, email

```
POST /auth/users/me/
```

### response
```json
{
    "email": "",
    "id": 4,
    "username": "Luke"
}
```

## Logout user

POST /api/auth/token/logout/
Required fields: None

### request

```
POST auth/token/logout
```

### response

```txt
204 No Content
```


## List of questions (non-logged in user)

GET /api/all_questions/
Response for GET: id, title, created_at

### request

User can be anonymous / guest

```txt
GET /questions/
```

### response

```txt
200 Message
```



## List of questions (logged in user)
## Create a new question for this user

GET /api/questions/
Allowed methods: GET, POST
Response for GET: id, title, created_at

### request

User must be logged in

```txt
GET /questions/id 
```

### response

```txt
200 Message
```

```json
{
	{
		"id": 5,
		"title": "Title Test",
		"created_at": "2022-06-04T18:50:40.911851-04:00",
		"author": "Luke"
	},
	{
		"id": 6,
		"title": "Power Converters",
		"created_at": "2022-06-06T19:36:36.928032-04:00",
		"author": "Luke"
	}
}
```

POST /api/questions/
Required Fields for POST: title, description

### request

User must be logged in

```txt
POST /questions/
```

```json
{
	"title": "Desert wanderer",	
	"description": "What's with that creepy guy walking around the desert with I hood on? Isn't he hot?!"
}
```

### response

```json
201 Created

{
	"id": 7,
	"title": "Desert wanderer",
	"author": "Luke",
	"created_at": "2022-06-06T19:40:31.577077-04:00",
	"description": "What's with that creepy guy walking around the desert with I hood on? Isn't he hot?!"
}
```

## Details for a specific question

GET /api/questions/id/
Response for GET: id, title, created_at, author, description, answers


### request

User must be logged in 


```txt
GET /question/id/ 
```


### response

```txt
200 Message
```

```json
{
    "id": 5,
    "title": "Title Test",
    "author": "Luke",
    "created_at": "2022-06-04T18:50:40.911851-04:00",
    "description": "is this on?"
}
```


## Update an existing question

Go to url: /api/questions/id/
Allowed Methods: PUT, PATCH
Required fields for PUT, PATCH: title, description
Response for PUT, PATCH: 

### request

User must be logged in 


```txt
PUT /question/id/ or PATCH /question/id/ 
```

```json
{
    "title": "Title Test",
    "description": "is this on?",
}
```

### response

```txt
200 Message
```

```json
{
    "id": 5,
    "title": "Testing 123",
    "author": "Luke",
    "created_at": "2022-06-04T18:50:40.911851-04:00",
    "description": "Is this thing on?!"
}
```

## Delete Question

### request

User must be logged in 

Required Fields: question

```txt
DELETE /question/id/
```

### response

```txt
204 No Content
```


|  Method  |  Endpoint  |  Description |
| -------- | ---------- | ------------ |
|POST|[/auth/users/](#create-a-new-user)|Create a new user|
|POST|[/auth/token/login/](#login-user)|Login user|
|POST|[/auth/users/me/](#users-info)|User's info|
|POST|[/auth/token/logout/](#logout-user)|Logout user|
|GET|[/all_questions/](#list-all-questions)|List all questions (not logged in/anonymous)|
|GET|[/questions/](#list-all-questions-for-a-user)|List all questions for a user|
|POST|[/questions/](#create-a-new-question)|Create a new question|
|GET|[/questions/{id}](#details-for-a-specific-question)|Details for a specific question|
|PUT|[/questions/{id}](#update-an-existing-question)|Update an existing question|
|PATCH|[/questions/{id}](#update-an-existing-question)|Update part of an existing question|
|DELETE|[/questions/{id}](#delete-question)|Delete an existing question|

# testing