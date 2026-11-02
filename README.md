<div align="center">

# 🎰 Roll Bot for MathAn

**Telegram-бот, который случайным образом выбирает студента из списка группы**

[![Telegram](https://img.shields.io/badge/Telegram-@Math__An__bot-26A5E4?logo=telegram&logoColor=white)](https://t.me/Math_An_bot)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![aiogram](https://img.shields.io/badge/aiogram-3.x-2CA5E0)](https://docs.aiogram.dev/)

[**👉 Открыть бота**](https://t.me/Math_An_bot)

</div>

---

## 📖 О проекте

Бот нужен для честного выбора случайного студента. Нажимаете кнопку, бот «крутит барабан» и называет случайное имя из списка группы.

## 🚀 Как пользоваться

1. Откройте бота: [@Math_An_bot](https://t.me/Math_An_bot)
2. Отправьте команду `/start`
3. Нажмите кнопку **🎰 Крутить барабан**




## 👥 Участники розыгрыша

В барабане **23 студента** группы 6345:

<details>
<summary><b>Показать список</b></summary>

<br>

| № | Студент | № | Студент |
|:-:|---------|:-:|---------|
| 1 | Азовсков Егор | 13 | Маковоз Дмитрий |
| 2 | Гаев Валерий | 14 | Максименко Кирилл |
| 3 | Григорьев Александр | 15 | Медведева Ольга |
| 4 | Дружинин Георгий | 16 | Муртазин Тимерлан |
| 5 | Заводчиков Сергей | 17 | Скорик Артём |
| 6 | Кадиров Артём | 18 | Таксатов Иван |
| 7 | Кисунько Глеб | 19 | Тимошенко Никита |
| 8 | Кондратьева Оксана | 20 | Ткаченков Максим |
| 9 | Краснов Лука | 21 | Токарева Полина |
| 10 | Лаптев Игорь | 22 | Хайдарова Дарина |
| 11 | Любушкин Александр | 23 | Черных Кирилл |
| 12 | Макаренков Константин | | |

</details>




## 🧩 Как это работает

```python
@router.message(Sub.roll)
async def roll_handler(message: Message, state: FSMContext):
    if message.text == '🎰 Крутить барабан':
        await message.answer_sticker(sticker='...')
        await message.answer('Вращаю барабанио....')
        time.sleep(3)
        await message.reply(random.choice(students), reply_markup=kb.io)
```




## 👤 Автор

**Егор Азовсков**: [@YegorAzovskov](https://github.com/YegorAzovskov)

---

<div align="center">

Сделано для группы 6345

</div>
