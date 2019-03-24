import tweepy

consumer_key='vQBmNczddMVN0UMlqHMmAA'
consumer_secret='ijnUbF9vnOEPvW9a7tiyV0J2SKqRODPdAp5Gub2MXKc'
access_token='210196015-7dO8LVU4xQiBO1wWdKQRBhqMeamZjrD1JqyFliQc'
access_token_secret='6Uw1XPfBQtdXTmk5jUYbeJONhIUmAbTs1ajqxib2P1hfK'

auth =  tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)#conectarse a la cuenta

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
	# print(tweet.text)
	
#devuelve el nombre del usuario
user = api.me()
print(user.name)

#actuaiizar el status en twitter
status= 'Escribiendo desde python usando tweepy'

api.update_status(status)





for follower in tweepy.Cursor(api.followers).items():#Accede a los usuarios que te siguen y los recorre con el for
	follower.follow()#.follow es la funcion para seguir a en este caso todos los que te siguen

 #Favoritea o retwitea segun un criterio
 
search = 'ciencia'
NofTweets= 5
 
for tweet in tweepy.Cursor(api.search, search).items(NofTweets):# busca con la api.search y el parametro search(definido por nosotros) entre los tweets, y con el numero de tweets(items) que le hemos indicado
	try:
		tweet.retweet()#.retweet para retwittear
		print('retweeted the tweet')
	except tweepy.TweepError as e:
		print(e.reason)
	except StopIteration:
		break
	