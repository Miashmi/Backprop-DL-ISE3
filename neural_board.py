import tkinter as tk
import random

weights = {
    "w1": round(random.uniform(-1, 1), 2),
    "w2": round(random.uniform(-1, 1), 2),
    "w3": round(random.uniform(-1, 1), 2),
}

inputs = [1, 1]
target = 1
step = 0
last_loss = None

def forward_pass():
    h = inputs[0] * weights["w1"] + inputs[1] * weights["w2"]
    out = h * weights["w3"]
    return round(out, 2)

def compute_loss():
    pred = forward_pass()
    return round((pred - target) ** 2, 4)

root = tk.Tk()
root.title("Backprop Trainer")
canvas = tk.Canvas(root, width=600, height=400, bg="white")
canvas.pack()
info = tk.Label(root, text="", font=("Times New Roman", 16 ))
info.pack(pady=5)

def draw_network(show_backprop=False):
    canvas.delete("all")
    coords = {
        "in1": (100, 100),
        "in2": (100, 200),
        "h1": (300, 150),
        "out": (500, 150),
    }

    for key, (x, y) in coords.items():
        color = "pink" if "in" in key else "light blue" if "h" in key else "light yellow"
        canvas.create_oval(x-20, y-20, x+20, y+20, fill=color)
        canvas.create_text(x, y, text=key.upper())

    canvas.create_line(120, 100, 280, 150, arrow=tk.LAST)
    canvas.create_text(200, 115, text=f"w1={weights['w1']}", fill="black")
    canvas.create_line(120, 200, 280, 150, arrow=tk.LAST)
    canvas.create_text(200, 185, text=f"w2={weights['w2']}", fill="black")
    canvas.create_line(320, 150, 480, 150, arrow=tk.LAST)
    canvas.create_text(400, 130, text=f"w3={weights['w3']}", fill="black")
    canvas.create_text(300, 250, text=f"Output: {forward_pass()}", font=("Times New Roman", 14))
    canvas.create_text(300, 280, text=f"Loss: {compute_loss()}", font=("Times New Roman", 14))
    if show_backprop:
        canvas.create_line(480, 150, 320, 150, arrow=tk.LAST, fill="dark violet", width=2)
        canvas.create_line(280, 150, 120, 100, arrow=tk.LAST, fill="dark violet", width=2)
        canvas.create_line(280, 150, 120, 200, arrow=tk.LAST, fill="dark violet", width=2)

def adjust_weight(w, delta):
    global step, last_loss
    prev_loss = compute_loss()
    weights[w] = round(weights[w] + delta, 2)
    step += 1
    new_loss = compute_loss()
    draw_network(show_backprop=True)
    if new_loss < 0.01:
        info.config(text=f"🎉 Success! Loss < 0.01 in {step} steps.")
        disable_buttons()
    elif new_loss > prev_loss:
        info.config(
            text=f"⚠️ Loss increased! (from {prev_loss} to {new_loss}) — Try stepping back!"
        )
    else:
        info.config(text=f"✅ Good move! Loss reduced to {new_loss}")

def disable_buttons():
    for btn in buttons:
        btn.config(state=tk.DISABLED)

def reset_game():
    global step, weights
    step = 0
    weights = {
        "w1": round(random.uniform(-1, 1), 2),
        "w2": round(random.uniform(-1, 1), 2),
        "w3": round(random.uniform(-1, 1), 2),
    }
    for btn in buttons:
        btn.config(state=tk.NORMAL)
    draw_network()
    info.config(text="Adjust weights to reduce loss. Watch for hints!")

btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)
buttons = []
for w in ["w1", "w2", "w3"]:
    b1 = tk.Button(btn_frame, text=f"{w} +0.1", command=lambda w=w: adjust_weight(w, 0.1))
    b2 = tk.Button(btn_frame, text=f"{w} -0.1", command=lambda w=w: adjust_weight(w, -0.1))
    b1.pack(side=tk.LEFT, padx=5)
    b2.pack(side=tk.LEFT, padx=5)
    buttons += [b1, b2]

tk.Button(btn_frame, text="🔁 Reset", command=reset_game).pack(side=tk.LEFT, padx=10)
draw_network()
info.config(text="Start adjusting weights to reach output = 1")
root.mainloop()