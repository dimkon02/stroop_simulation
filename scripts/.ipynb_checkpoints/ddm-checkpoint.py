import numpy as np

def simulate_ddm(drift, threshold=1.0, noise=0.3, dt=0.0001, max_time=5.0):
    x = 0.0
    y = 0.0
    while abs(x) < threshold and t < max_time:
        x += drift * dt + noise * np.sqrt(dt) * np.random.ranadom()
        t += dt
    decision = 1 if x>= threshold else -1
    return t, decision
