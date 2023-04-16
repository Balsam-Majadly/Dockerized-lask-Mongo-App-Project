import requests
import data_ip
from config import api_key

def add_to_mongo(movie_title):
    #movie_title = 'it'  # The title of the movie you want the poster for

    # Make the API request to search for the movie
    response = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={movie_title}')

    if response.status_code == 200:
        search_results = response.json()['results']

        if len(search_results) > 0:
            # Get the first result
            first_result = search_results[0]
            poster_path = first_result['poster_path']

            # Construct the URL for the poster image
            poster_url = f'https://image.tmdb.org/t/p/original{poster_path}'
            print(poster_url)

            # Download the poster image
            response = requests.get(poster_url)

            if response.status_code == 200:
                with open(f'{first_result["id"]}.jpg', 'wb') as f:
                    f.write(response.content)
                    print(f'Poster image saved as {first_result["id"]}.jpg')
                filename=str(first_result["id"]) + ".jpg"
                data_ip.add_data(movie_title, filename, first_result["id"], poster_url)
                return 1
            else:
                print('Unable to download poster image')
                return 0
        else:
            print('No search results found')
            return 0
    else:
        print('Unable to search for movie')
        return 0
