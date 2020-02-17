from flask import Flask, render_template, request
from flask_cors import CORS
import requests

app = Flask(__name__, template_folder='templates')
CORS(app)


@app.route('/', methods=['POST', 'GET'])
def main():
    return render_template('main.html')


@app.route('/categories', methods=['POST', 'GET'])
def categories():
    if request.method == "POST":
        return render_template('test.html')


@app.route('/categories_joke', methods=['POST', 'GET'])
def categori_joke():
    get_result = request.form
    get_text = get_result["Category_Name"]
    check_response = requests.get('https://api.chucknorris.io/jokes/categories')
    if get_text in check_response.json():
        response = requests.get('https://api.chucknorris.io/jokes/random?category=' + get_text)
        json_response = response.json()
        random_result = json_response['value']
        return render_template('category_joke.html', result=random_result)
    return "Enter valid  entry!!"


@app.route('/random', methods=['POST', 'GET'])
def random():
    if request.method == "POST" or request.method == "GET":
        response = requests.get('https://api.chucknorris.io/jokes/random')
        json_response = response.json()
        random_result = json_response['value']
        return render_template('random_result.html', result=random_result)


@app.route('/free_text', methods=['POST', 'GET'])
def free_text():
    result = []
    if request.method == "POST":
        get_result = request.form
        get_text = get_result["Free_Text"]
        response = requests.get('https://api.chucknorris.io/jokes/search?query=' + get_text)
        json_response = response.json()
        temp_store = json_response['result']
        for i, j in enumerate(temp_store):
            result.append(j['value'])
        return render_template('free_text.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
