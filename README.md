# Natural cosmetics
## Code institute Milestone Project4

[Click here to launch a natural cosmetics app](https://naturalcosmetics-2fcecfab55d3.herokuapp.com/)

Welcome to Natural Cosmetics, your trusted source for high-performance, guilt-free skincare. We understand the challenges of finding products that are effective, safe, and environmentally responsible.​

![](https://github.com/fatimagama20/naturalcosmetics_m4/blob/main/media/mockup.jpg?raw=true)

# About Natural cosmetics

Natural cosmetics are beauty and personal care products made primarily from natural ingredients—such as plant extracts, essential oils, minerals, and other naturally derived substances—without or with minimal use of synthetic chemicals. These products aim to be safer for human health and more environmentally friendly than conventional cosmetics.

## TABLE OF CONTENTS

* [User Experience](#user-experience)
    * [User stories](#user-stories)
* [Design](#design)    
    * [Typography](#typography)
    * [Colour Scheme](#colour-scheme)
    * [Wireframes](#wireframes)
* [Database Design](#database-design)
    * [Relational Database](#relational-database)
    * [Entity Relationship Diagram](#entity-relationship-diagram)
* [Models](#models)
    * [Custom Models](#custom-models)
* [Features](#features)
* [Technologies Used](#technologies-used)
    * [Front End Technologies](#front-end-technologies)
    * [Back End Technologies](#back-end-technologies)
    * [Additional Technologies](#additional-technologies)
* [Credits](#credits)
    * [Code](#code) 
    * [Content](#content)
    * [Media](#media) 
    * [Acknowledgements](#acknowledgements)  

# User Experience (UX)
* ## User stories
  * ### First time customer goal
      #### As a first-time customer, I want:

     1. To clearly understand the benefits of natural cosmetics so that I can decide if they suit my needs.

     2. To read honest reviews from other customers so that I can trust the product before buying.

     3. To try sample sizes or starter kits so that I can test the products before committing to full sizes.

     4. To easily find ingredient information so that I know what I’m buying aligns with my values.

     5. To have a smooth and secure checkout experience so that I feel confident purchasing from the site.

  * ### Returning Customer Goals
      #### As a returning customer, I want:

     1. To quickly reorder my favorite products so that I can save time.

     2. To view my order history and track shipments so that I can stay organized.

     3. To receive personalized product recommendations based on past purchases so that I discover new items I might like.

     4. To get loyalty points or discounts for being a repeat customer so that I feel valued.

     5. To leave feedback or reviews so that I can share my experience with others.

* ### Frequent Customer Goals
   #### As a frequent customer, I want:

     1. To subscribe to auto-delivery or bundles so that I never run out of my essentials.

     2. To get early access to new product launches or limited editions so that I feel like a VIP.

     3. To engage with the brand via community forums or social media so that I feel more connected.

     4. To access exclusive content (e.g., skincare tips, DIY recipes) so that I get more value from the brand.

* ### Site Owner Goals
    #### As the site owner, I want:

     1. To convert first-time visitors into buyers so that I grow my customer base.

     2. To track customer behavior (clicks, purchases) so that I can optimize the user experience.

     3. To reduce cart abandonment with reminders or incentives so that I improve sales performance.

     4. To segment my audience (new vs. loyal) so that I can send targeted marketing messages.

     5. To promote sustainability and transparency so that I build trust and strengthen my brand identity.

* ## Design
  * ### Colour Scheme
    
    I have chosen to use the black and and white as the main colour
  
    * Background colour - #555
    * Button - # White
    * Outline - #fff
    * Skincare section - #darkolivegreen
    * Input name placeholder - #aab7c4
    * Inner content - #6c757d


  * ### Typography

    * Font-family : Lato

  * ### Imagery
    * On the Homepage, I have used a professionally presented food image to suit the purpose of the website, which is providing a good impression for the visitors.
  
* ## Wireframes
  * ### Home page Wireframe
  
  ![](https://github.com/fatimagama20/naturalcosmetics_m4/blob/main/wireframes/homePage.png?raw=true)
  
  * ### Hair & Skincare Products

  ![](https://github.com/fatimagama20/naturalcosmetics_m4/blob/main/wireframes/hairandcare.png?raw=true)

  * ### Fragrances Products

  ![](https://github.com/fatimagama20/naturalcosmetics_m4/blob/main/wireframes/fragrances.png?raw=true)

  * ### Contact us page

  ![](https://github.com/fatimagama20/naturalcosmetics_m4/blob/main/wireframes/contactus.png?raw=true)

## Database
### Relational Database

This project utilises PostgreSQL, a relational database mangement system (RDBMS) managed by ElephantSQL which offers PostgreSQL as a service.

### Entity Relationship Diagram

- I have represented the data within an entity relationship diagram.

![Entity Relationship Diagram](https://github.com/fatimagama20/naturalcosmetics_m4/blob/main/media/databaseschema.png?raw=true)

## Models
In Django, a model is a Python class that defines the structure of a database table. It’s part of Django’s ORM (Object-Relational Mapping) system, which lets you interact with the database using Python code instead of writing raw SQL.

### Custom Models
The following are the custom built models for this app. Each App has been commented to explain the functionality:

#### Contact:
Facilitate communication without exposing your email address directly. It allows to contact via a form by submitting with name, email and message

#### Contact Model Database Table
- id: BigAutoField
- name : Charfield
- email: Charfield
- message : Textfield


### Mailing list:
A subscribe model in a website or web application is a data model used to manage email subscriptions — usually for newsletters, updates, or marketing communications.

#### Subscriber Model Database Table
- id: BigAutoField
- email : Charfield
- date_subscribed: Date

# Features

* Responsive on all device sizes

![Responsive Mockup](https://github.com/fatimagama20/naturalcosmetics_m4/blob/main/media/mockup.jpg?raw=true). 

* Interactive elements

## Navigation:

I created a menu to help enable the user to navigate the app. The menu is responsive and changes to a user-friendly side panel with dropdown functionality on mobile. 
### Purpose of navigation
- Provides quick access to key sections.
- Improves user experience and reduces frustration.
- Acts as a guide so users always know where they are and can easily explore more.
### HOME

Brings users back to the main landing page of the website. Usually includes a general overview, hero image, or featured content.

### ALL PRODUCTS

Likely links to a catalog or shop page listing every product available. Useful for browsing the full inventory at once.

### HAIR & SKIN

Directs to a filtered category showcasing products related to hair and skin care. Examples: shampoos, conditioners, face creams, serums.

### FRAGRANCES

Leads to a section or category for perfumes, colognes, or scented products. Often grouped separately due to specific interests or buying habits.

### CONTACT

Takes users to a contact form. Typically includes a form to send messages.

A Product app in a web project (especially in Django or similar frameworks) is a modular component that manages everything related to products in an online store or catalog. It handles the creation, storage, display, and management of product-related data.

#### Product App
Item_list [CRUD]

A Product app in a web project is a modular component that manages everything related to products in an online store or catalog. It handles the creation, storage, display, and management of product-related data.

Select products of in a specific category (Hair and skin, Fragrances). Sort the products by price, rating or category and add products to the bag - view the total cost of item in the modal box.
Products page layout shows the images of the various products, name, price, category and star rating.
Product detail pages allow the user to find out more about the product, add a product to the bag and increase or decrease the number of products selected. Users can redirect to the shopping page to view additional products to buy. Additional JavaScript code ensures that the decrement button is disabled from going below one item.
On adding the item to the bag, a user sees an automated popup with a Toast message providing feedback to the user confirming the action was successful and how many of that product were added to the bag. The user can also see a list of previous products if they have already been added to the bag, together with an image, description, total price, and a button to go to the checkout page for payment.




#### Bag App
The product summary page provides a list of products selected for purchase with options to increase or decrease the number of items in the bag, or to delete if required via a remove link.
Users can view delivery costs at this point and are advised of how much more spend is required to reach the minimum spend for free delivery as well as delivery costs if the user does not want to increase spend. 
User can proceed to complete purchase via a button stating ‘secure checkout’

#### Checkout App
- To complete the purchase, users complete the form with their delivery and payment details, and click the ‘complete order’ button to finalise. (The user, right to the final action still has the opportunity to adjust the bag contents. If users go ahead with the purchase they are informed for the total amount that will be charged to their card in advance.
- Payments are made via the Stripe payment solution integrated with the app..
A bag session is stored in the database with order details added to the order table 
- Users can save their order details, so then the database is updated with their profile linked to their order. Users on subsequent logins can view their previous orders in order history on their profile page.
- Users receive an email to their inbox to confirm their order and are provided with  the order number. 

#### Sign-up/Login
- The sign-in page allows users to log into their account by filling a username and a password field correctly. If the user has forgotten their password there is a link to the reset password page as well as links to return to the Home page if required.
- Annonymous users can sign up for an account by adding their email address and setting their passwords in the relevant fields. Toasts keep users informed if thier login has been successful. 
- New customers receive an email to their inbox requesting them to click a link to verify their account to complete sign-up.

#### Admin features:
CRUD functionality
Django @login_required decorator provides protection against anonymous users or users without superuser permissions accessing the data store. Superusers are permitted to Add, Edit and Delete products on the Product Management page on login. 

#### Add Product
There is a form on the product management allowing staff to complete the necessary fields. Category, Sku, Name, Description, Options, Price, rating and Image url. Some fields are optional as indicated by an asterisk next to their name. If no image is selected then a default image is used instead.

#### Edit Product 
Admin superusers can go to an existing product on the product page and use the edit link to provide access to the edit product functionality. There is a Toast feedback modal to alert supersuers to the fact they are editing a product. The details of a product can be amended as required and then updated or removed.

#### Delete Product
Admin superusers can go to an existing product on the product page and use the delete link which on click removes a product immediately, with a feedback popup (Toast) to confirm deletion was successful.

#### Contact App

The Contact app handles user communication through a contact form on the website. It allows visitors to send inquiries, feedback, or requests directly to the site administrator or support team.

#### Subscribe App
The Subscribe app manages email subscriptions on the website. It allows visitors to sign up for newsletters, product updates, or marketing emails by simply submitting their email addresses through a subscription form.

#### Future Features
- Product Tags to support for tagging products (e.g., "New", "Sale", "Popular")
- Inventory Management: Track stock levels per product and auto-disable "Add to Cart" if out of stock


# UX features:

# Technologies Used

## Languages Used

  * [HTML5](https://en.wikipedia.org/wiki/HTML5)
  * [CSS3](https://en.wikipedia.org/wiki/CSS)
  * [JS](https://en.wikipedia.org/wiki/JavaScript)
  * [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

  ##  Frameworks, Libraries & Programs Used
  1. [Materialize 1.0.0:](https://materializecss.com/)
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
  9. [Stripe API:](https://docs.stripe.com/api?lang=python)
     * Stripe API - Used to make secured payments on The Nutritionist.
 10. [Amazon AWS S3:](https://aws.amazon.com/)
     * Used to store staticfiles and media folders and files.
   
# Deployment 

## Setting up a GitHub caccount
- I set up a [GitHub account](https://github.com/)
- Used the Chrome browser
- Created the Project GitHub repository
- Clicked the green GitPod button in the top right hand cornner of the repository to create a new [workspace](https://gitpod.io/workspaces) to enable me to work locally

## Deploy application to Heroku:
- Create an account with ElephantSQL 
- Navigate to ElephantSQL.com and click “Log in”:
- Select “Sign in with GitHub”.
- Authorise ElephantSQL with your selected GitHub account.
- In the Create new team form:
   - Add a team name (your own name is fine)
   - Read and agree to the Terms of Service
   - Select Yes for GDPR
   - Provide your email address
   - Click “Create Team”
- Create a database
   - Click “Create New Instance”
   - Set up your plan
   - Give your plan a Name (this is commonly the   name of the project)
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
   - Inside the file, add the following command-web: python run.py
   - Open your __init__.py file
   - Add an if statement before the line setting the SLQALCHEMY_DATABASE_URI and, in the else, set the value to reference a new variable, DATABASE_URL.
   - To ensure that SQLAlchemy can also read our external database, its URL needs to start with “postgresql://”, but we should not change this in the environment variable. Instead, we’ll make an addition to our else statement from the previous step to adjust our DATABASE_URL in case it starts with postgres
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

Congratulations! You have successfully deployed your app to Heroku! [live site](http://naturalcosmetics-2fcecfab55d3.herokuapp.com/).

## AWS Deployment

- Set up hosting for static and media files with AWS (Amazon Web Services). Specifically, using S3 (“Simple Storage Service”) 

- Create an s3 bucket and add the user's groups and security policies for it.

- Connect Django by installing packages **boto3** and **django-storages** and freeze the packages into the requirements.txt file so they get installed on Heroku when deployed.

- Add storages to installed apps in settings.py

- To connect Django to s3 update settings.py - add an if statement to check if there's an environment variable called **USE_AWS** in the environment.

- If so, define the **AWS_STORAGE_BUCKET_NAME**, the **AWS_S3_REGION_NAME**, the **access key**, and **secret access key**, from the environment which must be kept secret.

- Go to Heroku and add the AWS keys to the config variables.

- Add a key **USE_AWS** and set to true. so that the settings file knows to use the AWS configuration when deployed to Heroku.

- Remove the **disable collectstatic** variable to ensure Django will collect static files automatically and upload them to s3 during deployment to Heroku.

- In settings.py file indicate where our static files will be coming from in production which will be the bucket name s3.amazonaws.com.

- Tell Django that in production to use s3 to store static files whenever collectstatic is run, and that any uploaded product images go there. Do this by creating a custom class called static storage which will inherit the one from Django storages, giving it all its functionality, and then tell it that we want to store static files in a location from the settings.py file.

- In settings.py set static file storage to use the storage class just created, and that the location it should save static files is a folder called static.

- Repeat for media files by using the default file storage, and media files location settings.

- Override and explicitly set the URLs for static and media files, using our custom domain and the new locations, so when the project is deployed, Heroku will run **python3 manage.py collectstatic** during the build process, which will search through all apps and project folders looking for static files, which will be collected into a static folder in the s3 bucket automatically.

## How to run this project locally 

### Cloning project into GitPod
1. Set up a [GitHub account](https://github.com/)
2. Use the Chrome browser.
3. Install browser extensions for Chrome.
4. After installation restart the browser.
5. Log into GitPod with your gitpod account
6. Navigate to the Project GitHub [repository](https://github.com/fatimagama20/naturalcosmetics_m4).
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








 