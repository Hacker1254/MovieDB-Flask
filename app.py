from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def posters():
    main_url = request.base_url

    if request.method == "POST":    
        name = request.form["movietitle"]
        year = request.form["movieyear"]

        api_key = "4c1c4651b470f738873f80310325d848"
        base_url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&language=en-US&query={name}&year={year}&page=1&include_adult=false"
        r = requests.get(base_url)
        response = r.json()

        tmdb_title = response['results'][0]['title']
        tmdb_poster = f"https://www.themoviedb.org/t/p/w1280{response['results'][0]['poster_path']}"
        tmdbid = response['results'][0]['id']
        tmdb_year = response['results'][0]['release_date']
        tmdb_rating = response['results'][0]['vote_average']
        tmdb_plot = response['results'][0]['overview']
        tmdb_bg_image = f"https://www.themoviedb.org/t/p/w1280{response['results'][0]['backdrop_path']}"

        streaming_link = f"https://www.2embed.ru/embed/tmdb/movie?id={tmdbid}"
        return render_template("movie.html", poster=tmdb_poster, streaming_link=streaming_link, tmdb_year=tmdb_year, tmdb_title=tmdb_title, tmdb_rating=tmdb_rating, tmdb_plot=tmdb_plot, main_url=main_url, tmdb_bg_image=tmdb_bg_image)
    else:
        return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, threaded=True)