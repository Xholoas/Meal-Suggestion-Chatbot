from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Load ChatGPT model
openai.api_key = "KEY"
model_engine = "text-davinci-003"  # Replace with your model engine ID

# Home page
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index2.html')
def BMRPage():
    return render_template(('index2.html'))

# AJAX endpoint to get meal recommendations
@app.route('/get_meal_recommendations', methods=['POST'])
def get_meal_recommendations():
    # Get user input from text area
    user_input = request.form['user_input']
    user_input = user_input + "Format suggested meals with a leading '-' ."

    # Call ChatGPT to generate meal recommendations
    meal_recommendations = generate_meal_recommendations(user_input)

    # Return meal recommendations as JSON response
    return jsonify({'meal_recommendations': meal_recommendations})

# Function to generate meal recommendations using ChatGPT
def generate_meal_recommendations(user_input):
    # Call ChatGPT to generate meal recommendations
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=user_input,
      temperature=0.5,
      max_tokens=1024,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    # Extract the generated text from the response
    meal_recommendations = response.choices[0].text.strip()
    meal_rec_list = []

    for meal in meal_recommendations.split("-")[1:]:
        meal_rec_list.append(" - "+meal)

    meal_recommendations = meal_rec_list
    print(meal_recommendations)
    return meal_recommendations

if __name__ == '__main__':
    app.run(debug=True)
