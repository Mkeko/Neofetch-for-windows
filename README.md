# 🪟 EasyWinfetch

A lightweight system info tool for Windows, inspired by **Neofetch**, but with Python vibes.

---

## ✨ Features

- ASCII art logos right in your terminal (because why not?)
- Configurable layout and data display
- Several prebuilt logos: Windows 10, Windows 11, Linux Tux, macOS, Python
- Control the info order and labels — your way
- Terminal colors for easy visual parsing
- Easy to install, fun to tweak

---

## 🚀 Installation

Install from PyPI:

```bash
pip install easywinfetch
```

Or install directly from GitHub:

```bash
pip install git+https://github.com/Mkeko/Neofetch-for-windows.git
```

---

## 🖥️ Usage

Once installed, just run:

```bash
easywinfetch
```

That's it! You should see a nice ASCII logo alongside your system stats.

---

## ⚙️ Configuration

Tweak your display by editing the `config.yml` file. Some things you can adjust:

- Which ASCII art to show
- Where the logo appears (left/right)
- What system info shows up — and in what order
- Colors, labels, spacing
- Custom logos (if you're feeling artistic)

Example snippet from a config:

```yaml
ascii:
  selected_logo: "windows_11"
  colors:
    enabled: true
    primary: "blue"
    secondary: "cyan"

display:
  show_logo: true
  logo_position: left
  spacing: 2
```

More complete sample config is included in the repo.

---

## 🎨 Available ASCII Logos

Here's what's built-in:

- `windows_10`
- `windows_11`
- `windows_simple`
- `linux_tux`
- `macos`
- `python`

You can even create your own! See `ASCII.py` and the config guide for instructions.

---

## 📦 Requirements

- Windows OS
- Python 3.6+
- Dependencies:
  - `wmi`
  - `psutil`
  - `pyyaml`

Use `pip` to install them if needed. Usually `pip install easywinfetch` handles this for you.

---

## 📄 License

MIT — do whatever you want, just don't blame us if your terminal explodes.

---

## 🤝 Contributing

PRs are welcome!

Spotted a bug? Got a logo idea? Want to improve the config flexibility? Jump in. Open an issue or send a pull request — let's make EasyWinfetch better together.

---

## 🔗 Links

- [PyPI Package](https://pypi.org/project/easywinfetch/)
- [GitHub Repository](https://github.com/Mkeko/Neofetch-for-windows)
