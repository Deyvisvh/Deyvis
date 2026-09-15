from fastapi import FastAPI, Request
import httpx, os
app = FastAPI()
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    msg = data.get("message", str(data))
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": f"🚨 ALERTA 🚨\n\n{msg}"}
    async with httpx.AsyncClient() as client:
        await client.post(url, json=payload)
    return {"ok": True}
@app.get("/")
async def home():
    return {"status": "ok"}
