from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
from Fetch_papers import fetch_arxiv_papers
from summarise import summarize_paper

# Bot Token from BotFather
TOKEN = "7772645711:AAEnhKnUnixACtkfr3hNB1mPGrebQlXx0uY"

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Hello! I am your Research Assistant bot. Send /research <query> to get paper summaries.")

async def research(update: Update, context: CallbackContext):
    query = " ".join(context.args)
    papers = fetch_arxiv_papers(query)
    
    if papers:
        summary = summarize_paper(papers)  # Summarize the fetched papers
        await update.message.reply_text(summary)
    else:
        await update.message.reply_text("No research papers found for your query.")

def main():
    # Use Application instead of Updater
    app = Application.builder().token(TOKEN).build()

    # Add handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("research", research))

    # Start the bot
    app.run_polling()

if __name__ == "__main__":
    main()
