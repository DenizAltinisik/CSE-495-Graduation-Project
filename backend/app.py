import openai
from flask import Flask, request, jsonify
import os
app = Flask(__name__)

openai.ap1_K3Y = "something"

@app.route('/api/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    cooperation_level = request.json.get('cooperationLevel')
    conversationTone = request.json.get('conversationTone')
    discussing = request.json.get('discussing')
    helpingOut = request.json.get('helpingOut')
    suggestive = request.json.get('suggestive')

    # Adjust chatbot's behavior based on all variables
    system_message = "You are an assistant."

    if cooperation_level == 'high':
        system_message += " You are very cooperative."
    elif cooperation_level == 'medium':
        system_message += " You are somewhat cooperative."
    else:
        system_message += " You are uncooperative."

    if conversationTone == 'friendly':
        system_message += " Your tone is friendly."
    elif conversationTone == 'formal':
        system_message += " Your tone is formal."
    else:
        system_message += " Your tone is informal."

    if discussing:
        system_message += " You are discussing topics."
    if helpingOut:
        system_message += " You are helping out."
    if suggestive:
        system_message += " You are being suggestive."

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