from flask import Flask, render_template, request, jsonify
import requests
import re

app = Flask(__name__, template_folder="templates", static_folder="static")

def validate_currency(amount: str) -> bool:
    pattern = r'^\d+(\.\d{2})?$'
    if re.match(pattern, amount):
        if '-' in amount[1:]:
            return False, " (-) In Given Amount"
        return True, ""
    else:
        return False, "Wrong Symbols"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    data = request.get_json()
    requested = data.get('expression', [])
    if requested[0] == requested[1]:
        return jsonify({"error": "Chosen Same Currencies"}), 400
    is_valid, err_msg = validate_currency(requested[2])
    if not is_valid:
        return jsonify({"error": err_msg}), 400
    try:
        result = requests.get(
             f"https://api.frankfurter.app/latest?amount={requested[2]}&from={requested[0]}&to={requested[1]}"
        )
        print(result)
        return jsonify({"result": str(result.json()['rates'][requested[1]])})
    except Exception as e:
        return jsonify({"error": f"Converting error:  {str(e)}"}), 400

if __name__ == '__main__':
    print("Starting Flask app...")
    app.run(host='0.0.0.0', port=5000, debug=True)
