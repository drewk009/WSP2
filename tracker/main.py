from datetime import date, datetime, timedelta
import time
import twitter
client = twitter.Api()
#latest_posts = client.GetUserTimeline("we_are_thankful")
time_stamp = date.fromtimestamp(time.time()).strftime("%A %d. %B %Y")
time_stamp = time_stamp
#print [s.text for s in latest_posts]
print time_stamp
fmt = '%H:%M:%S'
time = datetime.now().strftime(fmt)
print time