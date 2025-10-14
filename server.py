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
API_ID       = int(os.getenv('API_ID', 'Ваш API_ID'))
API_HASH     = os.getenv('API_HASH', 'Ваш API_HASH')
PHONE        = os.getenv('PHONE', '+71234567890')
GROUP_EXP    = int(os.getenv('GROUP_EXP', '-4731002756'))   # расход
GROUP_INC    = int(os.getenv('GROUP_INC', '-4829787389'))   # приход
SESSION_FILE = 'parser.session'
# =======================

app   = Flask(__name__)
client = TelegramClient(SESSION_FILE, API_ID, API_HASH)

def fetch_messages():
    """Возвращает список транзакций из двух групп."""
    if not client.is_connected():
        client.start(phone=PHONE)   # первый раз запросит код
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
