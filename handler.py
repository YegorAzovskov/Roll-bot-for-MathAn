import time
import asyncio
import sqlite3
from aiogram import F, Router, Bot, types
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery ,FSInputFile
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from config import token
import keyboard as kb
from datetime import datetime, timedelta
import random

students = [
    "Азовсков Егор",
    "Гаев Валерий",
    "Григорьев Александр",
    "Дружинин Георгий",
    "Заводчиков Сергей",
    "Кадиров Артём",
    "Кисунько Глеб",
    "Кондратьева Оксана",
    "Краснов Лука",
    "Лаптев Игорь",
    "Любушкин Александр",
    "Макаренков Константин",
    "Маковоз Дмитрий",
    "Максименко Кирилл",
    "Медведева Ольга",
    "Муртазин Тимерлан",
    "Скорик Артём",
    "Таксатов Иван",
    "Тимошенко Никита",
    "Ткаченков Максим",
    "Токарева Полина",
    "Хайдарова Дарина",
    "Черных Кирилл"

]
print(len(students))

bot = Bot(token)
router = Router()


cooldowns = {} 


class Form(StatesGroup):
    roll = State()
    cooldown_state = State()

@router.message(Command('start'))
async def start_msg(message: Message, state: FSMContext):
    if await state.get_state():
        return
    await message.reply('Здрав-в-вствуйте! А можно нажать на кнопио?', reply_markup=kb.io)


@router.message(F.text == '🎰 Крутить барабан')
async def roll_handler(message: Message, state: FSMContext):
    await state.set_state(Form.roll)

    sleep_time = 60
    user_id = message.from_user.id

    if message.text == '🎰 Крутить барабан':
        await message.answer_sticker(sticker='CAACAgIAAxkBAAEHyodq2zHRXaX36umlTfkqgvrFidlgewACgl4AArtjoUvknEjrSOpYhT0E')
        sent_msg = await message.answer('Вращаю барабанио....')
        time.sleep(5)
        await sent_msg.delete()
        
        await message.reply(random.choice(students))
        time.sleep(2)
        await message.reply(f'Следующий прокрут вы сможете сделать через {sleep_time} секунд.')
        asyncio.create_task(notify_user_after_cooldown(user_id,state,sleep_time))
        cooldowns[user_id] = datetime.now() + timedelta(seconds=sleep_time)
        await state.set_state(Form.cooldown_state)
        
@router.message(Form.cooldown_state)
async def cd(message: Message, state: FSMContext):
    if message:
        user_id = message.from_user.id
        if user_id in cooldowns and cooldowns[user_id] > datetime.now():
            remaining_time = (cooldowns[user_id] - datetime.now()).seconds
            await message.reply(f'Следующий прокрут вы сможете сделать через {remaining_time} секунд.')
            return


    

async def notify_user_after_cooldown(user_id: int, state: FSMContext,sleep_time):
    
    await asyncio.sleep(sleep_time)
    if user_id in cooldowns and datetime.now() >= cooldowns[user_id]:
        del cooldowns[user_id]  
        try:
            await bot.send_message(user_id, "Вы снова можете сделать прокрут",reply_markup=kb.io)
        except Exception as e:
            print(f"Ошибка отправки сообщения {user_id}: {e}")
            await bot.send_message(user_id, "Вы снова можете сделать прокрут!",reply_markup=kb.io)

    
    await state.clear()





