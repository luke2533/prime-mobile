# PrimeMobile - Project 4

PrimeMobile is an online phone provider offering a wide range of mobiles from budget to premium products with customisation options for customers to personalize their devices. The project's goals are to deliver a functional ecommerce store where users can purchase phones, create an account to keep track of their orders and write reviews for other users to read.

## Table of contents

<div id="toc"></div>

- [PrimeMobile - Project 4](#primemobile---project-4)
    * [Table of contents](#table-of-contents)
    * [1.0 UX](#10-ux)
        + [1.1 User goals](#11-user-goals)
        - [1.1.1 Target audience](#111-target-audience)
        + [User needs and goals](#user-needs-and-goals)
        - [1.2.1 User needs:](#121-user-needs-)
        - [1.2.2 How the user needs are met](#122-how-the-user-needs-are-met)
        + [1.3 Devloper and business goals](#13-devloper-and-business-goals)
        - [1.3.1 Goals of the business](#131-goals-of-the-business)
        + [1.4 User stories](#14-user-stories)
    * [2.0 Design choices](#20-design-choices)
        + [2.1 Fonts](#21-fonts)
        + [2.2 Icons](#22-icons)
        + [2.3 Colours](#23-colours)
        + [2.4 Wireframes](#24-wireframes)
        + [2.5 Mockups](#25-mockups)
    * [3.0 Features](#30-features)
        + [3.1 Existing features](#31-existing-features)
        + [3.2 Features left to implement](#32-features-left-to-implement)
    * [4.0 Technologies used](#40-technologies-used)
        + [4.1 HTML](#41-html)
        + [4.2 CSS](#42-css)
        + [4.3 Bootstrap 4.6](#43-bootstrap-46)
        + [4.4 JavaScript](#44-javascript)
        + [4.5 jQuery](#45-jquery)
        + [4.6 Python](#46-python)
        + [4.7 Django](#47-django)
        + [4.8 Stripe](#48-stripe)
    * [5.0 Testing](#50-testing)
    * [6.0 Development life cycle](#60-development-life-cycle)
        + [6.1 Initial commit](#61-initial-commit)
        + [6.10 Store models and updates to sim_free json file](#610-store-models-and-updates-to-sim-free-json-file)
        + [6.20 Updates to README 1.3 - 1.4](#620-updates-to-readme-13---14)
        + [6.30 Changes to phone models and fixture structure](#630-changes-to-phone-models-and-fixture-structure)
        + [6.40 Phone selections store in bag_items](#640-phone-selections-store-in-bag-items)
        + [6.50 Delivey cost displays correctly and change to store models price field](#650-delivey-cost-displays-correctly-and-change-to-store-models-price-field)
        + [6.60 Basic profiles app set up and small change to checkout models](#660-basic-profiles-app-set-up-and-small-change-to-checkout-models)
        + [6.70 Admin add phone page and form](#670-admin-add-phone-page-and-form)
        + [6.80 Reviews display on correct phone page](#680-reviews-display-on-correct-phone-page)
        + [6.90 Phone details page fully responsive on all devices and small changes to add to bag form design](#690-phone-details-page-fully-responsive-on-all-devices-and-small-changes-to-add-to-bag-form-design)
        + [6.100 Store / phone detail page shows overall rating but score accounts for all reviews giving every phone the same score](#6100-store---phone-detail-page-shows-overall-rating-but-score-accounts-for-all-reviews-giving-every-phone-the-same-score)
    * [7.0 Deployment](#70-deployment)
        + [7.1 Local deployment](#71-local-deployment)
        + [7.2 Heroku deployment](#72-heroku-deployment)
    * [8.0 Credits](#80-credits)
        + [8.1 Content](#81-content)
        + [8.2 Code](#82-code)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


## 1.0 UX

[Go to Table Contents](#toc)

### 1.1 User goals

#### 1.1.1 Target audience

PrimeMobile’s target audience are those in need of accessibility to high speed internet access, text and call capabilities over phone contracts that keep them using PrimeMobile long term. With a wide range in smartphones both budget and high end PrimeMobile’s audience is from 16 to 45 needing a connection to digital media at high speeds all over the world. 

### User needs and goals

#### 1.2.1 User needs:

1. Intuitive design
2. Personal user accounts
3. User reviews
4. Product information
5. Secure checkout system
6. Basket / Total cost
7. Store filter
8. Searching capabilities
9. Password security
10. Confirmation email

#### 1.2.2 How the user needs are met

1. First time users can easily navigate the site
2. Users can sign up and log into their accounts where they can save their payment details, view their order history and baskets
3. Signed up users can review a product giving it a star rating out of 5 and short review on their thoughts and experience with the product
4. Each phone will have an overview on the project and a easy to read spec overview with the phones camera, display size, OS and storage size
5. User’s details and purchases will be secure using stripe
6. As users add phones and accessories to their basket the total is displayed on the nav-bar so users don’t go over budget
7. Users can sort by highest rating, lowest rating, price high to low, price low to high and recommended to narrow their search down
8. Users can search for products via the search bar by key words
9. User accounts are password protected to ensure privacy over their personal details
10. After purchase confirmation emails for users after checkout

### 1.3 Devloper and business goals

#### 1.3.1 Goals of the business

1. Add and update phones
2. Sell phones
3. Growth of customers through word of mouth
4. User interaction through reviews and ratings
5. Users sign up to PrimeMobile

### 1.4 User stories

1. User is looking for highest rated phone
2. User wants to leave a review
3. The user wants to pay for a phone 
4. User wants to edit or remove an item in their bag
5. User wants to sign up
6. User wants to save their payment information
7. User wants to check their order history

1.4.1 - The user is looking for PrimeMobile’s highest rated phones according to user reviews to narrow their search and ensure they get the best deal for them. On the store page there are multiple sorting options such as price/rating low to high/high to low and a search bar where users can use keywords such as apple to filter out android phones.

1.4.2 - A user is satisfied or unhappy with the product they have purchased and wishes to write their take positive or negative on the performance, quality and experience with their phone rating it out of 5 stars. On the product page of the product users can scroll down to leave a review which will appear on the product page when submitted and can directly affect how high the phone is once filtered.

1.4.3 - The user wants to purchase their bag items securely through checkout after finalizing their phone specs on the bag page they can click the checkout link and fill in their delivery information and card details 

1.4.4 - A user wants to remove or change a detail on an item in the basket. In the basket under the summary of the item they can click delete to remove the item from the basket or edit to change the device's quantity.

1.4.5 - The user wants to create an account so that they can review their phone. When the user clicks to review the page while not signed up they are taken to the sign up page which can also be accessed via the nav-bar where they can sign up or if they have an account log in.

1.4.6 - The user wants to save their payment information for future purchases or payments towards SIM plans. To do so the user needs an account where they can tick a box on checkout that will save their details upon checkout so they can skip it on the next purchase.

1.4.7 The user wants to check their order history to see if it went through. On the user account page (when logged in) users can find their order history with the date of purchase, how much they paid, the type of purchase and the contract length. Users will also receive an email with a receipt as confirmation of a successful purchase. 

## 2.0 Design choices

[Go to Table Contents](#toc)

### 2.1 Fonts

Title / subtitles font is [Bebas Neue](https://fonts.google.com/specimen/Bebas+Neue?query=Bebas+Neue):

Text font is [Ubuntu](https://fonts.google.com/specimen/Ubuntu?query=Ubuntu):

### 2.2 Icons

[Font awesome:](https://fontawesome.com/)

- Bag icon
- Facebook icon
- YouTube icon 
- Twitter icon
- Instagram icon
- Home icon
- Account icom
- Phone icon
- Basket icon
- Star icon
- Camera icon
- CPU icon
- Storage icon

### 2.3 Colours

- #fff - Primary color
- #04162e - Background color
- #181818 - Input / button background color
- #c31a8f - Secondary color
- #21fdda - Highlighted color

### 2.4 Wireframes

[Go to Table Contents](#toc)

[Wireframe pdf](static/wireframes/Prime_Mobile_Wireframe.pdf)

Nav / Footer wireframes

![Nav / Footer mobile](static/wireframes/template-desktop_page-0001.jpg)

![Nav / Footer tablet](static/wireframes/template-tablet_page-0001.jpg)

![Nav / Footer desktop](static/wireframes/template-mobile_page-0001.jpg)

Home wireframes

![Home mobile](static/wireframes/home-desktop_page-0001.jpg)

![Home tablet](static/wireframes/home-tablet_page-0001.jpg)

![Home desktop](static/wireframes/home-mobile_page-0001.jpg)

Store wireframes 

![Store mobile](static/wireframes/store-desktop_page-0001.jpg)

![Store tablet](static/wireframes/store-tablet_page-0001.jpg)

![Store desktop](static/wireframes/store-mobile_page-0001.jpg)

Phone details wireframes

![Phone details mobile](static/wireframes/phone-desktop_page-0001.jpg)

![Phone details tablet](static/wireframes/phone-tablet_page-0001.jpg)

![Phone details desktop](static/wireframes/phone-mobile_page-0001.jpg)

Bag wireframes

![Bag mobile](static/wireframes/bag-desktop_page-0001.jpg)

![Bag tablet](static/wireframes/bag-tablet_page-0001.jpg)

![Bag desktop](static/wireframes/bag-mobile_page-0001.jpg)

Checkout wireframes

![Checkout mobile](static/wireframes/checkout-desktop_page-0001.jpg)

![Checkout tablet](static/wireframes/checkout-tablet_page-0001.jpg)

![Checkout desktop](static/wireframes/checkout-mobile_page-0001.jpg)

Profile wireframes

![Profile mobile](static/wireframes/profile-desktop_page-0001.jpg)

![Profile tablet](static/wireframes/profile-tablet_page-0001.jpg)

![Profile desktop](static/wireframes/profile-mobile_page-0001.jpg)

Review wireframes

![Review mobile](static/wireframes/review-desktop_page-0001.jpg)

![Review tablet](static/wireframes/review-tablet_page-0001.jpg)

![Review desktop](static/wireframes/review-mobile_page-0001.jpg)

Admin wireframes

![Admin mobile](static/wireframes/admin-desktop_page-0001.jpg)

![Admin tablet](static/wireframes/admin-tablet_page-0001.jpg)

![Admin desktop](static/wireframes/admin-mobile_page-0001.jpg)

Log in wireframes

![Log in mobile](static/wireframes/login-desktop_page-0001.jpg)

![Log in tablet](static/wireframes/login-tablet_page-0001.jpg)

![Log in desktop](static/wireframes/login-mobile_page-0001.jpg)

Sign up wireframes

![Sign up mobile](static/wireframes/signup-desktop_page-0001.jpg)

![Sign up tablet](static/wireframes/signup-tablet_page-0001.jpg)

![Sign up desktop](static/wireframes/signup-mobile_page-0001.jpg)

### 2.5 Mockups

[Go to Table Contents](#toc)

[Mockups pdf](static/mockups/primemobile-mockups.pdf)

Home mockups

![Home mobile](static/mockups/home-desktop.png)

![Home tablet](static/mockups/home-tablet.png)

![Home desktop](static/mockups/home-mobile.png)

Store mockups 

![Store mobile](static/mockups/store-desktop.png)

![Store tablet](static/mockups/store-tablet.png)

![Store desktop](static/mockups/store-mobile.png)

Phone details mockups

![Phone details mobile](static/mockups/phone-desktop.png)

![Phone details tablet](static/mockups/phone-tablet.jpg)

![Phone details desktop](static/mockups/phone-mobile.jpg)

Bag mockups

![Bag mobile](static/mockups/bag-desktop.png)

![Bag tablet](static/mockups/bag-tablet.png)

![Bag desktop](static/mockups/bag-mobile.jpg)

Checkout mockups

![Checkout mobile](static/mockups/checkout-desktop.png)

![Checkout tablet](static/mockups/checkout-tablet.png)

![Checkout desktop](static/mockups/checkout-mobile.png)

Profile mockups

![Profile mobile](static/mockups/profile-desktop.jpg)

![Profile tablet](static/mockups/profile-tablet.png)

![Profile desktop](static/mockups/profile-mobile.png)

Review mockups

![Review mobile](static/mockups/review-desktop.png)

![Review tablet](static/mockups/review-tablet.png)

![Review desktop](static/mockups/review-mobile.png)

Admin mockups

![Admin mobile](static/mockups/admin-desktop.png)

![Admin tablet](static/mockups/admin-tablet.png)

![Admin desktop](static/mockups/admin-mobile.png)

Log in mockups

![Log in mobile](static/mockups/login-desktop.png)

![Log in tablet](static/mockups/login-tablet.png)

![Log in desktop](static/mockups/login-mobile.png)

Sign up mockups

![Sign up mobile](static/mockups/signup-desktop.png)

![Sign up tablet](static/mockups/signup-tablet.png)

![Sign up desktop](static/mockups/signup-mobile.png)

## 3.0 Features

[Go to Table Contents](#toc)

### 3.1 Existing features

- Search bar - Search bar filter products by name
- Filter system - Filter products by price and rating low to high/high to low
- Customize product - Users can pick the color and storage capacity of their device
- Reviews - Product reviews submitted by users
- Ratings - Users can rate products out of 5 stars affecting where are positioned on store page
- Basket total - Upfront cost total in basket
- Secure checkout - Purchases and billing details are secured through stripe
- Email confirmation - Email receipt on confirmed orders
- Account creation - Users can sign up to save billing details, order history and monthly payment total
- Password security - User accounts are protected by password
- Save payment information - Billing details can be saved to accounts for faster checkout
- Free delivery - User’s who spend more than £799.99 get free delivery 

### 3.2 Features left to implement

- SIM deals - Users can pay overtime or in one payment
- Contact - Users can submit complaints to PrimeMobile
- Change password - Users can change their password if they forget it
- Phone deals - Phone discounts on certain products

## 4.0 Technologies used

[Go to Table Contents](#toc)

### 4.1 HTML

This project uses HTML5 used for templates and structure of the website

### 4.2 CSS

This project uses CSS3 used to style, more advanced responsive structuring for all devices

### 4.3 Bootstrap 4.6

This project uses Bootstrap a CSS libary to speed up devlopment and grid structure for more responsive website

### 4.4 JavaScript

This project uses JavaScript for slideshow, toast messages, phone color options and star rating reviews

### 4.5 jQuery

This project uses jQuery for more efficient JavaScript

### 4.6 Python

This project uses Python

### 4.7 Django

This project uses the Django framework

### 4.8 Stripe

This project uses stripe for secure checkout

## 5.0 Testing

[Go to Table Contents](#toc)

[Click here for Testing doc](testing.md)

## 6.0 Development life cycle

### 6.1 Initial commit

Additions:

- Django
- prime_mobile app
- gitignore file
- README Template
- Created admin account

### 6.2 Allauth setup and authentication 

Additions: 

- Installed and setup allauth
- Added requirements.txt
- Added templates file directory

### 6.3 Base template and allauth files

Additions:

- Allauth files
- Base.html template
- Nav bar
- Footer
- Bootstrap
- jQuery
- Fontawesome

### 6.4 Home app / page created

Additions:

- Created home app
- Home page html added
- Home app view added
- Created home urls.py

### 6.5 Home page CSS, reponsive breakpoints and static directory

Additions:

- Fixed home page issues
- Added static directory
- Added Nav, Footer and home page CSS
- Added responsive breakpoints for home page
- Added media file and background image

### 6.6 Log in, log out and sign up pages work

Additions:

- Users can log in and out
- Users can sign up

### 6.7 Store app and files

Additions:

- Store app
- Store urls
- Basic store views
- store.html

### 6.8 Store page structure and styling

Additions:

- store.html content
- Store page CSS
- Product images
- Fixtures file

### 6.9 Added phone fixtures files

Additions:

- Categories fixtures
- Phone fixtures

### 6.10 Store models and updates to sim_free json file

Additions:

- Updates to sim_free json file
- Store models

### 6.11 Pillow installed and fixtures loaded successfully

Additions:

- Pillow installed
- Fixtures migrated

### 6.12 Products list on store page

Additions: 

- Updates to store admin
- Store views
- Products listed on phone page

Issue #1: SimFree displays 162 phones on store page most duplicates

### 6.13 Product images appear on product card

Additions:

- Product images appear on product card

### 6.14 Store product card structuring and phone details page

Additions:

- Changes to product card structuring on devices
- Phone details page

### 6.15 Frosted glass background and phone image slideshows

Additions:

- Frosted glass product cards
- Phone detail image slideshow

### 6.16 Basic structural changes to phone details page

Additions:

- Changes to phone details page
- Basic structure for review section

### 6.17 Added phone fixtures

Additions:

- Updated SimFree model
- Added Phone model
- Added phone.json

### 6.18 Overhaul to to store fixtures and sim free phones fix

Additions:

- Changes to Categories fixtures and model
- Changes to Phone fixtures and model
- Changes to SimFree fixtures and model
- Only 1 product card per phone
- Updates to store admin
- Changes to store page
- Changes to product page

Issue #1 RESOLVED : SimFree displays 162 phones on store page most duplicates - RESOLVED (6.12)

### 6.19 Updates to README 1.1 - 1.2

Additions:

- README PrimeMobile overview
- README Target audience
- READNE User needs and how there are met

### 6.20 Updates to README 1.3 - 1.4

[Go to Table Contents](#toc)

Additions:

- README Goals of the buisness
- README User stories

### 6.21 Updates to README 3.1 Features

Additions:

- README Existing features

### 6.22 Search bar functional by name

Additions:

- Searching functionality

### 6.23 Sort by price working

Additions:

- Sort low to high price
- Sort high to low price

### 6.24 Search total and bag app created

Additions:

- Total products in search
- Created bag app
- Bag page
- Bag URLS file

### 6.25 Basic bag structure and small changes to product details page

Additions:

- Basic bag page structure
- Small changes to product details page

### 6.26 Fixture changes

Additions:

- Changes to phone fixtures

### 6.27 Updated data to store app

Additions:

- Changes to store models
- Migrations to store
- Deleted simFree fixtures

### 6.28 Small updates to nav and bag page

Additions:

- Changes to navbar buttons
- Changes to product page form
- Changes to bag page
- Nav bar has filters
- Bag button changes

### 6.29 Background for color button JS

Additions:

- Custom phone form structure
- Color buttons JS

### 6.30 Changes to phone models and fixture structure

Additions:

- Changes to phone models
- Updated fixtures structure

### 6.31 Phone detail page shows all phone colors

Additions:

- Changes to phone admin
- Displays phone colors
- Changes to phone JS for colors

### 6.32 Changes to store fixtures

Additions:

- Changes to fixtures to include 4 colors, storage capacities and prices
- Changes to store models
- Changes to store admin

### 6.33 Bag contents and place holder delivery banner

Additions:

- Context.py
- Placeholder free delivery banner

### 6.34 Adding and quantity working for bag

Additions:

- Color options text is hidden
- Can add items to bag
- Quantity works

### 6.35 Items show in bag, as well as grand total

Additions:

- Bag displays bag items
- Item name, SKU, storage_1 and price_1 display
- Bag total displayed

Note: price/storage 2 to 4 options do not display

### 6.36 Delete items from bag

Additions:

- Delete items from bag

### 6.37 Added toasts for adding/deleting items from bag

Additions:

- Toasts success
- Toasts error
- Toasts info
- Toasts warning
- Changes to bag page

### 6.38 Phone selection working

Additions:

- Color selection working
- Storage selection working
- Price based on storage works

### 6.39 Updates to fixtures price models to decimal

Additions:

- Updates to fixtures price models

### 6.40 Phone selections store in bag_items

[Go to Table Contents](#toc)

Additions:

- Color selections store in bag_items
- Storage selections store in bag_items
- Price selections store in bag_items
- Quantity selections store in bag_items 

Note: Does not yet display on bag page

### 6.41 Phone selections display in bag correctly

Additions:

- Phone selections display in bag correctly

Issue: Adding the same phone or with diffrent options to the bag when the same phone is already in the bag causes errors

### 6.42 Add same phone to bag more then once

Additions:

- Add same phone to bag more then once

### 6.43 Checkout app and page created

Additions:

- Checkout app
- Checkout HTML

### 6.44 Checkout models

Additions:

- Checkout models

### 6.45 Checkout models function order ID, Total and save override

Additions:

- Checkout generate order id
- Checkout update total
- Checkout override save for order and order items

### 6.46 Creation of signals.py, checkout migration, checkout models added to admin and changes to app.py

Additions:

- Checkout migration
- Added checkout to admin
- signals.py
- app.py ready function

### 6.47 Checkout form.py created for order from

Additions:

- Checkout form.py

### 6.48 Checkout views, urls added and installed crispy forms

Additions:

- Checkout views
- Checkout URLs
- Installed Django crispy forms
- Updated requirements.txt file

### 6.49 Basic checkout page structure

Additions:

- Checkout page structure
- Checkout page from

### 6.50 Delivey cost displays correctly and change to store models price field

Additions:

- Changed price 1 to 4 from float to decimal store models
- Migrated changes
- Delivery cost works
- Delivery cost displays on bag and checkout page

### 6.51 Set up stripe and added card details input

Additions:

- Setting up stripe.js
- static and JS file (checkout)
- CSS file (checkout)
- Added card details input

### 6.52 Installed stripe and added error to card detail input box

Additions:

- Installed stripe
- Updated requirements.txt file
- Added error message to card details input
- Checkout views current bag rounded total
- Keys exported from version control

### 6.53 Checkout form submission working

Additions:

- Checkout form submission working

### 6.54 Form sumbits landing user on checkout success page

Additions:

- Checkout success page
- User on checkout success page after form is submited
- Order Form and form data save to Order/Order items

### 6.55 Order details and items successfully POST 

Additions:

- Checkout init file default app config for signals.py
- Order details and items successfully POST

### 6.56 Checkout success page displays order information

Additions:

- Deleting orders succesfully
- Checkout success page displays order information

### 6.57 Webhooks.py created error 401

Additions:

- Webhook_handler.py
- Webhooks.py

Webhooks not working error 401

### 6.58 Checkout page will cache and reload page without charging user if form fails to submit

Additions:

- Checkout submit payment method object (JS)
- Checkout page will cache and reload page without charging user if form fails to submit

Webhooks not working error 401 (Public key issue?)

### 6.59 Installed django countries and updated checkout models

Additions:

- Installed django countries
- Updated requirements.txt file
- Updated checkout models country and phone_size to phone_storage

### 6.60 Basic profiles app set up and small change to checkout models

[Go to Table Contents](#toc)

Additions:

- Created Profile app
- Updates to checkout models
- UserProfile class created for profiles models
- Created profiles urls.py
- Created profile.html

### 6.61 Updates to allauth log in and sign up pages plus links from base template to profile page

Additions:

- Static file and profiles.css
- Changes to Allauth Log in page
- Changes to Allauth Sign up page
- Added links to profile page

### 6.62 Set delivery default form and basic structure for order history

Additions:

- Profile page displays username
- Profile form.py
- Set delivery default info form
- Basic order history structure

### 6.63 Webooks successful went through successfully

Additions:

- Webooks successful went through successfully (payment_intent.created=200)

### 6.64 Fixed issue with JS error

Additions:

- Fixed issue with JS getting the form data from the checkout page

### 6.65 Stripe bug fix and added basic structure to bag editing

Additions:

- Fixed bug where user can skip card box on checkout
- Metadata goes through with users order, save info and username
- Stripe succesfully charges user
- Failed charge working correctly
- Stripe authentication working correcly
- Added basic structure for bag editing

### 6.66 Successful payment webhook attempts being created multiple times before failure

Additions:

- Webhook payment succeeded handle
- Updates to model incase of user purchasing the same phone causing the previous order to be replaced
- Migrated checkout changes
- Updated checkout admin
- While loop on successful payment to attempt to create order multiple times before failure

### 6.67 Order history displays on profile page

Additions:

- Checkout success view updated
- Save users infomation
- Order history displays

### 6.68 Order history items display and links to past order success page

Additions:

- Order history items display
- Order number links to past orders confirmation page

### 6.69 Confirmation email and user info in checkout

Additions:

- Users with default checkout information will have their info ready for checkout
- Confirmation emails subject and body

### 6.70 Admin add phone page and form

Additions:

- Store forms.py for admin
- add_phone.html
- Add phone page form

### 6.71 Admin nav bar dropdown and Edit Phone page

Additions:

- Admin dropdown on navbar
- edit_phone.html
- Successfully added product

### 6.72 Admin can edit and add phones to store

Additions:

- Admin can edit phones
- Admin can add phones
- Throws correct errors if form is filled incorrectly

### 6.73 Admin edit and delete buttons on phone details pages and further security for admin

Additions:

- Admin can delete phones from store page
- Phone detail page edit and delete for admin only
- Further security for add, edit and deleting phones redirecting normal users back to home page

### 6.74 Basic set up for reviews app

Additions:

- Added reviews app
- Basic review setup
- Review urls.py

### 6.75 Bag edit not working and removed checkout edit and delete

Additions:

- Removed delete and edit buttons from checkout
- Removed bag edit collapse
- Bag edit not working

### 6.76 Working bag editing and reviews.html

Additions:

- Working bag editing
- Updates to phone detail review section
- Added reviews.html and template folder

### 6.77 Upated review and store models, review section only accessed by users with accounts

Additions:

- Updated rating field in store models (Phone)
- Users have to be logged in to access review page
- Created PhoneReview model in reviews models

### 6.78 Updated reviews admin and added JS setRating function to select rating

Additions:

- Migrated changes to store and review models
- Updated review admin
- JS setRating working

### 6.79 Issues with review form posting to django and stars not being checked

Additions:

- Fails to post to django but form works otherwise
- Stars working but won't check when hovered or clicked

### 6.80 Reviews display on correct phone page

[Go to Table Contents](#toc)

Additions:

- User's name, title and body display in review section (Added through admin)
- Reviews display on correct phone page

Issue: No reviews message repeats based on how many reviews there are due to being in for loop

### 6.81 Added forms file and changes to review views

Additions:

- Review function for views.py
- Changes to add review
- Added forms.py

### 6.82 Added review form, updated views, models and migrated changes

Additions:

- Added review form
- Updated view add review
- Changed review models and migrated them

Note: Still have not successfully posted to django
 
### 6.83 Reviews successfully POST

Additions:

- Reviews successfully POST

### 6.84 Admin can remove reviews

Additions:

- Admin can remove reviews

### 6.85 Stars have color when checked on review page and issue with review ratings

Additions:

- Stars have color when checked (Review page)
- Phone detail review section star rating

Issue: Phones with more then one review share the same rating or add together 

### 6.86 Nav and footer updated to be responsive on all devices

Additions:

- Nav updated to be responsive on all devices
- Footer updated to be responsive on all devices

### 6.87 Home updated to be responsive on all devices

Additions:

- Removed home page SIM type links
- Home updated to be responsive on all devices

### 6.88 Store page updated to be responsive on all devices

Additions:

- Store page updated to be responsive on all devices

### 6.89 Desktop phone detail page review section displays as a sidebar and responsive on all devices

Additions:

- Desktop phone detail page review section displays as a sidebar
- Phone detail page updated to be responsive on all devices

### 6.90 Phone details page fully responsive on all devices and small changes to add to bag form design

Additions:

- Changes to phone details review section design
- Changes to phone details phone options design
- Phone details page fully responsive on all devices

### 6.91 Bag page updated to be responsive on all devices

Additions:

- Fixed bag button on nav from changing shape when items are in the bag
- Bag page updated to be responsive on all devices

### 6.92 Checkout page updated to be responsive on all devices

Additions:

- Checkout page updated to be responsive on all devices

### 6.93 Checkout success page updated to be responsive on all devices

Additions:

- Checkout success page updated to be responsive on all devices

### 6.94 Toasts fixed empty space issue and updated admin pages to be responsive on all devices

Additions:

- Toasts updated and fixed empty space issue
- Admin add page updated to be responsive on all devices
- Admin edit page updated to be responsive on all devices

### 6.95 Profile page updated to be responsive on all devices

Additions:

- Profile page updated to be responsive on all devices

### 6.96 Review button and page updated to be responsive on all devices

Addition:

- Updated review button on phone details page to be more visable
- Review page updated to be responsive on all devices

### 6.97 Allauth log in / out pages updated to be responsive on all devices

Additions:

- Log out updated to be responsive on all devices
- Log in updated to be responsive on all devices

### 6.98 Allauth vefication and sign up pages updated to be responsive on all devices

Additions:

- Vefication sent (Allauth) updated to be responsive on all devices
- Sign up page updated to be responsive on all devices

### 6.99 Quick CSS fixes and user review ratings showing correct stars

Additions:

- Centered bag is empty text
- Checkout images don't overlap
- Bag buttons look and fit better
- Phone's without reviews don't have the "No reviews" text multiple times
- Fixed user reviews star ratings which no show correct stars
- Overall phone ratings show correctly (When changed manually by admin)

### 6.100 Store / phone detail page shows overall rating but score accounts for all reviews giving every phone the same score

[Go to Table Contents](#toc)

Additions:

- Phone detail page shows overall phone rating
- Store page shows overall phone rating

Issue: The overall score is made up of ALL reviews from ALL phones causing every phone to share the same score

### 6.101 Overall score issue RESOLVED overall phone rating displays correct rating

Additions:

- Overall score issue RESOLVED (6.100)
- Phone detail page shows overall indivdial phone rating
- Store page shows overall indivdial phone rating

### 6.102 Rating low to high / high to low working and quantity error resolved

Additions:

- Sort low to high / high to low by rating on store page filter
- Sort low to high / high to low by rating on navbar link
- Issue RESLOVED price is now a float when the quantity is 2 or higher

Issue RESLOVED (6.102): Checkout phone_price would become a string if the quantity was 2 or higher

### 6.103 Minor fixes to CSS, allauth pages and footer links for profile, store and bag

Additions:

- Minor changes to allauth pages
- Small CSS quick fixes on smaller devices
- Footer links to profile, store and bag pages

### 6.104 Added testing.md, added Samsung S22 during admin testing and minor CSS fixes

Additions:

- Added free delviery message at top of bag page
- Added Samsung S22
- Updated Samsung S22
- Added S22 images
- Added testing.md file

### 6.105 Updated README 1.0 UX and 3.0 Features

Additions:

- Updated 1.0 README UX
- Updated 3.0 README Features

### 6.106 Updated README 2.0 Design choices, 4.0 Tech used and 8.0 Credits

Additions:

- Updated 2.0 README Design choices
- Updated 4.0 README Technologies used
- Updated 8.0 README Credits
- Added testing.md links to README
- Comments to all files

### 6.107 README Table of contents

Additions:

- README table of contents

### 6.108 Updated README 2.4 wireframes, images and pdf

Additions:

- Go to table of contents README links
- Wireframe images
- Wireframe PDF
- Updated 2.4 README Wireframes

### 6.109 Updated 2.5 README Mockups, images and pdf

Additions:

- Mockup file
- Mockup images
- Mockup PDF
- Updated 2.5 README Mockups

### 6.110 Testing.md updated 5.1 to 5.6

[Go to Table Contents](#toc)

Additions:

- Testing.md 5.1 known bugs added
- Testing.md 5.2 code validation added
- Testing.md 5.3 navbar added
- Testing.md 5.4 log in added
- Testing.md 5.5 sign up added
- Testing.md 5.6 sign out added

### 6.111 Testing.md updated 5.7 to 5.11

Additions:

- Testing.md 5.7 verify account added
- Testing.md 5.8 footer added
- Testing.md 5.9 home added
- Testing.md 5.10 filters added
- Testing.md 5.11 search bar added

### 6.112 Testing.md updated 5.12 to 5.16

Additions:

- Testing.md 5.12 store added
- Testing.md 5.13 overall ratings store + detail page added
- Testing.md 5.14 image slideshow added
- Testing.md 5.15 spec overview added
- Testing.md 5.16 Spec picker / Color / Storage / Price / Quantity added

### 6.113 Testing.md updated 5.17 to 5.21

Additions:

- Testing.md 5.17 phone review section added
- Testing.md 5.18 bag page + phone info added
- Testing.md 5.19 delete phone from bag added
- Testing.md 5.20 update phone from bag added
- Testing.md 5.21 bag total added

### 6.114 Testing.md updated 5.22 to 5.26

Additions:

- Testing.md 5.22 checkout bag overview added
- Testing.md 5.23 checkout total added
- Testing.md 5.24 checkout form added
- Testing.md 5.25 checkout success added
- Testing.md 5.26 checkout success table added

### 6.115 Testing.md updated 5.29 to 5.30

Additions:

- Testing.md 5.27 profile page added
- Testing.md 5.28 order history added
- Testing.md 5.29 order number receipt page added
- Testing.md 5.30 review page / form added

### 6.116 Testing.md updated 5.31 to 5.34

Additions:

- Testing.md 5.31 Admin add phone added
- Testing.md 5.32 Admin edit phone added
- Testing.md 5.33 Admin remove phone added
- Testing.md 5.34 Admin remove review added

### 6.117 Testing.md 5.2 updated all python files up to PEP8 validation

Additions:

- Testing.md 5.2 Updated
- All python files up to PEP8 validation

### 6.118 Code validation complete and ready for deployment

Additions:

- All HTML files clear of errors
- All CSS files clear of errors
- All JS files clear of errors
- Testing.md 5.2 Updated
- Installed dj_database_url
- Installed psycopg2-binary
- Updated requirements file

### 6.119 Deployment to heroku

Additions:

- Installed gunicorn
- Updated requirements file
- Created Procfile

### 6.120 Removed secret key and changed debug mode

Additions:

- Removed secret key
- Changed debug mode

### 6.121 Setting up AWS static files to heroku and created custom_storages.py

Additions:

- Installed boto3
- Installed django-storages
- Updated requirements file
- Created custom_storages.py
- Setting up AWS static files to heroku

### 6.122 Profile quick fix

Additions:

- Profile quick fix

### 6.123 Settings quick fix

Additions:

- Changes to setting file

### 6.124 Set up emails for verification and order confirmation

Additions:

- Set up emails

## 7.0 Deployment

[Go to Table Contents](#toc)

### 7.1 Local deployment

### 7.2 Heroku deployment

## 8.0 Credits

[Go to Table Contents](#toc)

### 8.1 Content

- Icons - [Font Awesome](https://fontawesome.com/)
- Webhook handlers - Django mini project
- Webhooks - Django mini project
- Store page divisble rows - Django mini project
- Save info - Django mini project
- Order history - Django mini project
- Set default information - Django mini project
- Navbar tablet structure - Django mini project
- Bag total nav - Django mini project
- Search bar and results - Django mini project

### 8.2 Code

- Scroll bar CSS - [Scrollbar](https://stackoverflow.com/questions/12337821/css3-scrollbar-styling-on-a-div)
- Refresh the cache so CSS updates - [CSS Refresh](https://stackoverflow.com/questions/52682812/django-css-not-updating)
- Review star form - [Star form](https://dev.to/leonardoschmittk/how-to-make-a-star-rating-with-js-36d3)
- Bootstrap dropdown - [Dropdown](https://getbootstrap.com/docs/4.6/components/dropdowns/)
- Bootstrap slideshow - [Carousel](https://getbootstrap.com/docs/4.6/components/carousel/)
- Bootstrap nav - [Navbar](https://getbootstrap.com/docs/4.6/components/navs/)
- Bootstrap collapse - [Collapse](https://getbootstrap.com/docs/4.6/components/collapse/)
- Django mini project - [Mini Project](https://github.com/luke2533/Django-mini-project)

[Go to Table Contents](#toc)