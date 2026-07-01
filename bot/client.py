import os
from dotenv import load_dotenv
from binance.client import Client

load_dotenv()

client = Client(
    os.getenv("API_KEY"),
    os.getenv("SECRET_KEY")
)

client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"