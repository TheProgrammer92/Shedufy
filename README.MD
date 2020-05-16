
*********BACK-END***

```bash
# install python
$ Get the latest version of Python at https://www.python.org/downloads/ 



# install virtualenv
$  python -m pip install virtualenvwrapper-win
  #create a virtual environment for the project
  $ mkvirtualenv myproject
  #Activate virtual environment
  $ workon myproject
  ##reference :: https://docs.djangoproject.com/fr/3.0/howto/windows/
  
#install django in virtual environment 
$ python -m pip install Django

# Install package django  in virtual environment
$ pip install   rest_framework djoser corsheaders corsheaders 


# run migration

$ python manage.py makemigrations
$ python manage.py migrate


##For admin management

# create superuser admin just run
$ python manage.py createsuperuser    ## and enters de  information email , password


# now run applicaition

$ python manage.py migrate



go to http://localhost:8000
for admin, go to http://localhost:8000/admin

ENjoy it !! 😊
```







*******FRONTENT************
# ict_resources

> Ict resources for Uy1

## Build Setup

```bash
# install dependencies
$ npm install

# serve with hot reload at localhost:3000
$ npm run dev

# build for production and launch server
$ npm run build
$ npm run start

# generate static project
$ npm run generate
```

For detailed explanation on how things work, check out [Nuxt.js docs](https://nuxtjs.org).
