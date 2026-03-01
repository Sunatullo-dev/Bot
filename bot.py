import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "8533681990:AAFY87MifOKDiui3oaKXUTH4SvUkaCIpRHA"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Главное меню
menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🏢 О компании", callback_data="about"),
        InlineKeyboardButton(text="⚙️ Как работает", callback_data="how")
    ],
    [
        InlineKeyboardButton(text="🔥 Возможности", callback_data="features")
    ],
    [
        InlineKeyboardButton(text="🌐 Открыть сайт", url="https://sunatjan.com")
    ],
    [
        InlineKeyboardButton(text="📞 Поддержка", callback_data="support")
    ]
])

back_button = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="⬅️ Назад в меню", callback_data="menu")]
])

# Стартовое сообщение
@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer_photo(
        photo="https://images.unsplash.com/photo-1556761175-4b46a572b786",
        caption=(
            "👋 Добро пожаловать!\n\n"
            "Это современная платформа для автоматизации бизнеса.\n\n"
            "📈 Управляйте процессами\n"
            "⚡ Экономьте время\n"
            "🚀 Масштабируйте компанию"
        ),
        reply_markup=menu
    )

# Обработка нажатий кнопок
@dp.callback_query()
async def callbacks(call: types.CallbackQuery):

    if call.data == "menu":
        # Главное меню как текстовое сообщение
        await call.message.edit_text(
            "💼 Главное меню\n\nВыберите раздел ниже:",
            reply_markup=menu
        )

    elif call.data == "about":
        await call.message.answer_photo(
            photo="https://images.unsplash.com/photo-1521737604893-d14cc237f11d?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
            caption=(
                "🏢 О нашей компании\n\n"
                "Мы создаем технологии для автоматизации бизнеса.\n"
                "Наша цель — сделать управление компанией простым и быстрым."
            ),
            reply_markup=back_button
        )

    elif call.data == "how":
        await call.message.answer(
            "⚙️ Как работает сервис\n\n"
            "1️⃣ Регистрация на сайте\n"
            "2️⃣ Настройка системы\n"
            "3️⃣ Автоматизация процессов\n"
            "4️⃣ Рост бизнеса 📈",
            reply_markup=back_button
        )

    elif call.data == "features":
        await call.message.answer(
            "🔥 Возможности платформы\n\n"
            "• Автоматизация бизнеса\n"
            "• Управление клиентами\n"
            "• Аналитика\n"
            "• Контроль процессов\n"
            "• Оптимизация работы",
            reply_markup=back_button
        )

    elif call.data == "support":
        await call.message.answer(
            "📞 Поддержка\n\nЕсли возникли вопросы:\n@support_username",
            reply_markup=back_button
        )

    await call.answer()

# Запуск бота
async def main():
    print("Бот запущен 🚀")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())