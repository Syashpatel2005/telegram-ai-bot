# payments.py

from db import conn, cur

# Your UPI ID (change this)
UPI_ID = "yourupi@okaxis"

# Premium price
PREMIUM_PRICE = "₹99 / month"


def get_payment_message():
    """
    Message shown to user when they type /premium
    """
    return f"""
💎 *Premium Plan*

Price: {PREMIUM_PRICE}

✅ Unlimited AI chat
✅ No daily limits
✅ Priority access

📌 How to pay:1️⃣ Pay via UPI:
`{UPI_ID}`

2️⃣ Take payment screenshot

3️⃣ Send screenshot to admin

After verification, premium will be activated ✅
"""


def make_user_premium(user_id):
    """
    Admin manually upgrades user
    """
    cur.execute(
        "UPDATE users SET is_premium = 1 WHERE user_id = ?",
        (user_id,)
    )
    conn.commit()
