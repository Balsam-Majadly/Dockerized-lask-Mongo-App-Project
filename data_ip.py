from pymongo import MongoClient


DOMAIN = 'mongodb'
PORT = 27017
client = MongoClient(
        host = [ str(DOMAIN) + ":" + str(PORT) ],
        serverSelectionTimeoutMS = 3000, # 3 second timeout
        username = "admin",
        password = "root",
    )

db = client["movies"]
collection = db["movies"]

def add_data(movie_name,file_name,movie_ID,movie_url):
    with open(file_name, 'rb') as f:
        contents = f.read()
    result = collection.insert_one({'moviename': movie_name,'movieimdb': movie_ID,'filename': file_name, 'contents': contents,'movieurl': movie_url})
    return result
#add_data("creed_1.jpeg")

def search_in_mongo(movie_name):
    file = collection.find_one({'moviename': movie_name})
    if file is not None:
        print('The file exists')
        result=1
    else:
        print('The file does not exist')
        result=0
    return result

#search_in_mongo("cr.jpeg")
#
def search_to_get_poster(movie_name):
    file = collection.find_one({'moviename': movie_name})
    with open('image.jpeg', 'wb') as f:
        f.write(file['contents'])
    return 'image.jpeg'


def read(movie_name):
    file = collection.find_one({'moviename': movie_name})
    return file

def delete(movie_name):
    result = collection.delete_one({'moviename': movie_name})

# def replace(movie_name1,movie_name2):
#     delete(movie_name1)
#     add.add_movie(movie_name2)


