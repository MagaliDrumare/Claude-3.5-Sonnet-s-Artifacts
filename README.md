# Claude-3.5-Sonnet-s-Artifacts

### Claude Advances the LLM Interface
- https://www.deeplearning.ai/the-batch/claude-3-5-sonnets-artifacts-feature-makes-it-easier-to-build-and-code-on-site/
- https://aiexplorer.io/guides-ia/comment-utiliser-artifacts-de-claude-3-5-sonnet/

### Prompt create a streamlit App 

import streamlit as st
import pandas as pd
import numpy as np

### Set page title
st.set_page_config(page_title="My Streamlit App")

### Add a title
st.title("Welcome to My Streamlit App")

### Add some text
st.write("This is a simple demonstration of Streamlit's capabilities.")

### Create a sidebar
st.sidebar.header("Sidebar")
user_input = st.sidebar.text_input("Enter your name", "Guest")
st.sidebar.write(f"Hello, {user_input}!")

### Create a dataframe
df = pd.DataFrame({
    'Column 1': [1, 2, 3, 4],
    'Column 2': [10, 20, 30, 40]
})

### Display the dataframe
st.subheader("Sample DataFrame")
st.dataframe(df)

### Create a line chart
st.subheader("Line Chart")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C'])
st.line_chart(chart_data)

### Add a button
if st.button("Click me!"):
    st.balloons()

 ### How to run a streamlit App 
 Running Streamlit on an Apple Mac with an M2 chip is generally straightforward, as Python and most of its packages now have native support for Apple Silicon. Here's a step-by-step guide to get Streamlit running on your Mac M2:

1. Install Python:
   If you haven't already, install Python. For M2 Macs, it's recommended to use Python 3.9 or later, which has native ARM support.

   - You can download Python from the official website: https://www.python.org/downloads/macos/
   - Or use Homebrew (if installed) by running: `brew install python`

2. Set up a virtual environment (recommended):
   It's a good practice to use virtual environments for your projects. Open Terminal and run:

   ```
   python3 -m venv streamlit_env
   source streamlit_env/bin/activate
   ```

3. Install Streamlit:
   With your virtual environment activated, install Streamlit using pip:

   ```
   pip install streamlit
   ```

4. Create your Streamlit app:
   Create a Python file (e.g., `app.py`) and add your Streamlit code. You can use the example I provided earlier or create your own.

5. Run the Streamlit app:
   In the Terminal, navigate to the directory containing your app file and run:

   ```
   streamlit run app.py
   ```

   Streamlit should open your default web browser and display your app.

Additional tips:

- If you encounter any issues with package installations, make sure you're using the latest pip version:
  ```
  pip install --upgrade pip
  ```

- Some packages might require Rosetta 2 to run. If you haven't installed it yet, you can do so by running this command in Terminal:
  ```
  softwareupdate --install-rosetta
  ```

- If you prefer using Anaconda, there's now a native ARM64 version available for M1/M2 Macs, which can simplify package management.

- Make sure your code editor (if you're using one) is running natively on ARM for the best performance.

If you run into any specific errors or issues while setting up or running Streamlit on your Mac M2, please let me know, and I'll be happy to help troubleshoot.

