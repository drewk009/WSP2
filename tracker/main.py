from datetime import date, datetime, timedelta
from oauthtwitter import OAuthApi
import time
import twitter
client = twitter.Api()
#vAuthenticatedTwitterInstance = OAuthApi('J04dbzIKXvw9J3pdPC3XWQ', 'sFvh3IFjfiGK5T9owDhCdAIg6epx055LR3I9HwGU', '408029985-qvqbbDJYZOxXQhjoRVLrRegauTaeF05Ru8ANc4Zs')
latest_posts = client.GetUserTimeline("we_are_thankful")
time_stamp = date.fromtimestamp(time.time()).strftime("%A %d. %B %Y")
time_stamp = time_stamp
print [s.text for s in latest_posts]
print time_stamp
fmt = '%H:%M:%S'
time = datetime.now().strftime(fmt)
print time

first_order = client.GetFollowers()


first_order_count = 0
second_order_count = 0
social_capital = 0
for x in first_order:
  first_order_count = first_order_count + 1
  second_order = x.GetFollowersCount()
  second_order_count = second_order_count + second_order
  if second_order >= 60:
    social_capital = social_capital + 1

#Followers
print first_order_count
#FOllowers Followers
print second_order_count
#Social Capital
print social_capital/first_order_count
#Social Average
print second_order_count/first_order_count

friends = client.GetFriends()
friend_count = 0
for t in friends:
  friend_count = friend_count + 1
#Efficiency
print first_order_count/friend_count