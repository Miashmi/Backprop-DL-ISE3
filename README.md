# Backprop-DL-ISE3
# Backprop Trainer
An interactive educational game built with Python and Tkinter to help beginners understand the fundamentals of neural networks and backpropagation — by manually adjusting weights to minimize loss.

<img width="887" height="755" alt="image" src="https://github.com/user-attachments/assets/4412b570-ee4a-4da8-b206-94a0034a9a59" />


---

## 📚 Overview

This game simulates a tiny neural network with:

- **2 Input Neurons**
- **1 Hidden Neuron**
- **1 Output Neuron**

Your job is to manually adjust the weights (`w1`, `w2`, and `w3`) to train the network. The goal is to reduce the output error (loss) until it’s below **0.01**.

---

## How It Works

1. The input is fixed: `[1, 1]`
2. Target output is `1`
3. Neural network equation:

4. You adjust weights via `+0.1` or `-0.1` buttons
5. Visual feedback helps you learn how loss changes with weight updates

---

## Features

- 🎯 Manual weight tuning to simulate learning
- 🎓 Learn backpropagation by experience
- 💡 Hints on whether your changes helped or hurt
- 🎨 Neural network visualized with arrows and weights
- 🔁 Reset button to restart with random weights

---

## Requirements

- Python 3.x
- Tkinter (comes with standard Python installation)

No external libraries required.

---

## Running the Game

1. Clone this repo or copy the `.py` file.
2. Run it using Python:

```bash
python backprop_trainer.py
