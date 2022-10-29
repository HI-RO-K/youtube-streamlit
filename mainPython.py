import streamlit as st
import time
st.title('Streamlit 超入門')

st.write('Interactive Widgets')

'Start!!'

latest_iteration =st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.01)

option = st.sidebar.text_input('あなたの趣味を教えてください。')

condition = st.sidebar.slider('あなたの調子は？', 0, 50, 100)
'あなたの好きな趣味は、', option, 'です。'
'コンディション：', condition


# img = Image.open('sample.JPG')

# st.image(img, caption='book', use_column_width=True)



# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )

# st.map(df)

# st.table(df.style.highlight_max(axis=0))

