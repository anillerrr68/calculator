import tkinter as tk

# --- RENKLER ---
BG_COLOR = "#2c3e50"
BUTTON_COLOR = "#34495e"
TEXT_COLOR = "#ecf0f1"
ACCENT_COLOR = "#e74c3c"
OPERATOR_COLOR = "#f39c12"
HOVER_COLOR = "#3d566e"

# --- PENCERE KURULUMU ---
root = tk.Tk()
root.title("Hesap Makinesi")
root.geometry("350x550")
root.resizable(False, False)
root.configure(bg=BG_COLOR)

# --- DEĞİŞKEN ---
current_input = tk.StringVar()
current_input.set("")

# --- FONKSİYONLAR ---
def add_to_input(char):
    if current_input.get() == "Hata!":
        current_input.set("")
    if char == "X": char = "*"
    current_input.set(current_input.get() + str(char))

def clear_input():
    current_input.set("")

def backspace():
    if current_input.get() != "Hata!":
        current_input.set(current_input.get()[:-1])

def calculate():
    if not current_input.get():
        return
    try:
        # 'X' karakterini çarpma operatörüne çevir
        expression = current_input.get().replace("X", "*")
        result = eval(expression)
        current_input.set(str(result))
    except Exception as e:
        current_input.set("Hata!")

# --- EKRAN ---
entry = tk.Entry(root, textvariable=current_input, font=("Arial", 32, "bold"), bd=0, bg=BG_COLOR, fg=TEXT_COLOR, justify="right")
entry.pack(fill="both", ipadx=10, ipady=20, pady=(20, 0), padx=10)

# --- BUTON ÇERÇEVESİ ---
button_frame = tk.Frame(root, bg=BG_COLOR)
button_frame.pack(expand=True, fill="both", padx=10, pady=10)

# DÜZELTME: '%' butonu kaldırıldı ve operatörler yeniden düzenlendi.
buttons = [
    ['C', '⌫', '/', 'X'],
    ['7', '8', '9', '-'],
    ['4', '5', '6', '+'],
    ['1', '2', '3', '='],
    ['0', '.']
]

# Grid'in orantılı büyümesi için configure
for i in range(5): button_frame.grid_rowconfigure(i, weight=1)
for i in range(4): button_frame.grid_columnconfigure(i, weight=1)

def on_enter(e): e.widget.config(bg=HOVER_COLOR)
def on_leave(e):
    text = e.widget['text']
    if text == 'C': e.widget.config(bg=ACCENT_COLOR)
    elif text == '=': e.widget.config(bg=ACCENT_COLOR)
    elif text in ['/', 'X', '-', '+']: e.widget.config(bg=OPERATOR_COLOR)
    else: e.widget.config(bg=BUTTON_COLOR)

# --- BUTONLARI OLUŞTURMA ---
for r, row_list in enumerate(buttons):
    for c, char in enumerate(row_list):
        b = tk.Button(button_frame, text=char, font=("Arial", 18, "bold"), fg=TEXT_COLOR, bd=0, relief="flat")
        b.bind("<Enter>", on_enter)
        b.bind("<Leave>", on_leave)

        # Butonların özelliklerini ve komutlarını belirleme
        if char in ['/', 'X', '-', '+']:
            b.config(bg=OPERATOR_COLOR, command=lambda ch=char: add_to_input(ch))
        elif char == 'C':
            b.config(bg=ACCENT_COLOR, command=clear_input)
        elif char == '⌫':
            b.config(bg=BUTTON_COLOR, command=backspace)
        elif char == '=':
            b.config(bg=ACCENT_COLOR, command=calculate)
        else: # Sayılar ve nokta
            b.config(bg=BUTTON_COLOR, command=lambda ch=char: add_to_input(ch))

        # Butonları grid'e yerleştirme (ÖZEL DURUMLAR)
        if char == '0':
            b.grid(row=r, column=c, columnspan=2, sticky="nsew", padx=5, pady=5)
        elif char == '.':
            b.grid(row=r, column=c + 1, sticky="nsew", padx=5, pady=5)
        elif char == '=':
            # '=' butonu artık 2 satır kaplayarak daha iyi bir görünüm sunuyor.
            b.grid(row=r, column=c, rowspan=2, sticky="nsew", padx=5, pady=5)
        else:
            b.grid(row=r, column=c, sticky="nsew", padx=5, pady=5)

root.mainloop()