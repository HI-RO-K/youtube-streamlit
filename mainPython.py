from tkinter import Image
import streamlit as st
import numpy as np
import pandas as pd

st.title('Streamlit 超入門')

st.write('Display Image')

img = Image.open('sample.JPG')

st.image(img, caption='book', use_column_width=True)

# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )

# st.map(df)

# st.table(df.style.highlight_max(axis=0))

