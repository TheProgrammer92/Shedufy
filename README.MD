****COMMENT UTILISER L'APPLICATION***

1: Apres , avoir, suivis, toute les Etape ci dessous et lanc� l'application 
2: Se connecter a l'admin a , l'address   http://localhost:8000/admin 
3: creer des classe dans l'admin , et des materiel (equipement)
4: Creer un compte  a l'address http://localhost:3000/auth/register
5: Se connecter 
6: Aller a cette page http://localhost:3000/resources/classe
7: cliquer sur New Event et creer un emploie de temps
8: Vous verrez quelque photo de l'application dans le dossier  ***PHOTO**** 


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
