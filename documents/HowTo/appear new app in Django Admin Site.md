## How to make newly added django app in the django admin site?

- We need to make a new migration record for the new app and make the changes into our database.\
`$ python manage.py makemigrations blog`\
`$ python manage.py migrate blog `\
Here, blog is our new app.

- Don't forget to register the app in admin.py