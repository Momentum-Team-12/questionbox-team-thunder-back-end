## Base URL

All endpoints begin with `https://questionbox-team-thunder-api.herokuapp.com/api/`

NOTE: API Root is /api/


## Create a new user

Response: same info you provided means successful

### request

Required fields: username and password

Optional fields: email

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

Requires a user to be logged in.


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

### request

User can be anonymous / guest

Required fields: None

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

Required fields: title and description

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

Response for GET: id, title, created_at, author, description, answers (if any)


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

Required fields for PUT, PATCH: title, description

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

Required Fields: question id

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
|PATCH|[/questions/{id}](#update-an-existing-question)|Update an existing question|
|DELETE|[/questions/{id}](#delete-question)|Delete an existing question|




|GET|[/answers/](#list-all-answers)|List all answers|
# not listing when logged in
# ok on local when logged in

## List all answers

Requires a user to be logged in.

### request

```json
GET /answers/
```

### response

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



|POST|[/answers/](#create-a-new-answer)|Add a new answer|
# can't POST to /answers/ in Prod - tested with pk/id and title
# can do it via questions/question_pk/answers/ on local though -> is it pushed to Heroku?



|GET|[/answers/{id}](#details-for-a-specific-answer)|Details for a specific answer|

 ## Details for a specific answer

### request

User must be logged in.

Required Fields: answer id

```json
GET /answers/id/
```

### response

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


|PUT|[/answers/{id}](#update-an-existing-answer)|Update an existing answer|
|PATCH|[/answers/{id}](#update-an-existing-answer)|Update part an existing answer|

## Update an existing answer

Required fields for PUT, PATCH: description

### request

User must be logged in 

```json
PUT /answer/id/ or PATCH /answer/id/ 

{
    "description": "come to Alderaan..",
}
```

### response

```json
200 Message

{
	"pk": 2,
	"author": "Vader",
	"description": "mebbe.. come to the moon by Alderaan!!!",
	"created_at": "2022-06-05T17:08:08.343275-04:00",
	"question": "Speeder"
}
```


|DELETE|[/answers/{id}](#delete-answer)|Delete answer|

## Delete Answer

### request

User must be logged in 

Required Fields: answer id

```json
DELETE /question/id/answers/id
```

### response

```json
204 No Content
```


