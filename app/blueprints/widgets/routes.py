from flask import Blueprint, jsonify, request
import requests

widgets_bp = Blueprint('widgets_bp', __name__)

@widgets_bp.route('/weather', methods=['GET'])
def get_weather():
    # Example: Istanbul coordinates
    latitude = request.args.get('lat', 41.0082)
    longitude = request.args.get('lon', 28.9784)
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    resp = requests.get(url)
    if resp.status_code == 200:
        data = resp.json().get('current_weather', {})
        return jsonify({
            "temperature": data.get("temperature"),
            "windspeed": data.get("windspeed"),
            "weathercode": data.get("weathercode")
        })
    return jsonify({"error": "Weather API unavailable"}), 503

@widgets_bp.route('/quote', methods=['GET'])
def get_quote():
    resp = requests.get('https://api.quotable.io/random')
    if resp.status_code == 200:
        data = resp.json()
        return jsonify({"quote": data.get("content"), "author": data.get("author")})
    return jsonify({"error": "Quote API unavailable"}), 503
