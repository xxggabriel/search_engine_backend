import aioredis
from app import app

redis_pool = None


@app.on_event("startup")
async def startup_event():
    global redis_pool
    redis_pool = await aioredis.create_redis_pool(
        address=('192.168.99.100', 30379),
        db=0,
        password='mypassword'
    )


@app.on_event("shutdown")
async def shutdown_event():
    redis_pool.close()
    await redis_pool.wait_closed()


async def get_value(key: str):
    async with redis_pool as conn:
        value = await conn.get(key, encoding='utf-8')  # Encoding argument
    return value
