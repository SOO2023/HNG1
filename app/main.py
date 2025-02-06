from fastapi import FastAPI
from httpx import AsyncClient
from fastapi.responses import JSONResponse
from app.util import is_prime, is_perfect, get_property, digit_sum
from app.schemas import NumberInfoRead, ErrorRead
from apscheduler.schedulers.background import BackgroundScheduler
from app.cron_job import keep_alive


app = FastAPI()
scheduler = BackgroundScheduler()
scheduler.add_job(keep_alive, "interval", minutes=5)
scheduler.start()


@app.get("/api/classify-number", response_model=NumberInfoRead | ErrorRead)
async def get_number_info(number):
    async with AsyncClient() as client:
        response = await client.get(f"http://numbersapi.com/{number}/math?json=true")
        if response.status_code == 200:
            number = int(number)
            return NumberInfoRead(
                number=number,
                is_prime=is_prime(number),
                is_perfect=is_perfect(number),
                properties=get_property(number),
                digit_sum=digit_sum(number),
                fun_fact=response.json()["text"],
            )
        return JSONResponse(
            content=ErrorRead(number="alphabet", error=True).model_dump(),
            status_code=400,
        )
