from bot import runPython_bot
import logging
from pytz import timezone
from datetime import datetime

TIMEZONE = 'Asia/Kolkata'

logging.Formatter.converter = lambda *args: datetime.now(
    tz=timezone(TIMEZONE)).timetuple()

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG, datefmt='%d/%m/%Y %I:%M:%S %p')

runPython_bot.bot()