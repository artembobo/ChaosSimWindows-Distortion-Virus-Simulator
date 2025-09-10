import tkinter as tk
import subprocess
import random
import winsound  # для звуку beep
import pyautogui
import string
import os
import psutil

def monitor_taskmgr():
    if not running:
        return
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] and proc.info['name'].lower() == "taskmgr.exe":
            try:
                proc.kill()
            except Exception:
                pass
    root.after(500, monitor_taskmgr)

def flip_screen_text():
    if not running:
        return
    flipped_text = text_label.cget("text")[::-1]  # розвертаємо текст
    text_label.config(text=flipped_text)
    root.after(3000, flip_screen_text)


def kill_taskmgr():
    if not running:
        return
    try:
        # /F — примусово, /IM — за ім'ям процесу
        subprocess.run("taskkill /F /IM Taskmgr.exe", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except:
        pass
    root.after(1000, kill_taskmgr)  # пер

def spawn_many_windows():
    if not running:
        return
    for _ in range(10):
        win = tk.Toplevel()
        win.title("Вірус активований!")
        win.geometry(f"200x80+{random.randint(0, root.winfo_screenwidth()-200)}+{random.randint(0, root.winfo_screenheight()-80)}")
        label_win = tk.Label(win, text="Ваш комп'ютер заражено!", fg="red", font=("Arial", 10))
        label_win.pack(expand=True)
        win.after(5000, win.destroy)  # Закриваємо вікно через 5 секунд
    root.after(2000, spawn_many_windows)


def open_folders():
    if not running:
        return
    folders = [
        os.path.expanduser("~\\Documents"),
        os.path.expanduser("~\\Downloads"),
        os.path.expanduser("~\\Desktop"),
        os.path.expanduser("~\\Pictures"),
        os.path.expanduser("~\\Videos"),
        os.path.expanduser("~\\Music")
    ]
    folder_to_open = random.choice(folders)
    try:
        subprocess.Popen(f'explorer "{folder_to_open}"')
    except Exception as e:
        print(f"Не вдалося відкрити папку: {e}")
    root.after(4000, open_folders)

running = True
typed_text = ""
virus_message = "Вирус активирован... Удаление системных файлов..."
countdown = 30  # секунд

def glitch_text():
    if not running:
        return
    glitched = ''.join(random.choice(string.ascii_letters + string.digits + "!@#$%^&*") for _ in range(25))
    text_label.config(text=glitched, fg=random.choice(["red", "white", "yellow"]))
    root.after(700, glitch_text)

def countdown_timer():
    global countdown
    if not running or countdown <= 0:
        text_label.config(text="Система знищена!", fg="red")
        return
    text_label.config(text=f"Знищення через {countdown} секунд...", fg="orange")
    countdown -= 1
    root.after(1000, countdown_timer)

def move_mouse_randomly():
    if not running:
        return
    x = random.randint(0, root.winfo_screenwidth())
    y = random.randint(0, root.winfo_screenheight())
    pyautogui.moveTo(x, y, duration=0.2)
    root.after(3000, move_mouse_randomly)

def flicker_overlay():
    if not running:
        return
    overlay = tk.Toplevel(root)
    overlay.attributes("-fullscreen", True)
    overlay.attributes("-topmost", True)
    overlay.configure(bg=random.choice(["#111", "#333", "#555", "#777"]))
    overlay.after(100, overlay.destroy)
    root.after(1500, flicker_overlay)

def fake_typing():
    if not running:
        return
    message = random.choice(["help...", "error!", "who's there?", "system32 missing"])
    pyautogui.write(message, interval=0.1)
    root.after(4000, fake_typing)

def open_apps():
    if not running:
        return
    apps = ["taskmgr", "notepad", "calc"]
    subprocess.Popen(random.choice(apps))
    winsound.Beep(1000, 150)  # короткий звук при відкритті програми
    root.after(3000, open_apps)

def spawn_window():
    if not running:
        return
    win = tk.Toplevel()
    win.title("Вирус активирован!")
    win.geometry(f"250x100+{random.randint(0,1000)}+{random.randint(0,600)}")
    label_win = tk.Label(win, text="Ваш компьютер заражён!", fg="red", font=("Arial", 10))
    label_win.pack(expand=True)
    win.protocol("WM_DELETE_WINDOW", lambda: [win.destroy(), spawn_window()])
    root.after(2000, spawn_window)

def animate_text():
    if not running:
        return
    current = text_label.cget("text")
    new_text = current + "." if len(current) < 20 else ""
    text_label.config(text=new_text)
    text_label.config(fg=random.choice(["white", "yellow", "red"]))
    root.after(500, animate_text)

def type_writer():
    global typed_text
    if not running or len(typed_text) >= len(virus_message):
        return
    typed_text += virus_message[len(typed_text)]
    text_label.config(text=typed_text)
    root.after(150, type_writer)

def flicker_background():
    if not running:
        return
    colors = ["blue", "darkred", "black", "purple"]
    new_color = random.choice(colors)
    root.configure(bg=new_color)
    label.configure(bg=new_color)
    text_label.configure(bg=new_color)
    hint_label.configure(bg=new_color)
    root.after(300, flicker_background)

def shake_window():
    if not running:
        return
    try:
        x = root.winfo_x() + random.randint(-10, 10)
        y = root.winfo_y() + random.randint(-10, 10)
        root.geometry(f"+{x}+{y}")
    except:
        pass
    root.after(100, shake_window)

def random_beep():
    if not running:
        return
    freq = random.randint(500, 2500)
    dur = random.randint(100, 500)
    winsound.Beep(freq, dur)
    root.after(2000, random_beep)

def stop_virus(event=None):
    global running
    running = False
    root.destroy()

def glitch_overlay_text():
    if not running:
        return
    glitched = ''.join(random.choice("█▓▒░<>?/|") for _ in range(40))
    label.config(text=glitched, fg=random.choice(["lime", "magenta", "cyan", "red"]))
    root.after(400, glitch_overlay_text)

floating_windows = []

def move_floating_windows():
    if not running:
        return
    for win in floating_windows:
        try:
            x = win.winfo_x() + random.randint(-30, 30)
            y = win.winfo_y() + random.randint(-30, 30)
            win.geometry(f"+{x}+{y}")
        except:
            pass
    root.after(200, move_floating_windows)

def spawn_floating_window():
    if not running:
        return
    win = tk.Toplevel()
    win.title("⚠️")
    win.geometry(f"200x100+{random.randint(0, 1000)}+{random.randint(0, 600)}")
    win.configure(bg=random.choice(["black", "red", "purple"]))
    tk.Label(win, text="!!!", font=("Consolas", 24), fg="white", bg=win["bg"]).pack(expand=True)
    floating_windows.append(win)
    root.after(1000, spawn_floating_window)



# === Інтерфейс ===
root = tk.Tk()
root.title("Windows Error")
root.attributes("-fullscreen", True)
root.configure(bg="blue")

label = tk.Label(root, text="😵 Windows обнаружил критическую ошибку\nСистема нестабильна...", fg="white", bg="blue", font=("Consolas", 24))
label.pack(pady=50)

text_label = tk.Label(root, text="", fg="white", bg="blue", font=("Consolas", 18))
text_label.pack()

hint_label = tk.Label(root, text="Натисніть клавішу A або кнопку, щоб вимкнути вірус!", fg="white", bg="blue", font=("Arial", 14))
hint_label.pack(pady=20)

stop_button = tk.Button(root, text="Вимкнути вірус", fg="white", bg="green", font=("Arial", 16), command=stop_virus)
stop_button.pack(pady=30)

root.protocol("WM_DELETE_WINDOW", lambda: None)  # блокуємо закриття
root.bind("a", stop_virus)
root.bind("A", stop_virus)

# === Запуск ефектів ===
open_folders()
open_apps()
spawn_window()
animate_text()
type_writer()
flicker_background()
shake_window()
random_beep()
flicker_overlay()
move_mouse_randomly()
fake_typing()
countdown_timer()
spawn_many_windows()
kill_taskmgr()
monitor_taskmgr()
flip_screen_text()
glitch_overlay_text()
spawn_floating_window()
move_floating_windows()


root.mainloop()
