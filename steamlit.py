import streamlit as st
import random

# Oldal beállításai
st.set_page_config(
    page_title="Interaktív HTML Tanulás",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS stílusok hozzáadása fehér szöveghez
st.markdown("""
<style>
    /* Az előnézeti doboz stílusai */
    .html-preview {
        background-color: #1E1E1E;
        color: white;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #444;
        min-height: 300px;
    }
    
    /* Fehér szöveg biztosítása az előnézetben */
    .html-preview h1, .html-preview h2, .html-preview h3, 
    .html-preview h4, .html-preview h5, .html-preview h6,
    .html-preview p, .html-preview div, .html-preview span,
    .html-preview li, .html-preview a {
        color: white !important;
    }
    
    /* Linkek stílusa */
    .html-preview a {
        color: #4FC3F7 !important;
        text-decoration: underline;
    }
    
    /* Gomb stílusok */
    .stButton button {
        width: 100%;
    }
    
    /* Kód blokkok */
    .stCodeBlock {
        border: 1px solid #444;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

# Főcím
st.title("🚀 Interaktív HTML Tanuló")
st.markdown("Fedezd fel a HTML alapjait interaktív gyakorlatokkal!")
st.markdown("---")

# Munkamenet állapotok inicializálása
if 'current_exercise' not in st.session_state:
    st.session_state.current_exercise = 0
if 'user_code' not in st.session_state:
    st.session_state.user_code = ""
if 'show_solution' not in st.session_state:
    st.session_state.show_solution = False
if 'quiz_score' not in st.session_state:
    st.session_state.quiz_score = 0
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'quiz_finished' not in st.session_state:
    st.session_state.quiz_finished = False

# HTML alapok szekció
st.header("📚 HTML Alapok")

# Interaktív kód szerkesztő
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("💻 Írd meg a kódot:")
    
    # Alap HTML szerkezet
    base_code = """<!DOCTYPE html>
<html>
<head>
    <title>Az én oldalam</title>
    <style>
        body {{
            background-color: #1E1E1E;
            color: white;
            font-family: Arial, sans-serif;
            padding: 20px;
        }}
        h1, h2, h3, h4, h5, h6 {{
            color: white;
        }}
        p, div, span {{
            color: white;
        }}
        a {{
            color: #4FC3F7;
        }}
        li {{
            color: white;
        }}
    </style>
</head>
<body>
    {user_content}
</body>
</html>"""
    
    # Felhasználó kódjának szerkesztése
    user_content = st.text_area(
        "Írd ide a HTML kódodat:",
        height=200,
        placeholder='<h1>Üdvözöllek!</h1>\n<p>Ez az én weboldalam.</p>\n<a href="#">Ez egy link</a>',
        key="user_code_input"
    )
    
    # Előnézet gomb
    if st.button("🔍 Mutasd az előnézetet!", use_container_width=True):
        st.session_state.user_code = user_content

with col2:
    st.subheader("👀 Előnézet:")
    
    if st.session_state.user_code:
        # HTML megjelenítése fehér szöveggel
        try:
            full_html = base_code.format(user_content=st.session_state.user_code)
            st.components.v1.html(full_html, height=350, scrolling=True)
        except Exception as e:
            st.error("Hiba történt az előnézet megjelenítésekor")
            st.info("Próbáld meg egyszerűsíteni a kódot")
    else:
        st.info("Írj be valamilyen HTML kódot, majd kattints az előnézet gombra!")
        
        # Példa előnézet
        st.markdown("""
        <div class="html-preview">
            <h1 style="color: white;">Példa cím</h1>
            <p style="color: white;">Itt fog megjelenni a HTML kódod eredménye fehér szöveggel.</p>
            <a href="#" style="color: #4FC3F7;">Példa link</a>
        </div>
        """, unsafe_allow_html=True)

# Gyakorlatok szekció
st.header("🎯 Gyakorlatok")

exercises = [
    {
        "title": "1. Címek és bekezdések",
        "description": "Készíts egy oldalt, ami tartalmaz egy főcímet (h1), alcímet (h2) és egy bekezdést (p)!",
        "hint": "Használd a <h1>, <h2> és <p> tag-eket!",
        "solution": """<h1>Üdvözöllek a weboldalamon!</h1>
<h2>Rólam</h2>
<p>Ez az első weboldalam, amit készítek.</p>"""
    },
    {
        "title": "2. Lista készítése",
        "description": "Készíts egy rendezetlen listát 3 kedvenc ételedről!",
        "hint": "Használd a <ul> és <li> tag-eket!",
        "solution": """<ul>
<li>Pizza</li>
<li>Hamburger</li>
<li>Saláta</li>
</ul>"""
    },
    {
        "title": "3. Kép és link",
        "description": "Szúrj be egy képet és egy linket!",
        "hint": "Használd a <img> és <a> tag-eket!",
        "solution": """<img src="https://via.placeholder.com/150/333/white?text=KEP" width="150" alt="Példa kép">
<a href="https://www.google.com" style="color: #4FC3F7;">Google kereső</a>"""
    },
    {
        "title": "4. Színes szöveg",
        "description": "Készíts egy piros és egy zöld szövegrészletet!",
        "hint": "Használd a <span> tag-et style attribútummal!",
        "solution": """<p>Ez egy <span style="color: #FF6B6B;">piros</span> és egy <span style="color: #51CF66;">zöld</span> szöveg.</p>"""
    }
]

# Gyakorlat választó
current_exercise = st.selectbox(
    "Válassz egy gyakorlatot:",
    range(len(exercises)),
    format_func=lambda x: exercises[x]["title"]
)

# Gyakorlat megjelenítése
if current_exercise is not None:
    exercise = exercises[current_exercise]
    
    st.subheader(exercise["title"])
    st.write(exercise["description"])
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Gyakorlat kód szerkesztője
        practice_code = st.text_area(
            "Írd meg a megoldást:",
            height=150,
            key=f"exercise_{current_exercise}",
            value=st.session_state.get(f"exercise_{current_exercise}_code", "")
        )
        
        # Gombok
        col_btn1, col_btn2, col_btn3 = st.columns(3)
        
        with col_btn1:
            if st.button("💡 Tipp", key=f"hint_{current_exercise}", use_container_width=True):
                st.info(f"**Tipp:** {exercise['hint']}")
        
        with col_btn2:
            if st.button("✅ Megoldás", key=f"solution_{current_exercise}", use_container_width=True):
                st.session_state.show_solution = True
        
        with col_btn3:
            if st.button("🔍 Teszt", key=f"test_{current_exercise}", use_container_width=True):
                if practice_code:
                    test_html = base_code.format(user_content=practice_code)
                    st.components.v1.html(test_html, height=200, scrolling=True)
                else:
                    st.warning("Először írj be valamilyen kódot!")
    
    with col2:
        if st.session_state.show_solution:
            st.success("**Megoldás:**")
            st.code(exercise["solution"], language="html")
            
            # Megoldás tesztelése
            st.components.v1.html(
                base_code.format(user_content=exercise["solution"]), 
                height=200, 
                scrolling=True
            )
            
            if st.button("✖️ Megoldás elrejtése", key=f"hide_{current_exercise}"):
                st.session_state.show_solution = False

# Interaktív játék
st.header("🎮 HTML Kvíz")

quiz_questions = [
    {
        "question": "Melyik tag jelöl egy bekezdést?",
        "options": ["<p>", "<h1>", "<div>", "<span>"],
        "correct": 0
    },
    {
        "question": "Hogyan szúrunk be képet?",
        "options": [
            "<img src='kep.jpg'>",
            "<image src='kep.jpg'>", 
            "<picture src='kep.jpg'>",
            "<photo src='kep.jpg'>"
        ],
        "correct": 0
    },
    {
        "question": "Melyik a helyes link formátum?",
        "options": [
            "<a href='https://example.com'>Link</a>",
            "<link href='https://example.com'>Link</link>",
            "<a url='https://example.com'>Link</a>",
            "<href>https://example.com</href>"
        ],
        "correct": 0
    },
    {
        "question": "Hogyan készítünk rendezetlen listát?",
        "options": [
            "<ul><li>elem</li></ul>",
            "<ol><li>elem</li></ol>",
            "<list><item>elem</item></list>",
            "<ul><item>elem</item></ul>"
        ],
        "correct": 0
    }
]

if not st.session_state.quiz_finished:
    question = quiz_questions[st.session_state.current_question]
    
    st.subheader(f"Kérdés {st.session_state.current_question + 1}/{len(quiz_questions)}")
    st.write(question["question"])
    
    # Válasz opciók
    selected_option = st.radio(
        "Válassz egy választ:",
        question["options"],
        key=f"question_{st.session_state.current_question}"
    )
    
    if st.button("✅ Válasz ellenőrzése", key=f"check_{st.session_state.current_question}"):
        if question["options"].index(selected_option) == question["correct"]:
            st.session_state.quiz_score += 1
            st.success("🎉 Helyes válasz!")
        else:
            st.error("❌ Helytelen válasz!")
            st.info(f"**Helyes válasz:** `{question['options'][question['correct']]}`")
        
        # Következő kérdés vagy eredmény
        if st.session_state.current_question < len(quiz_questions) - 1:
            st.session_state.current_question += 1
            st.rerun()
        else:
            st.session_state.quiz_finished = True
            st.rerun()
else:
    st.subheader("🏆 Kvíz eredménye")
    score = st.session_state.quiz_score
    total = len(quiz_questions)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.metric("Elért pontszám", f"{score}/{total}")
    
    with col2:
        if score == total:
            st.balloons()
            st.success("🎉 Kiváló! Minden kérdésre helyesen válaszoltál!")
        elif score >= total / 2:
            st.warning("👍 Jó munka! Még gyakorolj egy kicsit!")
        else:
            st.error("💪 Ne add fel! Tekintsd át újra az anyagot!")
    
    if st.button("🔄 Új kvíz"):
        st.session_state.quiz_score = 0
        st.session_state.current_question = 0
        st.session_state.quiz_finished = False
        st.rerun()

# Gyors referencia
st.header("📖 Gyors Referencia")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("📝 Szöveg")
    st.code("""<h1>Főcím</h1>
<h2>Alcím</h2>
<p>Bekezdés</p>
<strong>Félkövér</strong>
<em>Dőlt</em>""", language='html')

with col2:
    st.subheader("🔗 Linkek & Képek")
    st.code("""<a href="url">
  Link szöveg
</a>
<img src="kep.jpg" 
     alt="leírás">""", language='html')

with col3:
    st.subheader("📋 Listák")
    st.code("""<ul>
  <li>Elem 1</li>
  <li>Elem 2</li>
</ul>
<ol>
  <li>Első</li>
  <li>Második</li>
</ol>""", language='html')

# Lábjegyzet
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: gray;">
    <p>Készítette Streamlit-tel | HTML Tanuló alkalmazás</p>
</div>
""", unsafe_allow_html=True)
