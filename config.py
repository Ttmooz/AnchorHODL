import os

mnemonic = os.environ.get('MNEMONIC', 'Terra1sk4zynpcaadkzyg2qq2yhhls34k0mhxgtrnqjv')
target_percent = 35
trigger_at_percent = 50

# (True or False)
enabled_auto_borrow = False
auto_borrow_at_percent = 30
NETWORK = 'MAINNET'

# NOTIFICATIONS (True or False)
NOTIFY_SLACK = False
NOTIFY_TELEGRAM = True

TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN', 'paste your access token here')
TELEGRAM_CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID', 'paste your chat id here')
SLACK_WEBHOOK_URL = os.environ.get('SLACK_WEBHOOK_URL', 'paste your webhook here')

