# Forex Signal Telegram Bot

A powerful, fast, and fully automated Forex signal bot tailored for private use. Built by **@POWERFULDANI**, this bot provides real-time analysis of forex symbols (like EURUSD, GBPUSD, and USDJPY) based on 15-minute swing trading intervals.

---

## Features

- **Swing Trading Analysis** (15-minute timeframe)
- **EMA20-based Technical Indicator**
- **Chart image generation with Matplotlib**
- **Auto Signal Delivery** every 30 minutes
- **Private Bot Access** (only you)
- **Fully Telegram-Integrated**
- **Modular and Clean Python Codebase**

---

## Technologies Used

- Python 3.10+
- `python-telegram-bot`
- TwelveData API
- Pandas, Matplotlib, Requests

---

## Folder Structure

```bash
forex_bot_dani/
├── bot.py                # Main bot logic
├── market_data.py        # API data fetching and charting
├── signal_handler.py     # Telegram messaging utility
├── get_telegram_id.py    # Script to get your numeric Telegram ID
├── requirements.txt      # Python dependencies
├── README.md             # This documentation file
```

---

## Setup Guide

### 1. Clone or Download Project
```bash
git clone https://github.com/YOUR_USERNAME/forex-signal-bot.git
cd forex-signal-bot
```
Or unzip manually if using ZIP:
```bash
unzip forex_bot_dani.zip && cd forex_bot_dani
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Get Your API Keys
- **Telegram Bot Token**: from [@BotFather](https://t.me/BotFather)
- **TwelveData API Key**: from [https://twelvedata.com](https://twelvedata.com)

### 4. Find Your Telegram Numeric ID
Run the helper script:
```bash
python get_telegram_id.py
```
Then message your bot `/start`. It will print and reply with your numeric ID.

### 5. Configure bot.py
Replace the placeholders:
```python
TOKEN = "<Your Bot Token>"
API_KEY = "<TwelveData API Key>"
AUTHORIZED_USER_ID = 123456789
```

### 6. Run the Bot
```bash
python bot.py
```
Bot runs every 30 minutes and responds to commands like:
```
تحلیل EURUSD
تحلیل GBPUSD
```

---

## Hosting Options

### Option 1: Railway (Recommended)

- Go to [railway.app](https://railway.app) and sign in with GitHub
- Create new project → Deploy from GitHub Repo
- Set environment variables:
  ```env
  TOKEN=YourBotToken
  API_KEY=YourTwelveDataKey
  AUTHORIZED_USER_ID=123456789
  ```
- Hit "Deploy"

### Option 2: Replit (Fastest Way to Test)

- Go to [replit.com](https://replit.com)
- Create a new Python project
- Upload all bot files
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```
- Run your bot by clicking **Run** button

---

## Telegram UX Flow

```text
User: /start
Bot: سلام دانی عزیز! آماده‌ام برای تحلیل. بنویس: تحلیل EURUSD

User: تحلیل GBPUSD
Bot: ارسال قیمت، نمودار، سیگنال خرید/فروش با تصویر تحلیلی
```

---

## License
MIT License – free for personal use & customization.

---

## Developed with passion by
**[@POWERFULDANI](https://t.me/POWERFULDANI)**

Code. Trade. Repeat.