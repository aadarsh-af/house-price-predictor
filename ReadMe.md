# Try using my [Bangalore House Price Predictor](https://aadarsh-house-price-predictor.herokuapp.com/)

## Steps to deploy your flask app on Heroku
### Create an account on [Heroku](https://www.heroku.com/)
### Go to [heroku_site](https://dashboard.heroku.com/apps)
### Create new app
### give app name
### Download and Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
### Go to your pycharm project and type the following commands in the terminal there
- `git init`
- `heroku login`
- `heroku git:remote -a your_app_name`
- `pip install gunicorn` (if not installed)
- `pip freeze > requirements.txt` (make sure you keep every library version according to your model's fit)
- Create a file from scratch and name it as `Procfile`
- Inside Procfile, write `web: gunicorn main:app` where main is the python file name like main.py and app is the variable which stores the instance of Flask
- `git add .` in terminal
- `git commit -m "message"`
- `git push heroku master`
- `heroku open` - this will open your deployed app!
- `heroku logs --tail` - to check logs  
  
# You can also use different platforms to deploy your flask app...
# PythonAnywhere | Wayscript | Heroku
### The above three are the best according to me
