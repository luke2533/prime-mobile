# 5.0 Testing documention

## 5.1 Known bugs

| Known bugs  | Issue | Pass/Fail |
| --------------- | ------------------------------------------------------------------------- | --------- |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |

## 5.2 Code validation

| Test  | Expected result | Pass/Fail |
| --------------- | ------------------------------------------------------------------------- | --------- |
| HTML W3C validator | All pages pass the validator |  |
| CSS W3C validator | All pages pass the validator |  |
| JS JSHint validator | All pages pass the validator |  | 
| PEP8 | All files pass PEP8 | |

## 5.3 Nav-bar

| Test  | Expected result | Pass/Fail |
| --------------- | ------------------------------------------------------------------------- | --------- |
| Prime mobile title link | Links user back to home page | Pass |
| Shop dropdown | Links to store page and filters | Pass |
| Profile link (When signed in) | Links users to profile page and order history | Pass |
| Profile link (When signed out) | Links to log in page | Pass |
| Admin dropdown | When user is admin link to add phone | Pass |
| Sign out (When signed in) | Links to sign out page | Pass |
| Log in (When signed out) | Links to log in page | Pass |
| Sign up (When signed out) | Links to sign up page | Pass |
| Tablet and smaller devices collapse menu | Smaller devices have a collapsable | Pass |
| Nav responsive on all devices | Nav is responsive on all devices | Pass |

## 5.4 Log in

| Test  | Expected result | Pass/Fail |
| --------------- | ------------------------------------------------------------------------- | --------- |
| Log in button | When clicked with correct info signs user in | Pass |
| Log in submit no username | Please fill in this field pop up | Pass |
| Log in submit no password | Please fill in this field pop up | Pass |
| Log in submit wrong username | Incorrect username/password message | Pass |
| Log in submit wrong password | Incorrect username/password message | Pass |
| Remember me checkbox | Returning users have their information preset | Pass |
| Forgot password button | Links to forget password page | Pass |
| Sign up link | Links user to sign up page | Pass |
| Log in responsive on all devices | Log in responsive on all devices  | Pass |
| User can reset their password | Sends reset password email | Pass |
| Reset page responsive on all devices | Reset page is resonsive on all devices | Pass |

## 5.5 Sign up

| Test  | Expected result | Pass/Fail |
| --------------- | ------------------------------------------------------------------------- | --------- |
| Sign up button | Takes user to verifcation page | Pass |
| Email fields empty | Please fill in this field pop up | Pass |
| Username filed empty | Please fill in this field pop up | Pass |
| Password field empty | Please fill in this field pop up | Pass |
| Weak password | If users password ins';'t secure enough text message warns them | Pass |
| Password don't match | Text message warns user | Pass |
| Email's don't match | Text message warns user | Pass |
| Username already exists | Text message warns user | Pass |
| Log in link | Links user to log in page | Pass |
| Sign up responsive on all devices | Sign up is responsive on all devices | Pass |

## 5.6 Sign out

| Test  | Expected result | Pass/Fail |
| --------------- | ------------------------------------------------------------------------- | --------- |
| Sign out button | Signs user out of their account | Pass |
| Sign out responsive on all devices | Sign out is responsive on all devices | Pass |

## 5.7 Verify account

| Test  | Expected result | Pass/Fail |
| --------------- | ------------------------------------------------------------------------- | --------- |
| Sends verifcation email to user | Sends email to the users email to confirm its correct | Pass |
<!-- ===================================================================== -->
| Email has link which verifies account | Verifies account email | Fail |
<!-- ===================================================================== -->
| Verify responsive on all devices | Verify is responsive on all devices | Pass |

## 5.8 Footer

| Test  | Expected result | Pass/Fail |
| --------------- | ------------------------------------------------------------------------- | --------- |
| Facebook link | Links user to facebook in a new tab | Pass |
| YouTube link | Links user to youtube in a new tab | Pass |
| Twitter link | Links user to twitter in a new tab | Pass |
| Instagram link | Links user to instagram in a new tab | Pass |
| Home link | Links user to home in a new tab | Pass |
| Profile link | Links user to profile in a new tab | Pass |
| Shop link | Links user to shop in a new tab | Pass |
| Bag link | Links user to bag in a new tab | Pass |
| Footer responsive on all devices | Footer is responsive on all devices | Pass |

## 5.9 Home

| Test  | Expected result | Pass/Fail |
| --------------- | ------------------------------------------------------------------------- | --------- |
| Shop now link | Links user to store page | Pass |
| Home responsive on all devices | Home is responsive on all devices | Pass |

## 5.10 Filters

| Test  | Expected result | Pass/Fail |
| --------------- | ------------------------------------------------------------------------- | --------- |
| High / Low ratings navbar | Links to store page with ratings high to low | Pass |
| Low / High ratings navbar | Links to store page with ratings low to high | Pass |
| High / Low price navbar | Links to store page with prices high to low | Pass |
| Low / High price navbar | Links to store page with prices low to high | Pass |
| High / Low ratings store dropdown | Reorders ratings high to low | Pass |
| Low / High ratings store dropdown | Reorders ratings low to high | Pass |
| High / Low price store dropdown | Reorders prices high to low | Pass |
| Low / High price store dropdown | Reorders prices low to high | Pass |

## 6.11 Search bar

| Test  | Expected result | Pass/Fail |
| --------------- | ------------------------------------------------------------------------- | --------- |
| Search for iPhone | Filters down to phones to iPhones | Pass |
| Search galaxy | Filters phones that match galaxy keywords | Pass |
| Search 5G | Filters phones that match 5G | Pass |
| Search icon button | When clicked filter phones by the keywords | Pass |
| Press enter to search | When clicked filter phones by the keywords | Pass |

## 6.12 Store

| Test  | Expected result | Pass/Fail |
| --------------- | ------------------------------------------------------------------------- | --------- |
| Product cards | Displays all prime mobiles phones | Pass |
| More details links | Links user to phone detail page | Pass |
| Phone name | Displays phones name | Pass |
| Phone price | Displays phones lowest price | Pass |
| Phone overall rating | Displays phones overall rating | Pass |
| Phone image | Displays phones first image | Pass |
| Store page on smaller devices | Shows less phones per row on smaller devices | Pass |
| Store page responsive on all devices | Store page is responsive on all devices | Pass |

## 6.13 Overall ratings store + detail page

| Test  | Expected result | Pass/Fail |
| --------------- | ------------------------------------------------------------------------- | --------- |
| Phone name | Displays user's name | Pass |
| Phone overall rating | Phone overall rating that updates when other reviews are submitted | Pass |
| Phone details responsive on all devices | Phone detail page is responsive on all devices | Pass |

## 6.14 Image slideshow

| Test  | Expected result | Pass/Fail |
| --------------- | ------------------------------------------------------------------------- | --------- |
| Phone images | Displays 3 images specific to that phone | Pass |
| Next button | When clicked it moves to the next slide | Pass |
| Previous button | When clicked it moves to the previous slide | Pass |
| Slide bars | Can click to any slide in one click | Pass |
| Responsive on all devices | Images scale down on smaller devices | Pass |

## 6.15 Spec overview

| Test  | Expected result | Pass/Fail |
| --------------- | ------------------------------------------------------------------------- | --------- |
| Phone camera spec | Show phone specific camera spec | Pass |
| Phone OS spec | Show phone specific OS spec | Pass |
| Phone display spec | Show phone specific display spec | Pass |
| Phone storage spec | Show phone specific storage spec | Pass |
| Responsive on all devices | Spec overview scales down on smaller devices | Pass |

## 6.16 Spec picker / Color / Storage / Price / Quantity

| Test  | Expected result | Pass/Fail |
| --------------- | ------------------------------------------------------------------------- | --------- |
| All phone colors display | Displays all phone specifc color options | Pass |
| All phone storage display | Displays all phone specific storage options | Pass |
| User can select a color | Users can choose their phone color | Pass |
| User can select a storage | Users can choose their phone storage | Pass |
| Users can select quantity 1 to 5 | User can charge phone quantity | Pass |
| Total cost displays | Based on the selected storage the price will update | Pass |
| Selected storage displays | Selected storage displays | Pass |
| Add to basket button | Add's phone with selected options to bag | Pass |
| Responsive on all devices | Spec picker scales down on smaller devices | Pass |

## 6.17 Phone review section

| Test  | Expected result | Pass/Fail |
| --------------- | ------------------------------------------------------------------------- | --------- |
| Shows phone specific reviews | Displays phone specific reviews | Pass |
| Rating and user | Displays user's name and number rating | Pass |
| Review title | Displays review title | Pass |
| Star rating | Displays star rating | Pass |
| Review body | Displays review body if review to long scrollbar shows whole review | Pass |
| Review link | Links user's to review page | Pass |
| Scrollbar if reviews take to much space | If there are more then 6 reviews a scrollbar will allow user to see the rest | Pass |
| Responsive on all devices | Review section scales down on smaller devices | Pass |

## 6.18 Bag page + phone info

| Test  | Expected result | Pass/Fail |
| --------------- | ------------------------------------------------------------------------- | --------- |
| Bag total link empty | Nav bag link has value of £0 and links to bag | Pass |
| Bag total link full | Nav bag link has value fo more then £0 and links to bag | Pass |
| Bag empty | If the user clicks the bag link with nothing in their bag a emtpy bag message appears | Pass |
| Phone image | Bag items images appears | Pass |
| Phone info | Bag items information name, storage, quantity and price displays  | Pass |
| Delivery message | Informs user purchases over £799.99 have free delivery | Pass |
| Responsive on all devices | Bag page scales down on smaller devices | Pass |

## 6.19 Delete phone from bag

| Test  | Expected result | Pass/Fail |
| --------------- | ------------------------------------------------------------------------- | --------- |
| Delete button | When clicked the bag item is removed | Pass |

## 6.20 Update phone from bag

| Test  | Expected result | Pass/Fail |
| --------------- | ------------------------------------------------------------------------- | --------- |
| Update button | When clicked the bag items quantity changes | Pass |
| Change quantity input | The user can choose to change quantity from 1 to 5 | Pass |

## 6.21 Bag total

| Test  | Expected result | Pass/Fail |
| --------------- | ------------------------------------------------------------------------- | --------- |
| Bag total | Total cost of all bag items dispalys | Pass |
| Delivery total | If total cost is over £799.99 it will be free otherwise it is 2% of total | Pass |
| Checkout button | Links user to checkout with bag items | Pass |

## 6.22 Checkout bag overview

| Test  | Expected result | Pass/Fail |
| --------------- | ------------------------------------------------------------------------- | --------- |
| Phone image | Displays phone images in checkout bag | Pass |
| Phone info | Displays phone infomation in checkout bag | Pass |
| Responsive on all devices | Checkout info scales down on smaller devices | Pass |

## 6.23 Checkout total

| Test  | Expected result | Pass/Fail |
| --------------- | ------------------------------------------------------------------------- | --------- |
| Bag total | Total cost of all bag items dispalys | Pass |
| Delivery total | If total cost is over £799.99 it will be free otherwise it is 2% of total | Pass |
| Grand total | Total bag cost and delivery cost added together | Pass |
| Responsive on all devices | Checkout total scales down on smaller devices | Pass |

## 6.24 Checkout form

| Test  | Expected result | Pass/Fail |
| --------------- | ------------------------------------------------------------------------- | --------- |
| Checkout form | Users can enter their checkout informtaion | Pass |
| Checkout form emtpy field | Empty required fields please fill in this field pop up | Pass |
| Save info | Users who are signed in can tick the box for pre-filled checkout next time | Pass |
| Stripe input | Secure way for users to enter their card details | Pass |
| Card declined error message | If the users card is inccorect or lacks funds an error informs user of issue | Pass |
| Stripe verifcation | If card requries verification a stripe pop comes up asking for verification | Pass |
| Total charge | Final total charge | Pass |
| Complete order button | When click order is processed | Pass |
| Responsive on all devices | Checkout form scales down on smaller devices | Pass |

## 6.25 Checkout success

| Test  | Expected result | Pass/Fail |
| --------------- | ------------------------------------------------------------------------- | --------- |
| Order information | Order number and order date | Pass |
| Delivery details | Users delivery info | Pass |
| Responsive on all devices | Checkout success scales down on smaller devices | Pass |

## 6.26 Checkout success table

| Test  | Expected result | Pass/Fail |
| --------------- | ------------------------------------------------------------------------- | --------- |
| Order items | Order items info name, color, sotrage, quantity and cost | Pass |
| Order total | Total, delivery and grand total | Pass |
| Scroll bar on smaller devices | Order number and table scroll bar on mobile phones | Pass |
| Responsive on all devices | Checkout success table scales down on smaller devices | Pass |

## 6.27 Profile page

| Test  | Expected result | Pass/Fail |
| --------------- | ------------------------------------------------------------------------- | --------- |
| Set default delivery info collapse button | When clicked the delivery info form opens | Pass |
| Set default delivery info form | Users can enter their set their delivery info for faster checkout | Pass |
| Empty required field | Please fill in this field pop up | Pass |
| Set default delivery info submit | Submits user info to django | Pass |
| Responsive on all devices | Profile delviery form scales down on smaller devices | Pass |

## 6.28 Order history

| Test  | Expected result | Pass/Fail |
| --------------- | ------------------------------------------------------------------------- | --------- |
| Order details | Order number and date | Pass |
| Link to order receipt | Order number links user to order success page | Pass |
| Order items | Order table with all items and specs | Pass |
| Order total | Total, delivery and grand total cost | Pass |
| Responsive on all devices | Profile order history scales down on smaller devices | Pass |

## 6.29 Order number receipt page

| Test  | Expected result | Pass/Fail |
| --------------- | ------------------------------------------------------------------------- | --------- |
| Order items | Order items info name, color, sotrage, quantity and cost | Pass |
| Order total | Total, delivery and grand total | Pass |
| Scroll bar on smaller devices | Order number and table scroll bar on mobile phones | Pass |
| Back to profile link | Links user back to profile page | Pass |
| Responsive on all devices | Order receipt page scales down on smaller devices | Pass |

## 6.30 Review page / form

| Test  | Expected result | Pass/Fail |
| --------------- | ------------------------------------------------------------------------- | --------- |
| Phone name | Correct phone name displays | Pass |
| Phone overall rating | Phone's overall rating displays | Pass |
| Phone image | Image of phone displays | Pass |
| Star rating | User can pick from 5 stars affecting overall score | Pass |
| Review title | User can enter a review title | Pass |
| Review body | User can enter their review | Pass |
| Submit button | Submits review to django and appears on phone detail page | Pass |
| Responsive on all devices | Review page scales down on smaller devices | Pass |

## 6.31 Admin add phone (S22)

| Test  | Expected result | Pass/Fail |
| --------------- | ------------------------------------------------------------------------- | --------- |
| Admin only link | Only admins can access add link in navbar | Pass |
| Add phone form | Admin can add a phone | Pass |
| Add phone submit | Adds phone to store page | Pass |
| User can buy phone | User can add to bag and checkout item | Pass |
| Responsive on all devices | Admin add phone scales down on smaller devices | Pass |

## 6.32 Admin edit phone

| Test  | Expected result | Pass/Fail |
| --------------- | ------------------------------------------------------------------------- | --------- |
| Admin only link | Only admins can access edit link on phone deatail page | Pass |
| Edit phone form | Admin can edit a phone | Pass |
| Edit phone submit | Updates info phone to store page | Pass |
| Responsive on all devices | Admin edit phone scales down on smaller devices | Pass |

## 6.33 Admin remove phone

| Test  | Expected result | Pass/Fail |
| --------------- | ------------------------------------------------------------------------- | --------- |
| Admin only link | Only admins can access remove link on phone deatail page | Pass |
| Admin clicks remove link | Removes phone from the database and store page | Pass |

## 6.34 Admin remove review

| Test  | Expected result | Pass/Fail |
| --------------- | ------------------------------------------------------------------------- | --------- |
| Admin only link | Only admins can access remove link on phone deatail page | Pass |
| Admin clicks remove link | Removes review from the database and page | Pass |

## 6.35 Emails

<!-- =========================== -->
| Test  | Expected result | Pass/Fail |
| --------------- | ------------------------------------------------------------------------- | --------- |
|  |  |  |
|  |  |  |
<!-- =========================== -->