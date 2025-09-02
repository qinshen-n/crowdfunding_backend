# crowdfunding_backend


# Crowdfunding Back End
Hello, my name is {{ Qin_n Shen }}

## Planning:
### Concept/Name
{{ Include a short description of your website concept here. }} Tips: Raise Fund for Protecting Snake-Necked Turtle in Perth
Turtlth Blitz: Svc th Snk Trtl (save the snake turtle)


### Intended Audience/User Stories
{{ Who are your intended audience? How will they use the website? }} animal/environment lovers

### Front End Pages/Functionality
- {{ Homepage }}
    - {{ Featured kickstarters }}
- {{ Create New Fundraiser Page }}
    - {{ Form with fundraiser details }}
    - {{ Ability to submit }}
    - {{ Nice error page for validation }}
- {{ Display Fundraiser }}
- {{ Shows all information about fundraiser }}
- {{ Show all pledges }}

- {{ A page on the front end }}
    - {{ A list of dot-points showing functionality is available on this page }}
    - {{ etc }}
    - {{ etc }}
- {{ A second page available on the front end }}
    - {{ Another list of dot-points showing functionality }}
    - {{ etc }}

### API Spec
{{ Fill out the table below to define your endpoints. An example of what this might look like is shown at the bottom of the page. 

It might look messy here in the PDF, but once it's rendered it looks very neat! 

It can be helpful to keep the markdown preview open in VS Code so that you can see what you're typing more easily. }}

| URL             | HTTP Method                            | Purpose | Request Body  | Success Response Code | Authentication/Authorisation |
| --------------- | -------------------------------------- | ------- | ------------- | --------------------- | ---------------------------- |
| /fundraisers    | Fetch all the fundraisers              | GET     | N/A           | 200                   | None                         |
| /fundraisers    | Create a new fundraisers               | POST    | Jason Payload | 201                   | Any logged in user           |
| /fundraisers/1/ | Fetch details of a specific fundraiser | GET     | N/A           |                       |                              |
| /pledges/       | Fetch all the pledges                  | GET     | N/A           | 200                   |                              |
| /pledges/       | Create a new pledge for a fundraiser   | POST    | Jason Payload | 201                   | Any logged in user           |

### DB Schema
![]( {{ .venv/database.drawio.svg }} )