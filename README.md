# Telegram Cash Parser

Веб-приложение для парсинга транзакций из Telegram групп и отображения баланса.

## ⚠️ Безопасность

**НИКОГДА не загружайте секретные ключи в публичные репозитории!**

- Создайте файл `.env` на основе `.env.example`
- Добавьте `.env` в `.gitignore`
- Используйте переменные окружения в Render

## Запуск

### Docker (рекомендуется)
```bash
# Скопировать переменные окружения
cp .env.example .env
# Отредактируйте .env с вашими реальными данными

# Запустить через Docker Compose
docker-compose up -d

# Посмотреть логи
docker-compose logs -f
```

### Локально без Docker
```bash
# Создать виртуальное окружение
python -m venv .venv

# Активировать
.venv\Scripts\activate  # Windows
# или
source .venv/bin/activate  # Linux/Mac

# Скопировать переменные окружения
cp .env.example .env
# Отредактируйте .env с вашими реальными данными

# Установить зависимости
pip install -r requirements.txt

# Запустить сервер (первый раз запросит код Telegram)
python server.py
```

### Только Docker
```bash
# Собрать образ
docker build -t telegram-cash-app .

# Запустить контейнер
docker run -p 8080:8080 \
  -e API_ID=your_api_id \
  -e API_HASH=your_api_hash \
  -e PHONE=your_phone \
  -e GROUP_EXP=your_expense_group \
  -e GROUP_INC=your_income_group \
  -v $(pwd)/parser.session:/app/parser.session \
  telegram-cash-app
```

### На Render
1. Создать сессию локально: `python server.py` и пройти авторизацию
2. Скопировать `parser.session` как `render.session`
3. Развернуть на Render с `render.yaml`
4. В Render установить `SKIP_AUTH=true` чтобы избежать запроса кода

## Переменные окружения

- `API_ID` - API ID от Telegram
- `API_HASH` - API Hash от Telegram
- `PHONE` - Номер телефона для авторизации
- `GROUP_EXP` - ID группы расходов (отрицательный для групп)
- `GROUP_INC` - ID группы приходов
- `SESSION_FILE` - Имя файла сессии (по умолчанию `parser.session`)
- `SKIP_AUTH` - Пропустить авторизацию если сессия существует

## Решение проблем с сессией

1. **Разные сессии для разных окружений**: Используйте `SESSION_FILE` переменную
2. **Пропуск авторизации в продакшене**: Установите `SKIP_AUTH=true`
3. **Если сессия сломана**: Удалите файл сессии и пройдите авторизацию заново