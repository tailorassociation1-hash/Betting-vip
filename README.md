# Betting VIP Telegram Bot

Educational sports stats & predictions bot. No real-money gambling.

## Deploy on Railway
1. Push this repo to GitHub.
2. Go to https://railway.app → New Project → Deploy from GitHub.
3. Select this repo.
4. Add environment variables:
   - BOT_TOKEN = <your BotFather token>
   - ADMIN_CONTACT = @YourUsername
5. Deploy. Railway auto-detects the Procfile worker.

## Run locally
pip install -r requirements.txt
export BOT_TOKEN=xxxxx
export ADMIN_CONTACT=@YourUsername
python bot.py
