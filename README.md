# PrimeMobile - Project 4

PrimeMobile is a phone provider with a wide range of devices, accessories and SIM plans for users to choose from with options to customize their phone, how they pay and contracts that covers text, calls and data for 1 to 2 years. The project's goal is to deliver an intuitive, secure and customer friendly experience for users to purchase phones/contracts with an assurance of quality and confidence in PrimeMobile, where user feedback directly reflects what products are promoted.

## Table of contents

## 1.0 UX

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

1. Provide users with text, call and high speed data
2. Sell phones
3. Sell SIM deals for long term revenue
4. Growth of customers through deals
5. User interaction through reviews and ratings
6. Users sign up to PrimeMobile

### 1.4 User stories

1. User is looking for highest rated phone
2. User wants to leave a review
3. The user wants to pay for a phone in one payment
4. The user wants to buy a SIM plan
5. User wants to edit or remove an item in their bag
6. User wants to sign up
7. User wants to save their payment information
8. User wants to check their order history

1.4.1 The user is looking for PrimeMobile’s highest rated phones according to user reviews to narrow their search and ensure they get the best deal for them. On the store page there are multiple sorting options such as price/rating low to high/high to low and a search bar where users can use keywords such as apple to filter out android phones.

1.4.2 A user is satisfied or unhappy with the product they have purchased and wishes to write their take positive or negative on the performance, quality and experience with their phone rating it out of 5 stars. On the product page of the product users can scroll down to leave a review which will appear on the product page when submitted and can directly affect how high the phone is once filtered.

1.4.3 The user wants to purchase the phone without a SIM card and pay in full at checkout. When on the phone's product page the user can select the SIM Free tab and add it to the basket where they can pay the full price in one payment.

1.4.4 The user wants to purchase a phone and a SIM Plan and pay over time with text, calls and mobile data. When on the phones product page the user can select the SIM Plan tab giving them the option to pick from 4 SIM plans for text, calls, data and the length of the contract based on the tier there will be an upfront cost and then a monthly cost.  

1.4.5 A user wants to remove or change a detail on an item in the basket. In the basket under the summary of the item they can click delete to remove the item from the basket or edit to change the device's color, storage capacity, add a SIM plan or buy the phone alone.

1.4.6 The user wants to create an account so that they can review their phone. When the user clicks to review the page while not signed up they are taken to the sign up page which can also be accessed via the nav-bar where they can sign up or if they have an account log in.

1.4.7 The user wants to save their payment information for future purchases or payments towards SIM plans. To do so the user needs an account where they can tick a box on checkout that will save their details upon checkout so they can skip it on the next purchase.

1.4.8 The user wants to check their order history to see if it went through. On the user account page (when logged in) users can find their order history with the date of purchase, how much they paid, the type of purchase and the contract length. Users will also receive an email with a receipt as confirmation of a successful purchase. 

## 2.0 Design choices

### 2.1 Fonts

### 2.2 Icons

### 2.3 Colours

### 2.4 Wireframes

### 2.5 Mockups

## 3.0 Features

### 3.1 Existing features

- Search bar - Search bar filter products by name
- Filter system - Filter products by price and rating low to high/high to low
- Customize product - Users can pick the color and storage capacity of their device
- SIM deals - Users can pay overtime or in one payment
- Reviews - Product reviews submitted by users
- Ratings - Users can rate products out of 5 stars affecting where are positioned on store page
- Contact - Users can submit complaints to PrimeMobile
- Basket total - Upfront cost total in basket
- Secure checkout - Purchases and billing details are secured through stripe
- Email confirmation - Email receipt on confirmed orders
- Account creation - Users can sign up to save billing details, order history and monthly payment total
- Password security - User accounts are protected by password
- Save payment information - Billing details can be saved to accounts for faster checkout

### 3.2 Features left to implement

## 4.0 Technologies used

### 4.1 HTML

### 4.2 CSS

### 4.3 Bootstrap 4.6

### 4.4 JavaScript

### 4.5 jQuery

### 4.6 Python

### 4.7 Django

### 4.8 Stripe

## 5.0 Testing

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

## 7.0 Deployment

### 7.1 Local deployment

### 7.2 Heroku deployment

## 8.0 Credits

### 8.1 Content

### 8.2 Code