# crowdfunding_backend
[My deployed site](https://conservation-catalyst-7ab9167ac176.herokuapp.com/fundraisers/)

# Crowdfunding Back End
Hello, my name is Qin_n Shen!

## Planning:
### Concept/Name
- Name: Conservation Catalyst
- Concept: The app is a crowdfunding platform specifically for Australian wildlife and habitat conservation projects. 
  The "Saving Our Snake-Necked Turtle" campaign is the featured or launch campaign, but other users can create their own fundraisers.

### Intended Audience/User Stories
The intended audience of this app are divided into three key segments: project creators, oonors, and the broader Community.

### Front End Pages/Functionality
- Homepage: Featured Fundraisers
    - Hero section with call to action
    - Featured fundraisers with progress bars and donation buttons
    - Overview of the platform's mission and impact

- All Fundraisers Page 
    - A list of all available Fundraisers
    - Filter options by species (e.g., Turtle, Koala, Wombat)
    - Ability to sort projects by funding progress or creation date

- Create New Fundraiser Page
    - Form with campaign details (name, species, description, goal) 
    - Ability to submit new campaign details to the database
    - User validation to ensure all fields are filled correctly

- A Specific  Fundraiser Details Page 
    - etailed information about a single fundraiser
    - Shows progress towards the fundraising goal 
    - Option to make a donation

### API Spec

| URL             | HTTP Method                             | Purpose | Request Body  | Success Response Code | Authentication/Authorisation |
| --------------- | --------------------------------------- | ------- | ------------- | --------------------- | ---------------------------- |
| /fundraisers/   | Fetch all the fundraisers               | GET     | N/A           | 200                   | None                         |
| /fundraisers/   | Create a new fundraiser                 | POST    | Jason Payload | 201                   | Any logged in user           |
| /fundraisers/1/ | Fetch details of a specific fundraiser  | GET     | N/A           | 200                   | None                         |
| /fundraisers/1/ | Update details of a specific fundraiser | PUT     | Jason Payload | 200                   | Any logged in user           |
| /pledges/       | Fetch all the pledges                   | GET     | N/A           | 200                   | None                         |
| /pledges/       | Create a new pledge for a fundraiser    | POST    | Jason Payload | 201                   | Any logged in user           |
| /pledges/1/     | Update comment of a specific pledge     | PUT     | Jason Payload | 200                   | Any logged in user           |
| /pledges/1/     | Fetch details of a specific pledge      | GET     | N/A           | 200                   | None                         |
| /users/         | Fetch all the users                     | GET     | N/A           | 200                   | None                         |
| /users/         | create a new user                       | POST    | Jason Payload | 201                   | Any logged in user           |
| /users/1/       | Fetch details of a specific user        | GET     | N/A           | 200                   | None                         |
| /users/1/       | Update details of a specific user       | PUT     | Jason Payload | 201                   | Any logged in user           |
| api-token-auth/ | Get User Token                          | POST    | Jason Payload | 200                   | Any logged in user           |

### API Usage Guide
This guide provides step-by-step instructions for interacting with the core functionality of the Conservation Catalyst API.
- Register a New User: To create a new user account, send a POST request to the /users/ endpoint. This is the first step to becoming a member and gaining access to authenticated features.
    - Endpoint: /users/
    - Method: POST
    - Boday Data: The request body should be a JSON object containing the new user's username, email, and password.
    - Response: A successful response will return a 201 Created status code and the new user's data.

- Create a New Fundraiser: Creating a new fundraiser requires a valid authentication token. First, register or log in to get a token, then include it in the Authorization header of your POST request.
    - Endpoint: /fundraisers/
    - Method: POST
    - Authorization: Include the token in the Authorization header using the Bearer Token scheme.
    - Body Data: The request body should be a JSON object containing the details of the new fundraiser.
    - Response: A successful response will return a 201 Created status code and the details of the new fundraiser.
  
### DB Schema
![Database Schema](database.drawio.svg)

### Screenshots
#### Fundraisers
GET Method - Return all fundraisers
![GET /fundraisers/ - Return all fundraisers](Screenshots/:fundraisers:%20-%20Return%20all%20fundraisers.png)
POST Method - Create new fundraiser
![POST /fundraisers/ - Create new fundraiser](Screenshots/:fundraisers:%20-%20Create%20new%20fundraiser.png)
GET Method - Return one fundraiser
![GET /fundraisers/<pk>/ - Return one fundraiser](Screenshots/:fundraisers:<pk>:%20-%20Return%20one%20fundraiser.png)
PUT Method - Update one fundraiser
![PUT /fundraisers/<pk>/ - Update one fundraiser](Screenshots/:fundraisers:<pk>:%20-%20Update%20one%20fundraiser.png)

#### Pledges
GET Method - Return all pledges
![GET /pledges/ - Return all pledges](Screenshots/:pledges:%20-%20Return%20all%20pledges.png)
POST Method - Create new pledge
![POST /pledges/ - Create new pledge](Screenshots/:pledges:%20-%20Create%20new%20pledge.png)
PUT Method - Update one pledge
![PUT /pledges/<pk>/ - Update one pledge](Screenshots/:pledges:<pk>:%20-%20Update%20one%20pledge.png)
GET Method - Return one pledge
![GET /pledges/<pk> - Return one pledge/](Screenshots/:pledges:%20-%20Return%20one%20pledge.png)

#### Users
GET Method - Return all users
![GET /users/ - Return all users](Screenshots/:users:%20-%20Return%20all%20users.png)
POST Method - Create new user
![POST /users/ - Create new user](Screenshots/:users:%20-%20Create%20new%20user.png)
GET Method - Return one user
![GET /users/<pk>/ - Return one user](Screenshots/:users:%20-%20Return%20one%20user.png)
PUT Method - Update one user
![PUT /users/<pk>/ - Update one user](Screenshots/:users:%20<pk>:%20-%20Update%20one%20user.png)
POST Method - Get User Token
![POST /users/<pk>/ - Get User Token](Screenshots/:api-token-auth:%20-%20Get%20User%20Token%20(Qin).png)