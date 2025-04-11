import streamlit as st
from streamlit_lottie import st_lottie
import requests
from page1 import HomePage
from utl import goto

# Load Lottie animation from URL
def load_lottieurl(url: str):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

# Lottie animations
lottie_ai = load_lottieurl("https://lottie.host/519f9670-1f79-4b42-90a1-e01d627c2b90/ZgQYmzqEpK.json")
lottie_dev = load_lottieurl("https://lottie.host/36923c1f-9f30-426e-b0fd-5ae9f58a2583/g6eNiDeRQC.json")

# Glowing multi-color header
def glowing_header(text):
    st.markdown(f"""
    <h1 style='text-align: center; font-size: 3em; text-shadow:
        0 0 5px #ff00ff,
        0 0 10px #00ffff,
        0 0 15px #ff9900,
        0 0 20px #00ffcc,
        0 0 25px #cc00ff,
        0 0 30px #ff0066;'>
        {text}
    </h1>
    """, unsafe_allow_html=True)

# Animated card block
def animated_card(title, description, icon, link=None):
    card_html = f"""
    <div style="padding: 1rem; border-radius: 15px; background: linear-gradient(145deg, #1e1e1e, #2a2a2a);
                box-shadow: 0 0 15px rgba(0, 255, 255, 0.4), 0 0 30px rgba(255, 0, 255, 0.4);
                color: #fff; margin-bottom: 1rem; transition: transform 0.3s ease-in-out;">
        <h3 style="color: #00ffff;">{icon} {title}</h3>
        <p>{description}</p>
        {'<a style="color: #ffd700; font-weight: bold;" href="'+link+'" target="_blank">🔗 Learn more</a>' if link else ''}
    </div>
    """
    st.markdown(card_html, unsafe_allow_html=True)

# Lead Developer Profile Section
def developer_section():
    st.markdown("""
    <h2 style='text-align: center; margin-bottom: 2rem;'>
        <span style='display: inline-block; 
                    animation: float 3s ease-in-out infinite; 
                    color: #00ffff;
                    text-shadow: 0 0 10px rgba(0, 255, 255, 0.7);'>👑</span> 
        <span style='background: linear-gradient(90deg, #00ffff, #ff00ff);
                    -webkit-background-clip: text;
                    background-clip: text;
                    color: transparent;
                    animation: gradientShift 5s ease infinite;
                    background-size: 200% 200%;'>Development Team</span>
    </h2>
    <style>
        @keyframes float {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-10px); }
            100% { transform: translateY(0px); }
        }
        @keyframes gradientShift {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        .lead-card {
            background: linear-gradient(135deg, #1a1a2e, #16213e);
            border-radius: 15px;
            padding: 2rem;
            margin: 0 auto 2rem;
            max-width: 800px;
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3);
            border-left: 5px solid #00ffff;
            transition: all 0.4s ease;
            animation: cardEntrance 1s ease-out;
        }
        .lead-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 30px rgba(0, 255, 255, 0.2);
        }
        @keyframes cardEntrance {
            from { opacity: 0; transform: scale(0.9); }
            to { opacity: 1; transform: scale(1); }
        }
        .lead-profile {
            display: flex;
            align-items: center;
            gap: 2rem;
        }
        .lead-img {
            width: 150px;
            height: 150px;
            border-radius: 50%;
            object-fit: cover;
            border: 3px solid #00ffff;
            box-shadow: 0 0 20px rgba(0, 255, 255, 0.5);
            transition: all 0.3s ease;
            animation: pulse 2s infinite;
        }
        .lead-img:hover {
            transform: scale(1.05);
        }
        @keyframes pulse {
            0% { box-shadow: 0 0 0 0 rgba(0, 255, 255, 0.7); }
            70% { box-shadow: 0 0 0 15px rgba(0, 255, 255, 0); }
            100% { box-shadow: 0 0 0 0 rgba(0, 255, 255, 0); }
        }
        .lead-info h3 {
            color: #00ffff;
            font-size: 1.8rem;
            margin-bottom: 0.5rem;
            animation: textGlow 2s ease-in-out infinite alternate;
        }
        @keyframes textGlow {
            from { text-shadow: 0 0 5px rgba(0, 255, 255, 0.5); }
            to { text-shadow: 0 0 15px rgba(0, 255, 255, 0.8); }
        }
        .lead-title {
            color: #ff66cc;
            font-weight: bold;
            margin-bottom: 1rem;
        }
        .lead-bio {
            color: #aaa;
            line-height: 1.6;
        }
        .team-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1.5rem;
            margin-top: 2rem;
        }
        .team-card {
            background: rgba(30, 30, 46, 0.8);
            border-radius: 10px;
            padding: 1.5rem;
            transition: all 0.3s ease;
            border-top: 3px solid #2a52be;
            animation: cardEntrance 1s ease-out;
            animation-delay: calc(var(--order) * 0.1s);
        }
        .team-card:hover {
            transform: translateY(-5px);
            background: rgba(30, 30, 46, 1);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
        }
        .team-img {
            width: 100px;
            height: 100px;
            border-radius: 50%;
            object-fit: cover;
            margin: 0 auto 1rem;
            display: block;
            border: 2px solid #2a52be;
        }
        .team-name {
            text-align: center;
            color: #2a52be;
            font-weight: bold;
            margin-bottom: 0.5rem;
        }
        .team-role {
            text-align: center;
            color: #777;
            font-size: 0.9rem;
            margin-bottom: 1rem;
        }
        .social-links {
            display: flex;
            justify-content: center;
            gap: 1rem;
        }
        .social-icon {
            color: #2a52be;
            font-size: 1.2rem;
            transition: all 0.3s ease;
        }
        .social-icon:hover {
            color: #00ffff;
            transform: scale(1.2);
        }
    </style>
    """, unsafe_allow_html=True)

    # Lead Developer Section
    with st.container():
        st.markdown("""
        <div class="lead-card">
            <div class="lead-profile">
                <img src="./Ayush.jpg" class="lead-img">
                <div class="lead-info">
                    <h3>Ayush Kathoke</h3>
                    <div class="lead-title">Lead Developer & AI Specialist</div>
                    <div class="lead-bio">
                        Leading the development of cutting-edge AI solutions with expertise in NLP and machine learning.
                        Passionate about building innovative tools that enhance education and productivity.
                    </div>
                    <div class="social-links">
                        <a href="#" class="social-icon">🐙</a>
                        <a href="#" class="social-icon">💼</a>
                        <a href="#" class="social-icon">🌐</a>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Team Members Grid
        st.markdown("""
        <div class="team-grid">
            <div class="team-card" style="--order: 1">
                <img src="./Ayush.jpg" class="team-img">
                <div class="team-name">Team Member 1</div>
                <div class="team-role">Frontend Developer</div>
                <div class="social-links">
                    <a href="#" class="social-icon">🐙</a>
                    <a href="#" class="social-icon">💼</a>
                    <a href="#" class="social-icon">🌐</a>
                </div>
            </div>
            <div class="team-card" style="--order: 2">
                <img src="https://via.placeholder.com/150" class="team-img">
                <div class="team-name">Team Member 2</div>
                <div class="team-role">Backend Developer</div>
                <div class="social-links">
                    <a href="#" class="social-icon">🐙</a>
                    <a href="#" class="social-icon">💼</a>
                    <a href="#" class="social-icon">🌐</a>
                </div>
            </div>
            <div class="team-card" style="--order: 3">
                <img src="https://via.placeholder.com/150" class="team-img">
                <div class="team-name">Team Member 3</div>
                <div class="team-role">UI/UX Designer</div>
                <div class="social-links">
                    <a href="#" class="social-icon">🐙</a>
                    <a href="#" class="social-icon">💼</a>
                    <a href="#" class="social-icon">🌐</a>
                </div>
            </div>
            <div class="team-card" style="--order: 4">
                <img src="https://via.placeholder.com/150" class="team-img">
                <div class="team-name">Team Member 4</div>
                <div class="team-role">QA Engineer</div>
                <div class="social-links">
                    <a href="#" class="social-icon">🐙</a>
                    <a href="#" class="social-icon">💼</a>
                    <a href="#" class="social-icon">🌐</a>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Enhanced launch button
    st.markdown("""
    <style>
        .stButton>button {
            width: 100%;
            padding: 1rem;
            border-radius: 8px;
            background: linear-gradient(90deg, #00ffff, #ff00ff);
            color: white;
            font-weight: bold;
            border: none;
            font-size: 1.2rem;
            margin-top: 2rem;
            transition: all 0.3s ease;
            animation: gradientShift 5s ease infinite;
            background-size: 200% 200%;
        }
        .stButton>button:hover {
            transform: scale(1.02);
            box-shadow: 0 0 20px rgba(0, 255, 255, 0.5);
        }
    </style>
    """, unsafe_allow_html=True)

# Module Features
def module_info():
    st.markdown("## 📦 Modules & Capabilities")
    animated_card("Question Extraction", "Find key sentences from content using transformers.", "❓")
    animated_card("Answer Generator", "Context-based generation of accurate answers.", "✅")
    animated_card("PDF & Text Upload", "Upload PDF, DOCX, or TXT formats.", "📂")
    animated_card("Export Results", "Download Q&A in CSV, JSON, Word.", "📁")
    animated_card("Dark/Light Theme", "Beautiful design across themes.", "🎨")
    animated_card("Real-Time Feedback", "Instant processing and AI interaction.", "⚡")
    animated_card("Multilingual Support", "Supports various regional and international languages.", "🌐")
    animated_card("Text Summarization", "Auto summarization of lengthy input before QA.", "📜")
    animated_card("Rich Text Editor", "Edit content live before running the AI.", "📝")

# Main Home function
def Home():
    st.set_page_config(
        page_title="Question Answering Generator",
        page_icon="📚",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Style
    st.markdown("""
        <style>
            html, body, [class*="css"]  {
                background-color: #0f0f0f;
                color: #ffffff;
                font-family: 'Segoe UI', sans-serif;
            }
            a {
                color: #00ffff;
            }
        </style>
    """, unsafe_allow_html=True)

    glowing_header("📚 Question Answering Generator")
    st.markdown("<h3 style='text-align: center; color: #ff66cc;'>Empowering Educators, Students & Professionals</h3>", unsafe_allow_html=True)

    if lottie_ai:
        st_lottie(lottie_ai, height=250, speed=1, key="ai")

    st.markdown("## ✨ Core Features")
    col1, col2 = st.columns(2)
    with col1:
        animated_card("AI-Based QA Generator", "Uses SOTA NLP models for question answering.", "🤖")
        animated_card("PDF & Text Upload", "Upload PDFs, DOCX or paste raw text.", "📄")
        animated_card("Export Options", "Save output in JSON, CSV or DOCX.", "💾")
    with col2:
        animated_card("Multilingual QA", "Supports multiple languages.", "🌍")
        animated_card("Theme Adaptive", "Beautiful experience across light & dark themes.", "🌓")
        animated_card("Instant Start", "No config needed. One-click to launch AI.", "🚀")

    module_info()
    developer_section()

    if lottie_dev:
        st_lottie(lottie_dev, height=200, speed=1, key="dev")

    st.button("🚀 Launch AI Module", on_click=goto("Main_page"))

if "current_page" not in st.session_state:
    st.session_state.current_page = "home"

if st.session_state.current_page == "home":
    Home()
elif st.session_state.current_page == "Main_page":
    HomePage()
