import twitter
client = twitter.Api()
latest_posts = client.GetUserTimeline("we_are_thankful")
print [s.text for s in latest_posts]
