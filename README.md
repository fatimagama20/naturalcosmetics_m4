# Natural cosmetics
## Code institute Milestone Project4

[Click here to launch a natural cosmetics app](https://naturalcosmetics-2fcecfab55d3.herokuapp.com/)

Welcome to Natural Cosmetics, your trusted source for high-performance, guilt-free skincare. We understand the challenges of finding products that are effective, safe, and environmentally responsible.​

![](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/screenshots/recipewebsite.png?raw=true)

# About Natural cosmetics

A recipe is a set of instructions that describes how to prepare or make something, especially a dish of prepared food.

##  Foodrecipe goals

This food recipe app allows users to sift through tons of recipes, and check cooking intructions. It also lets users know the main ingredients, and the type of meal, which the user wants to make.

# User Experience (UX)
* ## User stories
  * ### First time visitors goal
    * As a first time visitor, I want to easily understand the main purpose of the app and learn more about the feature of the app 
    * As a first time visitor, I want to look for different recipes and then add the recipes along with ingredients and categories.
    * Look to edit a recipe, ingredients and categories
    * User can delete recipe, category and ingredient at any time
    * Guide users by providing detailed instructions for preparing various dishes       
    * Offering comprehensive information on ingredients.
    * Provide step-by-step cooking procedures

  * ### Frequent User Goals
    * As a frequent User, I want to see if the preparation time
    * As a Frequent User, I want to see calories
    * As a Frequent User, I want to see who added the recipe
    * As a Frequent User, I want to see the reviews
    

* ## Design
  * ### Colour Scheme
    
    I have chosen to use the blue and white as the main colour, alongside grey and black, as well as using the accent colours red and light green.   
    Red is used as a warning colour on buttons used for deletion. Green accent is used for the edit button to easily differentiate the buttons.
  
    * Card colour - #03a9f4
    * Delete button - #888e5f
    * Edit button - #F44336
    * Text colour - #fff


  * ### Typography

    * Default fonts is used throughtout the website. I haven't use google fonts

  * ### Imagery
    * On the Homepage, I have used a professionally presented food image to suit the purpose of the website, which is providing a good impression for the visitors.
  
* ## Wireframes
  * ### Home page Wireframe - [View](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/wireframes/home.png)
  * ### New recipe Wireframe - [View](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/wireframes/newrecipe.png)
  * ### Ingredients Wireframe - [View](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/wireframes/ingredients.png)
  * ### Categories Wireframe - [View](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/wireframes/categories.png)

# Database Schema

- I have represented the data within an entity relationship diagram.
![Entity Relationship Diagram](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/tablestructure/tablestructure.png?raw=true)
- I have structured a database using [PostgreSQL](https://www.postgresql.org/), a object-relational database to support the Foodrecipe app.  
Based on this information, I then created a database structure called foodrecipe db, within which I created 4 tables: category, ingredients, recipe and ingredient_index.
![Foodrecipe database](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/tablestructure/foodrecipedb.png?raw=true)
- The 'category' stores the specific fields of information about the categories to which the recipe belongs for e.g. Lunch, dinner, chicken, beef, etc.
![foodrecipe category](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/tablestructure/categorytable.png?raw=true)
- The 'ingredients' stores the specific fields of information about the ingredients which is used to create a recipe for example, chicken, flour, pepper etc. 
![Ingredients collection](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/tablestructure/ingredientstable.png?raw=true)  
- The 'recipe' stores the actual recipe with all the other information for e.g. how the recipe is prepared, what ingredients are used and which category it belongs to
![Recipe collection](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/tablestructure/recipetable.png?raw=true).  
- The 'ingredient_index' stores the relation between the recipe and the ingredients of all the recipes for e.g. Chicken recipe and the ingredients of the chicken recipe
![Ingredients index](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/tablestructure/ingredient_indextable.png?raw=true)

# Features

* Responsive on all device sizes

![Responsive Mockup](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/screenshots/recipewebsite.png?raw=true). 

* Interactive elements

## Navigation:

I created a menu to help enable the user to navigate the app. The menu is responsive and changes to a user-friendly side panel with dropdown functionality on mobile. Users have access via the menu to an additional category, ingredient pages featuring a dashboard to add, delete and edit.
### Home page desktop
![Home page desktop](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/screenshots/homepage.png?raw=true)
### Home page mobile
![Home page mobile](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/screenshots/ipad10th.png?raw=true)
### Category desktop
![Category desktop](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/screenshots/categorieslist.png?raw=true)
### Category mobile
![Category mobile](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/screenshots/categoriesmobile.png?raw=true)
### Ingredient desktop
![Ingredient desktop](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/screenshots/ingredientlist.png?raw=true)
### Ingredient mobile
![Ingredient mobile](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/screenshots/ingredientsmobile.png?raw=true)

# UX features:
## Modal
- I have added a modal on delete functionality to make user aware of delete action. 

# CRUD 
I have incorporated features to enable Create, Read, Update & Delete functionallity within the Foodrecipe App 
## Add a recipe record
- I created a page called add_recipe.html and added the function in the routes.py file called add_recipe which uses the "GET" and "POST". The GET method is to used to request data , The POST method is used to send the data to the server. I then created and styled input text fields to enable users to input text and also an input field for users to add the recipe details. I used a dropdown list for category and ingredient selection. Specific minimum and maximum entry lengths were applied to each text field.
## Add recipe user interface:
![add_recipe user interface](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/screenshots/newerecipe.png?raw=true)
## Input fields features:
![category drop-down list](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/crudscreenshots/categoryfield.png?raw=true)
![ingredient drop-down list](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/crudscreenshots/ingredientfield.png?raw=true)
## add_recipe function:
![add_recipe function](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/crudscreenshots/addrecipefunction.png?raw=true)
## add_category function:
I created a categories page to manage categories with blue button to add categories at the top of the page under the title. On click of "Add category" button it redirects to "Add category" page with the help of an add_category.html template. I then created a function to add categories.  
![add_category function](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/crudscreenshots/addcategoryfunction.png?raw=true)
## add_ingredients function:
I created a ingredients page to manage ingredients with blue button to add ingredients at the top of the page under the title. On click of "Add ingredient" button it redirects to "Add ingredient" page with the help of an add_ingredients.html template. I then created a function to add ingredients.  
![add_ingredients function](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/crudscreenshots/addIngredientfunction.png?raw=true)
## Update a recipe:
I created edit_recipe.html to edit a recipe record. I fetch a recipe details based on the recipe id from the database. Once found, then the recipe record is updated with edit recipe button. After that's been updated in the database, I redirect to the home page where the list of recipes are displayed
![Updating a recipe record](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/crudscreenshots/editrecipefunction.png?raw=true)
## Update categories
I created an edit_category.html template and interface and a function to edit categories. The functionality was created in the same way as the create recipe record.
![Updating a cateory record](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/crudscreenshots/editcategoryfunction.png?raw=true)
## Update ingredients
I created an edit_ingredients.html template and interface and a function to edit ingredients. The functionality was created in the same way as the create recipe record.
![Updating a ingredient record](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/crudscreenshots/editIngredientfunction.png?raw=true)
## Delete a recipe:
The user can delete a recipe by clicking the red delete button at the foot of the recipe record. To do this I created a function as follows: The @app.route decorator is '/delete_recipe', which takes the 'recipe_id' as a variable. I then selected the specific recipe by the ObjectId that matched the 'recipe_id' variable. As soon as the record is removed I redirect the user to home page where the list of recipes are shown.  
![delete_recipe function](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/crudscreenshots/deleterecipefunction.png?raw=true). 
## Delete a category:
The user can delete a record by clicking a delete button for the specific category within the categoires dashboard. To do this, I created a function to delete categories. The functionality was created in the same way as the delete recipe record
![delete_category function](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/crudscreenshots/deletecategoryfunction.png?raw=true)
## Delete a ingredient:
The user can delete a record by clicking a delete button for the specific ingredient within the ingredients dashboard. To do this, I created a function to delete ingredients. The functionality was created in the same way as the delete recipe record
![delete_ingredient function](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/crudscreenshots/deleteIngredientfunction.png?raw=true)

# Technologies Used

## Languages Used

  * [HTML5](https://en.wikipedia.org/wiki/HTML5)
  * [CSS3](https://en.wikipedia.org/wiki/CSS)
  * [JS](https://en.wikipedia.org/wiki/JavaScript)
  * [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

  ##  Frameworks, Libraries & Programs Used
  1. [Materialize 1.0.0:](https://materializecss.com/)
     * Materialize is a modern responsive CSS framework based on Material Design by Google. Materialize was used to assist with the responsiveness and styling of the website; especially useful in this project  are the features for creating forms.
  2. [Font Awesome:](https://fontawesome.com/)
     *  Font Awesome is used to add help icon
  3. [Heroku:](https://www.heroku.com/)
     * The project was deployed to Heroku. Heroku is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.
  4. [PostgreSQL:](https://www.postgresql.org/)
     * PostgreSQL was used to store the data required for the project. It is a object-relational database used for data storage.
  5. [Git:](https://git-scm.com/)
     * Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
  6. [GitHub:](https://github.com/)
     * GitHub is used to store the projects code after being pushed from Git.
  7. [Balsamiq:](https://balsamiq.com/)
     * Balsamiq was used to create the [wireframes]() during the design process.
  8. [Am I reponsive:](https://ui.dev/amiresponsive)
     * Am I reponsive was used to create a mockup to add in a README.md file
 
# Deployment 
## Setting up a GitHub caccount
- I set up a [GitHub account](https://github.com/)
- Used the Chrome browser
- Created the Project GitHub repository
- Clicked the green GitPod button in the top right hand cornner of the repository to create a new [workspace](https://gitpod.io/workspaces) to enable me to work locally'

### Create the Flask Application
To create the Flask application I did the following:
- Created a new repository in [GitHub](https://github.com/fatimagama20/food-receipe)
- in the Terminal typed; 'pip3 install 'Flask-SQLAlchemy<3' psycopg2 sqlalchemy==1.4.46' so that Flask functionality was ready to be imported.
- created an env.py in which to store sensitive data.
- created a gitignore file which was set up to ignore env.py as well as the the '__pycache__/' directory.so that data that must be kept secure such as secret keys would not be saved to GitHub.
- imported os to set up default environment variables in the env.py file, as in the screenshot below:  
![Environment Variables](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/screenshots/environmentvarfile.png?raw=true)
- Initiate the appliation by creating __init__.py file as shown below:
![Initialize application](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/screenshots/initfile.png?raw=true)
- in run.py import Flask 
- imported the env package so Heroku would be able to find the environment variables as they would not be pushed to GitHub.
- created an instance of Flask, stored in a variable called 'app'.
- told the app how and where to run the application as in the screenshot below:  
![Run application](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/screenshots/runfile.png?raw=true)
- the final parameter was set to debug=True, during development, so I could see any actual errors that may appear, instead of a generic server warning. I changed this back to debug=False prior to final deployment.
- set up a test function to check the app was working correctly in advance of connecting the app to PostgreSQL.

## Set up the database with PostgreSQL
- Now that I have basic flask application up and running, it's time to create a database schema by defining models
- Within a foodrecipe package created models.py file and import a db from the package
- I created three separate tables, which will be represented by class-based models using SQLAlchemy's ORM.
- The first table will be for various categories, so let's call this class 'Category', which will use the declarative base from SQLAlchemy's model.
![Category model](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/screenshots/categorymodel.png?raw=true)
- The second table will be for various ingredients, so let's call this class 'Ingredients', which
will use the declarative base from SQLAlchemy's model.
![Ingredients model](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/screenshots/ingredientsmodel.png?raw=true)
- The third table will be for each recipe created, so we'll call this class 'Recipe', also using the default db.Model.
![Recipe model](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/screenshots/recipemodel.png?raw=true)
- And the last table will be relation between the recipe and ingredients
![Ingredient_index model](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/screenshots/ingredient_indexmodel.png?raw=true)
- Go ahead and save the file, and let's return back to routes.py file now.
At the top of the routes, import these classes in order to generate a database next.

#  Database schema created within Postgres.
- Let's navigate to the Terminal, and login to the Postgres CLI by typing 'psql' and hitting enter.
- To create the database, we can simply type: 
  - CREATE DATABASE foodrecipe;
- Once that's created, we'll switch over to that connection by typing:
  - \c foodrecipe;
- We don't need to do anything else within the Postgres CLI now that we have the database created, so let's come out of the CLI by typing \q.

#  Migrate models into new database.
- Next, need to use Python to generate and migrate models into this new database. This will take the models that I've created for Category, Ingredients, Recipe and Ingredient_index, and build the database schema using the details I've provided. It's important to note, that if you were to modify your models later, then you'll need to migrate these changes each time the file is updated with new context.
- Let's go ahead and access the Python interpreter by typing "python3" and enter.
- From here, we need to import 'db' variable found within the foodrecipe package, so type:
  - from taskmanager import db
- Now, using db, we need to perform the .create_all() method:
- Let's exit the Python interpreter by typing exit().

### Deploy application to Heroku:
I Create an account with ElephantSQL 
- Navigate to ElephantSQL.com and click “Log in”:
- Select “Sign in with GitHub”.
- Authorise ElephantSQL with your selected GitHub account.
- In the Create new team form:
    - Add a team name (your own name is fine)
    - Read and agree to the Terms of Service
    - Select Yes for GDPR
    - Provide your email address
    - Click “Create Team”
- Create a database.
    - Click “Create New Instance”
    - Set up your plan
       - Give your plan a Name (this is commonly the name of the project)
       - Select the Tiny Turtle (Free) plan
       - You can leave the Tags field blank
    - Select “Select Region”
    - Select a data center near you
    - Then click “Review”
    - Check your details are correct and then click “Create instance”
    - Return to the ElephantSQL dashboard and click on the database instance name for this project
    - In the URL section, clicking the copy icon will copy the database URL to your clipboard
    - Leave this tab open, we will come back here later
- Preparing your code for Deployment
    Now you have a database, we need to make some modifications to the code in your IDE.In your IDE workspace
    Before we can build our application on Heroku, we need to create a few files that Heroku will need to run our application:
    - A requirements.txt file which contains a list of the Python dependencies that our project needs in order to run successfully.
    - A Procfile which contains the start command to run the project.
    - Generate the requirements.txt file with the following command in the terminal. After you run this command a new file called requirements.txt should appear in your root directory
      - pip freeze --local > requirements.txt
   - Heroku requires a Procfile containing a command to run your program. Inside the root directory of your project create the new file. It must be called Procfile with a capital P, otherwise Heroku won’t recognise it
   - Inside the file, add the following command
      - web: python run.py
   - Open your __init__.py file
   - Add an if statement before the line setting the SLQALCHEMY_DATABASE_URI and, in the else, set the value to reference a new variable, DATABASE_URL. [database_url](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/screenshots/database_uri.png?raw=true)
   - To ensure that SQLAlchemy can also read our external database, its URL needs to start with “postgresql://”, but we should not change this in the environment variable. Instead, we’ll make an addition to our else statement from the previous step to adjust our DATABASE_URL in case it starts with postgres://:[postgresql](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/screenshots/postgresql.png?raw=true)
   - Save all your files and then add, commit and push your changes to GitHub
- Connecting the database to the hosting platform
   - Log into Heroku.com and click “New” and then “Create a new app”
   - Choose a unique name for your app, select the region closest to you and click “Create app”
   - Go to the Settings tab of your new app
   - Click Reveal Config Vars
   - Return to your ElephantSQL tab and copy your database URL
   - Back on Heroku, add a Config Var called DATABASE_URL and paste your ElephantSQL database URL in as the value. Make sure you click “Add”
   - Add each of your other environment variables except DEVELOPMENT and DB_URL from the env.py file as a Config Var
- Deploying the app
   - Navigate to the “Deploy” tab of your app
   - In the Deployment method section, select “Connect to GitHub”
   - Search for your repo and click Connect
   - Optional: You can click Enable Automatic Deploys in case you make any further changes to the project. This will trigger any time code is pushed to your GitHub repository
   - As we already have all our changes pushed to GitHub, we will use the Manual deploy section and click Deploy Branch. This will start the build process. When finished, it should look something like this
   - Now, we have our project in place, and we have an empty database ready for use. As you may remember from our local development, we still need to add our tables to our database. To do this, we can click the “More” button and select “Run console”
   - Type python3 into the console and click Run
   - This opens the Python terminal, in the same way as it would if we typed python3 into the terminal within our IDE. Let’s now create the tables with the commands we used before
     - from taskmanager import db
     - db.create_all()
   - Exit the Python terminal, by typing exit() and hitting enter, and close the console. Our Heroku database should now have the tables and columns created from our models.py file.
   - The app should be up and running now, so click the “Open app” button
Congratulations! You have successfully deployed your app to Heroku! [live site](https://foodrecipe-798974a40ee6.herokuapp.com/). 

## How to run this project locally 
### Cloning project into GitPod
1. Set up a [GitHub account](https://github.com/)
2. Use the Chrome browser.
3. Install browser extensions for Chrome.
4. After installation restart the browser.
5. Log into GitPod with your gitpod account
6. Navigate to the Project GitHub [repository](https://github.com/fatimagama20/food-receipe).
7. Click the green GitPod button in the top right hand cornner of the repository to create a new [workspace](https://gitpod.io/workspaces) to enable you to work locally'
8. More information about cloning is available [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) 

# Accessibility
Accessible features include:
- Created responsive layouts which I tested across multiple screen sizes. 
- Validated code - see [Testing section](/TESTING.md)

# Credits
## Code
* [Materializecss 1.0.0:](https://materializecss.com/) Materializecss was used significantly throughout the project to make it responsive. I used the navbar, collapsable, dropdown and form.

* [Courses.Code Institute](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DIWADRDB+2022_Q3/courseware/c0c31790fcf540539fd2bd3678b12406/6e44128b0b37416ab40c1a87ef2cb32a/) was used as base to design the project.

## Content
* [Google :](https://www.google.co.uk/) Some content was searched from google
* Some content by the developer.

## Media
* [Google:](https://www.google.co.uk/) Some Images were downloaded from google.

## Acknowledgements
* My Mentor for continuous helpful feedback.
* Tutor/Slack support at Code Institute for their support.








 