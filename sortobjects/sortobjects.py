import re
class Movies():
    '''
    A class to arrange movies based on different criterias. 
    
    '''
    def __init__(self):
        pass


    def movies_sorted_by_year(self,movies) :
        '''
        A method intended to Sort movies by year in dscending order
        args:list of objects
        retuns: ordered list of object based on the most recent years
        '''
        ordered_movies=sorted(movies, key=lambda x: x["year"],reverse=True)
        return ordered_movies


    def movies_sorted_by_title (self,movies):
        '''
        A method Sorts movies by title while ignoring leading "A"s, "An"s, or "The"s
        args:list of objects
        retuns: ordered list of object based on the alphabits
        '''
        ignore_prefix = r'^(A|An|The)\s'  # Regex pattern to match the ignored prefixes
        ordered_movies=sorted(movies, key=lambda x: re.sub(ignore_prefix, '', x["title"], flags=re.IGNORECASE))
        return ordered_movies

        


movies_set = [
    {"title": "The Avengers", "year": 2012, "genres": ["Action", "Adventure", "Sci-Fi"]},
    {"title": "Anchorman: The Legend of Ron Burgundy", "year": 2004, "genres": ["Comedy"]},
    {"title": "Avatar", "year": 2009, "genres": ["Action", "Adventure", "Fantasy", "Sci-Fi"]},
    {"title": "Iron Man", "year": 2008, "genres": ["Action", "Adventure", "Sci-Fi"]},
    {"title": "A Clockwork Orange", "year": 1971, "genres": ["Crime", "Drama", "Sci-Fi"]}
]
my_sort=Movies()
# print(my_sort.movies_sorted_by_year(movies_set))
print(my_sort.movies_sorted_by_title(movies_set))