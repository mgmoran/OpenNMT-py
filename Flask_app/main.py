from word_translate import *
from flask import *

app = Flask(__name__)

# Initialize global variables for rendering page
tmp_lang = ""
tmp_name = ""


# display query page
@app.route("/")
def search():
    return render_template('main.html')

# display results page for first set of results and "next" sets.
@app.route("/results", defaults={'page': 1}, methods=['GET', 'POST'])
def results(page):
    global tmp_name
    global tmp_translation
    global tmp_lang

    query = request.form['query']
    src_lang = request.form['src_lang']

    tmp_query = query
    tmp_lang = src_lang

    # store query values to display in search boxes in UI
    shows = {}
    shows['query'] = query
    shows['lang'] = src_lang
    input = "<" + src_lang + ">" + " " + query
    result = translate(input)
    print(result)

    return render_template('results.html', result=result)


if __name__ == "__main__":
    app.run(debug=True)
