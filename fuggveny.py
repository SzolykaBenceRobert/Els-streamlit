import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.title("Függvény ábrázolása")

with st.sidebar:
    st.header("Fukar")
    a = st.slider("a", -5.0, 5.0, 1.0, 0.1)
    b = st.slider("b", -5.0, 5.0, 0.0, 0.1)
    c = st.slider("c", -5.0, 5.0, 0.0, 0.1)
    
    x_min = st.number_input("X-min", -10.0, 10.0, -5.0)
    x_max = st.number_input("X-max", -10.0, 10.0, 5.0)


x = np.linspace(x_min, x_max, 200)
y1 = a * x**2 + b * x + c
y2 = b * x + c

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, y1, label=f'${a}x^2 + {b}x + {c}$', linewidth=2)
ax.plot(x, y2, label=f'${b}x + {c}$', linewidth=2)

ax.set_aspect('equal', adjustable='datalim')

ax.grid(True, alpha=0.3)
ax.axhline(y=0, color='black', linewidth=0.5)
ax.axvline(x=0, color='black', linewidth=0.5)

ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.legend()
ax.set_title("Függvények")

st.pyplot(fig)

st.latex(f"Függvény: f(x) = {a}x^2 + {b}x + {c}")
st.latex(f"Függvény: f(x) = {b}x + {c}")