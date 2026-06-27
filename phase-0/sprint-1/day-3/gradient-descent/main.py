import numpy as np
import matplotlib.pyplot as plt

# step-1 : Generate synthetic Data

# we create fake data where we know the true answer:
#  Tre line: 2x + 5
# After training, our gradient descent should recover m = 2 and b = 5

np.random.seed(42)  # Set seed => same random numbers every run

N = 100           # Number of data points

x = np.linspace(0, 10, N)  #100 evenly spaced points from 0 to 10
                           # linespace( start stop, num_points)


noise  = np.random.randn(N) * 1.5   # Gaussian noise (std=1.5)
                                    # Makes data realistic - real data is never perfect

# True relationship: y = 2x + 5 + noise
y = 2 * x + 5 + noise

# What we know: x values and y values
# What we DON'T know: m=2 and b=5 <- gradient descent will find these!

print(f"Data: {N} pints")
print(f"x range: [{x.min():.1f}, {x.max():.1f}]")
print(f"y range: [{y.min():.1f}, {y.max():.1f}]")



# step-2: Define the loss function (MSE)

def compute_loss(x, y, m, b):
    """
    Mean Squared Error: average of (actual - predicted)^2

    Args: 
    x, y: data arrays
    m, b: current line parameters

    Returns:
       A single float - how wrong our current line is
    """
    
    predictions = m * x + b     # y_hat = mx + b (vectorized!)
    errors = y - predictions    # error per point
    loss = np.mean(errors ** 2) # mean of squared errors
    return loss

# step-3: Define the Gradient Functions

def compute_gradients(x, y, m, b):
    """
    Compute partial derivatives of MSE with respect to m and b.
    These gradients tell us which direction to move m and b
    to DECREASE the loss.
    Math:
        dL/dm = (-2/N) * sum( x * (y - (mx+b)) )
        dL/db = (-2/N) * sum(     (y - (mx+b)) )
    Args:
        x, y: data arrays
        m, b: current parameters
    Returns:
        dm: gradient w.r.t. m
        db: gradient w.r.t. b
    """
    N = len(x)
    predictions = m*x+b   #current predictions
    errors = y - predictions

    dm = (-2 / N) * np.sum(x*errors)
    db = (-2/N) * np.sum(errors)

    return dm, db

# step-4: Gradent Descent Loop

def gradient_descent(x, y, learning_rate=0.01, epochs=500):
    """
    Run gradient descent to find the best m and b.
    Args:
        x, y          : training data
        learning_rate : step size (alpha) — how big each update is
        epochs        : how many times to loop through the data
    Returns:
        m, b          : learned parameters
        loss_history  : list of loss at each epoch (for plotting)
    """

    # Initialize parameters at zero
    m = 0.0           #start slope at 0
    b = 0.0           # start intercept at 0
    # we know the answer is m = 2, b = 5 - but we start from zero and learn!

    loss_history = []    # store loss at each step to plot later

    # main training loop -----------------------------------

    for epoch in range(epochs): 

        #1. Compute how wrong we are right now
        loss = compute_loss(x, y, m, b)
        loss_history.append(loss)

        #2. Compute which direction to move m and b
        dm, db = compute_gradients(x, y, m, b)

        #3. Take a step OPPOSITE to the gradient (= downhill)
        m = m - learning_rate * dm
        b = b - learning_rate * db

        #4. Print progress every 50 epochs
        if epoch % 50 == 0: 
            print(f"Epoch {epoch:4d} | Loss: {loss:8.4f} | m: {m:.4f} | b: {b:.4f}")

    print(f"\n✅ Training complete!")
    print(f"	True values: 	m = 2.0000, b = 5.0000")
    print(f"	Learned values: m = {m:.4f}, b = {b:.4f}")
    
    return m, b, loss_history


# step-5: run it

print("\n" + "="*55)
print(" GRADIENT DESCENT: Finding y = mx + b")
print("="*55 + "\n")

m_learned, b_learned, loss_history = gradient_descent(
    x, y,
    learning_rate=0.01,
    epochs=500
)

#step-6 - Visualize: Loss Curve + Fitted Line

fig, axes = plt.subplots(1, 2, figsize=(14, 5))
fig.suptitle("Gradient Descent: Linear Regression", fontsize=16, fontweight='bold')
# ── Plot 1: Loss Curve (the mountain descent) ─────────────────────────────
ax1 = axes[0]
ax1.plot(loss_history, color='#e74c3c', linewidth=2)
ax1.set_title("Loss Curve (MSE over Epochs)", fontsize=13)
ax1.set_xlabel("Epoch")
ax1.set_ylabel("Mean Squared Error (Loss)")
ax1.grid(True, alpha=0.3)
ax1.annotate(f"Start\nLoss={loss_history[0]:.1f}",
             xy=(0, loss_history[0]),
             xytext=(50, loss_history[0] * 0.8),
             arrowprops=dict(arrowstyle='->', color='black'),
             fontsize=9)
ax1.annotate(f"End\nLoss={loss_history[-1]:.2f}",
             xy=(len(loss_history)-1, loss_history[-1]),
             xytext=(len(loss_history)*0.6, loss_history[0]*0.3),
             arrowprops=dict(arrowstyle='->', color='black'),
             fontsize=9)

# ── Plot 2: Data + Fitted Line ────────────────────────────────────────────
ax2 = axes[1]
ax2.scatter(x, y, alpha=0.5, color='#3498db', s=20, label='Data points')
ax2.plot(x, 2*x + 5, color='green', linewidth=2,
         linestyle='--', label='True line (y=2x+5)')
ax2.plot(x, m_learned*x + b_learned, color='#e74c3c', linewidth=2,
         label=f'Learned: y={m_learned:.2f}x+{b_learned:.2f}')
ax2.set_title("Data + Fitted Line", fontsize=13)
ax2.set_xlabel("x")
ax2.set_ylabel("y")
ax2.legend(fontsize=10)
ax2.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("gradient_descent_result.png", dpi=150, bbox_inches='tight')
plt.show()
print("\n📊 Plot saved as 'gradient_descent_result.png'")




# Experiment: try different learning rates and see what happens


for lr in (0.001, 0.01, 0.1, 0.5):
    m, b, losses = gradient_descent(x, y, learning_rate=lr, epochs=200)
    print(f"lr={lr:5.3f} | Final loss: {losses[-1]:.4f} | m={m:.3f}, b={b:.3f}")