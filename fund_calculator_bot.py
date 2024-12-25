import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes

# Function to calculate fund table and total money
def calculate_fund_with_total(initial_investment, levels, multiplier):
    fund_table = []
    total_money = 0
    current_fund = initial_investment

    for level in range(1, levels + 1):
        fund_table.append(f"Level {level}: {current_fund} Rs")
        total_money += current_fund
        current_fund *= multiplier

    table_output = "\n".join(fund_table)
    return table_output, total_money

# Function to save user data
def save_user_data(user_id, initial_investment, levels, multiplier):
    with open("user_data.txt", "a") as file:
        file.write(f"{user_id},{initial_investment},{levels},{multiplier}\n")

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to the Investment Bot! Here’s what you can do:\n\n"
        "/help - Get instructions on how to use the bot\n"
        "/multiplier - Choose a multiplier using buttons\n"
        "Or send your input in this format:\n\n"
        "<starting_amount> <levels> <multiplier>\n\n"
        "Example: 10 5 3", parse_mode="Markdown"
    )

# Help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Here are the commands you can use:\n\n"
        "/start - Start the bot\n"
        "/help - Get instructions\n"
        "/multiplier - Choose a multiplier using buttons\n\n"
        "You can also send your input in this format:\n\n"
        "<starting_amount> <levels> <multiplier>\n\n"
        "Example: 10 5 3"
    )

# Message handler for calculation
async def calculate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user_input = update.message.text.split()
        if len(user_input) != 3:
            raise ValueError("Invalid input format!")

        initial_investment = float(user_input[0])
        levels = int(user_input[1])
        multiplier = float(user_input[2])

        if initial_investment <= 0 or levels <= 0 or multiplier <= 0:
            await update.message.reply_text("Error: All values must be positive numbers.")
            return

        table, total_money = calculate_fund_with_total(initial_investment, levels, multiplier)
        save_user_data(update.message.chat_id, initial_investment, levels, multiplier)

        await update.message.reply_text(
            f"Investment Table:\n\n{table}\n\n"
            f"Total Money Required: {total_money} Rs"
        )

    except Exception as e:
        await update.message.reply_text(f"An error occurred: {str(e)}")

# Inline keyboard for multiplier selection
async def choose_multiplier(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Multiplier: 2", callback_data="2")],
        [InlineKeyboardButton("Multiplier: 3", callback_data="3")],
        [InlineKeyboardButton("Multiplier: 5", callback_data="5")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Choose a multiplier:", reply_markup=reply_markup)

# Callback handler for button clicks
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    multiplier = float(query.data)
    context.user_data["multiplier"] = multiplier
    await query.edit_message_text(f"You selected multiplier: {multiplier}\n\n"
                                  "Now send input in the format:\n"
                                  "<starting_amount> <levels>")

# Main function
if __name__ == "__main__":
    TOKEN = "7767628970:AAEBt1HnJm1SusTJ-NTXHqqGlJYi0S0rgx0"  # Replace with your actual token
    PORT = os.getenv("PORT", 5000)  # Default to 5000 if PORT is not set

    # Create the Application instance with the provided token
    app = ApplicationBuilder().token(TOKEN).build()

    # Add handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("multiplier", choose_multiplier))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, calculate))

    # Start the webhook to listen on the correct port
    app.run_webhook(listen="0.0.0.0", port=int(PORT))
