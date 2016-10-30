import twitter
api = twitter.Api(consumer_key = '9zfJNe39F7R6isb9qtr8PkGQ4',
				  consumer_secret = '2q4BJdK0khZV8xIrjPyqtqYs0AtEQUecVE8DTZXMy30ZJiIoDv',
				  access_token_key = '2358696205-bEUbsHFv5pwpmw8JS0oOqCEMD8lGSyxXD6jELHN',
				  access_token_secret = 'tLyFwTK4iFgXYLpq8COjE71n3AjhjtuEirX4kdaEnr6Yp')


print(api.VerifyCredentials())
