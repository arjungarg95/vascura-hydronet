import streamlit as st
import plotly.graph_objects as go
import numpy as np
import pandas as pd

# --- SYSTEM CONFIGURATION ---
st.set_page_config(
    page_title="VASCURA | HydroNet Infrastructure Portal",
    page_icon="💠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --- VASCURA DESIGN LANGUAGE (Custom CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@200;400;600;800&family=JetBrains+Mono:wght@400;500&display=swap');

    :root {
        --primary: #00f2ff;
        --secondary: #00ff9d;
        --bg: #020408;
        --card: #0a1018;
    }

    .stApp { background-color: var(--bg); color: #cbd5e1; }
    
    /* Center Stage Hero Branding */
    .hero-container {
        text-align: center;
        padding: 80px 20px;
        background: radial-gradient(circle at center, rgba(0, 242, 255, 0.08) 0%, transparent 70%);
    }
    .hero-title {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        font-size: 7rem !important;
        font-weight: 800 !important;
        letter-spacing: -0.05em !important;
        margin-bottom: 0px !important;
        background: linear-gradient(to bottom, #fff 40%, #64748b);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .hero-subtitle {
        font-size: 1rem;
        letter-spacing: 0.6em;
        text-transform: uppercase;
        color: var(--primary);
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        font-weight: 400;
        margin-top: -10px;
    }

    /* Industrial Card Style */
    .eng-card {
        background: var(--card);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 24px;
        padding: 40px;
        margin-top: 20px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.4);
    }
    
    .tech-pill {
        background: rgba(0, 242, 255, 0.1);
        color: var(--primary);
        padding: 6px 14px;
        border-radius: 8px;
        font-family: 'JetBrains Mono';
        font-size: 0.8rem;
        border: 1px solid rgba(0, 242, 255, 0.2);
        margin-right: 10px;
    }

    /* Tab Customization */
    .stTabs [data-baseweb="tab-list"] { gap: 40px; justify-content: center; border-bottom: 1px solid rgba(255,255,255,0.05); }
    .stTabs [data-baseweb="tab"] { font-size: 1rem; font-family: 'Plus Jakarta Sans'; color: #64748b; font-weight: 600; text-transform: uppercase; letter-spacing: 0.1em; }
    .stTabs [data-baseweb="tab--active"] { color: var(--primary) !important; }
    </style>
    """, unsafe_allow_html=True)

# --- HERO SECTION ---
st.markdown("""
    <div class="hero-container">
        <h1 class="hero-title">VASCURA</h1>
        <p class="hero-subtitle">HydroNet Systems</p>
        <p style="max-width: 850px; margin: 25px auto; font-size: 1.25rem; color: #94a3b8; font-family: 'Plus Jakarta Sans';">
            Pioneering a decentralized, bio-inspired filtration infrastructure. 
            By merging the physics of gymnosperm xylem with Graph Neural Intelligence, 
            we intercept microplastic contamination at the urban source.
        </p>
    </div>
    """, unsafe_allow_html=True)

# --- CLEAN NAVIGATION TABS ---
tabs = st.tabs([
    "Executive Vision", 
    "Biomimetic Architecture", 
    "Computational Core", 
    "Industrial Scale",
    "Technical Personnel"
])

# --- TAB 1: EXECUTIVE VISION ---
with tabs[0]:
    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2 = st.columns([1.2, 1])
    with c1:
        st.markdown('<div class="eng-card">', unsafe_allow_html=True)
        st.subheader("The Infrastructure Crisis")
        st.write("""
        Current municipal stormwater systems are designed primarily for volumetric management, not particulate precision. 
        As a result, they act as high-speed conduits for micro-debris, bypassing infrastructure and entering food webs. 
        
        **VASCURA** transforms these passive networks into active, intelligent filtration nodes. Our system is designed 
        to be installed within existing storm drain geometries, utilizing biological principles to maintain 
        high hydraulic conductivity while capturing particles down to the 20μm scale.
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with c2:
        st.markdown('<div class="eng-card">', unsafe_allow_html=True)
        st.subheader("Physical Constraints")
        # Actual scientific indicators instead of "fake performance"
        st.write("• **Advection-Dominant Transport:** Solving the Peclet number trade-off in urban flow.")
        st.write("• **Embolism Resistance:** Utilizing torus-margo valves for surge protection.")
        st.write("• **Saturated Conductivity ($K_{sat}$):** Optimized for zero-overflow storm events.")
        st.markdown('</div>', unsafe_allow_html=True)

# --- TAB 2: BIOMIMETIC ARCHITECTURE ---
with tabs[1]:
    st.markdown("<br>", unsafe_allow_html=True)
    st.header("Hardware: The Torus-Margo Solution")
    
    col_l, col_r = st.columns([1, 1])
    with col_l:
        st.write("""
        The Vascura cartridge is inspired by the hierarchical structure of **Gymnosperm Xylem**. 
        In nature, these vascular systems transport water under high tension while preventing catastrophic 
        air embolisms (clogging). 
        
        Our biomimetic filter replicates the **Torus-Margo pit membrane**. The 'Margo' acts as a high-surface-area 
        sieve, while the 'Torus' functions as a passive valve that regulates flow velocity. This allows 
        the system to capture microplastics without the 'blinding' or surface-clogging typically seen in 
        static mesh filters.
        """)
        
        
        
        st.markdown("""
        <div class="eng-card" style="margin-top:40px;">
            <h3>Fabrication Fidelity</h3>
            <span class="tech-pill">SLA Stereolithography</span>
            <span class="tech-pill">20μm Resolution</span>
            <p style="margin-top:15px; font-size: 0.95rem;">
            Standard FDM (Filament) printing cannot replicate the intricate margo structures required for 
            functional hydraulic regulation. We utilize high-resolution resin photopolymerization to 
            recreate the exact geometry necessary for non-clogging microplastic interception.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col_r:
        
        st.caption("Conceptual Fluid Pathway Iteration")

# --- TAB 3: COMPUTATIONAL CORE ---
with tabs[2]:
    st.markdown("<br>", unsafe_allow_html=True)
    st.header("PIXGNN: The Physics-Informed Digital Twin")
    
    st.latex(r"\frac{\partial C}{\partial t} + \mathbf{u} \cdot \nabla C = D \nabla^2 C + S(x,t)")
    st.caption("The Advection-Diffusion-Source (ADS) Equation governing contaminant transport.")

    st.markdown('<div class="eng-card">', unsafe_allow_html=True)
    st.subheader("Dynamic Contaminant Plume Visualization")
    st.write("Our Graph Neural Network treats the urban network as a vascular map to predict 'Super-Spreader' nodes.")
    
    intensity = st.slider("Simulated Hydraulic Load (Discharge Rate)", 5, 100, 30)
    
    x = np.linspace(0, 15, 400)
    y = (intensity / 10) * np.exp(-(x - (intensity/15))**2 / (intensity/50))
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, fill='tozeroy', line=dict(color='#00f2ff', width=3), name="Concentration mg/L"))
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis_title="Network Distance (km)",
        yaxis_title="Contaminant Density",
        height=400
    )
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    

# --- TAB 4: INDUSTRIAL SCALE ---
with tabs[3]:
    st.markdown("<br>", unsafe_allow_html=True)
    st.header("Strategic Deployment & Circularity")
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="eng-card">', unsafe_allow_html=True)
        st.subheader("Flash-Joule Upcycling")
        st.write("""
        VASCURA closes the resource loop. Captured microplastics are processed through **Flash Joule Heating (FJH)**, 
        transforming mixed polymer waste into high-purity **Graphene**. 
        
        This graphene is then integrated into the manufacturing of our modular cartridges, increasing 
        the structural integrity of the filter membranes while reducing reliance on virgin materials.
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        




    with c2:
        st.markdown('<div class="eng-card">', unsafe_allow_html=True)
        st.subheader("Global Policy Alignment")
        st.write("• **UN SDG 6.3:** Improvement of ambient water quality via decentralized interception.")
        st.write("• **UN SDG 11.B:** Enhancing urban resilience against non-point source pollution.")
        st.write("• **Modular Integration:** Designed for rapid retrofitting into municipal storm drains.")
        st.markdown('</div>', unsafe_allow_html=True)

# --- TAB 5: TECHNICAL PERSONNEL ---
with tabs[4]:
    st.markdown("<br>", unsafe_allow_html=True)
    st.header("Project Leadership")
    
    p1, p2 = st.columns(2)
    with p1:
        st.markdown('<div class="eng-card">', unsafe_allow_html=True)
        st.subheader("Mohan Parthasarathy")
        st.markdown("<span class='tech-pill'>Systems & Applied Math</span>", unsafe_allow_html=True)
        st.write("""
        Specialized in Physics-Informed Neural Networks (PINNs) and Complex Analysis. 
        Focuses on the computational coupling of the finite difference methods with 
        urban graph neural network architectures.
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    with p2:
        st.markdown('<div class="eng-card">', unsafe_allow_html=True)
        st.subheader("Arjun Garg")
        st.markdown("<span class='tech-pill'>Biomimetics & Fabrication</span>", unsafe_allow_html=True)
        st.write("""
        Research background in Multi-Genome Alignment and Biotechnology. 
        Leads the design of the biomimetic torus-margo cartridges and high-fidelity 
        SLA manufacturing protocols.
        """)
        st.markdown('</div>', unsafe_allow_html=True)

# --- GLOBAL FOOTER ---
st.divider()
st.markdown("""
    <center style="opacity: 0.4; font-family: 'JetBrains Mono'; font-size: 0.75rem; letter-spacing: 0.2em;">
        VASCURA SYSTEMS // DECENTRALIZED INFRASTRUCTURE ARCHIVE // EST. 2026
    </center>
    """, unsafe_allow_html=True)
