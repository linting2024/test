import yfinance as yf
import streamlit as st
import plotly.graph_objects as go

# 下載日幣匯率和日本股市數據
jpy_data = yf.download("JPY=X", start="2020-01-01", end="2024-06-30")
nikkei_data = yf.download("^N225", start="2020-01-01", end="2024-06-30")

# Streamlit 應用的標題
st.title('USD/JPY 匯率與日經225指數')

# 繪製日幣匯率和日本股市指數的組合圖
fig = go.Figure()

# 添加日幣匯率數據
fig.add_trace(go.Scatter(x=jpy_data.index, y=jpy_data['Close'], name='USD/JPY 匯率',
                         line=dict(color='blue'), yaxis='y1'))

# 添加日本股市指數數據
fig.add_trace(go.Scatter(x=nikkei_data.index, y=nikkei_data['Close'], name='日經225指數',
                         line=dict(color='red'), yaxis='y2'))

# 設定圖表的佈局
fig.update_layout(
    title='USD/JPY 匯率與日經225指數',
    xaxis_title='日期',
    yaxis=dict(title='USD/JPY 匯率', side='left', showgrid=False),
    yaxis2=dict(title='日經225指數', side='right', overlaying='y', showgrid=False),
    legend=dict(x=0.01, y=0.99, bordercolor='Black', borderwidth=1)
)

# 使用 Streamlit 顯示圖表
st.plotly_chart(fig)
