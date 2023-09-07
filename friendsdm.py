import discord # pip install discord
import asyncio #bu modül hali hazırda pcnizde mevcuttur bu modülün amacı rate limit için kodu bekletmeye yarar.

TOKEN = 'hesap-token'

client = discord.Client()

async def get_friends(): #friends fonksiyonunu tanıttık
    friends = await client.http.get_relationships()
    return [rel['user'] for rel in friends if rel['type'] == 1] #burdada discord modülünden http isteğiyle arkadaş listenizi çekip dm atmak için hazır hale getiriyor yani user olarak koda tanıtıyor

@client.event
async def on_ready():
    print(f'{client.user} girildi') #hesabınızı gösteren kısım
    friends = await get_friends()
    total_friends = len(friends)
    print(f"Toplam arkadaşınız: {total_friends}") # toplam arkaadaşları gosterıor
    estimated_time = total_friends * 2
    print(f"Tahmini bitiş süresi: {estimated_time} saniye.")
    for user_info in friends:
        user = await client.fetch_user(user_info['id']) #burada kullanıcıların idlerini dm atması için düüzenliyor.
        try:
            await user.send('Merhaba bugun nasılsın?') #burada user.send komutu ile friendsden çeken kullanıcılara modül aracılığı ile dm atıyor.
            print(f"{user.name} gönderildi")
        except Exception as e:
            print(f"{user.name} bu kullanıcıda herhangi bir dm olmadığından captcha yedi ;/: {e}")
        await asyncio.sleep(2)  #2 saniyede bir mesaj gönderiyoruz.

client.run(TOKEN)