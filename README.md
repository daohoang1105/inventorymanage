# [Gradient Able](https://appseed.us/generator/gradient-able/) Django

Open-source **Django Dashboard** generated by `AppSeed` op top of a modern design. **[Gradient Able](https://appseed.us/generator/gradient-able/)** Bootstrap Lite is the most stylised Bootstrap Lite Admin Template, around all other Lite/Free admin templates in the market. It comes with high feature-rich pages and components with fully developer-centric code. Before developing Gradient Able our key points were performance and design.

- 👉 [Gradient Able Django](https://appseed.us/product/gradient-able/django/) - Product page
- 👉 [Gradient Able Django](https://django-gradient-able.appseed-srv1.com/) - LIVE deployment
- 👉 [Complete documentation](https://docs.appseed.us/products/django-dashboards/gradient-able) - `Learn how to use and update the product`
  - ✅ [Set up the environment](https://docs.appseed.us/products/django-dashboards/gradient-able#environment)
  - ✅ [Manage App users](https://docs.appseed.us/products/django-dashboards/gradient-able#manage-app-users)
  - ✅ [Application Bootstrap Flow](https://docs.appseed.us/products/django-dashboards/gradient-able#application-bootstrap-flow)
  - ✅ [App Routing](https://docs.appseed.us/products/django-dashboards/gradient-able#project-routing)
  - ✅ [UI Assets and Templates](https://docs.appseed.us/products/django-dashboards/gradient-able#ui-assets-and-templates)
  - ✅ [Set up the MySql Database](https://docs.appseed.us/products/django-dashboards/gradient-able#set-up-the-mysql-database)
  - ✅ [Adding a new app](https://docs.appseed.us/products/django-dashboards/gradient-able#adding-a-new-app)
  - ✅ [Static Assets for production](https://docs.appseed.us/products/django-dashboards/gradient-able#static-assets-for-production)   
  
<br />

> Built with [Gradient Able Generator](https://appseed.us/generator/gradient-able/)

- Timestamp: `2022-06-09 09:56`
- Build ID: `ec6a9a91-fa60-4d93-b84b-05e7669ee9dd`
- **Free [Support](https://appseed.us/support/)** (registered users) via `Email` and `Discord`

<br />

> Features

- `Up-to-date dependencies`
- Database: `sqlite`
- UI-Ready app, Django Native ORM
- `Session-Based authentication`, Forms validation

<br />

![Gradient Able - Starter generated by AppSeed.](https://user-images.githubusercontent.com/51070104/171583187-c4ca1bef-b535-458e-9250-8d62ba1f5b30.png)

<br />


## ✨ Start the app in Docker

> **Step 1** - Download the code from the GH repository (using `GIT`) 

```bash
$ # Get the code
$ git clone https://github.com/app-generator/django-gradient-able.git
$ cd django-gradient-able
```

<br />

> **Step 2** - Edit `.env` and remove or comment all `DB_*` settings (`DB_ENGINE=...`). This will activate the `SQLite` persistance. 

```txt
DEBUG=True

# Deployment SERVER address
SERVER=.appseed.us

# For MySql Persistence
# DB_ENGINE=mysql            <-- REMOVE or comment for Docker
# DB_NAME=appseed_db         <-- REMOVE or comment for Docker  
# DB_HOST=localhost          <-- REMOVE or comment for Docker 
# DB_PORT=3306               <-- REMOVE or comment for Docker
# DB_USERNAME=appseed_db_usr <-- REMOVE or comment for Docker
# DB_PASS=<STRONG_PASS>      <-- REMOVE or comment for Docker

```

<br />

> **Step 3** - Start the APP in `Docker`

```bash
$ docker-compose up --build 
```

Visit `http://localhost:5085` in your browser. The app should be up & running.

<br />




## ✨ How to use it

> Download the code 

```bash
$ # Get the code
$ git clone https://github.com/app-generator/django-gradient-able.git
$ cd django-gradient-able
```

<br />

### 👉 Set Up for `Unix`, `MacOS` 

> Install modules via `VENV`  

```bash
$ virtualenv env
$ source env/bin/activate
$ pip3 install -r requirements.txt
```

<br />

> Set Up Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> Start the app

```bash
$ python manage.py runserver
```

At this point, the app runs at `http://127.0.0.1:8000/`. 

<br />

### 👉 Set Up for `Windows` 

> Install modules via `VENV` (windows) 

```
$ virtualenv env
$ .\env\Scripts\activate
$ pip3 install -r requirements.txt
```

<br />

> Set Up Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> Start the app

```bash
$ python manage.py runserver
```

At this point, the app runs at `http://127.0.0.1:8000/`. 

<br />

### 👉 Create Users

By default, the app redirects guest users to authenticate. In order to access the private pages, follow this set up: 

- Start the app via `flask run`
- Access the `registration` page and create a new user:
  - `http://127.0.0.1:8000/register/`
- Access the `sign in` page and authenticate
  - `http://127.0.0.1:8000/login/`

<br />

## ✨ Code-base structure

The project is coded using a simple and intuitive structure presented below:

```bash
< PROJECT ROOT >
   |
   |-- core/                               # Implements app configuration
   |    |-- settings.py                    # Defines Global Settings
   |    |-- wsgi.py                        # Start the app in production
   |    |-- urls.py                        # Define URLs served by all apps/nodes
   |
   |-- apps/
   |    |
   |    |-- home/                          # A simple app that serve HTML files
   |    |    |-- views.py                  # Serve HTML pages for authenticated users
   |    |    |-- urls.py                   # Define some super simple routes  
   |    |
   |    |-- authentication/                # Handles auth routes (login and register)
   |    |    |-- urls.py                   # Define authentication routes  
   |    |    |-- views.py                  # Handles login and registration  
   |    |    |-- forms.py                  # Define auth forms (login and register) 
   |    |
   |    |-- static/
   |    |    |-- <css, JS, images>         # CSS files, Javascripts files
   |    |
   |    |-- templates/                     # Templates used to render pages
   |         |-- includes/                 # HTML chunks and components
   |         |    |-- navigation.html      # Top menu component
   |         |    |-- sidebar.html         # Sidebar component
   |         |    |-- footer.html          # App Footer
   |         |    |-- scripts.html         # Scripts common to all pages
   |         |
   |         |-- layouts/                   # Master pages
   |         |    |-- base-fullscreen.html  # Used by Authentication pages
   |         |    |-- base.html             # Used by common pages
   |         |
   |         |-- accounts/                  # Authentication pages
   |         |    |-- login.html            # Login page
   |         |    |-- register.html         # Register page
   |         |
   |         |-- home/                      # UI Kit Pages
   |              |-- index.html            # Index page
   |              |-- 404-page.html         # 404 page
   |              |-- *.html                # All other pages
   |
   |-- requirements.txt                     # Development modules - SQLite storage
   |
   |-- .env                                 # Inject Configuration via Environment
   |-- manage.py                            # Start the app - Django default start script
   |
   |-- ************************************************************************
```

<br />



## ✨ PRO Version

> For more components, pages and priority on support, feel free to take a look at this amazing starter:

Designed for those who like bold elements and beautiful websites, **Gradient Able** is the most stylish Bootstrap 4 Admin Template compare to all other Bootstrap admin templates. It comes with high feature-rich pages and components with fully developer-centric code. 

- 👉 [Django Gradient PRO](https://appseed.us/product/gradient-able-pro/django/) - product page
- 👉 [Django Gradient PRO](https://django-gradient-able-pro.appseed-srv1.com) - LIVE Deployment

<br >

![Gradient Able PRO - Starter generated by AppSeed.](https://user-images.githubusercontent.com/51070104/171583582-d9652e7e-f420-4cf0-8eb1-dda3c79f8c18.png)

<br />

---
[Gradient Able](https://appseed.us/generator/gradient-able/) Django - Open-source starter generated by **[AppSeed Generator](https://appseed.us/generator/)**.