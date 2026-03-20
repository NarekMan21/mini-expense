# mini-expense

Telegram-based transaction parser with balance tracking and a lightweight web interface.

## What it does
- Reads transaction-style messages from Telegram groups
- Separates income and expense streams
- Builds a simple balance view
- Exposes the data through a small web interface

## Use cases
- personal bookkeeping from Telegram logs
- lightweight finance tracking
- quick dashboards for manual transaction groups

## Setup
Create environment variables from the example file and provide your Telegram API credentials.

```bash
cp .env.example .env
```

Then run either with Docker or locally.

## Run with Docker
```bash
docker-compose up -d
```

## Run locally
```bash
python -m venv .venv
source .venv/bin/activate  # or use Windows activation
pip install -r requirements.txt
python server.py
```

## Important
- Do not commit Telegram API secrets or session files
- Keep session files out of public repositories
- Treat this as a practical personal-finance utility, not a polished banking product

## Screenshots
Add 1-3 screenshots in `docs/images/` and embed them like this:

```md
![Overview](docs/images/overview.png)
![Dashboard](docs/images/dashboard.png)
```

