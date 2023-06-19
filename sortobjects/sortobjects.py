import re

def sort_by_title(movies):
    # Custom comparison function to sort titles alphabetically, ignoring leading "A"s, "An"s, or "The"s
    def compare_titles(movie):
        ignore_prefix = r'^(A|An|The)\s'  # Regular expression to match the ignored prefixes
        
        # Remove the ignored prefix from the title for comparison
        title = re.sub(ignore_prefix, '', movie['title'], flags=re.IGNORECASE)
        
        return title
    
    # Sort the movies list using the custom comparison function
    movies.sort(key=compare_titles)
    
    return movies
