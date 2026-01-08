from json import load

class Oscar:
    def __init__(self):
        file_path = "json-works/task/oscar-list/oscar-best-picture-award-winners.json"
        fr = open(file_path, "r", encoding= "utf-8")
        self.data = load(fr)

    # Create a new list that contains only the movie titles from the dataset.
    def all_movies_list_with_title(self):
        all_movies_list_with_title_only = [m.get("name") for m in self.data]
        print(all_movies_list_with_title_only)

    
    # Create a list that contains the movie title and release year for each Oscar-winning film.
    def oscar_winning_film_with_title_year(self):
        oscar_winning_film_with_title_year = {m.get("name") : m.get("released_year") for m in self.data}
        print(oscar_winning_film_with_title_year)

    #Get all movies that were released before the year 2000
    def movies_released_before_2000(self):
        movie_released_before_2000 = [m.get("name") for m in self.data if int(m.get("released_year")) < 2000]
        print(movie_released_before_2000)


    #Find all movies whose runtime is greater than 150 minutes.
    def runtime_greater_than_150(self):
        runtime_greater_than_150_min = [m.get("name") for m in self.data if int(m.get("duration").rstrip(" min")) > 150]
        print(runtime_greater_than_150_min)

    #Create a list of movies where the director name starts with the letter “S”.
    def movie_director_name_starts_s(self):
        movie_director_name_starts_with_s = []
        directors = []
        for m in self.data:
            directors = m.get("directors")
            for d in directors:
                if d.startswith("S"):
                    movie_director_name_starts_with_s.append(m.get("name"))
                    break
            directors.clear()

        print(movie_director_name_starts_with_s)

    #Q6. Count the total number of Oscar-winning movies in the dataset.
    def count_oscar_winning_movies(self):
        print(len(self.data))

    #. Calculate the average runtime of all Oscar Best Picture winners.
    def avg_runtime_of_oscar_winning_movies(self):
        sum = 0
        for m in self.data:
            sum += int(m.get("duration").rstrip(" min"))
        print(f"Average Runtime : {sum/len(self.data)}")

    #Create a dictionary that shows the number of movies won per decade (example: 1990s, 2000s, 2010s).
    def decade_wise_movies_count(self):
        decade_wise_movies_count = {}

        for m in self.data:
            oscar_year = int(m.get("oscar")) 
            oscar_year = oscar_year - (oscar_year%10)
            
            decade_wise_movies_count[oscar_year] = decade_wise_movies_count.get(oscar_year, 0) + 1

        print(decade_wise_movies_count)

    # Find the earliest released movie in the dataset.
    def earliest_released_movie(self):
        earliest_released_movie = [m.get("name") for m in self.data if int(m.get("released_year")) == min(int(m.get("released_year")) for m in self.data)]
        print(f"Earliest Realeased movie {earliest_released_movie}")
            

    #Check whether any movie in the dataset has a runtime less than 90 minutes
    def movie_with_runtime_lt_90(self):
        movie_with_runtime_lt_90 = [m.get("name") for m in self.data if int(m.get("duration").rstrip(" min")) < 90]
        if movie_with_runtime_lt_90:
            print(movie_with_runtime_lt_90)
        else:
            print("No movies runtime less than 90 minutes.")

oscar_instance = Oscar()

# oscar_instance.all_movies_list_with_title()
# oscar_instance.oscar_winning_film_with_title_year()
# oscar_instance.movies_released_before_2000()
# oscar_instance.runtime_greater_than_150()
# oscar_instance.movie_director_name_starts_s()
# oscar_instance.count_oscar_winning_movies()
# oscar_instance.avg_runtime_of_oscar_winning_movies()
# oscar_instance.decade_wise_movies_count()
# oscar_instance.earliest_released_movie()
oscar_instance.movie_with_runtime_lt_90()


