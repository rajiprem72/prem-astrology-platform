from fastapi import FastAPI

app = FastAPI(
title="Prem Astrology Platform",
version="1.0.0"
)

@app.get("/")
def home():
return {
"message": "Prem Astrology Platform is running"
}
