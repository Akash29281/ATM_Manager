# ATM Manager Pro — Flask UI Integration

The generated HTML designs are now connected to the existing Python/MySQL logic.

## Connected routes
- `/` — Login + PIN verification + 3-attempt account locking
- `/dashboard` — real user/account data + transaction summaries
- `/balance` — live MySQL balance
- `/deposit` — deposits, balance update, transaction log
- `/withdraw` — validation, balance update, transaction log
- `/transfer` — account-number transfer, validation, sender/receiver updates, logs
- `/history` — live transaction history with dates and search
- `/change_pin` — current/new/confirm PIN validation
- `/logout` — session clear

## Important
The UI uses Tailwind via CDN, so internet access is needed for the styling CDN while developing.

Run:

```powershell
pip install -r requirements.txt
python app.py
```

Then open `http://127.0.0.1:5000`.
