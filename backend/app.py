from flask import Flask, request, jsonify

app = Flask(__name__)
reviews = []

@app.route('/submit-review', methods=['POST'])
def submit_review():
    data = request.json
    reviews.append(data)
    return jsonify({'message': 'Review added successfully'}), 201

@app.route('/get-reviews', methods=['GET'])
def get_reviews():
    return jsonify(reviews), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
