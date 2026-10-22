# MicroTask TG Bot

A Telegram bot for managing daily microtasks with statistics and scheduling capabilities.

## Features

- Daily microtask goals
- Task completion tracking
- Statistics collection
- User menu system

## Installation

1. Clone the repository
2. Install dependencies using poetry:
   ```bash
   poetry install
   ```
3. Create `.env` file with bot token and database URL
4. Run the bot:
   ```bash
   poetry run python -m microtask_tgbot
   ```

## Configuration

The bot requires a `.env` file with the following variables:
- `BOT_TOKEN`: Telegram bot API token
- `DB_URL`: PostgreSQL database connection URL

Example `.env`:
```
BOT_TOKEN=8932673646:AAH_peJ8ugnvLTtXL7-ep0FP9nY6D4DII3E
DB_URL=postgresql+asyncpg://neondb_owner:npg_egvxPqXI96oy@ep-hidden-violet-b40f8eq8-pooler.c-6.us-east-2.aws.neon.tech/microtask_bot_db
```