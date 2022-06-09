## Base URL

All endpoints begin with `https://questionbox-team-thunder-api.herokuapp.com/api/`

NOTE: API Root is /api/


|  Method  |  Endpoint  |  Description |
| -------- | ---------- | ------------ |
|POST|[/auth/users/](#create-a-new-user)|Create a new user|
|POST|[/auth/token/login/](#login-user)|Login user|
|POST|[/auth/users/me/](#users-info)|User's info|
|POST|[/auth/token/logout/](#logout-user)|Logout user|
|GET|[/all_questions/](#list-of-questions-non-logged-in-user)|List all questions (anonymous/guest)|
|GET|[/questions/](#list-of-questions-logged-in-user)|List all logged in user created questions|
|GET|[/all_questions?search=<search_term>/](#search-questions)|Search questions (limited to one search term)|
|POST|[/questions/](#create-a-new-question-for-this-user-logged-in-user)|Create a new question|
|GET|[/questions/{id}/](#details-for-a-specific-question)|Details for a specific question|
|PUT|[/questions/{id}/](#update-an-existing-question)|Update an existing question|
|PATCH|[/questions/{id}/](#update-part-of-an-existing-question)|Update part of an existing question|
|PUT|[/all_questions/{id}/favorite/](#favorite-a-question)|Favorite a question|
|DELETE|[/questions/{id}/](#delete-question)|Delete an existing question|
|GET|[/all_answers/](#list-all-answers)|List all answers (anonymous/guest)|
|GET|[/answers/](#list-all-users-answers)|List all logged in user created answers|
|GET|[/all_answers?search=<search_term>/](#search-answers)|Search answers (limited to one search term)|
|POST|[/questions/{id}/answers/](#create-a-new-answer)|Create a new answer|
|GET|[/answers/{id}/](#details-for-a-specific-answer)|Details for a specific answer|
|PUT|[/answers/{id}/](#update-an-existing-answer)|Update an existing answer|
|PATCH|[/answers/{id}/](#update-an-existing-answer)|Update an existing answer|
|PUT|[/all_answers/{id}/favorite/](#favorite-an-answer)|Favorite an answer|
|DELETE|[/answers/{id}/](#delete-answer)|Delete answer|
|PATCH|[/all_questions/{id}/all_answers/{id}/](#mark-answer-as-accepted)|Mark an answer as accepted|



## Create a new user

### Request

Required fields: username and password

Optional fields: email

```json
POST auth/users/

{
  "username": "Luke",
  "password": "Momentum1"
}
```

### Response

Response: If you receive the same info you provided, creation was successful!

```json
201 Created

{
  "email": "", 
  "username": "Luke",
  "id": 4, 
}

```


## Login user

### Request

Required fields: username, password

```json
POST auth/token/login/

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
NOTE: Must use the auth token from now on for logged in user.



## User's info

Requirement: user must be logged in.

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

### Request

Required fields: None

```json
POST /auth/token/logout/
```

### Response

```json
204 No Content
```



## List of questions (non-logged in user)

Returns list of all questions.

User can be anonymous / guest or logged in.

### Request

Required fields: None

```json
GET /all_questions/
```

### Response

```json
200 OK

[
	{
		"id": 6,
		"title": "Power Converters",
		"created_at": "2022-06-06T19:36:36.928032-04:00",
		"author": "Luke",
		"description": "Anywhere else got em?! Tosche Station is all out."
	},
	{
		"id": 5,
		"title": "Testing 123",
		"created_at": "2022-06-04T18:50:40.911851-04:00",
		"author": "Luke",
		"description": "Is this thing on?!"
	},
	{
		"id": 4,
		"title": "user2 question2",
		"created_at": "2022-06-03T17:57:07.532908-04:00",
		"author": "user2",
		"description": "user2 question2 description"
	},
]
```



## List of questions (logged in user)

Returns list of all questions for a logged in user.

### Request

Requirement: user must be logged in.

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



## Search questions

Search through questions.

### Request

Note: can only use 1 search parameter. It queries title and descriptions fields.

```json
GET /all_questions?search=converter
```

### Response

```json
200 OK

[
	{
		"id": 6,
		"title": "Power Converters",
		"created_at": "2022-06-06T19:36:36.928032-04:00",
		"author": "Luke",
		"description": "Anywhere else got em?! Tosche Station is all out."
	}
]
```



## Create a new question for this user (logged in user)

Requirement: user must be logged in.

### Request

Required fields: title and description

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

If anonymous / guest user attempts to POST:

```json
401 Unauthorized

{
	"detail": "Authentication credentials were not provided."
}
```



## Details for a specific question

Requirement: user must be logged in.

### Request

```json
GET /questions/id/ 
```

### Response

Response for GET: id, title, created_at, author, description, and answers (if any).

```json
200 OK

{
    "id": 5,
    "title": "Title Test",
    "author": "Luke",
    "created_at": "2022-06-04T18:50:40.911851-04:00",
    "description": "is this on?",
	"answers": []
}
```



## Update an existing question

Requirement: user must be logged in.

### Request

Required fields: title and description 

```json
PUT /question/id/

{
    "title": "Testing 123",
    "description": "Is this thing on?!"
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

If missing a required field, ex. description:

```json
400 Bad Request

{
	"description": [
		"This field is required."
	]
}
```



## Update part of an existing question

Requirement: user must be logged in.

### Request

Required fields: title and/or description 

```json
PATCH /question/id/ 

{
    "title": "This is a test..."
}
```

### Response

```json
200 OK

{
    "id": 5,
    "title": "This is a test...",
    "author": "Luke",
    "created_at": "2022-06-04T18:50:40.911851-04:00",
    "description": "Is this thing on?!"
}
```



## Favorite a question

Logged in user can favorite any question.

Requirement: user must be logged in.

### Request

Required in URL: question's id.

```json
PUT /all_questions/pk/favorite/
```

### Response

Return will be the question's id. 

```json
200 OK

{
	"id": 5
}
```



## Delete Question

Requirement: user must be logged in. 

### Request

Required in URL: question's id.

```json
DELETE /question/id/
```

### Response

A successful deletion returns:

```json
204 No Content
```

If another logged in user attempts to delete a question that is not theirs:
```json
404 Not Found
{
	"detail": "Not found."
}
```

If anonymous / guest attempts to delete a question:
```json
401 Unauthorized
{
	"detail": "Authentication credentials were not provided."
}
```



## List all answers

Returns list of all answers.

User can be anonymous / guest or logged in.

### Request

```json
GET /all_answers/
```

### Response

```json
200 OK

[
	{
		"id": 5,
		"created_at": "2022-06-06T13:46:05.672874-04:00",
		"author": "user1",
		"description": "user1 question2 answer1"
	},
	{
		"id": 4,
		"created_at": "2022-06-03T17:58:53.299983-04:00",
		"author": "user2",
		"description": "user2 question2 answer2"
	},
	{
		"id": 3,
		"created_at": "2022-06-03T17:58:45.838335-04:00",
		"author": "user2",
		"description": "user2 question2 answer1"
	},
	{
		"id": 2,
		"created_at": "2022-06-03T17:52:15.895155-04:00",
		"author": "user1",
		"description": "user1 question1 answer2"
	},
	{
		"id": 1,
		"created_at": "2022-06-03T17:52:10.041543-04:00",
		"author": "user1",
		"description": "user1 question1 answer1"
	}
]
```



## List all user created answers

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
]
```



## Search answers

Search through answers.

### Request

Note: can only use 1 search parameter. It queries the title field.

```json
GET /all_answers?search=test
```

### Response

```json
200 OK

[
	{
		"id": 11,
		"created_at": "2022-06-09T12:18:09.641307-04:00",
		"author": "user1",
		"description": "Test answer/description from user1"
	},
	{
		"id": 10,
		"created_at": "2022-06-09T12:16:02.861452-04:00",
		"author": "user1",
		"description": "Test answer/description from user1"
	},
	{
		"id": 8,
		"created_at": "2022-06-08T11:56:03.711841-04:00",
		"author": "Ben",
		"description": "Odd/scary sounds perhaps? Can anyone confirm?!"
	}
]
```



## Create a new answer

Requirement: user must be logged in.

### Request

Requirement: description

```json
POST /questions/id/answers/

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

Requirement: user must be logged in.

### Request

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

Requirement: user must be logged in.

### Request

Required field for PUT or PATCH: description 

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
	"description": "come to Alderaan..",
	"created_at": "2022-06-05T17:08:08.343275-04:00",
	"question": "Speeder"
}
```



## Favorite an answer

Logged in user can favorite any answer.

Requirement: user must be logged in.

### Request

Required in URL: answer's id.

```json
PUT /all_answers/pk/favorite/
```

### Response

```json
200 OK
```



## Delete Answer

Requirement: user must be logged in. 

### Request

Required in URL: question's id.

```json
DELETE /question/id/answers/id
```

### Response

A successful deletion returns:

```json
204 No Content
```



## Mark answer as accepted

Requirement: user must be logged in.

### Request

```json
PATCH /all_questions/id/all_answers/id/

200 OK 
{
	"accepted": true
}

```

### Response

Required field: accepted

```json
200 OK 
{
	"accepted": true
}
```