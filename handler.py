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

class Sub(StatesGroup):
    roll = State()

@router.message(Command('start'))
async def start_msg(message: Message, state: FSMContext):
    if await state.get_state():
        return
    await message.reply('Здрав-в-вствуйте! А можно нажать на кнопио?', reply_markup=kb.io)
    await state.set_state(Sub.roll)

@router.message(Sub.roll)
async def roll_handler(message: Message, state: FSMContext):
    if message.text == '🎰 Крутить барабан':
        await message.answer_sticker(sticker='CAACAgIAAxkBAAEHyodq2zHRXaX36umlTfkqgvrFidlgewACgl4AArtjoUvknEjrSOpYhT0E')
        await message.answer('Вращаю барабанио....')
        time.sleep(3)
        await message.reply(random.choice(students),reply_markup=kb.io)
        return
        





