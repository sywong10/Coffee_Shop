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
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InZEcm9MaTFHM3ZOQzZLNllQRlhkMiJ9.eyJpc3MiOiJodHRwczovL3N5d29uZ2lhbS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjI3NTAyYzgwOWJiMGQwMDY4ZTUwNTkzIiwiYXVkIjoiY29mZmVlYXBpIiwiaWF0IjoxNjUzNjQ4Nzc1LCJleHAiOjE2NTM2NTU5NzUsImF6cCI6IkNIVll3OTlWSmREZVFST2g2WWNoQ0padmFsQlBhZU1HIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6ZHJpbmtzLWRldGFpbCJdfQ.GoMNK8KLK6NwtiK0zB8HLUkdli_lxYNQxU9OFmVVtUd6sAeSnePoS3wEA0AqPfJFm1AVxVIEHyJd16L73O40EQCJp6-bQKLFp80Im1bTWIBITTXHbGMbpGzXXsFQuUGxdyycRT_c5JIEZHlUreF-bV1G5zscm0aMLMut3VBiDyFLY5GJCw5RiZtbEPQ3R-8aOdnAprCQuG3hP6pQ_k8aDpxvAUo5G_mvuKRJ9Byoot4VA-oYtrJg7XRQCljwlhMeZdl3F9y1GECxRLTuhElROHkm30HnUh9tItyUijUi603z_U5fM1qKQRYirekKl3TrcmhWNjs2jPQd40SLYjgSIw

manager JWT:
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InZEcm9MaTFHM3ZOQzZLNllQRlhkMiJ9.eyJpc3MiOiJodHRwczovL3N5d29uZ2lhbS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjI3NTAyYzgwOWJiMGQwMDY4ZTUwNTkzIiwiYXVkIjoiY29mZmVlYXBpIiwiaWF0IjoxNjUzNjQ4Nzc1LCJleHAiOjE2NTM2NTU5NzUsImF6cCI6IkNIVll3OTlWSmREZVFST2g2WWNoQ0padmFsQlBhZU1HIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6ZHJpbmtzLWRldGFpbCJdfQ.GoMNK8KLK6NwtiK0zB8HLUkdli_lxYNQxU9OFmVVtUd6sAeSnePoS3wEA0AqPfJFm1AVxVIEHyJd16L73O40EQCJp6-bQKLFp80Im1bTWIBITTXHbGMbpGzXXsFQuUGxdyycRT_c5JIEZHlUreF-bV1G5zscm0aMLMut3VBiDyFLY5GJCw5RiZtbEPQ3R-8aOdnAprCQuG3hP6pQ_k8aDpxvAUo5G_mvuKRJ9Byoot4VA-oYtrJg7XRQCljwlhMeZdl3F9y1GECxRLTuhElROHkm30HnUh9tItyUijUi603z_U5fM1qKQRYirekKl3TrcmhWNjs2jPQd40SLYjgSIw


### Backend configuration and start

1. in starter_code/backend/src/auth/auth.py file, contains auth0 domain, algorithms and api_audience in application in auth0 

AUTH0_DOMAIN = 'sywongiam.us.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'coffeeapi'

2. in auth.py file also contains functions to validate JWT token.  These functions are from Identity and Access Management class. 
3. virtual env is located in 03_coffee_shop_full_stack
4. cd 03_coffee_shop_full_stack
5. source venv/bin/activate
6. cd starter_code/backend
7. pip install -r requirements.txt
8. cd src
9. export FLASK_APP=api.py
10. flask run --reload


### Frontend
1. download and install Node (the download includes NPM) from [https://nodejs.com/en/download](https://nodejs.org/en/download/).
2. download and install ionic cli [Ionic Framework Docs](https://ionicframework.com/docs/installation/cli).
3. $ cd starter_code/frontend
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
2. Import the postman collection `./starter_code/backend/udacity-fsnd-udaspicelatte.postman_collection.json`
3. Right-clicking the collection folder for barista and manager, navigate to the authorization tab, and including the JWT in the token field (you should have noted these JWTs). 
4. Run the collection and correct any errors.

