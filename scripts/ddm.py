import numpy as np

def simulate_ddm(drift, threshold=0.8, noise=0.5, dt=0.001, max_time=5.0):
    x = 0.0
    t = 0.0
    while abs(x) < threshold and t < max_time:
        x += drift * dt + noise * np.sqrt(dt) * np.random.randn()
        t += dt
    decision = 1 if x>= threshold else -1
    return t, decision
