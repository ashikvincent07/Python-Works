all_movies_path = "x-tasks/27-11-25/movies.csv"

fr_all_movies = open(all_movies_path, "r")

# for index, line in enumerate(fr_all_movies):
#     if index == 5:
#         break
#     line = line.rstrip("\n")
#     print(line)


# total_number_of_movies = -1 #excluding header

# for line in fr_all_movies:
#     total_number_of_movies += 1
    
# print(f"Total number of movies = {total_number_of_movies}")


# for line in fr_all_movies:
#     line = line.rstrip("\n")
#     header_row = line.split(",")
    
#     for column in header_row:
#         column = column.rstrip("\n")
#         print(column)
#     break


# year = int(input("Enter year: "))
# movie_year = []

# for index, line in enumerate(fr_all_movies):
#     if index == 0:
#         continue
#     line = line.rstrip("\n")
#     row = line.split(",")
#     movie_year.append({row[0] : int(row[7])})

# for movie in movie_year:
#     for m, y in movie.items():
#         if y == year:
#             print(f"{m} : {y}")


# movie_audience_rating = {}

# print("Top rated movies : ",end="")

# for index, line in enumerate(fr_all_movies):
#     if index == 0:
#         continue
#     line = line.rstrip("\n")
#     row = line.split(",")
#     movie_audience_rating[row[0]] = float(row[3])

# max_rating = max(movie_audience_rating.values())

# for m, r in movie_audience_rating.items():
#         if max_rating == r:
#             print(m,end=", ")


# genre = input("Enter genre : ")
        
# movie_genre = {}

# for index, line in enumerate(fr_all_movies):
#     if index == 0:
#         continue
#     line = line.rstrip("\n")
#     row = line.split(",")
#     movie_genre[row[0]] = row[1]

# for m, g in movie_genre.items():
#     if g == genre:
#         print(m)


# top_rated_movies_path = "x-tasks/27-11-25/top_rated_movies.csv"
# fw_top_rated_movies = open(top_rated_movies_path, "w")

# movie_audience_rating = {}

# for index, line in enumerate(fr_all_movies):
#     if index == 0:
#         continue
#     line = line.rstrip("\n")
#     row = line.split(",")
#     movie_audience_rating[row[0]] = float(row[3])

# max_rating = max(movie_audience_rating.values())

# for m, r in movie_audience_rating.items():
#         if r > 80:
#             fw_top_rated_movies.write(m+"\n")


# genre_count_path = "x-tasks/27-11-25/genre_count.txt"
# fw_genre_count = open(genre_count_path, "w")

# genre_count = {}

# for index, line in enumerate(fr_all_movies):
#     if index == 0:
#         continue
#     line = line.rstrip("\n")
#     row = line.split(",")

#     if row[1] in genre_count:
#         genre_count[row[1]] += 1

#     else:
#         genre_count[row[1]] = 1

# for g, c in genre_count.items():
#     fw_genre_count.write(f"{g} : {c}\n")


# sorted_movie_rating_path = "x-tasks/27-11-25/sorted_movie_rating.csv"
# fw_sorted_movie_rating = open(sorted_movie_rating_path, "w")

# movie_audience_rating = {}

# for index, line in enumerate(fr_all_movies):
#     if index == 0:
#         continue
#     line = line.rstrip("\n")
#     row = line.split(",")
#     movie_audience_rating[row[0]] = float(row[3])

# sorted_movie_rating = sorted(movie_audience_rating,key=lambda k: movie_audience_rating.get(k),reverse=True)

# for movie in sorted_movie_rating:
#     rating = movie_audience_rating[movie]
#     fw_sorted_movie_rating.write(f"{movie} : {rating}\n")


# for line in fr_all_movies:
#     line = line.rstrip("\n")
#     print(line)


title_keyword = input("Enter keyword to search movies: ").casefold()

movies = []

for index, line in enumerate(fr_all_movies):
    if index == 0:
        continue
    line = line.rstrip("\n")
    row = line.split(",")
    movies.append(row[0])

for movie in movies:
    if title_keyword in movie.casefold():
        print(movie)




    
