from flask import Flask, request, jsonify
import time
import logging

# Налаштування логування
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Споживач Сервісу (Service Consumer)
consumer_app = Flask("consumer")
import requests

@consumer_app.route("/process", methods=["POST"])
def process():
    start_time = time.time()
    data = request.get_json()
    number = data.get("number")

    # Запит до Постачальника Сервісу
    provider_url = "http://provider:5001/calculate"
    response = requests.post(provider_url, json={"number": number})
    provider_response = response.json()

    time_taken = time.time() - start_time
    logging.info(f"Consumer: Запит завершено за {time_taken:.6f} секунд.")

    return jsonify({
        "input": number,
        "provider_result": provider_response,
        "consumer_time_taken": time_taken
    })
