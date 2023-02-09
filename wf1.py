import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def waterfilling_solution(ni_gi, P_total):
    ni_gi = np.array(ni_gi)

    for i in range(100):
      inv_lambda_star = i*0.1
      Parray = inv_lambda_star*np.ones(len(ni_gi))-ni_gi 
      Parray[Parray<0] = 0
      Ps = np.sum(Parray)
      if Ps >= P_total:
         break 

    return inv_lambda_star

def plot_waterfilling(ni_gi, P_total):
    inv_lambda_star = waterfilling_solution(ni_gi, P_total)
    fig, ax = plt.subplots()
    x = np.arange(len(ni_gi))
    bars = ax.bar(x, ni_gi, color='blue')
    powers = inv_lambda_star*np.ones(len(ni_gi))-ni_gi
    powers[powers<0] = 0
    bars2 = ax.bar(x, powers, color='yellow', bottom=ni_gi)
    line = ax.axhline(inv_lambda_star, color='red', linestyle='--')
    for i, bar in enumerate(bars):
        if ni_gi[i] < inv_lambda_star:
            bar.set_color('gray')
            ax.fill_betweenx([0, ni_gi[i]], i-0.35, i+0.35, color='blue', alpha=0.5)
    ax.set_xticks(x)
    ax.set_xlabel('Channel')
    ax.set_ylabel(r'$\frac{n_i}{g_i}$')
    st.pyplot()

ni_gi = [1, 2, 3, 4]
P_total = st.slider("Choose the P_total value", 0.1, 10.0, 1.0, 0.1)

plot_waterfilling(ni_gi, P_total)

