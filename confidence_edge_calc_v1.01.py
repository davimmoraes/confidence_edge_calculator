import tkinter as tk
from math import sqrt
from scipy.stats import norm

# Function to calculate the minimum edge and minimum win rate
def calculate_minimum_edge():
    try:
        # Get the parameters
        trades = int(entry_trades.get())
        payoff = float(entry_payoff.get())
        confidence_level = float(entry_confidence.get()) / 100
        
        # Calculate the breakeven point
        breakeven = 1 / (1 + payoff)
        
        # Critical Z-value
        z_value = norm.ppf(1 - (1 - confidence_level) / 2)
        
        # Calculate the minimum win rate required for the confidence interval to be above breakeven
        minimum_winrate = breakeven + z_value * sqrt(breakeven * (1 - breakeven) / trades)
        
        # Calculate the minimum edge
        minimum_edge = (minimum_winrate - breakeven) * 100  # Convert to percentage
        
        # Display the results in the interface
        label_result.config(text=(
            f"System random breakeven: {breakeven:.2%}\n"
            f"Minimum edge required: {minimum_edge:.2f}%\n"
            f"Minimum winrate required: {minimum_winrate:.2%}"
        ))

    except ValueError:
        label_result.config(text="Error: Please enter valid numeric inputs.")
        label_edge_minimum.config(text="")

# Configure the main window
root = tk.Tk()
root.title("Confidence Edge Calculator")
# Calculate the dimensions and position of the window
window_width = 320
window_height = 200

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Labels and entry fields
tk.Label(root, text="Number of Trades:").grid(row=0, column=0, padx=10, pady=5)
entry_trades = tk.Entry(root)
entry_trades.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Payoff (Return/Risk):").grid(row=1, column=0, padx=10, pady=5)
entry_payoff = tk.Entry(root)
entry_payoff.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Confidence Level (%):").grid(row=2, column=0, padx=10, pady=5)
entry_confidence = tk.Entry(root)
entry_confidence.grid(row=2, column=1, padx=10, pady=5)

# Button to calculate the minimum edge and win rate
btn_calculate = tk.Button(root, text="Calculate", command=calculate_minimum_edge)
btn_calculate.grid(row=3, columnspan=2, padx=10, pady=5)

# Label to display the breakeven and minimum win rate
label_result = tk.Label(root, text="")
label_result.grid(row=4, columnspan=2, padx=10, pady=5)

# Label to display the minimum edge in bold
label_edge_minimum = tk.Label(root, text="", font=("Arial", 10, "bold"))
label_edge_minimum.grid(row=5, columnspan=2, padx=10, pady=5)

# Run the application
root.mainloop()
