import csv

file_path = "x-tasks/08-12-25/instagram/Instagram_Analytics.csv"

with open(file_path, "r") as fr:
    reader = csv.DictReader(fr)
    data = list(reader)


# total number of posts
total_posts = len(data)
# print(f"Total posts = {total_posts}")



# count of each media type
count_media_type = {}
for posts in data:
    media_type = posts.get("media_type")

    if media_type in count_media_type:
        count_media_type[media_type] += 1
    else:
        count_media_type[media_type] = 1
# print(count_media_type)



# Which media type (Reel, Photo, Video) generates the highest engagement rate on average
engagement_rate_based_on_media_type = {}
for post in data:
    engagement_rate = float(post.get("engagement_rate"))
    media_type = post.get("media_type")

    if media_type in engagement_rate_based_on_media_type:
        engagement_rate_based_on_media_type[media_type] += engagement_rate
    else:
        engagement_rate_based_on_media_type[media_type] = engagement_rate

average_engagement_rate_based_on_media_type = {}
for m, e in engagement_rate_based_on_media_type.items():
    media_count = count_media_type.get(m)
    average_engagement_rate_based_on_media_type[m] = round(e/media_count,2)

# print(average_engagement_rate_based_on_media_type)



# Which content category (Technology, Fitness, Beauty, Music, etc.) brings the highest follower growth per post?
content_category_count = {}
for post in data:
    content_category = post.get("content_category")
    if content_category in content_category_count:
        content_category_count[content_category] += 1
    else:
        content_category_count[content_category] = 1

content_category_follower_gained_count = {}
for post in data:
    followers_gained = int(post.get("followers_gained"))
    content_category = post.get("content_category")

    if content_category in content_category_follower_gained_count:
        content_category_follower_gained_count[content_category] += followers_gained
    else:
        content_category_follower_gained_count[content_category] = followers_gained

average_content_category_follower_gained = {}
for c, f in content_category_follower_gained_count.items():
    content_category_len = content_category_count.get(c)
    average_content_category_follower_gained[c] = round(f / content_category_len, 2)

max_average_content_category_follower_gained = [c for c, fa in average_content_category_follower_gained.items() if fa == max(average_content_category_follower_gained.values())]
# print(f"Content category with highest follower growth per post : {max_average_content_category_follower_gained[0]}")



# Which traffic source drives the maximum reach and impressions across posts?
traffic_source_reach = {}
for post in data:
    reach = int(post.get("reach"))
    traffic_source = post.get("traffic_source")

    if traffic_source in traffic_source_reach:
        traffic_source_reach[traffic_source] += reach
    else:
        traffic_source_reach[traffic_source] = reach

traffic_source_impressions = {}
for post in data:
    impressions = int(post.get("impressions"))
    traffic_source = post.get("traffic_source")

    if traffic_source in traffic_source_impressions:
        traffic_source_impressions[traffic_source] += impressions
    else:
        traffic_source_impressions[traffic_source] = impressions

max_traffic_source_reach = [t for t, r in traffic_source_reach.items() if r == max(traffic_source_reach.values())]
max_traffic_source_impressions = [t for t, i in traffic_source_impressions.items() if i == max(traffic_source_impressions.values())]

# print(f"max_traffic_source_reach : {max_traffic_source_reach[0]}")
# print(f"max_traffic_source_impressions : {max_traffic_source_impressions[0]}")



# Which media type (Reel / Photo / Video) gets the most likes?
media_type_likes = {}
for post in data:
    media_type = post.get("media_type")
    likes = int(post.get("likes"))

    if media_type in media_type_likes:
        media_type_likes[media_type] += likes
    else:
        media_type_likes[media_type] = likes

most_likes_media_type = [m for m, l in media_type_likes.items() if l == max(media_type_likes.values())]
# print(f"most_likes_media_type : {most_likes_media_type[0]}")



# Which content category gets the most followers gained?
most_follower_gained_content_category = [c for c, f in content_category_follower_gained_count.items() if f == max(content_category_follower_gained_count.values())]
# print(f"most_follower_gained_content_category : {most_follower_gained_content_category[0]}")



# Which traffic source brings the highest reach?
highest_traffic_source_reach = [t for t, r in traffic_source_reach.items() if r == max(traffic_source_reach.values())]
# print(f"highest_traffic_source_reach : {highest_traffic_source_reach[0]}")



# Which posts have the most engagement rate
max_engagement_rate = max(float(post.get("engagement_rate")) for post in data)
max_engagement_rate_post = [post for post in data if post.get("engagement_rate") != None and float(post.get("engagement_rate")) == max_engagement_rate]
# print(f"max_engagement_rate_post : {max_engagement_rate_post}")
# print(max_engagement_rate)



# Which traffic source gives the most impressions?
max_traffic_source_impressions = [t for t, i in traffic_source_impressions.items() if i == max(traffic_source_impressions.values())]
print(f"max_traffic_source_impressions : {max_traffic_source_impressions[0]}")







    



