"""
ASCII logos for various OSes and tools.
Useful with neofetch_win.py or other terminal info tools.

Instructions for adding your own art:
--------------------------------------
1. Use one of these ASCII generators:
   - https://ascii-art-generator.org/
   - https://www.ascii-art-generator.org/
   - https://www.text-image.com/convert/

2. Settings:
   - Width: try 40-50 chars max
   - Height: 7-10 lines is ideal
   - Use a monospaced font
   - Simpler image = better results

3. Paste your ASCII logo into the ASCII_ART dict below:
   Example:
     "new_logo": [
         " ASCII LINE 1 ",
         " ASCII LINE 2 ",
         ...
     ]

4. Reference your new logo in config.yml like:
     pick: "new_logo"

Some tips:
----------
- Avoid high detail, keep contrast clear
- Same width per line helps a lot
- Double-check how it looks in your shell
"""

# Logo stash — feel free to add your own here
ASCII_ART = {
    # Placeholder example
    "custom_logo": [
        "    ╭━━━━━━━━━━╮",
        "    ┃  CUSTOM  ┃",
        "    ┃   LOGO   ┃",
        "    ╰━━━━━━━━━━╯"
    ],
    
    # Win 10-ish blocky thing
    "windows_10": [
        "                                ..,",
        "                    ....,,:;+ccllll",
        "      ...,,+:;  cllllllllllllllllll",
        ",cclllllllllll  lllllllllllllllllll",
        "llllllllllllll  lllllllllllllllllll",
        "llllllllllllll  lllllllllllllllllll",
        "llllllllllllll  lllllllllllllllllll",
        "llllllllllllll  lllllllllllllllllll",
        "llllllllllllll  lllllllllllllllllll",
        "                                   ",
        "llllllllllllll  lllllllllllllllllll",
        "llllllllllllll  lllllllllllllllllll",
        "llllllllllllll  lllllllllllllllllll",
        "llllllllllllll  lllllllllllllllllll",
        "llllllllllllll  lllllllllllllllllll",
        "llllllllllllll  lllllllllllllllllll",
        "`'ccllllllllll  lllllllllllllllllll",
        "       `' \\*::  :ccllllllllllllllll",
        "                       ````''*::cll",
        "                                 ``"
    ],
    
    # Win 11 - chunky version
    "windows_11": [
        "████████████████  ████████████████",
        "████████████████  ████████████████",
        "████████████████  ████████████████",
        "████████████████  ████████████████",
        "████████████████  ████████████████",
        "████████████████  ████████████████",
        "████████████████  ████████████████",
        "                                  ",
        "████████████████  ████████████████",
        "████████████████  ████████████████",
        "████████████████  ████████████████",
        "████████████████  ████████████████",
        "████████████████  ████████████████",
        "████████████████  ████████████████",
        "████████████████  ████████████████"
    ],
    
    # Simple 'Win' symbol — classic fallback
    "windows_simple": [
        " .--.",
        "|oo |",
        "|\\/ |",
        " `--'",
        "/ /__",
        "| |\\ \\",
        "\\_\\_)"
    ],
    
    # Good ol' Tux
    "linux_tux": [
        "   .--.",
        "  |o_o |",
        "  |:_/ |",
        " //   \\ \\",
        "(|     | )",
        "/'\\_   _/`\\",
        "\\___)=(___/"
    ],
    
    # macOS - abstract appleish blob
    "macos": [
        "      .:",
        "    _: :_",
        "  .' .' :",
        "  :  :  :",
        "  :  :  :",
        "  :  :  :",
        "  :  :  :",
        "  :  :  :",
        "  :  :  :",
        "  :  :  :",
        "  :  :  :",
        "  :  :  :",
        "  :  :  :",
        "  :  :  :",
        "  :  :  :",
        "  :  :  :",
        "  :  :  :",
        "  :  :  :",
        "  :  :  :",
        "  :  :  :"
    ],
    
    # Python logo with squishy curves
    "python": [
        "    ____        _   _",
        "   / __ \\____ _| |_| |_",
        "  / / _/ _  |  _| | |",
        " / /_/ / /_/ | |_| |_|",
        "/_____/\\__,_|\\__/\\__/"
    ]
}

def get_logo(logo_name=None, os_name=None):
    """
    Pick a logo based on name or OS.
    Returns: List of strings for ASCII art
    """
    # Explicit override first
    if logo_name and logo_name in ASCII_ART:
        return ASCII_ART[logo_name]
    
    # Try guessing from OS name
    if os_name:
        os_guess = os_name.lower()
        if "windows 11" in os_guess:
            return ASCII_ART["windows_11"]
        elif "windows 10" in os_guess:
            return ASCII_ART["windows_10"]
        elif "windows" in os_guess:
            return ASCII_ART["windows_simple"]
        elif "linux" in os_guess:
            return ASCII_ART["linux_tux"]
        elif "darwin" in os_guess or "macos" in os_guess:
            return ASCII_ART["macos"]
    
    # Fallback to basic win logo
    return ASCII_ART["windows_simple"]

def get_available_logos():
    """
    Returns list of all known logo keys
    """
    return list(ASCII_ART.keys())

def get_logo_dimensions(logo_name):
    """
    Get size of logo in lines (H) and max width (W)
    """
    if logo_name in ASCII_ART:
        lines = ASCII_ART[logo_name]
        h = len(lines)
        w = max(len(line) for line in lines)
        return h, w
    return 0, 0  # Hmm, logo not found
