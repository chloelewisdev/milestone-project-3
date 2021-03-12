## Testing

The testing process is outlined below. It includes:
* Testing User Stories
* Validating HTML, CSS, JavaScript and Python code
* Manually testing the functionality of features including links, forms and buttons
* Checking website compatibility on different browsers
* Testing responsiveness on multiple devices and screen sizes:

To return to the previous document, click [here]( https://github.com/chloelewisdev/milestone-project-3/blob/master/README.md).

### Testing User Stories:

#### New users

* ***I only started working remotely in the past year, and I have found it really difficult to adjust. I am therefore looking for a place that provides tips and suggestions about working from home. I am interested in learning about ways to organise my desk space and also how others create a routine, so that I can separate my work life and home life. I have a few tips about working from my kitchen table that may be useful for others which I think others may find useful too.***

This user arrives and the homepage, and will see that they can click on the button to view ‘Tips’. This takes the user to the tips page, displaying a community tips board full of ideas about working from home. This user can search the tips by typing in ‘desk’ or ‘routine’ for example into the search feature, to see if anyone has shared anything related to these topics. If they have, the user will be presented with tips related to the search query. After spending some time looking at the tips shared on the community tips board, the user may wish to share their own tips. They can click on the ‘Sign Up’ button in the nav bar, and then enter a username and password. Once complete, the user will be taken to their profile page, where they can click on a ‘Share tips’ button to start sharing their own tips on the community board.

* ***I am a user who has worked from home for years, but previously didn’t know that many other people who also worked from home. I want to share my tips for making working from home a positive experience as I love working remotely and have tried and tested many different ways of doing so. I am also keen to learn from others as I haven’t known many other people working from home prior to the pandemic.***

This user arrives at the home page and can click on ‘Tips’ (either in the nav or in a card on the index page) to view the community tips sharing board. They may wish to go straight to signing up, and can also click to do this from the home page. Once the user is signed up, they can start sharing their tips, either by clicking ‘Share Tips’ on their My Tips profile page, or by clicking ‘Share Tips’ in the nav bar once logged in. 

#### Returning users

* ***I am a returning user who has used this app for a few months and found it really helped create a positive remote working experience. I want to view the community tips board and see if there are any more remote working tips I could try.***

This user may wish to go straight to the ‘Tips’ board, which they can do so from the homepage or by clicking the ‘Tips’ option in the navbar. As they are a returning user, they may also wish to log in if they decide to share some tips later, and this can easily be done by clicking on ‘Log In’ on the nav bar from any page. 

This user could also choose to look at the Superleague Teams section and discover more about teams that play semi-professionally, perhaps enabling the user to plan to watch a match live or on tv. 

* ***I am a returning user who has previously signed up and added some of my own remote working suggestions to the community tips board, however I want to edit one of these now as I have an update on my suggestion which I’d like to share.***

This user would benefit from going straight to the log in page. They can do so from by clicking a button on the homepage, or by clicking ‘log in’ on the navbar. Once the user has entered their login details, they are taken to their tips profile page (mytips.html). Here they are welcomed with a personalised message containing their username. The user is shown on this page all of the tips they have added previously. Within each tip, the user can click to ‘Edit’ or ‘Delete’ a tip. If the user clicks to edit a tip, they are taken to a page with a prefilled form containing their tip. The user can make any updates, and then click ‘Save Update’. They are then redirected to the main Tips page, and a message tells them that their tip has successfully been updated. If the user wishes to edit any more tips, they can click on ‘My Tips’ in the nav bar whilst logged in which takes them to their profile page where they can continue to make any changes. If the user deletes a tip, they are redirected to the Tips page with a message showing them that they have successfully removed their tip from the tips board. Alternatively, if the user is on the main Tips page, they are able to edit or delete any tips that they have added when they are logged in, as ‘Edit’ and ‘Delete’ buttons appear on their own tips on the community board. 

#### Business Owner

* ***I am the creator of this app and want to see it succeed. I want to see more and more people signing up and sharing their remote working tips, hopefully inspiring and encouraging others to try their suggestions and benefit from the shared information. I want the app to add value to the users, encouraging them to return and enjoy the experience of using the app, therefore I want the app to be fully responsive, fresh and modern in design, friendly and also intuitive to use.***

The app is easy to use, with clear navigation, responsive design and professional yet friendly design and imagery. The user is provided with clear prompts to sign up, log in, log out, share a tip, edit or delete a tip. Overall the experience on the app should be positive for the user, allowing them to focus on either learning about new ways to make working from home enjoyable, or by sharing tips to help others in a similar situation. 

### Validating HTML, CSS and JavaScript code

#### HTML
I validated the HTML with the [W3C Markup Validation Service](https://validator.w3.org/)

**Issues found** 
For add_tip.html, I received an error saying the element ‘option’ without attribute ‘label’ must not be empty. I realised there was an unrequired element ‘<option selected></option>’ in the form, which I removed to resolve the problem.

On the login.html and signup.html, I received an error saying ‘Attribute placeholder not allowed on element input at this point’. I realised there was an error in the spelling of ‘placceholder’ on both forms, which I updated to ‘placeholder’ to resolve the problem. 


#### CSS
I validated the CSS with the [W3 CSS Validation Service](https://jigsaw.w3.org/css-validator/)

No errors were presented. 


#### JavaScript
I used [JSHint](https://jshint.com/) to check my JavaScript files.
* *script.js* - no errors were shown for this file

**Python**
I used [Pep8online](http://pep8online.com) check my Python app.py file
.
The issues raised were:

On line 107 ‘block comment should start with a ‘#’’, therefore I updated this to make sure there was a space after the hashtag to solve the problem as previously there was no space between the hashtag and the word. 

On line 134 the message was ‘line too long’ therefore I adjusted the code to address this problem. 

Finally on lines 33, 112, 185 and 186 I could see that there was a warning of ‘trailing whitespace’. I tried Googling this but unfortunately I was unable to fix this problem with the time restraints of the project deadline. 

### Manual tests

#### Navigation
-	Logo – clicking on this takes the user to index page
-	Home – clicking on this takes the user to index page
-	Tips – clicking on this takes the user to Tips page
-	Share Tips (when user is logged in) – takes the user to Share tips page
-	My Tips (when user is logged in) – takes the user to My Tips page
-	Sign Up – clicking on this takes the user to the sign up page
-	Log In – clicking on this takes the user to the log in page. 
-	Log Out (when user is logged in)- clicking on this returns the user to the log in page 

#### Home
-	View Tips button – clicking on this takes the user to the Tips page
-	Sign up button – clicking on this takes the user to the sign up page
-	Log In button – clicking on this takes the user to the log in page

#### Tips
-	I tested the search feature by adding part of words and full words – when clicking on ‘Search’ the feature correctly returned the results containing those words. When I clicked the ‘reset’ button the search form refreshed correctly. 
-	Whilst logged in, I could click on ‘Delete’ button or ‘Edit’ button on my own tips which correctly removed the tip or took me to a page where I could edit the tip.

#### Sign Up
-	Tried submitting the form with empty form fields and also with only a couple of characters – could not submit the form
-	Tried submitting the form with a username that I had already created, and I was shown the correct flash message saying the username already exists and to try again. 

#### Log In
-	Tried to submit the form with empty fields and was not able to submit the form. Was informed they were required fields. 
-	Submitted the form with incorrect username and also tried incorrect password, was shown an error message and to try again.
-	When the correct details were entered, I could submit the form and was successfully taken to ‘My Tips’ page.   

#### Share Tips 
-	Tried to submit the add task form with empty form values and this did not worked, the user is shown a message saying they are required fields. 
-	When the form was completed, I successfully shared a tip and was taken to the main Tips page, where my tip was now on the Tips board, and I was shown a flash message saying the tip was successfully added.


#### Edit Tips
-	The form was prefilled with the previous tip information 
-	I could click on ‘cancel’ to return to the Tips page and maintain the original tip information. 
-	I could edit the fields, click on ‘Save Update’, and then was successfully directed to the Tips page, where a flash message showed that the tip had been successfully updated. 

#### My Tips
-	‘Share Tips’ button worked successfully and took the user to the Share Tips page
-	I could click on ‘Edit’ and was taken to the Edit Tip page, I could also click on ‘Delete’ on all tasks to remove them successfully from the Tips board. 
-	I could ‘Log Out’ successfully by clicking on the Log Out button at the bottom of the page. 


#### Issues found from manual testing:
I realised that when the user signed up, they were taken to the ‘My Tips’page which showed a ‘Welcome back’ message, and asked the user if they wanted to share ‘more’ tips. Therefore for user experience I made sure the My Tips page would be appropriate for new users who had just signed up and also those who had logged in by tweaking the text. 
I also found that when I did a search on the Tips page, if I entered a search with a space at the end of the word I was searching or part of the word I was searching, the search did not bring up any results. I was unable to resolve this unfortunately due to time constraints of the project.

### Testing on different browsers:
I manually tested the website on the following browsers:
* Chrome
* Safari
* Mozilla Firefox

### Testing responsiveness on multiple devices and screen sizes:

* I manually tested the website by using Google Developer Tools to check each individual section and the website as a whole worked on different devices and different screen sizes, including: Moto G4, Galaxy S5, Pixel 2, Pixel 2 XL, iPhone 5 SE, iPhone 6/7/8, iPhone 6/7/8 Plus, iPhone X, iPad, iPad Pro, Surface Duo and Galaxy Fold. I also manually tested the site on my MacBook Air, iPad, and iPhone 11.
* By using Google Developer Tools I checked that all of the form were displayed correctly, as well as the flash messages, search results, and tips.  
* I asked family to visit the website on their devices including a variety of mobiles and tablets, interact with the page and sign up. 

To return to the previous document, click [here]( https://github.com/chloelewisdev/milestone-project-3/blob/master/README.md)
