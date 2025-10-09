
import streamlit as st

PRIMARY = "#4f46e5"  # violet-600
ACCENT = "#0ea5e9"   # sky-500

def inject_base_css():
    st.markdown(
        f'''
        <style>
        .stApp {{
            background: radial-gradient(1200px 600px at 10% 0%, rgba(78,70,229,0.08), transparent 60%),
                        radial-gradient(800px 400px at 90% 10%, rgba(14,165,233,0.08), transparent 60%);
        }}
        .card {{
            border-radius: 16px; padding: 16px; background: white; 
            box-shadow: 0 6px 24px rgba(79,70,229,0.15);
            border: 1px solid rgba(79,70,229,0.12);
        }}
        .badge {{
            display:inline-block; padding: 4px 10px; border-radius: 999px;
            color: white; background: linear-gradient(90deg, {PRIMARY}, {ACCENT});
            font-weight: 600; font-size: 12px;
        }}
        .progress-wrap {{ margin: 6px 0 10px; }}
        .progress-bar {{
            height: 10px; border-radius: 8px; background: #eef2ff; overflow: hidden;
        }}
        .progress-bar > div {{ height: 10px; background: {PRIMARY}; width: 0%; }}
        </style>
        ''', unsafe_allow_html=True
    )

def brand_header(title: str, subtitle: str = ""):
    st.markdown(
        f'''
        <div class="card" style="background:linear-gradient(90deg,{PRIMARY},{ACCENT});">
          <div style="display:flex;align-items:center;gap:10px;">
            <div style="font-size:28px;">🧠</div>
            <div>
              <div style="color:white;font-weight:800;font-size:20px;">{title}</div>
              <div style="color:#e0f2fe;font-size:13px;">{subtitle}</div>
            </div>
          </div>
        </div>
        ''', unsafe_allow_html=True
    )

def prob_bar(label: str, pct: float):
    pct = max(0, min(100, pct))
    st.markdown(
        f'''
        <div class="progress-wrap">
            <div style="font-weight:600;margin:2px 0 6px;">{label}: {pct:.1f}%</div>
            <div class="progress-bar"><div style="width:{pct:.1f}%;"></div></div>
        </div>
        ''', unsafe_allow_html=True
    )
