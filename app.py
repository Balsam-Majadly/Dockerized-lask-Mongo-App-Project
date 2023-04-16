from flask import Flask, render_template, request
import requests
from pymongo import MongoClient
import tmdbb

app = Flask(__name__)

# Connect to MongoDB container
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

@app.route('/')
def index():
    return render_template('searchH.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form['query']
        result = collection.find_one({'moviename': query})
        if result:
            #image_url ="http://image.tmdb.org/t/p/original/1Gu1IzSzlqvFuoVEfHqzQxRPOGi.jpg"
            image_url = result['movieurl']
            return render_template('result1.html', image_url=image_url)
        else:
           #res=add.add_movie(query)
           res1=tmdbb.add_to_mongo(query)
           if(res1==1):
                result = collection.find_one({'moviename': query})
                image_url = result['movieurl']
                return render_template('result1.html', image_url=image_url)
           else:
            return render_template('not_found.html')

    return render_template('searchH.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)