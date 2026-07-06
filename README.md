# mini-expense

Telegram-based transaction parser with balance tracking and a lightweight web interface.

This project is a practical automation tool for turning messy Telegram finance messages into a structured income/expense view.

## Problem

Small businesses and personal projects often track money in Telegram chats: payments, expenses, cash movements, deliveries, purchases, and short notes.

That data is useful, but it is usually unstructured. It is hard to answer simple questions quickly:

- How much came in?
- How much was spent?
- What is the current balance?
- Which messages are income and which are expenses?
- What happened during a specific period?

## Solution

`mini-expense` reads transaction-style Telegram messages, parses them into structured records, and shows the result in a lightweight web interface.

## What it does

- Reads transaction-style messages from Telegram groups
- Separates income and expense streams
- Builds a simple balance view
- Exposes the data through a small web interface
- Can be used as a base for business cash-flow tracking

## Example use cases

- Personal bookkeeping from Telegram logs
- Small business cash-flow tracking
- Quick dashboard for manual transaction groups
- Parsing messy finance notes into structured data
- Creating reports from chat-based accounting

## Architecture

```text
Telegram messages
   ↓
Parser / extraction logic
   ↓
Structured transactions
   ↓
Local storage
   ↓
Web dashboard
   ↓
Reports / balance view
```

## Stack

- Python
- Telegram API / Telegram client libraries
- Lightweight web server
- HTML templates / browser interface
- Docker / Docker Compose

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

## Important security notes

- Do not commit Telegram API secrets or session files
- Keep session files out of public repositories
- Treat exported chat data as private information
- Use anonymized/demo data for public screenshots
- Treat this as a practical finance utility, not a polished banking product

## Why this project matters

This project shows how automation can turn real business mess into usable data.

It demonstrates:

- parsing unstructured messages
- building a small internal dashboard
- working with Telegram data flows
- transforming manual finance tracking into a repeatable process
- creating practical business tools quickly

## Next improvements

- [ ] Add anonymized sample data
- [ ] Add dashboard screenshots
- [ ] Add CSV export
- [ ] Add monthly summary report
- [ ] Add category detection
- [ ] Add simple charts
- [ ] Add tests for parser examples

## Screenshots

Add 1-3 screenshots in `docs/images/` and embed them like this:

```md
![Overview](docs/images/overview.png)
![Dashboard](docs/images/dashboard.png)
```

## Target portfolio roles

This project supports portfolio positioning for:

- AI Automation Engineer
- Internal Tools Developer
- Technical Product Engineer
- Business Automation Consultant
