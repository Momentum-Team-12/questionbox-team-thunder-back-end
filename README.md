## Base URL

All endpoints begin with `https://questionbox-team-thunder-api.herokuapp.com/api/`

NOTE: API Root is /api/


|  Method  |  Endpoint  |  Description |
| -------- | ---------- | ------------ |
|POST|[/auth/users/](#create-a-new-user)|Create a new user|
|POST|[/auth/token/login/](#login-user)|Login user|
|POST|[/auth/users/me/](#users-info)|User's info|
|POST|[/auth/token/logout/](#logout-user)|Logout user|
|GET|[/all_questions/](#list-of-questions-non-logged-in-user)|List all questions (not logged in/anonymous)|
|GET|[/questions/](#list-of-questions-logged-in-user)|List all questions for a user|
|POST|[/questions/](#create-a-new-question-for-this-user-logged-in-user)|Create a new question|
|GET|[/questions/{id}/](#details-for-a-specific-question)|Details for a specific question|
|PUT|[/questions/{id}/](#update-an-existing-question)|Update an existing question|
|PATCH|[/questions/{id}/](#update-an-existing-question)|Update an existing question|
|DELETE|[/questions/{id}/](#delete-question)|Delete an existing question|
|GET|[/answers/](#list-all-answers)|List all answers|
|POST|[all_questions/{id}/all_answers/](#create-a-new-answer)|Create a new answer|
|GET|[/answers/{id}/](#details-for-a-specific-answer)|Details for a specific answer|
|PUT|[/answers/{id}/](#update-an-existing-answer)|Update an existing answer|
|PATCH|[/answers/{id}/](#update-an-existing-answer)|Update an existing answer|
|DELETE|[/answers/{id}/](#delete-answer)|Delete answer|


## Create a new user

### Request

Required fields: username and password

Optional fields: email

```json
POST auth/users

{
  "username": "Luke",
  "password": "Momentum1"
}
```

### Response

Response: same info you provided means successful

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

### Request

```json
POST auth/token/login

{
    "username": "Luke",
    "password": "Momentum1"
}
```

### Response


```json
200 OK

{
    "auth_token": "d99a2de1b0a09db0fc2da23c9fdb1fc2447fff5d"
}
``` 
NOTE: use auth token from now on


## User's info

Requires a user to be logged in.


```json
GET /auth/users/me/
```

### Response
```json
200 OK

{
    "id": 4,
    "username": "Luke",
    "email": "",
}
```



## Logout user

Required fields: None

### Request

```json
POST auth/token/logout
```

### Response

```json
204 No Content
```



## List of questions (non-logged in user)

### Request

User can be anonymous / guest

Required fields: None

```json
GET /all_questions/
```

### Response

```json
200 OK

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

### Request

User must be logged in

```json
GET /questions/
```

### Response

```json
200 OK

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

Required fields: title and description

### Request

User must be logged in

```json
POST /questions/

{
	"title": "Desert wanderer",	
	"description": "What's with that creepy guy walking around the desert with I hood on? Isn't he hot?!"
}
```

### Response

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

### Request

User must be logged in 

```json
GET /questions/id/ 
```


### Response

Response for GET: id, title, created_at, author, description, answers (if any)

```json
200 OK

{
    "id": 5,
    "title": "Title Test",
    "author": "Luke",
    "created_at": "2022-06-04T18:50:40.911851-04:00",
    "description": "is this on?"
}
```



## Update an existing question

Required fields for PUT, PATCH: title and/or description

### Request

User must be logged in 

```json
PUT /question/id/ or PATCH /question/id/ 

{
    "title": "Title Test",
    "description": "is this on?",
}
```

### Response

```json
200 OK

{
    "id": 5,
    "title": "Testing 123",
    "author": "Luke",
    "created_at": "2022-06-04T18:50:40.911851-04:00",
    "description": "Is this thing on?!"
}
```

## Delete Question

### Request

User must be logged in 

Required Fields: question id

```json
DELETE /question/id/
```

### Response

```json
204 No Content
```



## List all answers

Anonymous user will see all answers. 

Logged in user will only see their answers.

### Request

```json
GET /answers/
```

### Response

```json
200 OK

[
	{
		"pk": 1,
		"author": "user1",
		"description": "user1 question1 answer1",
		"created_at": "2022-06-03T17:52:10.041543-04:00",
		"question": "user1 question1"
	},
	{
		"pk": 2,
		"author": "user1",
		"description": "user1 question1 answer2",
		"created_at": "2022-06-03T17:52:15.895155-04:00",
		"question": "user1 question1"
	},
	{
		"pk": 3,
		"author": "user2",
		"description": "user2 question2 answer1",
		"created_at": "2022-06-03T17:58:45.838335-04:00",
		"question": "user2 question1"
	},
	{
		"pk": 4,
		"author": "user2",
		"description": "user2 question2 answer2",
		"created_at": "2022-06-03T17:58:53.299983-04:00",
		"question": "user2 question1"
	},
]
```



## Create a new answer

User must be logged in.

### Request

```json
POST /all_questions/id/all_answers/

{
	"description": "user1 response to user2's question pk4"
}
```

### Response

```json
200 OK
{
	"pk": 7,
	"author": "user1",
	"description": "user1 response to user2's question pk4",
	"created_at": "2022-06-07T10:24:08.771366-04:00",
	"question": "user2 question2"
}
```



## Details for a specific answer

### Request

User must be logged in.

Required Fields: answer id

```json
GET /answers/id/
```

### Response

```json
200 OK

{
	"pk": 2,
	"author": "Vader",
	"description": "mebbe.. come to the moon by Alderaan!",
	"created_at": "2022-06-05T17:08:08.343275-04:00",
	"question": "Speeder"
}

```


## Update an existing answer

Required fields for PUT, PATCH: description

### Request

User must be logged in 

```json
PUT /answer/id/ or PATCH /answer/id/ 

{
    "description": "come to Alderaan..",
}
```

### Response

```json
200 OK

{
	"pk": 2,
	"author": "Vader",
	"description": "mebbe.. come to the moon by Alderaan!!!",
	"created_at": "2022-06-05T17:08:08.343275-04:00",
	"question": "Speeder"
}
```


## Delete Answer

### Request

User must be logged in 

Required Fields: answer id

```json
DELETE /question/id/answers/id
```

### Response

```json
204 No Content
```
