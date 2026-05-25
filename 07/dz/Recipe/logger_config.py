import logging
import sys


def setup_logger():
    """Налаштовує логування з кольорами."""

    class ColoredFormatter(logging.Formatter):
        COLORS = {
            'DEBUG': '\033[36m',  # Cyan
            'INFO': '\033[32m',  # Green
            'WARNING': '\033[33m',  # Yellow
            'ERROR': '\033[31m',  # Red
            'CRITICAL': '\033[35m',  # Magenta
        }
        RESET = '\033[0m'

        def format(self, record):
            log_color = self.COLORS.get(record.levelname, self.RESET)
            record.levelname = f"{log_color}{record.levelname}{self.RESET}"
            return super().format(record)

    root_logger = logging.getLogger()
    if any(getattr(handler, "_is_colored_recipe_handler", False) for handler in root_logger.handlers):
        return

    handler = logging.StreamHandler(sys.stdout)
    handler._is_colored_recipe_handler = True
    handler.setFormatter(ColoredFormatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    ))

    root_logger.setLevel(logging.DEBUG)
    root_logger.addHandler(handler)