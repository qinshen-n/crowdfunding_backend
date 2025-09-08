# crowdfunding_backend


# Crowdfunding Back End
Hello, my name is {{ Qin_n Shen }}

## Planning:
### Concept/Name
{{ Conservation Catalyst
The app is a crowdfunding platform specifically for Australian wildlife and habitat conservation projects. 
The "Saving Our Snake-Necked Turtle" campaign is the featured or launch campaign, but other users can create their own fundraisers. }} 

### Intended Audience/User Stories
{{ animal/environment lovers }} 

### Front End Pages/Functionality
- {{ Homepage }}
    - {{ Hero section with call to action }}
    - {{ Featured campaigns with progress bars and donation buttons }}
    - {{ Overview of the platform's mission and impact }}
- {{ All Campaigns Page }}
    - {{ A list of all available campaigns }}
    - {{ Filter options by species (e.g., Turtle, Koala, Wombat) }}
    - {{ Ability to sort projects by funding progress or creation date }}

- {{ Create New Campaign Page }}
    - {{ Form with campaign details (name, species, description, goal) }}
    - {{ Ability to submit new campaign details to the database }}
    - {{ User validation to ensure all fields are filled correctly }}

- {{ Project Details Page }}
    - {{ Detailed information about a single campaign }}
    - {{ Shows progress towards the fundraising goal }}
    - {{ Option to make a donation }}

### API Spec

| URL             | HTTP Method                             | Purpose | Request Body  | Success Response Code | Authentication/Authorisation |
| --------------- | --------------------------------------- | ------- | ------------- | --------------------- | ---------------------------- |
| /fundraisers    | Fetch all the fundraisers               | GET     | N/A           | 200                   | None                         |
| /fundraisers    | Create a new fundraisers                | POST    | Jason Payload | 201                   | Any logged in user           |
| /fundraisers/1/ | Fetch details of a specific fundraiser  | GET     | N/A           |                       |                              |
| /fundraisers/1/ | Update details of a specific fundraiser | POST    | Jason Payload | 201                   | Any logged in user           |
| /pledges/       | Fetch all the pledges                   | GET     | N/A           | 200                   |                              |
| /pledges/       | Create a new pledge for a fundraiser    | POST    | Jason Payload | 201                   | Any logged in user           |
| /pledges/1/     | Fetch details of a specific pledge      | GET     | N/A           | 200                   | Any logged in user           |
| /users/         | Fetch all the users                     | GET     | N/A           | 200                   |
| /users/         | create a new user                       | POST    | Jason Payload | 201                   |
| /users/1/       | Fetch details of a specific user        | GET     | N/A           | 200                   | Any logged in user           |
| /users/1/       | Update details of a specific fundraiser | POST    | Jason Payload | 201                   |                              |

### DB Schema
![]( {{ .venv/database.drawio.svg }} )