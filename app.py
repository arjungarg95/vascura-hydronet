import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from datetime import datetime

# --- CONFIGURATION & BRANDING ---
st.set_page_config(
    page_title="Vascura HydroNet | Advanced Urban Resilience",
    page_icon="💠",
    layout="wide",
)

# --- ADVANCED CUSTOM STYLING (The "Handcrafted" Look) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;800&family=JetBrains+Mono:wght@300;500&display=swap');

    :root {
        --primary: #00e5ff;
        --secondary: #00ff9d;
        --bg-dark: #03070c;
        --card-bg: rgba(13, 20, 30, 0.7);
    }

    /* Global Overrides */
    .main { background-color: var(--bg-dark); }
    p, li { font-family: 'Plus Jakarta Sans', sans-serif; color: #a1a1aa; line-height: 1.8; font-size: 1.05rem; }
    h1, h2, h3 { font-family: 'Plus Jakarta Sans', sans-serif; font-weight: 800; letter-spacing: -0.03em; }

    /* Custom Official Header */
    .official-header {
        border-left: 4px solid var(--primary);
        padding-left: 20px;
        margin-bottom: 40px;
    }

    /* Engineering Card Style */
    .eng-card {
        background: var(--card-bg);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 24px;
        padding: 35px;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
    .eng-card:hover {
        border-color: var(--primary);
        box-shadow: 0 0 30px rgba(0, 229, 255, 0.1);
    }

    /* Sidebar Navigation */
    section[data-testid="stSidebar"] {
        background-color: #060a0f !important;
        border-right: 1px solid rgba(255, 255, 255, 0.05);
    }

    /* Status Pill */
    .status-pill {
        background: rgba(0, 229, 255, 0.1);
        color: var(--primary);
        border: 1px solid var(--primary);
        padding: 4px 12px;
        border-radius: 100px;
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.1em;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR & GLOBAL STATS ---
with st.sidebar:
    st.markdown("### VASCURA // ARCHIVE")
    st.markdown("`SYSTEM STATUS: OPTIMIZED`")
    nav = st.radio("ARCHIVE SECTIONS", [
        "01 // EXECUTIVE SUMMARY", 
        "02 // BIOMIMETIC HARDWARE", 
        "03 // PIXGNN COMPUTATIONAL CORE", 
        "04 // STRATEGIC OPERATIONS", 
        "05 // THE VASCURA TEAM"
    ])
    st.divider()
    st.markdown("### PROJECT TELEMETRY")
    st.metric("PARTICLE RES", "20μm", "Target")
    st.metric("HYDRAULIC COND", "94%", "Predicted")
    st.caption("Last Update: Jan 2026")

# --- SECTION 01: EXECUTIVE SUMMARY ---
if nav == "01 // EXECUTIVE SUMMARY":
    st.markdown('<div class="official-header">', unsafe_allow_html=True)
    st.markdown('<span class="status-pill">THINK Scholar // Conrad Finalist</span>', unsafe_allow_html=True)
    st.title("Vascura HydroNet: The Future of Urban Water Resilience")
    st.markdown('</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1.5, 1])
    with col1:
        st.write("""
        Microplastic pollution is the most pervasive form of environmental contamination in modern urban environments. 
        Traditional stormwater infrastructure acts as a passive conduit, funneling tire wear, synthetic textiles, 
        and fragmented packaging directly into our food webs.

        **Vascura HydroNet** is a decentralized, intelligent filtration ecosystem. By inverting the 
        mechanics of gymnosperm xylem and coupling it with Physics-Informed Neural Networks, we transform 
        cities from pollution sources into active purification hubs.
        """)
        
        st.markdown("### CORE OBJECTIVES")
        st.markdown("""
        - **Precision Interception:** Capturing micro-particles without catastrophic pressure loss.
        - **Predictive Placement:** Using Digital Twins to identify 'Super-Spreader' nodes in pipe networks.
        - **Resource Circularity:** Converting waste into industrial-grade graphene and biochar.
        """)
    
    with col2:
        st.image("https://images.unsplash.com/photo-1518066000714-58c45f1a2c0a?auto=format&fit=crop&q=80&w=800", caption="Urban Runoff: The Invisible Threat")

# --- SECTION 02: BIOMIMETIC HARDWARE ---
elif nav == "02 // BIOMIMETIC HARDWARE":
    st.title("02 // Hardware Engineering")
    st.write("Solving the 'Permeability-Selectivity' trade-off through 400 million years of botanical evolution.")

    

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        <div class="eng-card">
            <h3>Torus-Margo Architecture</h3>
            <p>Our filter utilizes a biomimetic pit membrane structure. Unlike static meshes, the <b>Torus-Margo</b> acts as a dynamic valve. 
            Under normal flow, the porous 'margo' traps microplastics. During storm surges, the central 'torus' helps regulate 
            hydraulic conductivity, preventing the embolism-like failures seen in traditional filters.</p>
            <span style="color:#00e5ff; font-family:'JetBrains Mono';">FABRICATION: SLA PHOTOPOLYMERIZATION</span>
        </div>
        """, unsafe_allow_html=True)
    
    with c2:
        st.markdown("""
        <div class="eng-card">
            <h3>Graded Layering System</h3>
            <p>We distribute the filtration load across hierarchical pathways. By grading the 'vascular' channels within 
            the modular cartridge, we reduce the rate of surface blinding (clogging), extending the maintenance 
            cycle by a predicted <b>240%</b> over standard storm-drain screens.</p>
            <span style="color:#00ff9d; font-family:'JetBrains Mono';">RESOLUTION: 20 MICROMETER</span>
        </div>
        """, unsafe_allow_html=True)

    st.divider()
    st.subheader("Physical Prototype Iteration")
    st.write("Iteration from Fusion 360 CAD to SLA fabrication allows us to replicate the functional micrometer-scale features of the torus-margo.")

# --- SECTION 03: PIXGNN COMPUTATIONAL CORE ---
elif nav == "03 // PIXGNN COMPUTATIONAL CORE":
    st.title("03 // Computational Intelligence")
    st.write("Bridging Fluid Dynamics and Graph Theory via Physics-Informed Neural Networks.")
    
    st.latex(r'''
    \underbrace{\frac{\partial C}{\partial t} + \mathbf{u} \cdot \nabla C}_{\text{Advection}} = \underbrace{D \nabla^2 C}_{\text{Diffusion}} + \underbrace{\sum S_i}_{\text{Sources}}
    ''')
    
    st.markdown("""
    ### The PIXGNN Framework
    The city is a vascular network. Our **Physics-Informed Xylem Graph Neural Network (PIXGNN)** treats pipes as edges 
    and junctions as nodes. We apply a spatially-extended **SIR (Susceptible-Infected-Recovered)** model where:
    - **Infected Nodes:** High concentration microplastic hotspots.
    - **Recovered Nodes:** Nodes protected by Vascura filtration units.
    """)

    # --- INTERACTIVE SIMULATION (PLOTLY) ---
    st.subheader("Simulated Contaminant Plume Convergence")
    x = np.linspace(0, 10, 100)
    y = np.exp(-0.5 * (x - 5)**2) + np.random.normal(0, 0.05, 100)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Pollutant Load', line=dict(color='#00e5ff', width=3)))
    fig.update_layout(
        template="plotly_dark", 
        paper_bgcolor='rgba(0,0,0,0)', 
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis_title="Distance from Entry Point (km)",
        yaxis_title="Concentration (mg/L)"
    )
    st.plotly_chart(fig, use_container_width=True)

# --- SECTION 04: STRATEGIC OPERATIONS ---
elif nav == "04 // STRATEGIC OPERATIONS":
    st.title("04 // Business & Strategic Roadmap")
    
    col1, col2 = st.columns([1, 1.5])
    
    with col1:
        st.markdown("### REVENUE STREAMS")
        st.write("""
        1. **MUNICIPAL CAPEX:** Direct sale and installation of modular hardware.
        2. **SaaS (Software as a Service):** Subscription to the PIXGNN Digital Twin for predictive maintenance alerts.
        3. **CIRCULAR RECOVERY:** Wholesale revenue from recovered carbon materials (Graphene/Biochar).
        """)
        
    with col2:
        st.markdown("### IMPLEMENTATION TIMELINE")
        timeline = {
            "Phase": ["R&D", "SLA Prototyping", "Hydraulic Testing", "Pilot Deployment", "Scale-Up"],
            "Completion": [100, 85, 40, 10, 0]
        }
        st.table(pd.DataFrame(timeline))

    st.markdown("""
    <div class="eng-card" style="border-left: 4px solid #00ff9d;">
        <h3>Circular Economy Impact</h3>
        <p>By processing captured microplastics through <b>Flash-Joule Heating</b>, we recover carbon that would otherwise 
        enter the ocean. This graphene derivative is high-purity and suitable for soil remediation, effectively 
        turning an environmental liability into a municipal asset.</p>
    </div>
    """, unsafe_allow_html=True)

# --- SECTION 05: THE VASCURA TEAM ---
elif nav == "05 // THE VASCURA TEAM":
    st.title("05 // Leadership & Expertise")
    
    c1, c2 = st.columns(2)
    
    with c1:
        st.markdown("""
        <div class="eng-card">
            <h2>Mohan Parthasarathy</h2>
            <p style="color:#00e5ff; font-family:'JetBrains Mono';">SYSTEMS STRATEGY & APPLIED MATH</p>
            <p>Specializing in Complex Analysis and Math Modeling. Mohan manages the mathematical coupling 
            of the PDE systems and the municipal economic integration of the HydroNet ecosystem.</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="eng-card">
            <h2>Arjun Garg</h2>
            <p style="color:#00ff9d; font-family:'JetBrains Mono';">CFD & BIOMIMETIC FABRICATION</p>
            <p>Specializing in Biotechnology and Computational Fluid Dynamics. Arjun leads the 
            SLA fabrication process and the hardware-software interfacing of the Digital Twin.</p>
        </div>
        """, unsafe_allow_html=True)

    st.divider()
    st.markdown("### OUR PARTNERS & ADVISORS")
    st.caption("Proudly developing under the mentorship of the MIT THINK Program and the Conrad Challenge. Dedicated to solving SDG 6, 11, and 12.")

# --- FOOTER ---
st.markdown("<br><br><center style='color:#444; font-size:0.8rem;'>VASCURA HYDRONET // OFFICIAL ARCHIVE // CLASSIFIED [PUBLIC] // 2026</center>", unsafe_allow_html=True)
