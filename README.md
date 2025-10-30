# Jack Frost Discord Bot

Jack Frost is a multi-purpose Discord bot designed to bring fun and utility to your server. It features an economy system, RPG elements, moderation tools, and various interactive commands.

## Features

*   **Economy System**:
    *   Earn daily "Macca" (the bot's currency).
    *   Gamble with `/adivinhar` and `/aposta`.
    *   Invest `/investir` your Macca for potential gains (or losses!).
    *   Spin the `/roleta` for a chance to win Macca.
    *   `/doar` Macca to other users (with a small tax!).
    *   A `/lojinha` to buy temporary boosts for commands and custom commands.
    *   A `/premium` system for enhanced benefits.
    *   An `/onlyjack` (OnlyFans parody) feature where users can create pages, subscribe, and upload content.
*   **RPG System**:
    *   `/rpg register` to create your character and start your adventure in "Da'at".
    *   `/rpg dungeon` to undertake missions, gain XP, and find loot.
    *   `/rpg status` to view your character's progress, equipped items, and mission count.
    *   `/rpg equipar_arma` and `/rpg equipar_armadura` to manage your gear.
    *   `/rpg guild` to view, create, invite, and manage your guild.
    *   Level up your DHA Rank (Da'at Hunter Association).
*   **Fun & Interaction**:
    *   `/battle` to simulate battles between two concepts.
    *   `/cancelamento` to simulate a "cancellation" event for a user.
    *   `/sabio` for life advice.
    *   `/ppt` to declare your love.
    *   `/jogo` to predict game scores.
    *   `/ship` to calculate compatibility between two people.
    *   `/ppp` (Pego, Penso, Passo) to get random server members.
    *   `/roll` a dice.
    *   `/cowsay` to make a cow say a phrase.
    *   `/gacha` (exclusive to a specific guild) to roll for server roles.
    *   `/chess` to challenge other users to a chess match.
*   **Utility & Information**:
    *   `/ping` to check bot latency.
    *   `/perfil` to view your own or other users' profiles, including custom "About Me" sections and images.
    *   `/conquistas` to see your earned achievements.
    *   `/rank` to see leaderboards for Macca, XP, and duels.
    *   `/avatar` and `/banner` to view user profiles.
    *   `/sobre` for general bot information and to report errors.
    *   `/ajuda` to list all available commands.
    *   `/images` to search for images.
*   **Moderation & Customization (Administrator only)**:
    *   `/habilitarlvup` / `/desabilitarlvup` to enable/disable level-up messages in a channel.
    *   `/mensagemdelevelup` to customize the level-up message.
    *   `/increasexp` / `/decreasexp` to modify user XP.
    *   `/habilitarnsfw` / `/desabilitarnsfw` to control NSFW command usage.
    *   `/habilitarcomandos` / `/desabilitarcomandos` to enable/disable general commands in a channel.
    *   `/habilitarboasvindas` / `/desabilitarboasvindas` to manage welcome messages.
    *   `/mensagemdeboasvindas` to customize welcome messages.
    *   `/removercomando` to delete custom commands.
    *   Owner-only commands for `load`, `reload`, `unload` extensions, `sync` commands, `say` messages, `updatestatus`, `new_news`, and `darpremium`.

## Development Status

This bot is actively developed and maintained, though some features might be hardcoded for specific use cases (as indicated in the original `readme`).

## Deployment Instructions

This section outlines the steps to deploy and run the Jack Frost Discord Bot.

### Prerequisites

*   Python 3.10 or higher
*   pip (Python package installer)
*   `ImageMagick` (for the chess command's `.svg` to `.png` conversion)
*   A Discord Bot Token (from the Discord Developer Portal)
*   A Rule34Py API key (if using NSFW commands)
*   A `log_url` and `webhook_url` for Discord webhooks (for error logging and general logging)
*   An `openai` API key (if integrating with OpenAI, though this appears to be commented out in the provided `bot.py`)
*   A `custom_status` file with the bot's custom activity message.

### Setup Steps

1.  **Clone the Repository (or copy files)**:
    Ensure all bot files (`bot.py`, `rpg.py`, `roles.py`, `jacktita_to_macca.py`, `LICENSE`, `readme`, `config_channels.toml`, `config_nsfw.toml`, `custom_status`, `log_url`, `webhook_url`) are in the same directory.

2.  **Install Dependencies**:
    Navigate to the bot's directory in your terminal and install the required Python packages:

    <RUN>
    pip install -r requirements.txt
    </RUN>

    If you don't have a `requirements.txt` file, you can create one by inspecting the `bot.py` and `rpg.py` files. Based on the imports, here's a likely `requirements.txt`:

    ```
    discord.py
    pytoml
    python-dateutil
    humanize
    cowsay
    rule34Py
    cunnypy # This import exists but cunnypy might not be on pypi
    chess
    openai
    ddg # The DuckDuckGo scraper (AsyncDDGS) used in the images command
    ```
    You might need to install `pillow` as well for `ImageMagick` to work with `convert` properly, especially if it's interacting with Python.

3.  **Install ImageMagick**:
    The `/chess` command uses `ImageMagick` to convert SVG board images to PNG. Install it according to your operating system:

    *   **Debian/Ubuntu**:
        <RUN>
        sudo apt update
        sudo apt install imagemagick
        </RUN>
    *   **Fedora**:
        <RUN>
        sudo dnf install ImageMagick
        </RUN>
    *   **CentOS/RHEL**:
        <RUN>
        sudo yum install ImageMagick
        </RUN>
    *   **macOS (with Homebrew)**:
        <RUN>
        brew install imagemagick
        </RUN>
    *   **Windows**: Download from the [official ImageMagick website](https://imagemagick.org/script/download.php). Ensure it's added to your system's PATH.

4.  **Configure Environment Files**:
    Create the following files in the bot's root directory:

    *   `bot_token`: Contains your Discord bot token.
        ```
        YOUR_DISCORD_BOT_TOKEN_HERE
        ```
    *   `test_token` (optional, for testing instances): Contains a separate Discord bot token for a test bot.
        ```
        YOUR_TEST_DISCORD_BOT_TOKEN_HERE
        ```
    *   `log_url`: Contains the URL for your general bot log webhook.
        ```
        YOUR_LOGGING_WEBHOOK_URL_HERE
        ```
    *   `webhook_url`: Contains the URL for your error logging webhook.
        ```
        YOUR_ERROR_WEBHOOK_URL_HERE
        ```
    *   `custom_status`: A single line of text for the bot's custom activity status (e.g., "Playing with Macca | d$help").
        ```
        My awesome status | d$help
        ```
    *   `config_channels.toml`:
        ```toml
        channels = []
        ```
    *   `config_nsfw.toml`:
        ```toml
        channels = []
        ```
    *   `rpg/news`: A text file containing the bot's RPG news.
        ```
        Welcome to Da'at, new hunter!
        ```
    *   `profile/`: This directory will be created automatically, but ensure write permissions for the bot.
    *   `guilds/`: This directory will be created automatically, but ensure write permissions for the bot.
    *   `ships/`: This directory will be created automatically, but ensure write permissions for the bot.
    *   `rpg/dungeons/`: This directory needs to exist and contain subdirectories for levels (e.g., `1`, `2`) with `.toml` files defining dungeons.
        Example: `rpg/dungeons/1/1.toml`
        ```toml
        [dungeon]
        name = "Floresta Iniciante"
        description = "Uma floresta tranquila para novos caçadores."
        lv_required = 1
        time = 60 # seconds
        min_xp = 50
        max_xp = 100
        loot = false
        fake_weapon_loot = []
        real_weapon_loot = []
        fake_armor_loot = []
        real_armor_loot = []
        ```
    *   `rpg/items/weapon/` and `rpg/items/armor/`: These directories need to exist and contain `.toml` files defining items.
        Example: `rpg/items/weapon/1.toml`
        ```toml
        [item]
        name = "Espada Comum"
        description = "Uma espada básica."
        effect = "None"
        ```
        Example: `rpg/items/armor/1.toml`
        ```toml
        [item]
        name = "Armadura Comum"
        description = "Uma armadura básica."
        effect = "None"
        ```

5.  **Rule34Py Configuration (Optional, for NSFW commands)**:
    The `rule34Py` library *may* require API keys for full functionality, or it might work without them for public endpoints. Consult the `rule34Py` documentation for details. If keys are needed, store them securely and pass them to the `rule34Py()` constructor if required. The current code does not show direct key passing, implying it might use public access or assumes environment variables.

6.  **OpenAI Configuration (Optional)**:
    The `openai` import is present but `AsyncOpenAI` is not used in the provided code snippet. If you intend to use AI features, you'll need to uncomment the relevant code and set up your OpenAI API key as an environment variable (`OPENAI_API_KEY`) or pass it directly.

### Running the Bot

To start the bot, execute `bot.py` with Python. You need to pass the token file name as a command-line argument.

*   **For Production**:
    <RUN>
    python bot.py bot_token
    </RUN>
*   **For Testing**:
    <RUN>
    python bot.py test_token
    </RUN>

The bot will print a "Logged on as..." message when successfully connected to Discord.

### Important Notes

*   **Permissions**: Ensure your bot has all necessary Discord permissions configured in the Discord Developer Portal (e.g., `message_content` intent, read/write messages, manage roles, etc.). The `intents = discord.Intents.all()` line requests all intents, but you still need to enable them in the Developer Portal.
*   **Rate Limits**: Be mindful of Discord API rate limits when developing or scaling the bot.
*   **Hardcoded Values**: As mentioned in the original `readme`, some parts of the bot might be hardcoded. Review `bot.py` and `rpg.py` for any specific user IDs, guild IDs, or channel IDs that might need adjustment for your deployment. For example, `bot.get_user(727194765610713138)` is used multiple times and refers to the bot owner's ID.
*   **Microservices**: The `send_request` and `recieve_message` functions suggest interaction with external microservices on `localhost` ports `6000` and `6001`. If these microservices are essential, they need to be deployed and running separately. The provided code does not include these microservices.
*   **Error Handling**: The bot includes global error handling for commands and events, which sends detailed tracebacks to a configured webhook. This is crucial for monitoring.
*   **Conversion Script**: The `jacktita_to_macca.py` script converts an old currency (`Jacktitas`) to `Macca`. This is a one-time migration script and should be run carefully, likely before the bot goes live with the new currency. It contains logic to cap/set default coin values.