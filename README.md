# Week 21 RevoU Assignment
***
<img align='center' width='900' src='https://github.com/hlmyrsyd/thereadmestuff/blob/main/100%25.svg' />

## Hello!
This is an Backend of a Tweet app using Flask as a Python Framework 
 
## API Available
### /auth/register

**Status Code 200** if user are new 
<img align='center' width='500' src='assets/register200.png' />

**Status Code 400** if user are using the same username
<img align='center' width='500' src='assets/register4001.png' />

**Status Code 400** if user are using the same email
<img align='center' width='500' src='assets/register4002.png' />
***

### /auth/login

**Status Code 200** if user login without problem 
<img align='center' width='500' src='assets/login200.png' />

**Status Code 400** if user type wrong username or password
<img align='center' width='500' src='assets/login400.png' />
***

### /tweet

**Status Code 200** POST for tweet always needs ***Token for Authorization*** 
<img align='center' width='500' src='assets/tweetAuth.png' />

and also ***JSON body*** for the tweet text content
<img align='center' width='500' src='assets/tweetJSONBody.png' />

**Status Code 400** if the tweet is having an issues, for example: ***has no text in the JSON***
<img align='center' width='500' src='assets/tweetJSONEmpty.png' />

or ***typing more than 150 characters***
<img align='center' width='500' src='assets/tweetJSONOver150.png' />
***

### /follow

**Status Code 200** POST for follow other user need ***Token for Authorization*** and a ***JSON body*** just like the code below
 <img align='center' width='500' src='assets/follow.png' />

if send it again it will change the status back to **"unfollow"**
<img align='center' width='500' src='assets/unfollow.png' />

***

### /user

**Status Code 200** GET for user to check up the user profile
<img align='center' width='500' src='assets/userProfile.png' />

**Status Code 401** will appear if the 1 minute time given for the Token Authorization was abandoned and the user must login again to receive new token
<img align='center' width='500' src='assets/userTimeOut.png' />

***



## Deployment
postman deployed link for this app be is here https://documenter.getpostman.com/view/28996075/2s9YeD8DHj

## THANKYOU
Thankyou for visiting

