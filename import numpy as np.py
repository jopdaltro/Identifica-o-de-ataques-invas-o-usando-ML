import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do problema
F = 15 * 10**9    # bits
us = 30 * 10**6   # bits/s
d = 2 * 10**6     # bits/s

# Modo cliente-servidor
t_cs = F / us

# Modo distribuição P2P
N_vals = [10, 100, 1000]
u_vals = [300 * 10**3, 700 * 10**3, 2 * 10**6]

for N in N_vals:
    plt.figure()
    plt.title(f"N={N}")
    for u in u_vals:
        t_p2p = F / (u + (N-1) * d)
        plt.plot(u / 10**6, t_p2p / 60, 'o-', label=f"u={u/10**6:.1f} Mbps")
    plt.axhline(y=t_cs / 60, linestyle='--', color='black', label="Cliente-servidor")
    plt.xlabel("Taxa de upload (Mbps)")
    plt.ylabel("Tempo mínimo de distribuição (min)")
    plt.legend()
    plt.show()