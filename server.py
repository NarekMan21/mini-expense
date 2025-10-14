#!/usr/bin/env python3
"""
Запуск:  python server.py
Первый раз спросит код подтверждения Telegram.
Сессия сохранится в parser.session – дальше без запросов.
"""
import os, json, re
from flask import Flask, jsonify, send_from_directory, request
from telethon.sync import TelegramClient
from datetime import datetime

# ===== ваши данные =====
# Все переменные окружения обязательны - без них приложение не запустится
API_ID_STR   = os.getenv('API_ID')
API_HASH     = os.getenv('API_HASH')
PHONE        = os.getenv('PHONE')

if not all([API_ID_STR, API_HASH, PHONE]):
    print("Ошибка: отсутствуют обязательные переменные окружения API_ID, API_HASH, PHONE")
    print("Создайте файл .env на основе .env.example и заполните значения")
    exit(1)

# Преобразование с проверкой
try:
    API_ID = int(API_ID_STR)
except ValueError:
    print(f"Ошибка: API_ID должен быть числом, получено: {API_ID_STR}")
    exit(1)

GROUP_EXP_STR = os.getenv('GROUP_EXP')
GROUP_INC_STR = os.getenv('GROUP_INC')

if not all([GROUP_EXP_STR, GROUP_INC_STR]):
    print("Ошибка: отсутствуют переменные GROUP_EXP, GROUP_INC")
    print("Создайте файл .env на основе .env.example и заполните значения")
    exit(1)

try:
    GROUP_EXP = int(GROUP_EXP_STR)
    GROUP_INC = int(GROUP_INC_STR)
except ValueError as e:
    print(f"Ошибка преобразования GROUP ID: {e}")
    exit(1)

SESSION_FILE = os.getenv('SESSION_FILE', 'parser.session')
SKIP_AUTH = os.getenv('SKIP_AUTH', '').lower() == 'true'

# Ensure session directory exists and has proper permissions
session_dir = os.path.dirname(SESSION_FILE) if os.path.dirname(SESSION_FILE) else '.'
if not os.path.exists(session_dir):
    os.makedirs(session_dir, exist_ok=True)
# =======================

app   = Flask(__name__)
client = TelegramClient(SESSION_FILE, API_ID, API_HASH)

def fetch_messages():
    """Возвращает список транзакций из двух групп."""
    try:
        if not client.is_connected():
            client.start(phone=PHONE)   # первый раз запросит код
    except Exception as e:
        print(f"Auth error: {e}")
        return []  # return empty list on auth failure

    rows = []
    try:
        # 1) расходная группа
        for msg in client.iter_messages(GROUP_EXP, limit=100):
            numbers = re.findall(r'\d+', msg.text or '')
            amount = int(numbers[-1]) if numbers else 0
            rows.append({
                'date': msg.date.isoformat(),
                'type': 'expense',
                'amount': amount,
                'desc': (msg.text or '')[:60]
            })
    except Exception as e:
        print(f"Error fetching expense group {GROUP_EXP}: {e}")
    try:
        # 2) приходная группа
        for msg in client.iter_messages(GROUP_INC, limit=100):
            numbers = re.findall(r'\d+', msg.text or '')
            amount = int(numbers[-1]) if numbers else 0
            rows.append({
                'date': msg.date.isoformat(),
                'type': 'income',
                'amount': amount,
                'desc': (msg.text or '')[:60]
            })
    except Exception as e:
        print(f"Error fetching income group {GROUP_INC}: {e}")
    # сортируем новые сверху
    rows.sort(key=lambda x: x['date'], reverse=True)
    return rows

@app.route('/api/transactions')
def api():
    """Отдаёт JSON транзакций."""
    data = fetch_messages()
    return jsonify(data)

@app.route('/api/update_groups', methods=['POST'])
def update_groups():
    global GROUP_EXP, GROUP_INC
    data = request.get_json()
    GROUP_EXP = data['expense']
    GROUP_INC = data['income']
    return jsonify({'status': 'ok'})

@app.route('/')
def index():
    """Отдаёт статический Mini App."""
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=8080, debug=False, threaded=False)
