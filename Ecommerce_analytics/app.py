import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path
from io import BytesIO
st.set_page_config(page_title="E-commerce Intelligence",page_icon="🛍️",layout="wide",initial_sidebar_state="expanded")
BG = "#100D20"
SIDEBAR = "#17132B"
CARD = "#211B38"
CARD2 = "#292344"
PURPLE = "#A78BFA"
CYAN = "#22D3EE"
ORANGE = "#F59E0B"
GREEN = "#34D399"
PINK = "#F472B6"
RED = "#FB7185"
TEXT = "#F8FAFC"
MUTED = "#A8A3BC"

PALETTE = [
    PURPLE, CYAN, ORANGE, GREEN,
    PINK, RED, "#818CF8", "#2DD4BF"
]# ==========================================================
# 3. CUSTOM CSS
# ==========================================================

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {{
    font-family: 'Inter', sans-serif;
}}

.stApp {{
    background: linear-gradient(135deg, {BG} 0%, #17112B 55%, #100D20 100%);
    color: {TEXT};
}}

[data-testid="stHeader"] {{
    background: transparent;
}}

[data-testid="stSidebar"] {{
    background: {SIDEBAR};
    border-right: 1px solid #342B50;
}}

[data-testid="stSidebar"] * {{
    color: {TEXT};
}}

.main .block-container {{
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1500px;
}}

h1, h2, h3 {{
    color: {TEXT} !important;
    font-weight: 700 !important;
}}

p, label, span {{
    color: {TEXT};
}}

.stMarkdown p {{
    color: {MUTED};
}}

div[data-testid="stMetric"] {{
    background: {CARD};
    border: 1px solid #3B3158;
    padding: 18px;
    border-radius: 14px;
    box-shadow: 0 5px 18px rgba(0,0,0,0.15);
}}

div[data-testid="stMetricLabel"] {{
    color: {MUTED} !important;
}}

div[data-testid="stMetricValue"] {{
    color: {TEXT} !important;
    font-size: 27px;
    font-weight: 800;
}}

div[data-testid="stMetricDelta"] {{
    color: {GREEN} !important;
}}

div[data-testid="stPlotlyChart"] {{
    background: {CARD};
    border: 1px solid #3B3158;
    border-radius: 15px;
    padding: 8px;
}}

div[data-testid="stDataFrame"] {{
    background: {CARD};
    border-radius: 12px;
}}

.stButton button, .stDownloadButton button {{
    background: linear-gradient(90deg, #7C3AED, #A78BFA);
    color: white;
    border: none;
    border-radius: 9px;
    font-weight: 600;
}}

.stButton button:hover, .stDownloadButton button:hover {{
    border: 1px solid {CYAN};
    color: white;
}}

hr {{
    border-color: #39304E;
}}

div[data-testid="stExpander"] {{
    background: {CARD};
    border: 1px solid #3B3158;
    border-radius: 12px;
}}

div[data-testid="stAlert"] {{
    border-radius: 12px;
}}

[data-testid="stCaptionContainer"] {{
    color: {MUTED};
}}

</style>
""", unsafe_allow_html=True)
 # 4.REUSEABLE CHART THEME
def style_chart(fig, height=380):
    fig.update_layout(
        template="plotly_dark",
        height=height,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter", color=TEXT,size=11),
        title=dict(font=dict(size=16, color=TEXT), x=0.03),
        margin=dict(l=25, r=25, t=65, b=35),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1, font=dict(color=MUTED)),
        hoverlabel=dict(bgcolor=CARD2,font_color=TEXT))
    fig.update_xaxes(gridcolor="#39304E",zerolinecolor="39304E")
    fig.update_yaxes(gridcolor="#39304E",zerolinecolor="39304E")
    return fig



                    