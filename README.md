## Base URL

All endpoints begin with `https://questionbox-team-thunder-api.herokuapp.com/api/`

NOTE: API Root is /api/


## Create a new user

Required fields: username, password
Optional fields: email
Response: same info you provided means successful

### request

Username and password are required.

```json
POST auth/users

{
  "username": "Luke",
  "password": "Momentum1"
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

Required fields: username, password
Response: auth_token
NOTE: use auth token from now on

### request

```json
POST auth/token/login

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

Fields you can see: id, username, email

```json
GET /auth/users/me/
```

### response
```json
{
    "id": 4,
    "username": "Luke",
    "email": "",
}
```



## Logout user

Required fields: None

### request

```json
POST auth/token/logout
```

### response

```json
204 No Content
```



## List of questions (non-logged in user)

GET /api/all_questions/
Response for GET: id, title, created_at, author

### request

User can be anonymous / guest

```json
GET /all_questions/
```

### response

```json
200 Message

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



## List of questions (logged in user)

GET /api/questions/
Allowed methods: GET, POST
Response for GET: id, title, created_at

### request

User must be logged in

```json
GET /questions/
```

### response

```json
200 Message

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



## Create a new question for this user (logged in user)

Required Fields for POST: title, description

### request

User must be logged in

```json
POST /questions/

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

```json
GET /questions/id/ 
```


### response

```json
200 Message

{
    "id": 5,
    "title": "Title Test",
    "author": "Luke",
    "created_at": "2022-06-04T18:50:40.911851-04:00",
    "description": "is this on?"
}
```



## Update an existing question

Allowed Methods: PUT, PATCH
Required fields for PUT, PATCH: title, description
Response for PUT, PATCH: id, title, author, created_at, description

### request

User must be logged in 

```json
PUT /question/id/ or PATCH /question/id/ 

{
    "title": "Title Test",
    "description": "is this on?",
}
```

### response

```json
200 Message

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

```json
DELETE /question/id/
```

### response

```json
204 No Content
```


|  Method  |  Endpoint  |  Description |
| -------- | ---------- | ------------ |
|POST|[/auth/users/](#create-a-new-user)|Create a new user|
|POST|[/auth/token/login/](#login-user)|Login user|
|POST|[/auth/users/me/](#users-info)|User's info|
|POST|[/auth/token/logout/](#logout-user)|Logout user|
|GET|[/all_questions/](#list-of-questions)|List all questions (not logged in/anonymous)|
|GET|[/questions/](#list-all-questions-for-a-user)|List all questions for a user|
|POST|[/questions/](#create-a-new-question)|Create a new question|
|GET|[/questions/{id}](#details-for-a-specific-question)|Details for a specific question|
|PUT|[/questions/{id}](#update-an-existing-question)|Update an existing question|
|PATCH|[/questions/{id}](#update-an-existing-question)|Update part of an existing question|
|DELETE|[/questions/{id}](#delete-question)|Delete an existing question|
