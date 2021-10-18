import tkinter as tk

# Configurations and Globals

config = {
    "DB_PORT": 3306,
    "DB_NAME": "hms",
    "DB_AUTOCOMMIT": True,
    # Server Details
    "DB_HOST": "mohityadav.codes",
    # Localhost Details
    # 'DB_HOSt': 'localhost',
    "acceptables": (
        *[chr(i) for i in range(97, 123)],
        "_",
        *[str(i) for i in range(10)],
        ".",
    ),
    "windows": {"main_window": {"win_width": 840, "win_height": 450, "nav_width": 170}},
    "sidebar_button_positions": [],
}

# Font
fonts = {"h1": ("arial", 22, "bold"), "h2": ("arial", 18, "bold")}
