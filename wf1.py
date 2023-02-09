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
    st.pyplot(fig)

st.title("Illustration of Waterfilling with 4 channels")

st.write("Please enter ni/gi for each of the 4 channels")
num1 = st.number_input("Please enter n1/g1: ")
num2 = st.number_input("Please enter n2/g2: ")
num3 = st.number_input("Please enter n3/g3: ")
num4 = st.number_input("Please enter n4/g4: ")
ni_gi = [num1, num2, num3, num4]
st.write(str(ni_gi))

P_total = st.slider("Choose the P_total value", 0.1, 10.0, 1.0, 0.1)

st.write("See solution below")
plot_waterfilling(ni_gi, P_total)
inv_lambda_star = waterfilling_solution(ni_gi,P_total)
st.write("The value of 1/lambda* in this case is: "+str(inv_lambda_star))
st.write("The power level allocated to each channel is ")
powers = inv_lambda_star*np.ones(len(ni_gi))-ni_gi
powers[powers<0] = 0
st.write(str(powers))
