import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s |--%(levelname)s - %(message)s"
)


# Beispiel-Logs
logging.debug("This is a debug message")  # Debug-Level
logging.info("This is an info message")   # Info-Level
logging.warning("This is a warning message")  # Warnung
logging.error("This is an error message")  # Fehler
logging.critical("This is a critical message")  # Kritisches Problem
