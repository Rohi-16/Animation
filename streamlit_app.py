import streamlit as st
import streamlit.components.v1 as components
import html

# Page config
st.set_page_config(page_title="Animated Name Banner Generator", page_icon="✨", layout="centered")

st.markdown("<h1 style='text-align:center;margin-bottom:0.1rem'>Animated Name Banner Generator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:#999;margin-top:0.1rem'>Generate a premium, Apple-style animated hero — copy the HTML+CSS and paste anywhere.</p>", unsafe_allow_html=True)
st.write("")

# Inputs
col1, col2 = st.columns([2, 1])
with col1:
    name = st.text_input("Enter your name / brand", value="NovaSync")
    tagline = st.text_input("Enter tagline (optional)", value="Intelligence. Elegance. Innovation.")
with col2:
    font_size = st.slider("Title size (px)", 48, 160, 80)
    glow = st.slider("Glow intensity", 0, 40, 18)

st.write("---")

# Build the animated HTML snippet (single HTML file string)
escaped_name = html.escape(name)
escaped_tagline = html.escape(tagline)

snippet = f"""<!-- Animated Hero - paste into your HTML file -->
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<title>{escaped_name} — Animated Banner</title>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;600&display=swap" rel="stylesheet">
<style>
  /* ===== Reset & layout ===== */
  html,body{{height:100%;margin:0}}
  body{{display:flex;align-items:center;justify-content:center;background:#020205; font-family:'Poppins',sans-serif; -webkit-font-smoothing:antialiased; -moz-osx-font-smoothing:grayscale;}}
  .hero-wrap{{width:100%;max-width:1100px;padding:48px;box-sizing:border-box;position:relative;overflow:hidden;min-height:320px;display:flex;align-items:center;justify-content:center;flex-direction:column}}

  /* ===== Particles (pure CSS) ===== */
  .particle {{
    position:absolute;
    width:10px; height:10px;
    background: radial-gradient(circle, rgba(255,255,255,0.85) 0%, rgba(255,255,255,0.12) 40%, rgba(255,255,255,0) 100%);
    border-radius:50%;
    filter: blur(6px);
    animation: float 8s linear infinite;
    opacity:0.7;
  }}
  /* generate variety via nth-child */
  .particle:nth-child(1){{left:8%; top:14%; animation-duration:10s; transform:scale(1.6)}}
  .particle:nth-child(2){{left:28%; top:8%; animation-duration:12s; transform:scale(1.2)}}
  .particle:nth-child(3){{left:72%; top:10%; animation-duration:9s; transform:scale(1.4)}}
  .particle:nth-child(4){{left:88%; top:30%; animation-duration:11s; transform:scale(0.9)}}
  .particle:nth-child(5){{left:12%; top:70%; animation-duration:14s; transform:scale(1.1)}}
  .particle:nth-child(6){{left:40%; top:82%; animation-duration:13s; transform:scale(0.9)}}
  .particle:nth-child(7){{left:68%; top:76%; animation-duration:10s; transform:scale(1.5)}}
  .particle:nth-child(8){{left:48%; top:40%; animation-duration:16s; transform:scale(2)}}

  @keyframes float {{
    0% {{ transform: translateY(0) scale(var(--s,1)); opacity:0.65; }}
    50% {{ transform: translateY(-28px) scale(var(--s,1.05)); opacity:0.95; }}
    100% {{ transform: translateY(0) scale(var(--s,1)); opacity:0.65; }}
  }}

  /* ===== Glowing radial behind the text ===== */
  .glow {{
    position:absolute;
    width:60vmax;
    height:60vmax;
    left:50%;
    top:40%;
    transform:translate(-50%,-50%);
    background: radial-gradient(circle at center, rgba(255,255,255,0.14), rgba(255,255,255,0.02) 25%, transparent 60%);
    filter: blur({glow}px);
    opacity:0.9;
    animation: pulse 6s ease-in-out infinite;
    pointer-events:none;
  }}
  @keyframes pulse {{
    0% {{ transform:translate(-50%,-50%) scale(0.98); opacity:0.85; }}
    50% {{ transform:translate(-50%,-50%) scale(1.03); opacity:1; }}
    100% {{ transform:translate(-50%,-50%) scale(0.98); opacity:0.85; }}
  }}

  /* ===== Title & shimmer ===== */
  .title {{
    font-size:{font_size}px;
    line-height:1;
    font-weight:600;
    letter-spacing:2px;
    margin:0;
    padding:0;
    color:transparent;
    display:inline-block;
    -webkit-background-clip:text;
    background-clip:text;
    background: linear-gradient(90deg, #bfbfbf, #ffffff 40%, #dcdcdc 60%, #bfbfbf);
    -webkit-text-fill-color:transparent;
    transform: translateY(18px);
    opacity:0;
    animation: titleIn 1s cubic-bezier(.2,.9,.2,1) forwards 0.25s;
    position:relative;
  }}
  .title::after {{
    content:'';
    position:absolute;
    inset:0;
    left:-120%;
    background: linear-gradient(120deg, transparent 0%, rgba(255,255,255,0.75) 50%, transparent 100%);
    transform: skewX(-15deg);
    animation: shine 2.2s ease-in-out 1.1s forwards;
    mix-blend-mode:overlay;
    pointer-events:none;
  }}

  @keyframes titleIn {{
    from {{ opacity:0; transform: translateY(28px) scale(0.98); filter: blur(6px); }}
    to   {{ opacity:1; transform: translateY(0) scale(1); filter: blur(0); }}
  }}
  @keyframes shine {{
    0% {{ left:-120%; }}
    60% {{ left:120%; }}
    100% {{ left:120%; opacity:0; }}
  }}

  /* Tagline */
  .tagline {{
    margin-top:14px;
    color:#bfbfbf;
    font-weight:300;
    font-size:18px;
    opacity:0;
    transform: translateY(8px);
    animation: tagIn 1s ease forwards 1.2s;
  }}
  @keyframes tagIn {{
    from {{ opacity:0; transform:translateY(12px); }}
    to {{ opacity:1; transform:translateY(0); }}
  }}

  /* Responsive tweaks */
  @media (max-width:720px) {{
    .hero-wrap{{padding:32px}}
    .title{{font-size: clamp(32px, 12vw, {font_size}px)}}
    .tagline{{font-size:14px}}
  }}
</style>
</head>
<body>
  <div class="hero-wrap" role="img" aria-label="{escaped_name} animated hero">
    <div class="glow" aria-hidden="true"></div>

    <!-- Particles -->
    <div class="particle" style="--s:1.6"></div>
    <div class="particle" style="--s:1.2"></div>
    <div class="particle" style="--s:1.4"></div>
    <div class="particle" style="--s:0.9"></div>
    <div class="particle" style="--s:1.1"></div>
    <div class="particle" style="--s:0.9"></div>
    <div class="particle" style="--s:1.5"></div>
    <div class="particle" style="--s:2"></div>

    <!-- Title -->
    <h1 class="title">{escaped_name}</h1>
    <div class="tagline">{escaped_tagline}</div>
  </div>
</body>
</html>"""

# Show live preview inside Streamlit (embedding the snippet)
st.markdown("### Live preview")
components.html(snippet, height=420, scrolling=False)

st.write("")
st.markdown("### HTML + CSS (copy & paste)")
st.info("Tip: Click the Copy button below to copy the entire snippet to clipboard. You can paste it into a file like `banner.html` and open in browser. For Twitter — screen-record or convert to GIF.")

# Create an embeddable copy button + text area using a tiny HTML wrapper
copy_html = f"""
<html>
  <body>
    <textarea id="code" style="display:none">{html.escape(snippet)}</textarea>
    <button id="copyBtn" style="border:0;padding:10px 14px;border-radius:8px;background:#111;color:#fff;cursor:pointer">
      Copy snippet to clipboard
    </button>
    <script>
      const btn = document.getElementById('copyBtn');
      btn.addEventListener('click', async () => {{
        const txt = document.getElementById('code').value;
        try {{
          await navigator.clipboard.writeText(txt);
          btn.innerText = 'Copied ✅';
          setTimeout(()=> btn.innerText = 'Copy snippet to clipboard', 1800);
        }} catch(e) {{
          alert('Copy failed — please select and copy manually.');
        }}
      }});
    </script>
  </body>
</html>
"""

# Render the copy button (this lives outside the code block)
components.html(copy_html, height=60)

# Show code in a scrollable block as well
st.code(snippet, language="html")

st.write("---")
st.markdown("### How to use")
st.markdown("""
1. Click **Copy snippet to clipboard**.  
2. Create a file `banner.html`, paste, open in browser — or paste the snippet into your site/template.  
3. To post on Twitter / LinkedIn: open the snippet in a browser and record a **5–8s** screen capture (OBS/Loom or a phone screen recorder) and post the clip or convert it to GIF.  
4. For README.md (GitHub): GitHub does not execute inline CSS the same as a web page; recommend linking to the animation via an image/GIF or host a small demo page and link it in your README.
""")

st.success("Your animated banner is ready. Customize colors, sizes, and timing in the snippet to create different themes.")