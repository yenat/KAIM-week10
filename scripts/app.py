from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Load the merged dataset
merged_data = pd.read_csv('merged_data.csv')

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify(merged_data.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True, port=5001)
