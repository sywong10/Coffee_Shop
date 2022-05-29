# Coffee Shop Full Stack

## Full Stack Nano - IAM Final Project

Udacity has decided to open a new digitally enabled cafe for students to order drinks, socialize, and study hard. But they need help setting up their menu experience.

You have been called on to demonstrate your newly learned skills to create a full stack drink menu application. The application must:

1. Display graphics representing the ratios of ingredients in each drink.
2. Allow public users to view drink names and graphics.
3. Allow the shop baristas to see the recipe information.
4. Allow the shop managers to create new drinks and edit existing drinks.


### configuration in auth0

1. tenant created named sywongiam
2. application created named coffee 
3. 2 users are created in User Management -> Users
   sywong10@yahoo.com    barista role
   sywong109@gmail.com   manager role
4. barisa role includes permission get:drinks-detail
5. manager role includes permissions delete:drinks, get:drinks, get:drinks-detail, patch:drinks, post:drinks

##  below are two JWT tokens with permissions needed for barista and manager to manage coffee shop.
##

JWT for barista and manager

barista JWT:
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InZEcm9MaTFHM3ZOQzZLNllQRlhkMiJ9.eyJpc3MiOiJodHRwczovL3N5d29uZ2lhbS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjI3NTAyYzgwOWJiMGQwMDY4ZTUwNTkzIiwiYXVkIjoiY29mZmVlYXBpIiwiaWF0IjoxNjUzODIzNzk2LCJleHAiOjE2NTM4MzA5OTYsImF6cCI6IkNIVll3OTlWSmREZVFST2g2WWNoQ0padmFsQlBhZU1HIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6ZHJpbmtzLWRldGFpbCJdfQ.ctVMreO8KAZPJxNntxWES7y-i3WzSFLa8pjOX4h79YRnvH9rI2wxB9iNZjdoDN6CWW9L2Va-W8uDWUcH3NPCBo0aiXUdcuccx9Oxzzs3j2iCzZtGJ2MQa9HBkVnkDsn7kd9K6ji92Tmvf5tUOalgcnsIZ6YH0ChiG3mVCs9VSrZhQrsDJirGXL9T4eFCIIrUX2QZlNIne0HRT9_Tw5Bk1VLU2FXEuYEVafz0L0pyH-IT0pBwsEnct6gRSWNmaiiZKG4oPyqF9ZTbDirl64-mHKwWqSWp4EF4HicYQZ_xLOEMc2UJY7c3Qj_HZpXcNqRQVa77lJ2eix7NPd2tgj_l-w

manager JWT:
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InZEcm9MaTFHM3ZOQzZLNllQRlhkMiJ9.eyJpc3MiOiJodHRwczovL3N5d29uZ2lhbS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjI3NjI5MzM0Y2JmYTAwMDZlNmY1ZjNlIiwiYXVkIjoiY29mZmVlYXBpIiwiaWF0IjoxNjUzODI0Mjc1LCJleHAiOjE2NTM4MzE0NzUsImF6cCI6IkNIVll3OTlWSmREZVFST2g2WWNoQ0padmFsQlBhZU1HIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6ZHJpbmtzIiwiZ2V0OmRyaW5rcyIsImdldDpkcmlua3MtZGV0YWlsIiwicGF0Y2g6ZHJpbmtzIiwicG9zdDpkcmlua3MiXX0.NolKZ1J9CqGVECGJ97J3gRDnDnSGCKhxagPSUOGN4m9bfU-TsSAOOKux0_S-Y41erAvZEzfnfHIdCtDCLUGQafbkdMwUQ1FldQRdZ3OZ6mqqlBvGQBwUsoUAPK-q0XmTlC9hRzLEdnoSlFFYb2zPhiEVO7F_h_hzlu5NMGpiCtVdDmv3fvGw2dd89JODntylPYxfWYWuYzQpGpuzR9v-7jgSN2hgzGIcXhPxHQP1Fm-PpHP-jD-CelnTSgio2whfHbFOxhn2TUKlwyYyPtkTvBV8L50IMLrSR6ptUhKOubgev0Z44p4NXjmP1DXgZzHR_OpDnSs2O1fAR_k9JuwHgg


### Backend configuration and start

1. in backend/src/auth/auth.py file, contains auth0 domain, algorithms and api_audience in application in auth0 

AUTH0_DOMAIN = 'sywongiam.us.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'coffeeapi'

2. in auth.py file also contains functions to validate JWT token.  These functions are from Identity and Access Management class. 
3. create virtual env main folder
4. source venv/bin/activate
5. cd backend
6. pip install -r requirements.txt
7. cd src
8. export FLASK_APP=api.py
9. flask run --reload


### Frontend
1. download and install Node (the download includes NPM) from [https://nodejs.com/en/download](https://nodejs.org/en/download/).
2. download and install ionic cli [Ionic Framework Docs](https://ionicframework.com/docs/installation/cli).
3. $ cd frontend
4. $ npm install
5. application and auth0 variables are setup in start_code/frontend/src/environments/environments.ts  
6. $ ionic serve 
7. once ionic server is running, coffee images should be present in the drink-menu page
    http://localhost:8100/tabs/drink-menu
8. coffee recipes can be added, updated and deleted via interacting with rest endpoints using Postman.
9. login to frontend page by clicking on "User" - Login
10. once Login, the page will show existing recipes in database.


###  postman
###
1. install postman
2. Import the postman collection `./backend/udacity-fsnd-udaspicelatte.postman_collection.json`
3. Right-clicking the collection folder for barista and manager, navigate to the authorization tab, and including the JWT in the token field (you should have noted these JWTs). 
4. Run the collection and correct any errors.

