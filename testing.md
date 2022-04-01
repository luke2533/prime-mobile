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

## 6.22

| Test  | Expected result | Pass/Fail |
| --------------- | ------------------------------------------------------------------------- | --------- |
|  |  |  |
|  |  |  |
|  |  |  |