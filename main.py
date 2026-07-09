"""
Shadow's Box Bot — main.py
Production-ready | pyTelegramBotAPI | Python 3
"""

import telebot
from telebot.types import (
    ChatMemberUpdated,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    BotCommand,
)
from keep_alive import keep_alive

# ══════════════════════════════════════════════
#  Configuration
# ══════════════════════════════════════════════
TOKEN      = "8879720952:AAFx8bT6SvcHwasPM1yQam4Jq0QanpEmhxk"
# Both admins — all reports go to both, both can use /admin
ADMIN_IDS  = [8239921711, 7477336713]   # @Hunter11110001, @refreshaccount_shadow
ADMIN_ID   = ADMIN_IDS[0]              # primary (kept for backward compat)
ADMIN_PASS = "siam123"
OWNER_USER = "@Hunter11110001"
OWNER_USER ="@refreshaccount_shadow"

# Groups to monitor for join/leave
FAKE_PROFILE_GROUP = -1003839550639
CAPTION_BOX_GROUP  = -1004296475096

# Main group (where bans are applied)
DISCUSSION_GROUP   = -1004387391206
MAIN_CHANNEL       = -1004455607053

# Group names
FAKE_PROFILE_NAME  = "Shadow's Box — Fake Profile"
CAPTION_BOX_NAME   = "Shadow's Box — Caption Box"
DISCUSSION_NAME    = "Shadow's Box Chat"

# Links
FAKE_PROFILE_LINK  = "https://t.me/vip_profile_pic_free"
CAPTION_BOX_LINK   = "https://t.me/caption_box_free"
MAIN_CHANNEL       = "https://t.me/shadows_box"
DISCUSSION_LINK    = "https://t.me/+eCgqMOqxeyo0NTE1"
FB_PAGE_LINK       = "https://www.facebook.com/VortexBD.official"

# ══════════════════════════════════════════════
#  Bot initialisation
# ══════════════════════════════════════════════
bot = telebot.TeleBot(TOKEN, parse_mode="Markdown")

# Tracks unique users who interacted with the bot
joined_users: set[int] = set()

# Admin signature appended to every message
ADMIN_SIG = (
    "\n\n👑 *Official Admins:*\n"
    "• @Hunter11110001\n"
    "• @refreshaccount_shadow"
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
        InlineKeyboardButton("🖼️ Fake Profile Group",    url=FAKE_PROFILE_LINK),
        InlineKeyboardButton("✍️ Caption Box",           url=CAPTION_BOX_LINK),
        InlineKeyboardButton("💬 Discussion Group",      url=DISCUSSION_LINK),
        InlineKeyboardButton("⭐  Main Channel",         url=MAIN_CHANNEL),
        InlineKeyboardButton("📘 Facebook Page",         url=FB_PAGE_LINK),
    )

    text = (
        f"💎 *Welcome, {display_name(user)}!*\n\n"
        "*আমাদের সব গ্রুপ ও পেজে যোগ দাও:*\n\n"
        "  🖼️ *Fake Profile Group*\n"
        "  ✍️ *Caption Box*\n"
        "  💬 *Discussion Group*\n"
        "  📘 *Facebook Page*\n\n"
        f"🛡️ Support: *{OWNER_USER}*"
    )

    bot.send_message(message.chat.id, text, reply_markup=markup)


# ══════════════════════════════════════════════
#  /admin — Public info or password login
# ══════════════════════════════════════════════
@bot.message_handler(commands=["admin"])
def cmd_admin(message):
    # Only admins can use this command
    if message.from_user.id not in ADMIN_IDS:
        bot.reply_to(message, "🚫 *এই command টি শুধু Admin ব্যবহার করতে পারবে।*")
        return

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

    if chat_id not in (FAKE_PROFILE_GROUP, CAPTION_BOX_GROUP, DISCUSSION_GROUP):
        return

    if chat_id == FAKE_PROFILE_GROUP:
        group_label = FAKE_PROFILE_NAME
    elif chat_id == CAPTION_BOX_GROUP:
        group_label = CAPTION_BOX_NAME
    else:
        group_label = DISCUSSION_NAME

    # ── User joined → DM the Discussion Group link ───────
    if just_joined:
        joined_users.add(user.id)
        try:
            bot.send_message(
                user.id,
                f"Hi, *{display_name(user)}*\n\n"
                f"⚡ *WELCOME TO {group_label.upper()}* ⚡\n"
                f"Your trusted platform for Premium Paid Services 🚀\n\n"
                f"🔗 *আমাদের সব লিংক:*\n\n"
                f"🖼️ *{FAKE_PROFILE_NAME}:* {FAKE_PROFILE_LINK}\n"
                f"✍️ *{CAPTION_BOX_NAME}:* {CAPTION_BOX_LINK}\n"
                f"💬 *{DISCUSSION_NAME}:* {DISCUSSION_LINK}\n"
                f"💬 *{MAIN_CHANNEL_NAME}:* {MAIN_CHANNEL}\n"
                f"📘 *Facebook Page:* {FB_PAGE_LINK}\n\n"
                f"⚠️ Warning: Beware of scammers. Check usernames carefully before dealing. "
                f"We never DM first!"
                + ADMIN_SIG
            )
        except Exception as e:
            for aid in ADMIN_IDS:
                try:
                    bot.send_message(aid, f"⚠️ Welcome DM failed for {display_name(user)} (ID: {user.id})\nError: {e}")
                except Exception:
                    pass

    # ── User left → DM goodbye, ban from Discussion + report to admin ─────
    elif just_left:
        username = f"@{user.username}" if user.username else "_none_"
        ban_ok   = True

        # Send goodbye DM to the user
        try:
            bot.send_message(
                user.id,
                f"👋 *GOOD BYE, {display_name(user)}!*\n"
                f"FROM *{group_label}* 👋\n\n"
                f"গ্রুপ থেকে চলে যাওয়ার জন্য ধন্যবাদ! "
                f"আবার join করতে চাইলে:\n\n"
                f"💬 *{DISCUSSION_NAME}:* {DISCUSSION_LINK}\n\n"
                "👑 *Any issues? Contact Admins:*\n\n"
                "• @Hunter11110001\n"
                "• @refreshaccount_shadow\n\n"
                "Take care and see you again! ✨"
            )
        except Exception as e:
            for aid in ADMIN_IDS:
                try:
                    bot.send_message(aid, f"⚠️ Goodbye DM failed for {display_name(user)} (ID: {user.id})\nError: {e}")
                except Exception:
                    pass

        try:
            bot.ban_chat_member(DISCUSSION_GROUP, user.id)
        except Exception as err:
            ban_ok = False
            for aid in ADMIN_IDS:
                bot.send_message(aid, f"⚠️ *Ban failed:* `{err}`")

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
                for aid in ADMIN_IDS:
                    bot.send_photo(aid, file_id, caption=caption)
                photo_sent = True
        except Exception:
            pass

        # Fallback: text-only report if no photo
        if not photo_sent:
            for aid in ADMIN_IDS:
                bot.send_message(aid, caption)


# ══════════════════════════════════════════════
#  Register bot commands (shown in Telegram menu)
# ══════════════════════════════════════════════
def set_commands():
    bot.set_my_commands([
        BotCommand("start",  "বটের সাথে পরিচিত হও ও সব লিংক দেখো"),
        BotCommand("help",   "কীভাবে বট ব্যবহার করবে"),
        BotCommand("admin",  "Admin দের সাথে যোগাযোগ করো"),
        BotCommand("stats",  "গ্রুপের সদস্য সংখ্যা দেখো"),
    ])


# ══════════════════════════════════════════════
#  Entry point
# ══════════════════════════════════════════════
if __name__ == "__main__":
    keep_alive()
    set_commands()
    print("━" * 40)
    print("  💎 Shadow's Box Bot — ONLINE")
    print("━" * 40)
    bot.infinity_polling(
        allowed_updates=["message", "chat_member"],
        timeout=30,
        long_polling_timeout=30,
    )
