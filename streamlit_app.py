
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm


st.title("Impact of Q-Factor and Meta-State Factors")

st.header("Overview")
st.markdown("""
![https://a9group.net/a9logo.png](https://a9group.net/a9logo.png) Welcome to the interactive dashboard designed to illuminate how the Q-Factor affects ticket resolution times in Jira. Originating from fields like engineering and sports, the Q-Factor here measures the efficiency and effectiveness of your project management efforts.
""")

st.header("Simulation Purpose")
st.markdown("""
Explore how different Q-Factor scores can change the way tickets are resolved. Adjust the Q-Factor, simulate various management scenarios, and see real-time impacts on resolution timelines. This visualization helps pinpoint operational improvements and enhance resource allocation for better project outcomes.
""")

st.header("How It Works")
st.markdown("""
- **High Q-Factor Scores**: Indicate efficient management, speeding up ticket resolutions.
- **Low Q-Factor Scores**: Suggest inefficiencies, potentially slowing down processes.
Manipulate the sliders below to alter the Q-Factor score and other metrics, and watch how these changes affect ticket resolution times through dynamic visualizations.
""")

st.header("Dashboard Features")
st.markdown("""
- **Dynamic Updates**: Watch the graphs and stats update instantly as you tweak the settings.
- **Comparative Visualizations**: Compare different Q-Factor scenarios side-by-side to directly see their impact.
- **Advanced Statistical Models**: Dive deeper with complex models for a more accurate prediction of outcomes.
- **Interactive Scenarios**: Experiment with various "what-if" setups by modifying the Q-Factor, offering a strategic tool for planning and decision-making.
""")

# Sliders for input
creation_time = st.slider("Creation Time (days ago)", min_value=0, max_value=100, value=50, step=1)
activity_level = st.slider("Activity Level (number of interactions)", min_value=0, max_value=50, value=10, step=1)
similarity_index = st.slider("Similarity Index (0 to 1 scale)", min_value=0.0, max_value=1.0, value=0.5, step=0.05)
component_relevance = st.slider("Component Relevance (0 to 1 scale)", min_value=0.0, max_value=1.0, value=0.75, step=0.05)
text_similarity = st.slider("Text Similarity (0 to 1 scale)", min_value=0.0, max_value=1.0, value=0.65, step=0.05)


def calculate_score(creation, activity, similarity, component, text):
    # Example formula to compute a score
    score = (activity * 0.3) + (similarity * 0.2) + (component * 0.2) + (text * 0.3)
    return score

# Calculate and display the score
score = calculate_score(creation_time, activity_level, similarity_index, component_relevance, text_similarity)
st.write(f"Meta-State Score: {score:.2f}")


def plot_scores():
    # Create data for plotting
    factors = ['Creation Time', 'Activity', 'Similarity', 'Component', 'Text']
    values = [creation_time / 100, activity_level / 50, similarity_index, component_relevance, text_similarity]
    fig, ax = plt.subplots()
    ax.bar(factors, values, color='blue')
    ax.set_ylim([0, 1])
    ax.set_ylabel('Factor Impact')
    ax.set_title('Impact of Various Factors on Meta-State Score')
    st.pyplot(fig)

plot_scores()


st.title("Dynamic Jira Ticket Resolution Simulation Based on Q-Factor")

# Function to simulate resolution times
def simulate_and_plot(q_score):
    mean_time = 30 - 20 * q_score
    std_dev = 5 * (1 - q_score)
    times = norm.rvs(loc=mean_time, scale=std_dev, size=1000)

    # Plotting
    fig, ax = plt.subplots()
    ax.hist(times, bins=30, color='skyblue', alpha=0.7)
    ax.set_title('Simulated Ticket Resolution Times')
    ax.set_xlabel('Days to Resolve')
    ax.set_ylabel('Frequency')
    st.pyplot(fig)
    return times

# Slider for Q-Factor score
q_factor = st.slider("Q-Factor Score (0 to 1 scale)", min_value=0.0, max_value=1.0, value=0.7, step=0.01, on_change=lambda: simulate_and_plot(q_factor))

# Initial plot
times = simulate_and_plot(q_factor)
st.write(f"Estimated Average Resolution Time: {np.mean(times):.2f} days")
st.write(f"Standard Deviation of Resolution Times: {np.std(times):.2f} days")


# Function to plot comparative histograms
def plot_comparative_hist(scores):
    fig, axes = plt.subplots(1, len(scores), figsize=(15, 4), sharey=True)
    for ax, score in zip(axes, scores):
        times = norm.rvs(loc=30 - 20 * score, scale=5 * (1 - score), size=1000)
        ax.hist(times, bins=30, color=np.random.choice(['skyblue', 'salmon', 'lightgreen']), alpha=0.7)
        ax.set_title(f'Q-Factor {score:.2f}')
        ax.set_xlabel('Days to Resolve')
    axes[0].set_ylabel('Frequency')
    st.pyplot(fig)

# Example scores to compare
plot_comparative_hist([0.3, 0.5, 0.7])


# Scenario testing function
def scenario_testing(base_score, adjustment):
    adjusted_score = base_score + adjustment
    base_times = simulate_and_plot(base_score)
    adjusted_times = simulate_and_plot(adjusted_score)
    st.write(f"Change in average resolution time from {np.mean(base_times):.2f} to {np.mean(adjusted_times):.2f} days")
    st.write(f"Change in standard deviation from {np.std(base_times):.2f} to {np.std(adjusted_times):.2f} days")

# User inputs for scenario testing
base_q_factor = st.slider("Base Q-Factor Score", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
adjustment = st.slider("Adjustment", min_value=-0.5, max_value=0.5, value=0.1, step=0.01)
st.button("Run Scenario Test", on_click=lambda: scenario_testing(base_q_factor, adjustment))

# Display the copyright notice
st.markdown("""
**EXPERIMENTAL**  
Copyright William Kennedy, A9 Group, Inc.
""")
