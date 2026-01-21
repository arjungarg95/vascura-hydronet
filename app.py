import streamlit as st
import plotly.graph_objects as go
import numpy as np
import pandas as pd

# --- SYSTEM CONFIGURATION ---
st.set_page_config(
    page_title="Vascura HydroNet",
    page_icon="💠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --- VASCURA DESIGN LANGUAGE (DARK MODE) ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@200;400;600;800&family=JetBrains+Mono:wght@400;500&display=swap');

:root {
    --primary:   #40c4ff;     /* bright cyan-blue   */
    --secondary: #00e676;     /* vivid green        */
    --bg:        #0a0e14;     /* very dark blue-gray*/
    --card:      #111927;     /* slightly lighter   */
    --accent:    #94a3b8;     /* cool gray          */
    --text:      #e2e8f0;     /* light slate        */
    --caption:   #94a3b8;     /* muted for captions */
    --border:    rgba(64, 196, 255, 0.18);
}

html, body, [data-testid="stAppViewContainer"] {
    background-color: var(--bg) !important;
}

.stApp { 
    background-color: var(--bg); 
    color: var(--text); 
}

/* Center Stage Hero Branding */
.hero-container {
    text-align: center;
    padding: 80px 20px;
    background: radial-gradient(circle at center, rgba(64, 196, 255, 0.12) 0%, transparent 70%);
}
.hero-title {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 7rem !important;
    font-weight: 800 !important;
    letter-spacing: -0.05em !important;
    margin-bottom: 0px !important;
    background: linear-gradient(to bottom, #e0f7ff 30%, var(--primary));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.hero-subtitle {
    font-size: 1rem;
    letter-spacing: 0.6em;
    text-transform: uppercase;
    color: var(--secondary);
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-weight: 400;
    margin-top: -10px;
}

/* Industrial Card Style – dark mode */
.eng-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 24px;
    padding: 40px;
    margin: 20px 0;
    box-shadow: 0 12px 32px rgba(0,0,0,0.4);
}

.tech-pill {
    background: rgba(0, 230, 118, 0.14);
    color: var(--secondary);
    padding: 6px 14px;
    border-radius: 8px;
    font-family: 'JetBrains Mono';
    font-size: 0.8rem;
    border: 1px solid rgba(0, 230, 118, 0.25);
    margin-right: 10px;
}

/* Tab Customization */
.stTabs [data-baseweb="tab-list"] { 
    gap: 40px; 
    justify-content: center; 
    border-bottom: 1px solid rgba(148, 163, 184, 0.15); 
}
.stTabs [data-baseweb="tab"] { 
    font-size: 1rem; 
    font-family: 'Plus Jakarta Sans'; 
    color: #94a3b8; 
    font-weight: 600; 
    text-transform: uppercase; 
    letter-spacing: 0.1em; 
}
.stTabs [data-baseweb="tab--active"] { 
    color: var(--primary) !important; 
    border-bottom: 3px solid var(--primary) !important;
}

/* General typography */
p, li, .stMarkdown {
    font-family: 'Plus Jakarta Sans', sans-serif;
    line-height: 1.6;
    color: var(--text) !important;
}

h1, h2 {
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: var(--primary);
}

h3, h4 {
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: var(--secondary);
}

.stImage figcaption,
.stCaption {
    color: var(--caption) !important;
    font-size: 0.9rem;
}

.stExpander {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 12px;
    color: var(--text);
}

.stExpander summary {
    color: var(--primary);
}

/* Improve contrast in plotly (already dark) */
.js-plotly-plot .plotly .bg {
    fill: transparent !important;
}
</style>
""", unsafe_allow_html=True)

# --- HERO SECTION (with proper unsafe_allow_html=True) ---
st.markdown("""
<div class="hero-container">
    <img 
        src="vascura_logo.png" 
        onerror="this.src='https://via.placeholder.com/140/40c4ff/0a0e14?text=Vascura';"
        style="width:140px; height:auto; margin-bottom:24px; filter: drop-shadow(0 4px 12px rgba(64,196,255,0.35));"
        alt="Vascura Logo"
    />
    
    <h1 class="hero-title">VASCURA</h1>
    <p class="hero-subtitle">HydroNet</p>
    <p style="max-width: 850px; margin: 25px auto; font-size: 1.25rem; color: var(--text); font-family: 'Plus Jakarta Sans';">
    A bio-inspired infrastructure platform that treats urban stormwater systems as living vascular networks — designed to protect ecosystems at the source.
    </p>
</div>
""", unsafe_allow_html=True)

# Rest of your code remains **exactly the same** from here onward
# (tabs, content, images, plotly, video, etc.)

tabs = st.tabs([
    "Home",
    "Team",
    "Problem",
    "Solution",
    "Progress",
    "Market",
    "Business",
    "Video",
    "References"
])

# --- TAB 1: HOME ---
with tabs[0]:
    st.markdown("<br>", unsafe_allow_html=True)
    st.header("Overview")
    st.subheader("Why Vascura?")
    st.write("""
    The name **Vascura** is derived from *vascular* and *cura*, the Latin word for care.
    It reflects our core philosophy: treating urban water systems as living vascular networks
    that require intelligent care rather than brute-force control.
    
    Just as biological vascular systems transport fluids efficiently while preventing failure,
    Vascura is built to move stormwater safely while intercepting pollution before it spreads.
    Our name captures this fusion of biology, infrastructure, and responsibility.
    """)

    st.write("""
    Microplastic pollution has become one of the most pervasive and least mitigated forms of environmental contamination in modern urban environments. Urban stormwater systems, designed primarily for volume management, inadvertently act as conduits for these particles, allowing them to bypass infrastructure and accumulate in food webs. Current mitigation is reactive, relying on screens that rapidly clog or centralized treatments incompatible with decentralized runoff. To address this, we propose the Vascura HydroNet, a modular filtration system inspired by the hydraulic efficiency of gymnosperm xylem. Physically, the filter utilizes a biomimetic ``torus-margo'' pit membrane structure arranged in graded layers to capture particles down to the micrometer scale while maintaining hydraulic conductivity. Computationally, we couple this hardware with a Physics-Informed Xylem Graph Neural Network (PIXGNN) Digital Twin. We model the water network as a system of Partial Differential Equations (PDEs) to optimize filter placement. 
    """)

    st.markdown('<div class="eng-card">', unsafe_allow_html=True)
    st.subheader("Our Business Philosophy")
    
    st.write("""
    **Mission**  
    To stop microplastic pollution at the source by transforming passive stormwater
    infrastructure into intelligent, bio-inspired filtration networks.
    
    **Vision**  
    Cities where water infrastructure actively protects ecosystems instead of quietly
    polluting them — monitored, optimized, and improved over time.
    
    **Values**  
    • Learn from nature before engineering solutions  
    • Design for real-world constraints, not idealized systems  
    • Measure impact through data, not assumptions  
    • Build infrastructure that lasts
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.image("Vascura HydroNet Innovation Image.png", caption="HydroNet Prototype Rendering", use_column_width=True)
    with col2:
        st.image("Vascura Team Picture.png", caption="The Vascura Team: Arjun Garg and Mohan Parthasarathy", use_column_width=True)

# --- TAB 2: TEAM ---
with tabs[1]:
    st.markdown("<br>", unsafe_allow_html=True)
    st.header("Our Team")
    st.subheader("Formation and Motivation")
    st.write("""
    Our partnership is built on the convergence of mathematics and biological systems. Mohan brings a deep passion for applied mathematics, having completed coursework up to Complex Analysis and serving as an officer in our school’s Math Modeling Club. His independent work on pedagogy and coupling for Physics-Informed Neural Networks (PINNs), which he will present at the Joint Mathematics Meetings in D.C. this upcoming week, forms the computational backbone of our digital twin. Arjun complements this with a strong foundation in biology, helping run our school’s Cardiology and Biotechnology clubs and having researched on multi-genome alignment and RNA sequencing at medical labs at Harvard and Johns Hopkins.
    """)
    st.write("""
    Our journey began with a failure. Standing in our garage, we watched standard filtration meshes clog in seconds, realizing that current infrastructure forces a choice between flood safety and pollution control. This frustration deepened during conversations with mentors at the U.S. Department of Energy, who confirmed that this permeability-selectivity trade-off is a massive, unsolved blind spot in urban engineering. HydroNet is our answer to that deadlock. Arjun Garg (CEO) leverages his background in computational genomics to reverse-engineer gymnosperm anatomy into manufacturable CAD designs. Mohan Parthasarathy (CTO) architects the digital brain, applying his research in mathematical modeling with Physics-Informed Neural Networks to simulate complex fluid dynamics. United by this vision, we combine the grit to build physical hardware with the high-level mathematics needed to optimize it, transforming a high school project into the engineering standard for sustainable cities.
    """)
    st.subheader("Capabilities and Skills")
    st.write("""
    We are entering this project with a lot of technical skills. We are proficient in MATLAB, which we are using to implement the finite difference methods for our PDE system, and we have the CAD skills (Fusion 360) necessary to model the modular cartridge. Both of our prior research have taught us to read technical literature and iterate from evidence, and since we’re both interested in different fields of STEM, we’re able to cover even more ground and split the project well. However, to successfully build the Vascura HydroNet, we must expand our skillset into physical fabrication and applied fluid mechanics. We need to learn how to use high-resolution SLA 3D printing to accurately replicate the micrometer-scale torus-margo structures. Also, we need to gain the skills we need to validate our digital twin using real-world sensor data rather than synthetic inputs, which we’d gain through THINK. We are eager to learn how to design hydraulic tests to produce statistically meaningful, deployable data under MIT mentorship.
    """)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="eng-card">', unsafe_allow_html=True)
        st.subheader("Mohan Parthasarathy")
        st.markdown("<span class='tech-pill'>Systems & Applied Math</span>", unsafe_allow_html=True)
        st.write("""
        Specialized in Physics-Informed Neural Networks (PINNs) and Multivariable Calculus.
        Focuses on the computational coupling of the finite difference methods with
        urban graph neural network architectures.
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="eng-card">', unsafe_allow_html=True)
        st.subheader("Arjun Garg")
        st.markdown("<span class='tech-pill'>Biomimetics & Fabrication</span>", unsafe_allow_html=True)
        st.write("""
        Research background in Multi-Genome Alignment and Biotechnology.
        Leads the design of the biomimetic torus-margo cartridges and high-fidelity
        SLA manufacturing protocols.
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    st.image("Vascura Team Picture.png", caption="The Vascura Team", use_column_width=True)

# --- TAB 3: PROBLEM ---
with tabs[2]:
    st.markdown("<br>", unsafe_allow_html=True)
    st.header("The Problem: Urban Microplastic Crisis")
    st.write("""
    Urban runoff is the single largest source of microplastics entering oceans. Every time it rains, tire wear particles and synthetic debris wash into storm drains. Municipalities face a critical operational failure because fine mesh screens clog and cause street flooding, while coarse screens let microplastics pass right through. Furthermore, cities lack data observability and cannot track the non-linear transport of contaminants through complex pipe networks.
    """)
    st.subheader("Real-World Insights")
    st.write("""
    We confronted the reality of this crisis during our meetings with the stormwater team at the Fairfax County Department of Public Works. Officials described to us how they fight a losing battle: without data, they are managing vast pipe networks blind. They explained that installing current filters often causes more problems than it solves, turning drains into dams during heavy rain and forcing their crews to manually unclog them. This feedback highlighted to us that the industry doesn't just need a scientific fix; it needs an operational one. We saw that departments are paralyzed by a lack of options and are actively searching for a solution that doesn't require choosing between flooded streets and polluted rivers.
    """)
    st.subheader("Market Gap")
    st.write("""
    As environmental regulations tighten, cities are desperate for compliance tools, yet current options remain polarized between cheap drain guards that fail quickly and million-dollar hydrodynamic separators requiring major excavation. HydroNet targets this gap in the $14 billion municipal stormwater market. By offering a modular retrofit that fits standard 2-inch piping, the system bypasses the need for expensive construction. By providing a digital twin, HydroNet offers compliance-as-a-service to help cities prove they are meeting reduction targets. HydroNet provides the only solution combining biological clog-resistance with the predictive power of AI to solve this operational nightmare.
    """)
    st.markdown('<div class="eng-card">', unsafe_allow_html=True)
    st.subheader("Key Pain Points")
    st.write("• Rapid clogging of existing filters leading to flooding.")
    st.write("• Lack of data for contaminant tracking.")
    st.write("• High costs for large-scale solutions.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- TAB 4: SOLUTION ---
with tabs[3]:
    st.markdown("<br>", unsafe_allow_html=True)
    st.header("Our Solution: Vascura HydroNet")
    st.subheader("Elevator Pitch")
    st.write("""
    Vascura HydroNet is a first-of-its-kind bio-inspired, AI-optimized defense against the urban microplastic crisis. While cities invest billions in stormwater infrastructure, microscopic tire particles and synthetic fibers bypass systems, turning drains into superhighways for pollution. Existing filters clog rapidly or restrict flow, forcing municipalities to choose between flooding and pollution. We resolve this with a dual-layer innovation. Physically, we engineered a modular cartridge inspired by gymnosperm xylem, using torus-margo membrane geometry that regulates flow and captures micrometer-scale particles without clogging. Digitally, every unit is powered by a physics-informed digital twin that predicts contaminant spread and optimizes filter placement. By converting storm drains into self-regulating networks, HydroNet offers municipalities a scalable, low-maintenance solution to meet environmental regulations. We tap into the $14 billion stormwater market with a circular economy model that transforms compliance costs into asset protection and upcycles captured waste into high-value byproducts like graphene and biochar.
    """)
    with st.expander("How It Works"):
        st.write("""
        The HydroNet is a cyber-physical system designed to secure urban water networks. Our innovation lies in decoupling filtration efficiency from hydraulic risk through a novel combination of bio-mimicry and physics-informed machine learning. Standard filters are static; they catch debris until they block water, creating a binary failure mode where municipalities must choose between pollution control and flood prevention. We have eliminated this trade-off by engineering a system that adapts to changing flow conditions physically and optimizes its own deployment digitally.
        """)
    with st.expander("Physical Hardware: Biomimetic Architecture"):
        st.write("""
        Physically, our filtration module draws inspiration from the xylem structure of gymnosperm trees. In nature, the torus-margo pit membrane allows water to flow freely while sealing off embolisms to protect the tree from cavitation [2]. We reverse-engineered this biological valve into a graded mechanical cartridge. The device features a multi-stage architecture designed to handle the chaotic hydrodynamics of storm drains. The intake utilizes a radial fin array engineered to laminarize turbulent stormwater flow. By converting turbulent flow into laminar flow, we prevent the resuspension of settled particles and allow for more efficient interception. Behind this intake, the core filtration unit is constructed from layers of torus-margo analogs. Under normal flow, water passes through highly porous margo-like strands, trapping microplastics down to the micrometer scale. However, during storm surges or when a section becomes clogged, the central torus structure shifts to open bypass channels. This passive regulation prevents the upstream flooding that causes standard mesh screens to fail. To manufacture the complex torus-margo geometry for our functional prototype, we utilize high-resolution Stereolithography (SLA) 3D printing with engineering-grade resin to achieve micrometer-scale pores. For commercial-scale production, we have designed the cartridge for high-volume injection molding using recycled Polypropylene. This ensures the units are not only cost-effective but possess the mechanical toughness to withstand hydraulic shear stress and abrasive grit during peak flow events, meeting the 'Practicality' standard for long-term urban deployment.
        """)
        col1, col2 = st.columns(2)
        with col1:
            st.image("top_view_prototype.jpg", caption="Top View of Physical Prototype", use_column_width=True)
            st.image("side_view1_prototype.jpg", caption="Side View 1 of Physical Prototype", use_column_width=True)
        with col2:
            st.image("side_view2_prototype.jpg", caption="Side View 2 of Physical Prototype", use_column_width=True)
            st.image("isometric_cad.jpg", caption="Isometric CAD View", use_column_width=True)
        st.image("back_cad.jpg", caption="Back CAD View", use_column_width=True)
        st.video("cad_rotation.mp4")
    with st.expander("Digital Software: PIXGNN Computational Core"):
        st.write("""
        Digitally, every HydroNet unit is powered by a Physics-Informed Xylem Graph Neural Network, or PIXGNN. Unlike standard black box AI which merely finds patterns in data, our model is explicitly constrained by the conservation laws of physics. We model the urban pipe network as a graph where the transport of contaminants is governed by a system of partial differential equations under fluid dynamics approximations. Simulations have shown that the software is able to effectively optimize filtration locations, reducing capital expenditure by forty to sixty percent compared to a blanket deployment.
        """)
        st.latex(r"\frac{\partial C}{\partial t} + \mathbf{u} \cdot \nabla C = D \nabla^2 C + S(x,t)")
        st.caption("The Advection-Diffusion-Source (ADS) Equation governing contaminant transport.")
        st.subheader("Dynamic Contaminant Plume Visualization")
        st.write("Our Graph Neural Network treats the urban network as a vascular map to predict 'Super-Spreader' nodes.")
        intensity = st.slider("Simulated Hydraulic Load (Discharge Rate)", 5, 100, 30)
        x = np.linspace(0, 15, 400)
        y = (intensity / 10) * np.exp(-(x - (intensity/15))**2 / (intensity/50))
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x, y=y, fill='tozeroy', line=dict(color='#1f6fa5', width=3), name="Concentration mg/L"))
        fig.update_layout(
            template="plotly_dark",
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            xaxis_title="Network Distance (km)",
            yaxis_title="Contaminant Density",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
        with st.expander("Mathematical Model"):
            st.latex(r"""
            \begin{align*}
            \frac{\partial C}{\partial t} + U \frac{\partial C}{\partial x} &= \alpha \frac{\partial^2 C}{\partial x^2} - \delta C + D_1 I \\
            \frac{\partial U}{\partial t} + U \frac{\partial U}{\partial x} &= \nu \frac{\partial^2 U}{\partial x^2} + g D_2 C \\
            \frac{\partial S}{\partial t} + U \frac{\partial S}{\partial x} &= D_s \frac{\partial^2 S}{\partial x^2} - \beta_1 S I - \beta_2 S C \\
            \frac{\partial I}{\partial t} + U \frac{\partial I}{\partial x} &= D_i \frac{\partial^2 I}{\partial x^2} + \beta_1 S I + \beta_2 S C - \gamma I \\
            \frac{\partial R}{\partial t} + U \frac{\partial R}{\partial x} &= D_r \frac{\partial^2 R}{\partial x^2} + \gamma I
            \end{align*}
            """)
            st.caption("Coupled PDE system modeling fluid dynamics and pollution spread.")
        # st.image("pinn_photo1.jpg", caption="Physics-Informed Neural Network Visualization 1", use_column_width=True)
        st.image("pinn_photo2.jpg", caption="Physics-Informed Neural Network Visualization", use_column_width=True)
    with st.expander("Impact and Intellectual Property"):
        st.write("""
        Our impact metrics are both quantitative and qualitative. We measure success through Capture Efficiency and hydraulic conductivity. Our laboratory simulations target a capture efficiency of over eighty percent for particles larger than fifty micrometers, with less than a twenty percent reduction in flow rate. Beyond these basics, our core metrics now include kilograms of microplastics captured per year, the percentage conversion yield of waste to biochar and graphene, total reduction in pollutant load, operational uptime of filter units, and the growth of recurring subscription customers for data-driven monitoring. This tracking allows us to validate that we are removing tire wear particles containing 6PPD-quinone, directly restoring ecosystem health and protecting biodiversity [8].
        """)
        st.write("""
        To protect our commercial advantage, we are pursuing a dual-track intellectual property strategy. We intend to file a utility patent for the mechanical variable-geometry of the artificial torus-margo cartridge, as this is a novel hardware invention. Simultaneously, the weighting, architecture, and xylem-inspired loss functions of the neural network, specifically the architecture and loss functions of the model, will be retained as a proprietary trade secret, preventing competitors from reverse-engineering our optimization logic.
        """)
    with st.expander("Strategic Deployment & Circularity"):
        st.write("""
        VASCURA closes the resource loop. Captured microplastics are processed through **Flash Joule Heating (FJH)**,
        transforming mixed polymer waste into high-purity **Graphene**.
        
        This graphene is then integrated into the manufacturing of our modular cartridges, increasing
        the structural integrity of the filter membranes while reducing reliance on virgin materials.
        """)
        st.write("• **UN SDG 6.3:** Improvement of ambient water quality via decentralized interception.")
        st.write("• **UN SDG 11.B:** Enhancing urban resilience against non-point source pollution.")
        st.write("• **Modular Integration:** Designed for rapid retrofitting into municipal storm drains.")

# --- TAB 5: PROGRESS ---
with tabs[4]:
    st.markdown("<br>", unsafe_allow_html=True)
    st.header("Validation and Progress")
    st.write("""
    HydroNet has moved rapidly from concept to physical validation following a tight feedback loop between computational modeling, prototyping, and expert mentorship. On the physical front, we have completed the Fusion 360 designs for the modular cartridge, including the radial fin intake and slide-out xylem core. To move beyond CAD, we constructed a functional small-scale prototype housed in a transparent clear PVC assembly to simulate our intended flow environment. This physical rig features a multi-stage graded filtration stack, allowing us to visually monitor fluid dynamics and particle interception patterns in real-time. Initial flow tests using standard steel mesh screens within this transparent housing revealed rapid clogging and immediate hydraulic failure. This failure provided critical physical evidence, visible to the naked eye, that conventional filter geometries cannot handle the particulate load of urban runoff, validating the necessity of our bio-inspired design. To refine this architecture, we are working with an official (who requested anonymity) from the US Department of Energy’s Water Power Technologies Office. This ongoing mentorship validated our torus-margo geometry and exposed critical inefficiencies in existing technologies, directly inspiring our pivot toward a circular economy model and the conversion of captured waste into graphene and biochar.
    """)
    st.subheader("Computational Validation")
    st.write("""
    On the computational front, we have written and validated a MATLAB prototype for our neural network. To ensure the mathematical rigor of our model before training, we utilized the Method of Manufactured Solutions (MMS). By constructing a known analytical solution and forcing it through our coupled PDE system, we verified that our custom finite-difference solvers converge with the correct order of accuracy. This rigorous verification step guarantees that our Digital Twin is trained on valid physical laws, not numerical artifacts. To ground this model in reality, we engaged with the Fairfax County Department of Public Works and Environmental Services. During a video conference, we walked their stormwater management team through our MATLAB code and MMS validation results. They provided critical feedback on real-world pipe connectivity that led us to incorporate a specialized xylem-based loss function into our algorithm. While the department does not specialize in contaminants, their feedback validated our computational design and confirmed a drastic market need for new products capable of handling modern drainage challenges. Our immediate next step is a laboratory demonstration using water spiked with fluorescent microplastic simulants between ten and five hundred micrometers to generate mass balance data and prove our capture efficiency targets.
    """)

# --- TAB 6: MARKET ---
with tabs[5]:
    st.markdown("<br>", unsafe_allow_html=True)
    st.header("Market Analysis")
    st.write("""
    Our thorough market research segments the opportunity starting with a Total Addressable Market of twenty billion dollars, representing the projected global stormwater management industry by 2028 [9]. We narrowed our Serviceable Available Market to the 7,550 regulated municipalities in the United States operating under MS4 permits, a sector valued at approximately four billion dollars annually. Our Serviceable Obtainable Market focuses on the five percent of these entities actively seeking smart city pilots and green infrastructure upgrades, representing an immediate two hundred million dollar opportunity.
    """)
    with st.expander("Customers and Segments"):
        st.write("""
        Crucially, the buyer and the customer in this market are often different, creating a unique entry point. While the customer is the municipal stormwater utility responsible for clean water, the buyer is often a General Contractor or Civil Engineering firm hired to execute maintenance retrofits. What is important to the City is regulatory safety: avoiding EPA fines and lawsuits. What is important to the General Contractor is low installation cost and predictability. We bridge this gap by offering a unit price of one hundred and fifty dollars, which is competitively priced against dumb catch basin inserts but offers the intelligence of a capital project. This price point allows contractors to bundle HydroNet into existing maintenance contracts without triggering complex municipal capital expenditure reviews.
        """)
    with st.expander("Industry Ecosystem"):
        st.write("""
        The industry ecosystem is driven by regulatory pressure but slowed by bureaucratic procurement. Regulators set the standards, Cities face the liability, and private Contractors execute the work. HydroNet inserts itself into this ecosystem as a compliance-as-a-service tool. By selling to the Contractors who already hold long-term maintenance agreements, we avoid the slow municipal sales cycle while providing the City with the data dashboard they crave. This positions us not just as a hardware vendor, but as an essential risk-management layer in the rapidly exploding Digital Water infrastructure market.
        """)
    data = {
        "Market Segment": ["Total Addressable Market", "Serviceable Available Market", "Serviceable Obtainable Market"],
        "Size": ["$20B (Global by 2028)", "$4B (US MS4 Permits)", "$200M (Smart City Pilots)"],
        "Focus": ["Global Stormwater Management", "US Regulated Municipalities", "Green Infrastructure Upgrades"]
    }
    df = pd.DataFrame(data)
    st.table(df)
    with st.expander("Competition"):
        st.write("""
        The competitive landscape is polarized between low-end drain guards and high-end hydrodynamic separators, leaving a critical gap in the middle market. At the low end, passive geotextile inserts suffer from a binary failure mode: either large pores let microplastics pass, or fine pores clog instantly, causing street flooding. Their need for frequent manual cleaning creates hidden labor costs exceeding the initial purchase price. At the high end, hydrodynamic separators are effective but prohibitively expensive, costing tens of thousands of dollars and requiring major excavation. They work for new construction but are unscalable for retrofitting millions of existing storm drains.
        """)
        st.write("""
        HydroNet disrupts this middle market by combining the low footprint of a drain guard with the high performance of a separator. Our positioning is "smart retrofitting." We compete on operational expenditure reduction rather than just hardware price. Our primary advantages are the patentable torus-margo geometry and the proprietary PIXGNN model. No other competitor uses variable-geometry filtration, enabling us to capture smaller particles without the flood risk of static meshes. Furthermore, existing solutions lack data observability; they are "dumb" hardware requiring manual checks. In contrast, our digital twin provides the missing data layer, telling operators exactly when to clean filters and saving thousands in labor hours.
        """)
        st.write("""
        Our main disadvantage is the initial capital intensity of injection molding compared to cheap fabric. We offset this through a superior ROI driven by extended maintenance intervals. While municipal procurement is difficult, partnering with agile private-sector General Contractors allows us to bypass red tape. Finally, emerging 6PPD-quinone regulations create a regulatory moat, transforming our specific particle-targeting capability from a luxury into a legal necessity that generic competitors cannot match [8].
        """)
        comparison_data = {
            "Aspect": ["Cost", "Performance", "Installation", "Maintenance", "Data Observability"],
            "HydroNet": ["Medium ($150/unit)", "High (80%+ capture)", "Retrofit (no excavation)", "Low (predictive)", "High (Digital Twin)"],
            "Low-End Guards": ["Low", "Low", "Easy", "High (frequent cleaning)", "None"],
            "High-End Separators": ["High ($10k+)", "High", "Difficult (excavation)", "Medium", "Low"]
        }
        comp_df = pd.DataFrame(comparison_data)
        st.table(comp_df)
    with st.expander("Go-to-Market Strategy"):
        st.write("""
        We will bypass the slow direct-to-city sales cycle by positioning HydroNet as a strategic bid-winner for General Contractors. Large engineering firms frequently bid on stormwater retrofits but struggle to differentiate their proposals or meet strict new microplastic removal mandates. By partnering with us, a regional General Contractor gains a competitive edge, promising superior compliance data to the city while we gain immediate distribution. Our initial beachhead market will be university campuses and designated green city pilot zones, which offer high visibility and significantly lower bureaucratic barriers than full municipal deployments. Once validated in these controlled environments, our goal is to have HydroNet formally spec-in to standard civil engineering blueprints. This makes our technology the default requirement for future municipal contracts, effectively locking out competitors. Long-term, we will transition to a licensing model, offering our PIXGNN software to other hardware manufacturers to become the intelligence layer for the entire global industry.
        """)
        st.write("• University campuses for pilot testing.")
        st.write("• Green city pilot zones for visibility.")
        st.write("• Direct partnerships with general contractors.")
        st.write("• Licensing for long-term scalability.")
        st.write("• Distribution through existing maintenance contracts.")

# --- TAB 7: BUSINESS ---
with tabs[6]:
    st.markdown("<br>", unsafe_allow_html=True)
    st.header("Business Model")
    st.write("""
    Our business model is simple: we sell the hardware once, but the intelligence every month. We generate revenue through three streams. First is Hardware. We sell the permanent housing and LPWAN sensor suite for one hundred and fifty dollars. By utilizing a disposable-core architecture, we keep production costs at scale to approximately fifty-five dollars. This provides a sustainable margin while lowering the entry barrier for municipalities. Second is Consumables. The 3D-printed xylem cartridges act like 'printer ink,' ensuring a steady recurring revenue stream.
    """)
    st.write("""
    Third, and most importantly, is Software. We charge fifty dollars per node, per month, for the Digital Twin dashboard. This is a bargain for the customer: cities currently pay unionized crews over one hundred dollars per hour to manually inspect drains that may not even be clogged. Paying six hundred dollars a year to know exactly when to send a truck saves thousands in wasted labor and EPA fines.
    """)
    with st.expander("Circular Economy"):
        st.write("""
        To handle the circular economy realistically without a massive fleet, we use a standard automotive "core charge" model. When a contractor buys a new cartridge, they pay a deposit. They only recover that cash if they mail us the old, saturated cartridge in a provided prepaid box. This financial incentive ensures the plastic comes back to us automatically. We then aggregate these recovered cartridges and bulk-transport them to conversion partners to be transformed into graphene and biochar. This allows us to monetize the waste material while ensuring a closed loop, all without incurring the capital expense of a dedicated logistics network. Despite high initial R&D costs, by piggybacking on existing contractor logistics, we expect to break even by year three, as demonstrated in our first additional attachment.
        """)
    revenue_data = {
        "Revenue Stream": ["Hardware", "Consumables", "Software"],
        "Description": ["One-time sale of housing and sensors", "Recurring cartridge replacements", "Monthly subscription for dashboard"],
        "Pricing": ["$150/unit", "Variable (ink model)", "$50/node/month"],
        "Cost": ["$55/unit at scale", "Low", "Minimal (cloud-based)"]
    }
    rev_df = pd.DataFrame(revenue_data)
    st.table(rev_df)

# --- TAB 8: FUNDRAISING ---
# with tabs[7]:
#     st.markdown("<br>", unsafe_allow_html=True)
#     st.header("Fundraising and Resources")
#     st.write("""
#     We are seeking five thousand dollars in pre-seed funding to bridge the gap between our current CAD models and a field-deployable unit. Our immediate budget allocates nine hundred and thirty-seven dollars for critical prototyping materials, including a Phrozen Sonic Mini 8K S printer ($350) for high-resolution fabrication, engineering-grade resin ($100), and a suite of turbidity and pressure sensors ($117). The remaining pre-seed funds will cover patent filing fees to protect our torus-margo geometry and legal costs for incorporation. To fully develop the product and execute a market rollout, we project a subsequent capital need of fifteen thousand dollars to fund initial injection molding tooling and a fifty-unit pilot production run. We are prioritizing non-dilutive funding sources like the MIT THINK Scholars Program to de-risk the technology before seeking angel investment. We are lean, student-led, and capital-efficient.
#     """)
#     st.subheader("Project Budget")
#     budget_data = {
#         "Item": ["Phrozen Sonic Mini 8K S (22μm Res)", "Aqua-Gray 8K Resin (1kg)", "Submersible Water Pump (Adjustable)", "Gravity: Analog Water Pressure Sensor", "Flow Rate Sensor (1 inch)", "Raspberry Pi 4 (Data Logging)", "Turbidity Sensor", "PVC Pipes, Caps, and Connectors", "Silicone O-Rings (Pack of 10)", "Fluorescent Microplastic Simulants"],
#         "Amount": [1, 2, 1, 2, 1, 1, 1, "Various", 1, "1 set"],
#         "Supplier": ["Phrozen 3D", "Phrozen 3D", "Amazon", "DFRobot", "Adafruit", "CanaKit", "DFRobot", "Home Depot", "Walmart", "Cospheric"],
#         "Cost ($)": [350.00, 100.00, 45.00, 32.00, 25.00, 55.00, 60.00, 80.00, 15.00, 175.00]
#     }
#     budg_df = pd.DataFrame(budget_data)
#     st.table(budg_df)
#     st.write("**Total: $937.00**")

# --- TAB 9: VIDEO ---
with tabs[7]:
    st.markdown("<br>", unsafe_allow_html=True)
    st.header("Pitch Video")
    st.write("""
    Watch our 5-minute pitch video demonstrating the HydroNet innovation, including prototypes, models, and how it works.
    """)
    st.video("https://youtu.be/CAmE3-J0Uvo")
    st.write("""
    In this video, we showcase the biomimetic design, computational modeling, and potential impact of Vascura HydroNet.
    """)

# --- TAB 10: REFERENCES ---
with tabs[8]:
    st.markdown("<br>", unsafe_allow_html=True)
    st.header("References and Attachments")
    st.subheader("Citations")
    st.write("""
    Boutilier, M. S., Lee, J., Chambers, V., Venkatesh, V., and Karnik, R. (2014). Water filtration using plant xylem. PLoS One, 9(2):e89934.
    
    Hitchcock, J. N. (2020). Storm events as key moments of microplastic contamination in aquatic ecosystems. Science of the Total Environment, 734:139361.
    
    Jambeck, J. R., Geyer, R., Wilcox, C., Siegler, T. R., Perryman, M., Andrady, A., Narayan, R., and Law, K. L. (2015). Plastic waste inputs from land into the ocean. Science, 347(6223):768–771.
    
    Karniadakis, G. E., Kevrekidis, I. G., Lu, L., Perdikaris, P., Wang, S., and Yang, L. (2021). Physics-informed machine learning. Nature Reviews Physics, 3(6):422–440.
    
    Prata, J. C., da Costa, J. P., Lopes, I., Duarte, A. C., and Rocha-Santos, T. (2019). Solutions and integrated strategies for the control and mitigation of plastic and microplastic pollution. International Journal of Environmental Research and Public Health, 16(13):2411.
    
    Raissi, M., Perdikaris, P., and Karniadakis, G. E. (2019). Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations. Journal of Computational Physics, 378:686–707.
    
    Scarselli, F., Gori, M., Tsoi, A. C., Hagenbuchner, M., and Monfardini, G. (2008). The graph neural network model. IEEE Transactions on Neural Networks, 20(1):61–80.
    """)
    # st.subheader("Additional Resources")
    # st.write("For more details, refer to our attached documents:")
    # st.write("• Vascura HydroNet Pitch.pdf")
    # st.write("• Vascura HydroNet Supplementals.pdf")
    # st.write("• Vascura HydroNet References.pdf")

# --- GLOBAL FOOTER ---
st.divider()
st.markdown("""
<center style="opacity: 0.5; font-family: 'JetBrains Mono'; font-size: 0.8rem; letter-spacing: 0.15em; color: #94a3b8;">
VASCURA HYDRONET // EST. 2025 <br>
Arjun Garg & Mohan Parthasarathy <br>
Student‑led research team based in Virginia, USA
</center>
""", unsafe_allow_html=True)
