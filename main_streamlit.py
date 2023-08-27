import streamlit as st
import time


st.write('プログレスバーの表示')

if st.checkbox('timer start !!'):
    'start!!'
    latest_iteration = st.empty() #空を追加

    bar = st.progress(0)
    for i in range(100):
        latest_iteration.text(f'Iteration {i+1}')
        bar.progress(i+1)
        time.sleep(0.1)
    'Done!!!!!'



#2カラム化
st.write('第２カラムか')

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右からむ')

#expander
expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1の回答')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2の回答')