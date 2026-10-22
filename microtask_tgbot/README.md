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