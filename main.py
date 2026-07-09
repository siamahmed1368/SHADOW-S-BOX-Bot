"""
Shadow's Box Bot — main.py
Production-ready | pyTelegramBotAPI | Python 3
"""

import telebot
from telebot.types import (
    ChatMemberUpdated,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from keep_alive import keep_alive

# ══════════════════════════════════════════════
#  Configuration
# ══════════════════════════════════════════════
TOKEN      = "8569070620:AAFtpPX-BFsAwcd8_OgJJ_SuQky40-_cmx8"
ADMIN_ID   = 8239921711
ADMIN_PASS = "siam123"
OWNER_USER = "@devil1111000"

DISCUSSION_GROUP = -1003301200964
PAYMENT_GROUP    = -1003964578696
MAIN_GROUP       = -1003510861203

DISCUSSION_LINK = "https://t.me/+KEZuXNU7a31iNDg1"
PAYMENT_LINK    = "https://t.me/+066jiPs3Z7Y5Mzc1"
MAIN_LINK       = "https://t.me/+ms4EzkABlqs3Njdl"

# ══════════════════════════════════════════════
#  Bot initialisation
# ══════════════════════════════════════════════
bot = telebot.TeleBot(TOKEN, parse_mode="Markdown")

# Tracks unique users who interacted with the bot
joined_users: set[int] = set()

# Admin signature appended to every message
ADMIN_SIG = (
    "\n\n👑   *Official Admins:*\n"
    "• @Hunter11110001\n"
    "• @refreshaccount\\_shadow"
)


def display_name(user) -> str:
    """Return a clean full name for a user object."""
    first = (user.first_name or "").strip()
    last  = (user.last_name  or "").strip()
    return f"{first} {last}".strip() or "Unknown"


# ══════════════════════════════════════════════
#  /start — VIP welcome with join buttons
# ══════════════════════════════════════════════
@bot.message_handler(commands=["start"])
def cmd_start(message):
    user = message.from_user
    joined_users.add(user.id)

    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton("1️⃣  Discussion Group", url=DISCUSSION_LINK),
        InlineKeyboardButton("2️⃣  Payment Group",    url=PAYMENT_LINK),
    )

    text = (
        f"💎 *Welcome, {display_name(user)}!*\n\n"
        "*To unlock the Main Group, complete both steps:*\n\n"
        "  1️⃣ Join the *Discussion Group*\n"
        "  2️⃣ Join the *Payment Group*\n\n"
        "📲 The *Main Group link* will arrive here automatically once you join.\n\n"
        f"🛡️ Support: *{OWNER_USER}*"
    )

    bot.send_message(message.chat.id, text, reply_markup=markup)


# ══════════════════════════════════════════════
#  /admin — Public info or password login
# ══════════════════════════════════════════════
@bot.message_handler(commands=["admin"])
def cmd_admin(message):
    parts = message.text.strip().split(maxsplit=1)

    if len(parts) == 1:
        text = (
            "🛡️ *Admin Panel*\n\n"
            f"👤 Owner: *{OWNER_USER}*\n\n"
            "_Use_ `/admin <password>` _to authenticate._"
        )
    elif parts[1].strip() == ADMIN_PASS:
        text = "🔐 *Admin Access Granted.*\n\nWelcome back, Admin."
    else:
        text = "❌ *Incorrect password.* Please try again."

    bot.send_message(message.chat.id, text)


# ══════════════════════════════════════════════
#  /stats — Join count dashboard
# ══════════════════════════════════════════════
@bot.message_handler(commands=["stats"])
def cmd_stats(message):
    text = (
        "📊 *Bot Statistics*\n\n"
        f"💎 *Total Users:* `{len(joined_users)}`\n\n"
        "_Shadow's Box Bot_"
    )
    bot.send_message(message.chat.id, text)


# ══════════════════════════════════════════════
#  /help — Command list (also triggers on text "help")
# ══════════════════════════════════════════════
@bot.message_handler(commands=["help"])
@bot.message_handler(func=lambda m: m.text and m.text.strip().lower() == "help")
def cmd_help(message):
    text = (
        "💎 *Bot Commands List* 💎\n\n"
        "🚀 /start — Bot start & Verification\n"
        "🛡️ /admin — Admin contact & Login\n"
        "📊 /stats — Check total join counts\n"
        "❓ /help  — Show this help menu"
    )
    bot.send_message(message.chat.id, text)


# ══════════════════════════════════════════════
#  Admin keyword handler
# ══════════════════════════════════════════════
@bot.message_handler(func=lambda m: m.text and m.text.strip().lower() in [
    "admin", "অ্যাডমিন", "এডমিন"
])
def cmd_admin_keyword(message):
    text = (
        "👑 *Any issues? Contact Admins:*\n\n"
        "• @Hunter11110001\n"
        "• @refreshaccount\\_shadow"
    )
    bot.reply_to(message, text)


# ══════════════════════════════════════════════
#  Hi / Hello keyword handler
# ══════════════════════════════════════════════
@bot.message_handler(func=lambda m: m.text and m.text.strip().lower() in [
    "hi", "hello", "হাই", "হ্যালো", "হেলো"
])
def cmd_hi(message):
    text = (
        "👋 *ঐ মিয়া, শুধু 'Hi' 'Hello' দিয়ে ভাব মারলে হবে?*\n\n"
        "কথা সোজা, প্রিমিয়াম সার্ভিস লাগলে বলো, আর চ্যাট করতে চাইলে "
        "বক্সে ঝড় তোলো\\! ফাও পিনিক নিবা না। 🤫\n\n"
        "👑 *Official Admins:*\n\n"
        "• @Hunter11110001\n"
        "• @refreshaccount\\_shadow"
    )
    bot.reply_to(message, text)


# ══════════════════════════════════════════════
#  Inbox keyword handler
# ══════════════════════════════════════════════
@bot.message_handler(func=lambda m: m.text and any(
    word in m.text.lower() for word in ["inbox", "ইনবক্স", "dm", "নক"]
))
def cmd_inbox(message):
    text = (
        "🚨 *ইনবক্সের কথা কে বলল রে??*\n\n"
        "সাবধান\\! আমাদের কোনো অ্যাডমিন আগে ইনবক্স \\(DM\\) করে না\\। "
        "কেউ যদি নিজে থেকে আগে নক দিয়ে সার্ভিস বেচতে চায়, তাইলে বুঝবা "
        "ওটা চোর \\(Scammer\\)\\! 🚫\n\n"
        "👑 *আসল খলিফাদের আইডি এখানে:*\n\n"
        "• @Hunter11110001\n"
        "• @refreshaccount\\_shadow"
    )
    bot.reply_to(message, text)


# ══════════════════════════════════════════════
#  Free keyword handler
# ══════════════════════════════════════════════
@bot.message_handler(func=lambda m: m.text and any(
    word in m.text.lower() for word in ["free", "ফ্রি", "ফ্রী"]
))
def cmd_free(message):
    text = (
        "🚫 *ফ্রি? ভাইরে ভাই, দুনিয়ায় বাতাস ছাড়া ফ্রি কিছু আছে?*\n\n"
        "এখানে সব সার্ভিস প্রিমিয়াম আর পেইড\\! ফ্রি চাহিয়া লজ্জা দিবেন না "
        "এবং নিজেকেও লজ্জিত করিবেন না। 💸\n\n"
        "👑 *টাকা রেডি থাকলে নক দাও:*\n\n"
        "• @Hunter11110001\n"
        "• @refreshaccount\\_shadow"
    )
    bot.reply_to(message, text)


# ══════════════════════════════════════════════
#  Chat Member Handler — join / leave detection
# ══════════════════════════════════════════════
@bot.chat_member_handler()
def on_chat_member(update: ChatMemberUpdated):
    old = update.old_chat_member.status
    new = update.new_chat_member.status
    user    = update.new_chat_member.user
    chat_id = update.chat.id

    active   = {"member", "administrator", "creator"}
    inactive = {"left", "kicked", "banned", "restricted"}

    just_joined = old in inactive and new in active
    just_left   = old in active   and new in inactive

    if chat_id not in (DISCUSSION_GROUP, PAYMENT_GROUP):
        return

    group_label = "Discussion" if chat_id == DISCUSSION_GROUP else "Payment"

    # ── User joined → DM the Main Group link ────────────
    if just_joined:
        joined_users.add(user.id)
        try:
            bot.send_message(
                user.id,
                f"Hi, *{display_name(user)}*\\!\n\n"
                f"⚡ *WELCOME TO SHADOW'S BOX CHAT* ⚡\n"
                f"Your trusted platform for Premium Paid Services\\! 🚀\n\n"
                f"⚠️ *Warning:* Beware of scammers\\. Check usernames carefully before dealing\\. "
                f"We never DM first\\!\n\n"
                f"🔗 *Main Group:* {MAIN_LINK}"
                + ADMIN_SIG
            )
        except Exception:
            pass  # User has DMs disabled

    # ── User left → DM goodbye, ban from Main + report to admin ─────
    elif just_left:
        username = f"@{user.username}" if user.username else "_none_"
        ban_ok   = True

        # Send goodbye DM to the user
        try:
            bot.send_message(
                user.id,
                f"👋 *GOOD BYE, {display_name(user)}\\!*\n"
                "FROM SHADOW'S BOX CHAT 👋\n\n"
                "গ্রুপ থেকে চলে যাওয়ার জন্য ধন্যবাদ\\! আশা করি আমাদের প্রিমিয়াম সার্ভিস "
                "এবং চ্যাট আপনার ভালো লেগেছে।\n\n"
                "👑 *Any issues? Contact Admins:*\n\n"
                "• @Hunter11110001\n"
                "• @refreshaccount\\_shadow\n\n"
                "Take care and see you again\\! ✨"
            )
        except Exception:
            pass  # User has DMs disabled

        try:
            bot.ban_chat_member(MAIN_GROUP, user.id)
        except Exception as err:
            ban_ok = False
            bot.send_message(ADMIN_ID, f"⚠️ *Ban failed:* `{err}`")

        status_line = "*Banned from Main*" if ban_ok else "*Ban failed — action needed*"

        # Photo + caption report
        caption = (
            "🚨 *SECURITY ALERT*\n\n"
            f"👤 *Name:* {display_name(user)}\n"
            f"🆔 *ID:* {user.id}\n"
            f"🛡️ *Status:* *Banned from Main*"
        )

        photo_sent = False
        try:
            photos = bot.get_user_profile_photos(user.id, limit=1)
            if photos and photos.photos:
                file_id = photos.photos[0][-1].file_id  # highest resolution
                bot.send_photo(ADMIN_ID, file_id, caption=caption)
                photo_sent = True
        except Exception:
            pass

        # Fallback: text-only report if no photo
        if not photo_sent:
            bot.send_message(ADMIN_ID, caption)


# ══════════════════════════════════════════════
#  Entry point
# ══════════════════════════════════════════════
if __name__ == "__main__":
    keep_alive()
    print("━" * 40)
    print("  💎 Shadow's Box Bot — ONLINE")
    print("━" * 40)
    bot.infinity_polling(
        allowed_updates=["message", "chat_member"],
        timeout=30,
        long_polling_timeout=30,
    )
