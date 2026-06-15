import streamlit as st

st.title("Hello Streamlit")

st.header("헤더입니다")
st.subheader("서브헤더입니다")

st.write("일반 텍스트")

st.markdown("# Markdown H1")
st.markdown("## Markdown H2")
st.markdown("### Markdown H3")

st.write("😀 Streamlit 공부중")

"""
### 텍스트 색상 변경

:red[맨유]

:blue[첼시]

:green[맨시티]

:orange[아스날]

:gray[토트넘]
"""

'#:blue[Streamlit 그래프]'

import pandas as pd
import numpy as np

st.write("# 그래프 예제")

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
)

st.area_chart(chart_data)

st.line_chart(chart_data)

st.bar_chart(chart_data)

st.scatter_chart(chart_data)

import matplotlib.pyplot as plt
import numpy as np

st.write("# :blue[시각화 라이브러리]")

st.write("#### :orange[Matplotlib: st.pyplot()]")

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()

ax.plot(x, y)

st.pyplot(fig)


