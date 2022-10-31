# Useful Applications / Projects
## Advanced Level
Day 70: [Hosting Blog Website](https://github.com/byJingL/blog-test):【Heroku, PostgreSQL, gunicorn】
- Host the blog website on Heroku. Switch the database from SQLite to PostgresSQL. Visite it [here](https://jane-blog-test.herokuapp.com/)

Day 69: [Fully Blog Website](/Advanced/day69_FullyBlogWeb/main.py):【Authentication with Flask, Relational Database, Decorator in Flask, Flask Gravatar, Flask Login】
- Add users to blog website built in Day67. Users who register or sign up can comment on blog posts and all comments will be listed below.
- Protect Routes to achive only blog owner can add/edit/delete posts.

Day 68: [File Download Website](/Advanced/day68_FileDownload/main.py):【Authentication with Flask, Flask Login, Hashing Password with werkzeug module, Message Flashing】
- Create a secret website. User with authentication can download file from this website.

Day 67: [RESTful Blog Website](/Advanced/day67_RESTfulBlog/main.py):【RESTful Routing, Flask, SQLite, SQLAlchemy, Flask-WTForm】
- Create a blog website with database. Users can create new post and edit or delete past posts.

Day 66: [Nearby Café API](/Advanced/day66_CafeAPI/main.py):【RESTful API, Flask, SQLite, SQLAlchemy】
- Create an API for users to access a database on nearby cafés. The information include café name, location, coffee price, WIFI availability, ect.
- User can use API by reading this [document](https://documenter.getpostman.com/view/24083770/2s8YCgDY7B).

Day 64: [Top 10 Movies](/Advanced/day64_Top10Movies/main.py):【Flask, SQLite, SQLAlchemy, Flask-WTForm, TMDB API】
- Create a website list my top 10 movies, showing the title, poster, overview, rating, review and ranking of them.
- Every movie can be updated and deleted. New movie can be added through [TMDB](https://www.themoviedb.org/) API.

Day 63: [Virtial Bookshelf](/Advanced/day63_VirtualBookshelfwithSQLite/main.py):【Database, SQLite, SQLAlchemy, Flask-WTForm】
- Build a website bookshelf with SQLite database. User can add new book ratingds, edit the rating and delete it.

Day 62: [Café Library](/Advanced/day62_WIFIandCoffeProject/main.py):【Flask, WTForm, Flask-Bootstrap, CSV】
- Build a website list some café nearby, includ relevent ionformation such as location, opening time, WIFI situation, etc.
- User can add new café to database and check all cafés.

Day 61: [Secrets Web](/Advanced/day61_SecretsWebwithWTForm/main.py):【Flask-WTForm, Flask-Bootstrap, Jinja Template Inheritance】
- Build a Log-in check website using Flask-WTForm, Flask-Bootstrap and Jinja Template Inheritance
  
Day 59-Day 60: [Blog Website](/Advanced/day59-60_UpgradedBlog/main.py):【Flask, Jinja, Bootstrap, HTML Form, smtplib module】
- Upgrad the blog buit in Day57 with Boostrap template from [Start Bootstrap's website](https://startbootstrap.com/previews/clean-blog).
- Get the contact form to work and send email to blog owner when visitors use contact form.

## Intermediate Level
Day 58: [Web App Website](/Intermediate/day58_Boostrap/index.html):【Bootstrap, Advanced CSS, [Google Font](https://fonts.google.com/), [Font Awesome](https://fontawesome.com/)】
- Create a introduction website for a web App. 
  
Day 57: [Blog Website](/Intermediate/day57_WebBlogwithJinja/main.py):【Flask, Jinja】
- Create a blog website including homepage and blog pages. Preview is [here](/Intermediate/day57_WebBlogwithJinja/previewhomepage.png) and [here](/Intermediate/day57_WebBlogwithJinja/previewblogpage.png).

Day 56: [Personal Name Card](/Intermediate/day56_PersonalNameCard/server.py):【Flask, HTML/CSS】
- Create web name card based on pre-built template in [HTML5up](https://html5up.net/). Preview is [here](/Intermediate/day56_PersonalNameCard/preview.png).

Day 56: [Personal Website](/Intermediate/day56_PersonalWeb/sever.py):【Flask, HTML/CSS】
- Render personal website buit in day44 with Flask.

Day 55: [Higher and Lower Web Game](/Intermediate/day55_HigherLowerGamewithFlask/server.py):【Flask, HTML, Parser URL】
- User can play guessing number game in web and get cute gifs as feedback.

Day 55: [Function Explaination Decorator](/Intermediate/day55_FlaskandDecorator/functionDecorator.py):【Decoration Function】
- Explain any function in detail with function name, inputs and results.

Day 54: [Function Run Speed Checker](/Intermediate/day54_FlaskBasicandDecorater/function_speed.py):【Decoration Function, time module】
- Calculate how many seconds the function run can cost by using decorate function.
  
Day 53: [Rent Seeker (Data Entry Job Automation)](/Intermediate/day53_RentSeeker/main.py):【Selenium, BeautifulSoup module, Google Form, Web Scraping】
- Gather rent information from Website according to the given requirements.
- Turn these information to Google Form and create excel of information in Google Sheet.

Day 51: [Internet Speed Complainer](/Intermediate/day51_InternetSpeedTwitterComplaintBot/main.py):【 Selenium, Web Scraping, OOP】  
- Check current internet speed automatically from [SpeedTest Website](https://www.speedtest.net/).  
- If internet speed is slower than provider has guaranteed, tweet on Tweeter to camplain automatically.  

Day 49: [Linkedin Jobs Saver](/Intermediate/day49_AutoJobSaver/main.py):【 Selenium, Web Scraping】  
- Auto go to given Linkedin page and sign in.
- Auto save first 7 jobs on Linkedin that match filters in past 24 hours.

Day 48: [Cookie Game Playing Bot](/Intermediate/day48_AutoGamePlayingBot/game.py):【 Selenium, Web Scraping】  
- Create a bot to click cookie in [Cookie Clicking Game](http://orteil.dashnet.org/experiments/cookie/) automatically.
- Users can adjust their strategies to buy items in shop.

Day 47: [Amazon Price Tracker](/Intermediate/day47_AmazonPriceTracker/main.py):【 BeautifulSoup module, Web Scraping, smtplib module 】  
- Set target price on specific thing in Amazon and check the real-time price of it.
- Sens an alert email when the real-time price is lower than target price.

Day 46: [Musical Time Machine](/Intermediate/day46_MusicalTimeMachine/main.py):【 BeautifulSoup module, Web Scraping, Spotipy module, Spotify API 】  
- Ask user to type a specific date and find Top 100 songs on that date in Billboard.
- Generate a playlist of Top 100 songs in Spotify and provide the link to this playlist.

Day 45: [Top 100 Movies](/Intermediate/day45_Top100Movies/main.py):【 Beautiful Soup Module, Web Scraping, File processing 】  
- Scraping [EMPIRE](https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/) to make a "Top 100 movies" list and save it to local file.

Day 38: [Workout Tracking](/Intermediate/day38_WorkoutTracking/main.py):【 APIs(Nutritionix API, Sheety API), API Header, Datetime, Bearer authentication 】  
- Analyse users' workout information by [NLP](https://en.wikipedia.org/wiki/Natural_language_processing) and record it to [Google Sheet](https://www.google.com/sheets/about/).

Day 37: [Habit Tracking](/Intermediate/day37_HabitTracking/main.py):【 API header, HTTP requests(GET, POST, PUT, DELETE), Datetime, Pixel API 】  
- Users can track coding learning progress and record coding hours everyday by using [Pixel](https://pixe.la/).

Day 36: [Stock News Alert](/Intermediate/day36_StockNewsAlert/main.py):【 APIs(Stock Price API, News API, Twilio API) 】  
- When stock users focusing has a big change, send SMS containing the latest 3 news of the company to them.

Day 35: [Rain Alert](/Intermediate/day35_RainAlert/main.py):【 OpenWeatherMap API, smtplib module, Environment variables 】  
- Email to alert users when it will rain in the following 12 hours.

Day 34: [The GUI Quiz App (Based on Day17)](/Intermediate/day34_GUIQuizApp/main.py):【 API, OOP, Unescape HTML entities, Tkinter 】  
- Randomly generate 10 questions by Trivia Database.
- Users can take a True/False question quiz and get the result.  

Day 33: [ISS Overhead Notifier](/Intermediate/day33_API_ISSOverheadNotifier/main.py):【 API, smtplib module 】  
- Send notification emails when International Space Station (ISS) is overhead at nights.

Day 32: [Auto Birthday Wisher](/Intermediate/day32_AutoBirthdayWisher/main.py):【 smtplib module, Datetime module 】  
- Update users' "Birthday to remember" list.
- Send emails to people whose birthday is today based on existing list.

Day 31: [Flashcard](/Intermediate/day31_Flashcard/main.py):【 Tkinter 】  
- Users can learn English through English-Chinese flash cards.
- Users' learning process can be updated.

Day 30: [Advanced Password Manager App](/Intermediate/day30_advanced/main.py):【 Tkinter, Exception catching, JSON data 】  
- Increase the function that can search saved passwords by website name.
- Increase exceptions catching and give relative warning.

Day 29: [Password Manager App](/Intermediate/day29_PasswaorManager/main.py):【 Tkinter 】  
- Generate complex safe password for users.
- Save specific web/account/password information to a local text file.

Day 28: [Promodoro Timer App](/Intermediate/day28_Promodoro/main.py):【 Tkinter 】  
- This is a time management tool using [Pomodoro Technique](https://en.wikipedia.org/wiki/Pomodoro_Technique).

