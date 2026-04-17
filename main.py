import os
import discord
from flask import Flask
from threading import Thread

# Discord bot setup
intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

# Flask server (voor Render)
app = Flask('')

@app.route('/')
def home():
    return "Bot draait!"

def run():
    port = int(os.environ.get("PORT", 10000))  # 🔥 BELANGRIJK
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()

# Start alles
keep_alive()
client.run(os.getenv("TOKEN"))
