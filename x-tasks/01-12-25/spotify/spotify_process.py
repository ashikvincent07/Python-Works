import csv

file_path = "x-tasks/01-12-25/spotify/spotify_data clean.csv"

with open(file_path, "r", encoding="utf-8") as fr:
    reader = csv.DictReader(fr)
    data = [row for row in reader]

# five_track_names = []
# # for track in data:
# #     five_track_names.append(track.get("track_name"))
# #     if len(five_track_names) == 5:
# #         break
# # print(five_track_names)

# total_tracks = len(data)
# # print(f"Total tracks = {total_tracks}")


# # unique artist names
# artists_name = {track.get("artist_name") for track in data}
# # print(artists_name)


# explicit_true_tracks = [track for track in data if track.get("explicit") == "TRUE"]
# total_of_explicit_true_tracks = len(explicit_true_tracks)
# # print(f"Explicit true tracks count = {total_of_explicit_true_tracks}")

# # more_than_50_popularity_tracks = [track.get("track_name") for track in data if int(track.get("track_popularity")) > 50]
# # print(more_than_50_popularity_tracks)

# most_popular_track = ""
# top_popularity = 0
# # for track in data:
# #     if int(track.get("track_popularity")) > top_popularity:
# #         top_popularity = int(track.get("track_popularity"))
# #         most_popular_track = track.get("track_name")

# # print(most_popular_track)

# total_popularity_of_all_tracks = 0
# # for track in data:
# #     total_popularity_of_all_tracks += int(track.get("track_popularity"))

# average_popularity = total_popularity_of_all_tracks/len(data)
# # print(f"Average popularity = {average_popularity}")


# all_albums = [track.get("album_name") for track in data]
# album_count = {album : all_albums.count(album) for album in set(all_albums)}
# # print(album_count)


# # Write a program to input an artist name and display all songs by that artist.
# # artist_name = input("Enter artist name: ")
# # tracks_of_given_artist = [track.get("track_name") for track in data if track.get("artist_name") == artist_name]
# # print(tracks_of_given_artist)


# # Find the track with the maximum track_duration_min.
# max_track_duration = [track.get("track_name") for track in data if float(track.get("track_duration_min")) == max(float(track.get("track_duration_min")) for track in data)]
# # print(max_track_duration)

# artists_followers = {track.get("artist_name") : int(track.get("artist_followers")) for track in data}
# sorted_artists_followers = sorted(artists_followers,key=artists_followers.get,reverse=True) 

# print(sorted_artists_followers[:5])


# # Compare popularity of explicit vs non-explicit tracks
# explicit_track = [track for track in data if track.get("explicit") == "TRUE"]
# non_explicit_track = [track for track in data if track.get("explicit") == "FALSE"]

# explicit_track_popularity = [int(track.get("track_popularity")) for track in explicit_track]
# non_explicit_track_popularity = [int(track.get("track_popularity")) for track in non_explicit_track]

# # print(f"Average of explicit track popularity = {sum(explicit_track_popularity)/len(explicit_track):.2f}")
# # print(f"Average of non explicit track popularity = {sum(non_explicit_track_popularity)/len(non_explicit_track):.2f}")

# all_genres = [track.get("artist_genres") for track in data]
# generes_count = {genre : all_genres.count(genre) for genre in set(all_genres)}
# # print(generes_count)


# # Find the artist who has the highest number of songs in the dataset.
# all_artists = [track.get("artist_name") for track in data]
# artists_track_count = {artist : all_artists.count(artist) for artist in set(all_artists)}
# artist_has_most_track = [a for a, c in artists_track_count.items() if c == max(artists_track_count.values())]
# print(artist_has_most_track)




# Create a new column “popularity_level”
# Conditions: 0–20 → "Low"   21–60 → "Medium"   61–100 → "High"
for row in data:
    if row.get("track_popularity").isdigit():
        pop = int(row.get("track_popularity"))

        if 0 <= pop < 21:
            row["popularity_level"] = "Low"
        elif pop < 61:
            row["popularity_level"] = "Medium"
        elif pop < 101:
            row["popularity_level"] = "High"

# 3. Rewrite the CSV WITH the new column included
fieldnames = list(data[0].keys())

with open(file_path, "w", newline="",encoding="utf-8") as fw:
    writer = csv.DictWriter(fw, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)












