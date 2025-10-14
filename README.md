<<<<<<< HEAD
# Telegram Cash Parser

Веб-приложение для парсинга транзакций из Telegram групп и отображения баланса.

## ⚠️ Безопасность

**НИКОГДА не загружайте секретные ключи в публичные репозитории!**

- Создайте файл `.env` на основе `.env.example`
- Добавьте `.env` в `.gitignore`
- Используйте переменные окружения в Render

## Запуск

### Локально
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
=======
# Telegram Cash Parser

Веб-приложение для парсинга транзакций из Telegram групп и отображения баланса.

## Запуск

### Локально
```bash
# Создать виртуальное окружение
python -m venv .venv

# Активировать
.venv\Scripts\activate  # Windows
# или
source .venv/bin/activate  # Linux/Mac

# Установить зависимости
pip install -r requirements.txt

# Запустить сервер (первый раз запросит код Telegram)
python server.py
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
>>>>>>> cba8ccfd8bcae7508b7271bbd90979ee0a11265b
3. **Если сессия сломана**: Удалите файл сессии и пройдите авторизацию заново