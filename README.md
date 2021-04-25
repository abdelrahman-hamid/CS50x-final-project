# Fatouta Consultancy
#### Video Demo:  https://youtu.be/MhfixRLA0ww
#### Description:
My final project is a consultancy company website, built using HTML, CSS, JavaScript and Python. It is implemented as a flask application to handle the back-end of the website's contact form. The applicaton follows a MVC design pattern. The model is the data submitted through the website's contact form. The view consists of the static directory containing CSS, JavaScript and image files, and a templates directory that include the website's HTML pages. The controller is the application.py Python file.

The application.py file - the application's controller - is responsible for rendering the html templates. In addition to this, flask mail is configurated to send a confirmation email to the user after the contact form is submitted successfully. The user of the app must first enter their gmail login details securely through environment variables before deploying the app. The requirements.txt file contains the required Python libaries for the application.py file.

The templates directory contains a layout.html file that is used as a basis for all the website's pages via Jinja. The head tag contains the standard meta tags, plus an additional tag for SEO purposes. It also contains links to Bootstrap's stylesheet, a local stylesheet to override some of Bootstrap's CSS, and Font Awesome's icons library. Finally, it includes the page's title, which is set automatically using Jinja. The header tag consists of a navbar with centered nav links, a logo on the left, and a button on the right directing to the contact page. For screens smaller than 768px, the nav links are replaced with a toggler button containing the nav links and the contact button. This is pushed to the far right and the logo stays on the left. Next is the main tag, which is filled by each of the html files for each page. Finally is the footer tag followed by links to Bootsrap's JavaScript files and 2 local JavaScript files.

The index.html, about.html and services.html pages are structured using Boostrap's grid layout, and form the main content of the website. The contact.html page contains a contact form. This features client-side verification for the form inputs through required & minlength tags. The decision to choose client-side was to prevent the server from being overflooded with incorrect form submissions. The second half of the page contains links to the company's phone numbers, email, whatsapp, and LinkedIn, opening up the default app for each service.

The active_link.js file dynamically assigns the active class to the currently active page based on the current url of the user. The alert.js file displays a success alert below the contact form when it is submitted successfully. I chose a client-side approach for both goals using JQuery, rather than using Jinja in the layout.html file. This was done to separate programming logic and html code.





