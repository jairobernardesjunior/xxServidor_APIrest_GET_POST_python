from flask import Flask, jsonify, request

# create app
app = Flask(__name__, static_folder='static')

# routes
@app.route('/square/', methods=['POST'])
def square():
    # get data
    data = request.get_json()[0]
    num_list = data.values()

    response = {}
    response['results'] = []

    for n in num_list:
        square = n ** 2
        response['results'].append(square)

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)