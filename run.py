import asyncio
from aiogram.fsm.storage.memory import MemoryStorage


from config import token
from aiogram import Bot, Dispatcher
from handler import router

bot = Bot(token)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

    
async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
