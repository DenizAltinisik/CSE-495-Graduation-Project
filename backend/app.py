import openai
from flask import Flask, request, jsonify
import os
app = Flask(__name__)

openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/api/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    cooperation_level = request.json.get('cooperationLevel')

    # Adjust chatbot's behavior based on cooperation level
    if cooperation_level == 'high':
        system_message = "You are a very helpful and cooperative assistant helping to solve problems like building a dog house."
    elif cooperation_level == 'medium':
        system_message = "You are a somewhat helpful assistant, providing some advice but leaving the user to figure out the rest."
    else:
        system_message = "You are an uncooperative assistant who doesn't help much."

    # Use the new ChatCompletion API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or the model you're using
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message},
        ]
    )

    return jsonify({
        'reply': response['choices'][0]['message']['content']
    })

if __name__ == '__main__':
    app.run(debug=True)
