from telethon import TelegramClient, events

# O'z Telegram akkauntingiz uchun API ID va API HASH
api_id = 22624543  # O'zingizning API ID
api_hash = "aa6be2a7642de167481c86e92834277a"  # O'zingizning API HASH

client = TelegramClient("session_name", api_id, api_hash)

# Kuzatilayotgan kanal ID'si
source_channel = -1002331884910  # Begona kanal ID'si (uni @username_to_id_bot orqali toping)

# Post izohiga avtomatik javob yozish
@client.on(events.NewMessage(chats=source_channel))
async def comment_handler(event):
    if event.is_channel and event.message:  # Faqat kanal postlarini tekshirish
        try:
            post_id = event.message.id  # Postning ID'sini olish
            comment_text = "🗿 Kanal yaxshi ekan, menga yoqdi, fikringiz qanday?"
            
            # Postning izoh bo‘limiga yozish
            await client.send_message(source_channel, comment_text, comment_to=post_id)
            
            print(f"✅ Postga izoh yozildi: {post_id}")
        
        except Exception as e:
            print(f"⚠️ Xatolik: {e}")

async def main():
    await client.start()
    print("✅ Bot ishlamoqda (Admin bo‘lmay)...")
    await client.run_until_disconnected()

client.loop.run_until_complete(main())
