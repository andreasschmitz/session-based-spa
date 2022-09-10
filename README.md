# Session-based Authentication & Single-page Applications

This project tries to demonstrate, in multiple "scenarios", how single-page applications, session-based authentication and established CSRF protection mechanisms can be brought together without a lot of hassle.

Unfortunately, it's quite common to find recommendations to use token-based authentication (e.g. JWTs) when building single-page web applications. Since there still isn't a good solution to store tokens without making them vulnerable to XSS attacks, this approach cannot be used in good conscience. One of the driving reasons to use token-based authentication instead of the established, more secure and well understood session-based authentication seems to be the extra complexity that comes from protecting against [Cross-site Request Forgery (CSRF)](https://owasp.org/www-community/attacks/csrf) attacks.

This isn't a installable dependency. If you look into the code you will find out that you can simply set this up on your own. If you are looking for an opinionated solution for Django and React, check-out the [AI-Kit: Authentication](https://github.com/ambient-innovation/django-ai-kit-auth) project by my friends at [Ambient](https://ambient.digital).

This project is based on Django and React and was created for the DjangoCon EU 2022 talk [Everything you didn't want to know about Cross-site Request Forgery (CSRF) in Django](https://pretalx.evolutio.pt/djangocon-europe-2022/talk/LWJHYJ/). You can find my blog post with furter information about the talk and a link to the recording here: [My DjangoCon Europe 2022 Talk About Cross-site Request Forgery](https://www.andreas.earth/s/djangocon-22).


## Setup & Requirements

The backend code was tested using **Python 3.10.6**. It should work with all Python versions supported by Django 4.1. I suggest to use [pyenv](https://github.com/pyenv/pyenv) to install and maintain Python versions. The backend resides in the `spa-backend` directory. The dependencies can be installed using [poetry](https://python-poetry.org) or the attached **requirements.txt** file (`pip install -r requirements.txt`).

The web-app was tested using **node 16.17 LTS**. To install the dependencies, switch to the `web-app` folder and run **npm install**.


The db.sqlite3 file was added to the repository to offer a quick start.

The **default credentials** are:
 - user_1: csrf1234
 - admin: csrf1234 (If you need to log in to the Admin `http://localhost:8000/admin`)


## Run the application

* Start the backend server (`spa-backend` directory) `python manage.py runserver 8000`
* Start the frontend application (`web-app` directory) `npm start`
* Open `http://localhost:3000` in your browser


### Scenarios

This project comes with 6 pre-configured scenarios, which can be set in `web-app/src/config.js` and `spa-backend/spa_backend/settings.py` (search for "CSRF SCENARIOS") respectively.

There are 3 groups of scenarios: localhost (1+2), .example.org with /etc/hosts config (3+4) and cross-site scenarios (5+6).

The odd-numbered scenarios use the Double Submit Cookie (1,3,5) CSRF protection mechanism, while the even-numbered ones use the Synchronizer Token Pattern (2,4,6).

Scenario 1 is configured by default.

#### Scenario 1 + 2

These scenarios are cross-origin and same-site. It's the easiest setup which works out of the box without any further configuration to your system. Just start the frontend and backend application and you are good to go.

- Frontend URL: http://localhost:3000
- Used Backend URL: http://localhost:8000
- SameSite: Lax for csrftoken and session cookies
- Double Submit Cookie (1) and Synchronizer Token Pattern (2)

#### Scenario 3 + 4

These scenarios are cross-origin and same-site. This requires more configuration, but is closer to a real-world setup. The easiest way to try this out is to update your /etc/host file by adding the following entries:

```
127.0.0.1 api.example.org
127.0.0.1 web.example.org
```

- Frontend URL: http://web.example.org:3000
- Used Backend URL: http://api.example.org:8000
- SameSite: Lax for csrftoken and session cookies
- csrftoken Cookie domain: .example.org
- Double Submit Cookie (3) and Synchronizer Token Pattern (4)


#### Scenario 5 + 6

These scenarios are cross-origin and same-site. This requires even more configuration. Apart from the changes to your /etc/host file:

```
127.0.0.1 api.example.org
127.0.0.1 myfrontend.com
```

You also need to find a browser that allows using cookies with `SameSite: 'None'` and the `Secure` flag not set. I tried this with Firefox 102 by using the following settings:
 1) Type `about:config` into the URL bar, click on accept and search for samesite. Set `network.cookie.sameSite.noneRequiresSecure` to `false`.
 2) Open the privacy preferences `about:preferences#privacy`. At the section **Enhanced Tracking Protection** choose the **custom** configuration and uncheck **cookies**.

Alternatively, you can setup TLS for the backend and frontend applications.

This might change in future versions of Firefox.


- Frontend URL: http://myfrontend.com:3000
- Used Backend URL: http://api.example.org:8000
- SameSite: None for csrftoken and session cookies
- Double Submit Cookie (5) and Synchronizer Token Pattern (6)


#### Manual Configuration

Feel free to try out combinations of different settings. The files `web-app/src/config.js` and `spa-backend/spa_backend/settings.py` should be self explanatory and come with a "manual" section.
