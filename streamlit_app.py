import streamlit as st

# Page setup
st.set_page_config(page_title="Luxury Text Animation", page_icon="✨", layout="centered")

# Custom CSS animation
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;600&display=swap');

    body {
      background: radial-gradient(circle at top, #0a0a0a, #000);
      height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;
      color: white;
      font-family: 'Poppins', sans-serif;
    }

    .container {
      text-align: center;
      margin-top: 15vh;
    }

    .reveal-text {
      font-size: 3rem;
      font-weight: 600;
      letter-spacing: 2px;
      display: inline-block;
      background: linear-gradient(90deg, #d6d6d6, #ffffff, #bfbfbf);
      background-clip: text;
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      color: #fff;
      opacity: 0;
      transform: translateY(30px);
      animation: reveal 1.8s ease forwards 0.5s;
      position: relative;
      overflow: hidden;
    }

    .reveal-text::after {
      content: "";
      position: absolute;
      top: 0;
      left: -100%;
      width: 100%;
      height: 100%;
      background: linear-gradient(120deg, transparent 0%, rgba(255,255,255,0.7) 50%, transparent 100%);
      animation: shimmer 2s ease-in-out 2s infinite;
    }

    .tagline {
      font-weight: 300;
      color: #bbb;
      opacity: 0;
      animation: fadeIn 1.5s ease forwards 2s;
      font-size: 1.1rem;
      margin-top: 0.8rem;
    }

    @keyframes reveal {
      0% {
        opacity: 0;
        transform: translateY(30px);
        filter: blur(10px);
      }
      100% {
        opacity: 1;
        transform: translateY(0);
        filter: blur(0);
      }
    }

    @keyframes shimmer {
      0% { left: -100%; }
      100% { left: 100%; }
    }

    @keyframes fadeIn {
      0% { opacity: 0; transform: translateY(10px); }
      100% { opacity: 1; transform: translateY(0); }
    }

    @media (max-width: 600px) {
      .reveal-text {
        font-size: 2.4rem;
      }
      .tagline {
        font-size: 1rem;
      }
    }
    </style>

    <div class="container">
        <h1 class="reveal-text">NovaSync</h1>
        <p class="tagline">Intelligence. Elegance. Innovation.</p>
    </div>
""", unsafe_allow_html=True)
