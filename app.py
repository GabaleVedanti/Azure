from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/weather')
def get_weather():
    city = request.args.get('city', default='Pune')
    api_key = "YOUR_API_KEY"  # 🔁 Replace with your actual OpenWeatherMap API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    try:
        response = requests.get(url)
        data = response.json()
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': 'Failed to fetch weather data'}), 500

if __name__ == '__main__':
    app.run(debug=True)
