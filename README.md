# REMOTE

## Code Institute - Milestone Project 3

![REMOTE responsive website mockup]( https://github.com/chloelewisdev/milestone-project-3/blob/master/static/images/Responsive-web-mockup.png)

Remote is an app that aims to help users who are working remotely. My main aim with this project is for the app to be a useful, positive community environment, which enables users to share information and tips to help people physically and mentally with their experience of working from home. Ultimately, Remote is an app which could help people to have a positive experience whilst working from home, and see it as an opportunity rather than a hindrance. 

The idea for this website came to me as due to the Coronavirus Pandemic, most people I know are now working from home in all sorts of different circumstances. Some with children around in a busy environment, some with no one around who are finding the situation quite lonely, and everything in between! One thing that has been certain in these recent uncertain times is that people need connection and at a time when this is mainly possible online, users who work from home can find a community within Remote where they can share their ideas and suggestions, helping others benefit from their own direct experience and providing a source of information. Once the pandemic is over, many people will continue to work remotely as many businesses have found this to be a success, and so even when offices do open again, this app should therefore continue to be a useful place for people to come as their remote experiences continue but change over time. 

This was the third of four Milestone Projects that made up the Full Stack Web Development Program at The Code Institute. The main requirements were to build site a site using HTML, CSS, JavaScript, Python + Flask and MongoDB. 

Click [here](https://ms3-remote-app.herokuapp.com/index/) to view the website live. 

## Table of Contents:

* [User Experience](#User-Experience)
    * [User Stories](#User-Stories)
    * [Strategy Plane](#Strategy-Plane)
    * [Scope Plane](#Scope-Plane)
    * [Structure Plane](#Structure-Plane)
    * [Skeleton Plane](#Skeleton-Plane)
    * [Surface Plane](#Surface-Plane)

* [Existing Features](#Existing-Features)
    * [Features to consider implementing in the future](#Features-to-consider-implementing-in-the-future)

* [Technologies Used](#Technologies-Used)

* [Testing](#Testing)

* [Deployment](#Deployment)

* [Credits](#Credits)
    * [Content](#Content)
    * [Media](#Media)

* [Acknowledgements](#Acknowledgements)

## **User Experience**
This section provides insight into the UX process, focusing on Remote’s target audience, the main aims of the project and how the website can help users meet their needs.  

### User Stories

**New users:** 
* I only started working remotely in the past year, and I have found it really difficult to adjust. I am therefore looking for a place that provides tips and suggestions about working from home. I am interested in learning about ways to organise my desk space and also how others create a routine, so that I can separate my work life and home life. I have a few tips about working from my kitchen table that may be useful for others which I think others may find useful too.
* I am a user who has worked from home for years, but previously didn’t know that many other people who also worked from home. I want to share my tips for making working from home a positive experience as I love working remotely and have tried and tested many different ways of doing so. I am also keen to learn from others as I haven’t known many other people working from home prior to the pandemic.

**Returning user:**
* I am a returning user who has used this app for a few months and found it really helped create a positive remote working experience. I want to view the community tips board and see if there are any more remote working tips I could try. 
* I am a returning user who has previously signed up and added some of my own remote working suggestions to the community tips board, however I want to edit one of these now as I have an update on my suggestion which I’d like to share.  

**Business Owner:**

* I am the creator of this app and want to see it succeed. I want to see more and more people signing up and sharing their remote working tips, hopefully inspiring and encouraging others to try their suggestions and benefit from the shared information. I want the app to add value to the users, encouraging them to return and enjoy the experience of using the app, therefore I want the app to be fully responsive, fresh and modern in design, friendly and also intuitive to use. 

### Strategy plane: 

I started the UX process by creating the User Stories above which helped me work out who the project was aimed at and what I would need to include in the website to satisfy the needs of the users. 

The website should be professional and user-friendly, providing an easy navigation journey to reach different sections with ease. 

**Project goals:**
* To create a community area where people can view tips and suggestions shared by others about working remotely. The user can view these tips and benefit from the app without having to sign up or log in, therefore making the app 
* To enable new users to be able to sign up, and then share their own tips easily on the community tips board if they wish
* For users who have already signed up previously, to be able to log in with ease
* For users that are logged in, to be able to easily share, delete and edit a tip from the community board.
* For users that are logged in, to be able to view their own profile, which displays all the tips they have shared so far on the community tips board and be able to easily delete or edit these if they wish. 
* For users that are logged in, to easily be able to log out.
* To provide direction to social media links, in order to expand followers and increase brand awareness
* To make Remote seem a reputable company in order to encourage users to sign up, by creating a professional website, whilst maintaining a friendly appeal. 

**Customer goals:**

* App designed with mobile-first approach
* Fixed navigation bar providing a user-friendly experience
* Enable users to easily scroll back to the top 
* Relevant social media icons provided in the footer
* Log in and sign up forms so the customer can sign up to become a part of the Remote community
* Customer profile page which enables them to maintain the information they share easily
* App is visually appealing, and fully responsive on all devices and screen sizes

### Scope plane:

The key features of the website were developed based on the main aims of the website and user needs, as well as my current skill-set of HTML, CSS, JavaScript, Python + Flask and MongoDB. Users should be able to do the following on the website:

* View a clear path on the homepage to either view the community tips board, sign up to Remote to begin sharing remote working tips, or log in. 
* Visit the ‘Tips’ page where the user can view many different tips shared by others about working remotely, even if the user has not got an account with Remote. 
* On the Tips page, the user should be able to search part of a word or a full word in the search bar to be then shown results containing tips that match their search. The user should then be able to reset the search to start another search if they wish. 
* The user needs to be able to complete a sign-up form by providing a username and password, which enables them to join the Remote community. Once they have signed up they can then start adding, editing and deleting their own tips and they should also have access to their own profile page which will enable them to have control over the tips they have shared to date. 
* A user that has previously signed-up and is revisiting the site, should be able to easily log in by providing a username and password in the log in form. When on the log in page, if a user has arrived here by accident, and they want to sign up instead, they should easily be able to navigate to the  ‘Sign Up’ page instead. 
* Once a user has completed the log in form, they should be taken to a profile page, which displays their username in a welcome message at the top. On the profile page, the user should be able to view all of the tips they have added so far, and then easily click on a button on each tip to edit or delete the tip should they wish. 
* Once logged in, the user should be able to see ‘Share Tips’ displayed in the navbar, and when clicked the user visits a page where they can add a tip to the community board. The user can complete a form by selecting a category, tip suggestion and then further tip details. Once they have added their information they can click on the share button which then adds the tip to the community board (and also their profile page), and the user is shown a message thanking them for sharing the tip. 
* Once logged in, the user should be able to view the tips they have shared on the community tips board as their username will ideally be displayed by each tip. The tip will also be displayed on their profile page. The user should be able to click on the ‘Edit’ button on their tip on either page, where they are then taken to a page which displays a form prefilled with their tip information. They should be able to edit the tip within this form, and then save their update, and then return to the main Tips page. The user should be shown a message which informs them they have successfully updated their tip, and the updated tip is displayed in the tips board on the Tips page. If the user also goes to their profile page, the updated tip is also displayed here too. 
* Once logged in, the user should be able to click on a ‘Delete’ button displayed on the tips added by them only, and this should remove the tip from the community tips board and also from their profile. The user is shown a message informing them they have successfully removed their tip from the community board. 
* When logged in, the user should be able to easily log out by clicking on the ‘Log Out’ option on the nav bar. When the user clicks to log out, they should be then taken back to the ‘Log In’ page and displayed a message informing them that they have now been logged out. On this page the user should be able log back in by completing the log in form should they wish. 

Therefore the user should be able to create their own account, manage their own tips by using the four CRUD functions, and easily navigate their way around the site. The app needed to be personalised when the user was logged in, and so I needed to feature the user’s chosen Username in certain parts of the app.

### Structure plane:

Once I had worked out which features I'd like to include, I began to think about the information architecture and the different interactions that could take place across the site, and the order they should be in. 

There needed to be two different presentable versions of the website, one that was accessible and an enjoyable experience for users visiting the website with open access and no account with Remote, and then a different experience for users that have created an account and logged in. Therefore I needed to ensure that certain pages would be visible to everyone, and others would only be visible to those with an account and logged in. The nav bar would therefore need to change when a user logged in, displaying certain pages only available to those with an account, and removing the ‘Sign Up’ option which would create a confusing user experience if logged in. 
Therefore all users with open access would be able to view the following pages ‘Home’, ‘Tips’ ‘Sign Up’ and ‘Log In’. And those that are logged in would no longer see ‘Sign Up’ and ‘Log In’, but would now see ‘Share Tips’, ‘My Tips’ and ‘Log Out’. 

As well as the sign up and log in forms, points of contact for users would also be provided in the links to social media in the footer. 

### Skeleton plane:

At this stage I was ready to put together wireframes. I used Figma for these, creating wireframes for the website on desktop, tablet and mobile all showing the five main sections. 

I wanted to make sure it would be easy for users to navigate between the different sections within the one page, and therefore I decided it would be essential to create a fixed nav, as well as a Hamburger icon for smaller devices so that the user could easily choose to move to a different section on the site if they wished. 

I wanted to ensure there would be a sticky footer as I knew on many pages there wouldn’t be a lot of content and I wanted this to still be a positive user experience. 

I decided that a 'Back To Top' button on the site would be useful, and thought it would be beneficial to add this to the ‘Base’ template, however the main page where this would be useful would be on the ‘Tips’ page so the user could quickly move back to the top of the website if they had scrolled far down the different shared tips.

I decided a clean white background with a box layout would be a good way to present information in the different sections, allowing enough space between text, images and any key features. 

The wireframes can be viewed on [Figma](XXX)

### Surface plane:

I next moved on to the design work. 

* **Colours & Logo:** 
Colours were an important choice – I wanted the website to have a modern, colourful and friendly feel. I didn’t want to use images of people working from home, because I didn’t want users to see an image they couldn’t identify with and therefore lessen the appeal of the website. I decided graphics and illustrations would therefore be a good way to provide some colourful content to the site. After researching different sites and I decided to use DrawKit. The images I chose from DrawKit then enabled me to the colour palette for the website, including the logo. I decided the logo would be the word ‘REMOTE’, with wavy text decoration underneath – I thought this was simple but also fitted in well with the style of the graphics. 

* **Typography:** I used Google Fonts to select the fonts for my project and decided on the font ‘Cabin’ – I thought this worked well when bold as a heading but also looked good when regular weight for the body text. 

* **Images:**  The images used on the website are all from DrawKit, which is an open source of free illustrations updated every week. I downloaded the Peach Illustration System for this website from DrawKit, as it included illustrations of people working from home, as well as different scenes, and technology illustrations which I thought would be useful. I decided to include a mix of illustrations of people working at home, technology such as an artistic illustration of a computer, as well as illustrations of plants which created a ‘home’ feel.

* **Layout:** I decided to keep the background clean, spacious and fresh by using a white background for the pages. This then enabled me to add different colours as a background to certain areas of content, such as a the tips board, and the form for adding a tip. 

## Existing features and Database Structure
This project consists of seven different pages, three of which are only accessible to users once they have an account and have logged in.

**Database Structure**

The data for this project is stored in my MongoDB database within three collections as follows:
* Users - This collection stores the user's username and their encrypted password created when they signed up to Remote.
* Categories - When a user creates a task, they can choose a category stored in this collection – currently there are 5 categories all stored under ‘category_name’: “Workspace”, “Exercise”, “Routine”, “Breaks” and “Positivity”. 
* Tips – Working from home tips are added by users who already have an account and are stored in this collection. They are stored together with the username of the user who created the tip and the actual tip content itself which includes a category name, tip suggestion, tip details. 
 

**Existing Features** 

* **Fixed navigation** - allows the user to easily navigate to different sections of the website. The nav bar also displays Remote’s logo in the top left corner. Although the content of the nav bar changes if a user is logged, the navbar design and fixed position remains the same. 
* **'Back to top' button** - enables users to quickly move back to the top of the page rather than scrolling back up
* Although each page features different graphics, they are all designed with the same colour palette and are from the same illustrator for consistency.
* **Active page on navbar**The active page becomes highlighted with a green colour to show the user which page they are on. 
* **Flash messages** All flash messages appear under the nav bar with the same font and colour throughout the app for consistency.
* **Home** - The user sees an image and introductory text explaining the purpose of the website. When scrolling down, the user is then presented with three different cards each containing a next step the user can take and accompanying text explaining each action – they can click on a button to view ‘Tips’ on the community tips board, they can click on ‘Sign Up’ if they want to add their own tips to work from home on the community board, or they can click on a button to ‘Log In’ if they have previously signed up and want to log in. 

* **Tips** - This page welcomes the user to the community tips board with an image and then some introductory text. The user is then presented with all the different tips that have been shared by others, as well as a search feature at the top of the tips section.   
Each tip card displays a title, a category, more details about the tip, and the username of the person that has shared tip.  If the user is logged in, they are shown a ‘Delete’ button and an ‘Edit’ button on the tips they have shared on the board. By clicking the delete button, the logged in user removes the tip, and are shown a flash message confirming this. If the user wants to edit their tip, they can click ‘Edit’ and are then taken to a page which displays a form prefilled with their original tip. Here they can edit the tip and click ton ‘Save Update’, which updates the tip, takes the user back to the community Tips page, and confirms that their message has been updated with a flash message.

* **Search** The searcg feature on the Tips page enables the user to type in part or all of a word, click on the button ‘Search’ which then provides them with the results of their search (the tips containing the word they have searched for), or a message is displayed showing the user that there are no results. The user can then click to ‘Reset’ the search function which displays all of the tips again to the user so that they can do a fresh search if they wish. 

* **Log In** – This feature contains a log in form where an existing user can input their username and password to log in. If they enter the wrong password and/or username, they are shown a flash message telling the username that the details are incorrect and to try again. Users on this page that don’t yet have an account are prompted to sign up with a message and sign up button underneath the log in form.  Once users successfully log in, they are taken to the ‘My Tips’ page. 

* **Sign Up** - This feature contains a form where the user can input a username and password in order to create an account. If they enter a username that already exists, they are shown a message explaining this and asking them to try again. Once the user clicks on ‘Sign Up’, the user is taken to the ‘My Tips’ page, where they can begin sharing their tips with the community. Users on this page that already have an account are prompted to log in with a message and a log in button underneath the sign up form.  

* **My Tips** - once the user is logged in, they are taken to the ‘My Tips’page and this feature is now displayed in the navbar, (otherwise hidden for users that don’t have an account). This page contains a feature that displays all of the tips that the user has shared so far. Within those tips, the user can edit them by clicking on an ‘Edit’ button which takes them to the Edit Tip page, or they can delete them by clicking on a ‘Delete’ button. The user’s username is shown at the top of the page so that they user knows that these tips are personal to them. Underneath the ‘My Tips’ feature shown on this page, the user is given the option to ‘Share Tips’, which is relevant to both users that have only just signed up with no tips and also those that have shared lots of tips and have something new they want to share. The ‘Share Tips’ page takes the user to ‘Share Tips’ page. Alternatively, next to the ‘Share Tips’ button, the user can click on the ‘Log Out’ button to log out if they wish. 

* **Share Tips** - This page features a form with three fields – users are prompted to add a category, tip title and tip details. All fields are required in order to submit the form, if the user leaves a field blank they are shown a message asking them to complete the empty field. When the user has finished adding their tip, they can click on the ‘Share’, which takes the user to the ‘Tips’ page, displays a flash message to the user so that they know their tip has been shared successfully, and the tip is added to the list of tips displayed on the Tips page. Alternatively, on the Share Tips page, if the user changes their mind and decides they no longer want to share a tip, they can click on a ‘Cancel’ button at the bottom of the form which directs the user back to the ‘Tips’ page.  

* **Edit Tip** - this page features a form where the user can edit a tip they have previously added. It is only available to users that have an account and that are logged in, and users can arrive at this feature by clicking on an ‘Edit’ button displayed on tips they have shared which are displayed on the Tips page or on the My Tips page. The user is presented with their tip already prefilled into the form, and they can click on any field to edit the information. Once complete, the user can click on ‘Save Update’ which takes the user back to the Tips page, displaying a message explaining the tip has been successfully updated, and the updated tip is displayed on the ‘tips board’.  Alternatively, on the Edit Tips feature, if the user changes their mind and decides they no longer want to edit a tip, they can click on a ‘Cancel’ button at the bottom of the form which directs the user back to the ‘Tips’ page.  

* **Log Out** - this feature appears in the nav bar when a user is logged in, and also it appears on a button on the My Tips page. When the user clicks to log out, they are taken to the Log In page, and displayed a message at the top which explains they are now logged out. If they change their mind and wish to log back in they can quickly do so on the Log In page. 

* **Footer** - the footer contains social media icons with links to social media pages that open up in a new page. 

### Features to consider implementing in the future:

* The Tips feature could be developed much further in the future. It would be good if each tip that was added contained a date, and then on the Tips page, the tips could be displayed in date order starting with the newest first. 
* It would also be good if the Tips feature contained pagination, because currently if lots of tips were added, the user would have to scroll a long way down the page to read them which isn’t necessarily good user experience.  The ‘Scroll to top’ hopefully helps the user for now but this would definitely be something to implement in the future. 
* It would also be useful if the user could search the tips by username, so this is something that would be great to add in the future. Then if the user finds certain tips shared by a particular user helpful, they would be able to search for just the tips just shared by that user.
* It would be useful if the Profile page contained a section where the user could update their login details including username and password. 


## Technologies Used

### Languages, libraries, databases, frameworks, editors and version control

- HTML5
    * The language used to create add structure and content to the website.
- CSS3 
    * The language used to style the HTML5 elements according to the design colour scheme.
- JavaScript
    * The language used to make the app interactive
- [jQuery](https://jquery.com/)
    * I used the jQuery library to help write the JavaScript code used in this project
- Python
    * The programming language used to create the back-end function of the app.
- PyMongo
    * PyMongo was used as the Python API for MongoDB. This API enabled me to link the data from the back-end database to the front-end app.
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
    * The Python microframework I used for writing the Python code for this project.
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
    * Jinja templating language was used with Flask in the HTML code. This allowed for template inheritance from the base.html file and to link the back-end to the front-end. 
- [MongoDB](https://www.mongodb.com/)
    * This was the selected database chosen to store data in the cloud.  
- [Bootstrap framework](https://getbootstrap.com/) 
    * I used Bootstrap's grid system in order to have a 'mobile'-first' approach
* [Gitpod](https://www.gitpod.io/)
    * I used Gitpod's development environment to write the code for the website
* [Git Version Control](https://git-scm.com/)
    * I used Git for Version Control to record changes and updates to my files
* [GitHub](https://github.com/)
    * I used GitHub’s repository hosting service to host my deployed website as well as track previous versions of my code 
* [Heroku](https://www.heroku.com/)
    * I used Heroku as a hosting platform to deploy the live version of my app. 

### Other tools used
- [Figma](https://www.figma.com/) 
    * Figma helped me design my project, by creating wireframes for desktop, tablet and mobile devices. 
- [FontAwesome](https://fontawesome.com/) 
    * I relied on free FontAwesome icons, including a copy icon, different types of arrows and a 'tick' to show items as complete.
- [DrawKit](https://www.drawkit.io/) 
    * This was the source of all graphics and illustrations used on the website. 
- [Google Fonts](https://fonts.google.com/)
    * I used the font ‘Cabin’ for this project. 
- [Favicon](https://favicon.io/)
    * I used this website to create the favicon for the website 
* [FontAwesome](https://fontawesome.com/)
    * I also used three social media icons for Twitter, Instagram and Facebook


**Resources**

* [Code Institute Course Content](https://courses.codeinstitute.net/) – Main source of knowledge, especially the ‘Task Manager Mini Project’
part of the course 
* Code Institute **SLACK Community** - General resource
* [Stack Overflow](https://stackoverflow.com/) – General resource
* [W3C Schools](https://www.w3schools.com/) 
* [CSS-Tricks](https://css-tricks.com/) - General resource
* [Youtube](https://www.youtube.com/) - General resource
* [Am I Responsive](http://ami.responsivedesign.is/) - Responsive website mockup image generator.


## Testing:

Testing documentation can be found on a separate document [here](https://github.com/chloelewisdev/milestone-project-2/blob/master/assets/docs/testing.md)

- [W3C Markup Validation Service](https://validator.w3.org/) 
    * This was a great tool throughout the project to check whether there were any errors in my HTML and CSS code (as discussed in more detail in the Testing section).
 - [JSHint](https://jshint.com/) 
    * This tool helped me test my JavaScript and jQuery code (explained in more detail in the Testing section). 
- [PEP 8 online](http://pep8online.com/)
    * I used PEP 8 to check that my Python code complied with formatting standards. 


## Deployment

This project was developed using Gitpod as the chosen IDE and GitHub as a remote repository. 

The deployed project can be viewed on the following link: [Remote: Live Website] http://ms3-remote-app.herokuapp.com/index/)

The project's GitHub repository can be viewed with the following link: [Remote: GitHub Repository]( https://github.com/chloelewisdev/milestone-project-3

### Local deployment

If you would like to work on this project further you can clone it to your local machine using the following steps:

1. Scroll to the top of this repository and click on the "clone or download button"
2. Decide whether you want to clone the project using HTTPS or an SSH key and do the following:
    * HTTPS: click on the checklist icon to the right of the URL to copy it
    * SSH key: first click on 'Use SSH' then click on the same icon as above
3. Open a new Terminal window in your IDE of choice
4. Change the current working directory to the location where you want the cloned directory.
5. Enter the following command and press 'Enter' to create your local clone:
```
git clone https://github.com/chloelewisdev/milestone-project-3
```
6. Now create a Database that you intend to use for this cloned project with MongoDB.
7. Return to the Terminal and enter the following to install all required dependencies:
```
pip3 install -r requirements.txt
```
8. Create an env.py file with the following content, replacing the 'username','password', 'cluster_name' and 'database_name' with your MongoDB database values:
```
import os

os.environ["MONGO_URI"] = "mongodb+srv://<username>:<password>@<cluster_name>-ocous.mongodb.net/<database_name>?retryWrites=true&w=majority" 
```
9. Add your env.py file to .gitignore to make sure your database information is not viewable to others
10. Your cloned version is now ready to run locally with the following command:
```
python3 app.py
```

You can find both the source of this information and learn more about the process with the following link: [Cloning a Repository](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

### Deploying this project to Heroku 

To deploy the project to Heroku, I used the following steps:

1. I created a Heroku account, signed in and created a new app with a unique name that had not already been taken (this project uses 'ms3-move-on'). I then set the region to the closest to me: 'Europe'.
2. With the app created, I went to the 'Settings' tab and clicked the 'Reveal Config Variables' button. From here, I input the following values:
```
MONGO_URI: mongodb+srv://<username>:<password>@<cluster_name>-ocous.mongodb.net/<database_name>?retryWrites=true&w=majority
IP: 0.0.0.0
PORT: 5000
```
(Note: within the MONGO_URI value, I replaced the 'username','password', 'cluster_name' and 'database_name' with my specific database values. They are kept private for security reasons.)


3. In Gitpod, I created a requirements.txt file with the following command:
```
pip3 freeze --local > requirements.txt
```
4. I then created a Procfile with the following content within (making sure that 'Procfile' was written with a capitalized 'P'):
```
echo web: python app.py > Procfile
```
5. I then committed these new files with the following:
```
git add
git commit -m 
```
6. With these files committed, I logged in to Heroku using this command and entered my details at the prompt:
```
heroku login
```
7. Once logged in, I linked my Heroku app created above as the remote repository with this command:
```
heroku git:remote -a ms3-move-on
```
8. I then completed the deployment by pushing the projekt to Heroku:
```
git push heroku master
```
9. This completed the process of deploying the project to Heroku. Once deployed, I continued to push all changes made to the project to Heroku throughout the remaining development process.

## Credits

### Content

The content of this website is entirely fictional and written by myself.

### Images

The images are all from DrawKit, which is an open source of illustrations. I used the ‘Peach Illustration System’ collection, which included characters, backgrounds and more. More information can be found on their website: [DrawKit](https://www.drawkit.io/)

### Acknowledgements

A big thank you to my mentor Seun Owonikoko for her useful suggestions and time with this project.  

Thanks to the Code Institute Slack Community.

Thanks also to my family and friends for taking the time to look over the website, test the features and for providing feedback.

