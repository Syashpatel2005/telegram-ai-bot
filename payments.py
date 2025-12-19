# ==============================
# payments.py
# ==============================

from db import conn, cur

UPI_ID = "yashpatel14082005-3@okhdfcbank"   # CHANGE THIS
PREMIUM_PRICE = "₹99 / month"


def get_payment_message():
    return f"""
💎 *Premium Plan*

Price: {PREMIUM_PRICE}

✅ Unlimited AI chat
✅ No daily limits

📌 How to pay:
1️⃣ Pay via UPI:
`{UPI_ID}`

2️⃣ Send payment screenshot to admin

Premium will be activated after verification ✅
"""


def make_user_premium(user_id):
    cur.execute(
        "UPDATE users SET is_premium = 1 WHERE user_id=?",
        (user_id,)
    )
    conn.commit()
