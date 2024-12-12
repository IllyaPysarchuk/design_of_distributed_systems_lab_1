from flask import Flask, request, jsonify
import time
import logging

# Налаштування логування
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Постачальник Сервісу (Service Provider)
provider_app = Flask("provider")

@provider_app.route("/calculate", methods=["POST"])
def calculate():
    start_time = time.time()
    data = request.get_json()
    number = data.get("number")
    result = number * number  # Просте обчислення (наприклад, квадрат числа)
    time_taken = time.time() - start_time
    logging.info(f"Provider: Обчислення завершено за {time_taken:.6f} секунд.")
    return jsonify({"result": result, "time_taken": time_taken})

