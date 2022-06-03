NOTE: API Root is /api/


Want to create a new user?

Go to url: /api/auth/users/
method: POST
Required fields: username, password
Optional fields: email
Response: same info you provided means successful


Want to login user?

Go to url: /api/auth/token/login/
Allowed methods: POST
Required fields: username, password
Response: auth_token
NOTE: use auth token from now on


Want logged in user's info?

Go to url: /api/auth/users/me/
Fields you can see: id, username, email


Want to logout user?

Go to url: /api/auth/token/logout/
Allowed methods: POST
Required fields: None


Want to view a list of logged in user's questions?
Want to create a new question for this user?

Go to url: /api/questions/
Allowed methods: GET, POST
Required Fields for POST: title, description
Response for GET: id, title, created_at


Want to see details for a specific question?

Go to url: /api/questions/id/
Allowed Methods: GET, PUT, PATCH, DELETE
Required fields for PUT: title, description


need