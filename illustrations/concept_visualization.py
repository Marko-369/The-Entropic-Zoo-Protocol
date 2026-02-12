"""
CONCEPTUAL ILLUSTRATION ONLY - THE ENTROPIC ZOO PROTOCOL
--------------------------------------------------------
This script visualizes the theoretical dynamics of the (S, V, P) tuple.
It is a pedagogical tool designed to map the "Support Contraction" hypothesis.

WARNING: This is not empirical validation.
For scientific data, protocols, and formal results, refer to:
https://github.com/0rion-369/closed-loop-optimization-risks
"""

import numpy as np
import matplotlib.pyplot as plt

def simulate_support_dynamics(steps=120, B0=1.0, P=0.12, V=0.03):
    """
    Simulates the evolution of Support Breadth (B) over time (t).
    Logic: B[t+1] = B[t] - (P * B[t]) + V
    
    Variables:
    - B: Support Breadth (Exploratory space)
    - P: Optimization Pressure (Selection force)
    - V: Irreducible Variance (Exogenous entropy/Bio-Seeds)
    """
    breadth = [B0]
    for _ in range(steps):
        current_B = breadth[-1]
        # Core inequality logic: Optimization vs. Entropy
        next_B = current_B - (P * current_B) + V
        breadth.append(max(0, next_B))
    return breadth

# --- SCENARIOS ---

# 1. Collapse Regime: Optimization Pressure overrides Entropy (P > V/B)
# High self-reference (S), Low exogenous variance (V)
collapse_trajectory = simulate_support_dynamics(P=0.18, V=0.01)

# 2. Stable Regime: Hybrid Axis integration (P balanced by V)
# Controlled self-reference, High irreducible variance (Bio-Seeds)
stable_trajectory = simulate_support_dynamics(P=0.18, V=0.15)

# --- VISUALIZATION ---

plt.figure(figsize=(12, 7))
plt.style.use('dark_background') # Aesthetic choice for the Zoo

plt.plot(collapse_trajectory, label='Collapse Regime (S -> 1, V -> 0)', color='#ff4c4c', linewidth=2.5)
plt.plot(stable_trajectory, label='Stable Hybrid Axis (V > 0)', color='#00ffcc', linewidth=2.5)

# Annotations
plt.axhline(y=0, color='white', linestyle='--', alpha=0.3)
plt.title('The Entropic Zoo: Support Breadth Topology (Conceptual)', fontsize=16, pad=20)
plt.xlabel('Optimization Steps (t)', fontsize=12)
plt.ylabel('Support Breadth (B)', fontsize=12)
plt.grid(color='gray', linestyle=':', alpha=0.2)
plt.legend(frameon=False, fontsize=11)

# Interpretation Note
plt.figtext(0.5, 0.02, 
            "Dynamics defined by the inequality: P > (B + V)", 
            ha="center", fontsize=10, bbox={"facecolor":"orange", "alpha":0.2, "pad":5})

plt.tight_layout()
plt.show()

print("Illustration generated: Mapping the threshold between crystallization and discovery.")