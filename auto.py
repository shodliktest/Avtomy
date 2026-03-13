import os
import asyncio
import random
from telethon import TelegramClient
from telethon.sessions import StringSession

# GitHub Secrets
api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]
session_str = os.environ["SESSION"]
alert_chat = os.environ.get("ALERT_CHAT", "Otavaliyev_M")
event_name = os.environ.get("EVENT_NAME", "") # Qanday ishga tushgani

targets = [
    "Transcript_robot", "SHodlikAIbot", "Hammaga_javobot", 
    "Longmanrobot", "teacher_tutorbot", "TTSpro_robot", "Otavaliyev_M"
]

words = [
    "salom", "qalaysiz", "ishlar yaxshimi", "hello", "hi", "test", "ping", 
    "start", "ok", "SHodlik", "run", "python", "telegram", "bot", "coding", 
    "uzbekistan", "tashkent", "quyosh", "osmon", "kitob", "ilm", "omad"
]

intervals = [0, 2, 0, 1, 3, 0]

client = TelegramClient(StringSession(session_str), api_id, api_hash)

async def send_alert(msg):
    try:
        await client.send_message(alert_chat, f"🚨 MUAMMO YUZ BERDI:\n\n{msg}")
    except Exception as e:
        print(f"Alert yuborishda xato: {e}")

async def main():
    try:
        await client.start()
        
        # QANDAY ISHGA TUSHGANINI TEKSHIRISH
        if event_name == "workflow_dispatch":
            wait_min = 0
            print("⚡️ Qo'lda ishga tushirildi: Kutish bekor qilindi, darhol xabar yuboriladi!")
        else:
            wait_min = random.choice(intervals)
            print(f"⏳ Avtomatik ishga tushdi: {wait_min} daqiqa kutish boshlandi...")
            
        await asyncio.sleep(wait_min * 60)

        for target in targets:
            random_word = random.choice(words)
            try:
                await client.send_message(target, random_word)
                print(f"✅ {target} ga '{random_word}' yuborildi.")
                # Spam himoyasi
                await asyncio.sleep(random.randint(5, 10))
            except Exception as e:
                err_msg = f"{target} ga yuborishda xato: {str(e)}"
                print(f"❌ {err_msg}")
                await send_alert(err_msg)

    except Exception as e:
        await send_alert(f"Bot butunlay to'xtadi: {str(e)}")
    finally:
        await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
    


