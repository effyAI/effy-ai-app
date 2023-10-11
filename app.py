from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from resources.calculator import calculator

app = Flask(__name__)
cors = CORS(app)
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate_api', methods=['POST'])
def calculate_api():

    app.logger.info('This is an access log message.')
    try: 
        input = request.get_json()
        print(input)
        currentAge = int(input.get("currentAge"))
        retirementAge = int(input.get("retirementAge"))
        corpusGoal = float(input.get("corpusGoal"))
        interestRate = float(input.get("interestRate"))
        response = calculator(currentAge, retirementAge, corpusGoal, interestRate)
        return response
    except Exception as e:
        #print("Post data reading error:",e) # Send error to server 
        return {"error":403}
    

if __name__ == "__main__":
    app.run(port=5000)