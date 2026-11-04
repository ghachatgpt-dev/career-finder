import streamlit as st

# ---------------------------------------------------------
# PATHORA | Your Future, Your Path
# ---------------------------------------------------------

st.set_page_config(
    page_title="PATHORA | Career Discovery",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Theme styling
st.markdown("""
<style>
    .stApp { background: #f4f7f4; }
    .block-container { max-width: 1100px; padding-top: 2rem; padding-bottom: 3rem; }
    .hero {
        background: linear-gradient(120deg, #123f32, #287a58);
        padding: 2.2rem 2rem; border-radius: 22px; color: white;
        margin-bottom: 1.5rem;
    }
    .hero h1 { color: white; font-size: 3rem; margin: 0; letter-spacing: 1px; }
    .hero p { color: #e0eee5; font-size: 1.1rem; margin-bottom: 0; }
    .section-card {
        background: white; padding: 1.2rem 1.3rem; border-radius: 16px;
        border: 1px solid #e1eae3; margin-bottom: 1rem;
    }
    .result-card {
        background: white; padding: 1.2rem 1.3rem; border-radius: 16px;
        border: 1px solid #dce8df; margin-bottom: 1rem;
    }
    .small-muted { color: #607268; font-size: .92rem; }
    div.stButton > button[kind="primary"] {
        background: #287a58; border: 0; color: white;
        border-radius: 10px; padding: .65rem 1.2rem; font-weight: 700;
    }
    div.stButton > button[kind="primary"]:hover { background: #164b3b; color: white; }
</style>
""", unsafe_allow_html=True)

# Each career area is matched against selectable student attributes.
CAREERS = {
    "Technology": {
        "matches": {
            "interests": ["Technology", "Computers", "Mathematics", "Science"],
            "abilities": ["Coding", "Problem solving", "Critical thinking", "Mathematics", "Research"],
            "hobbies": ["Gaming", "Building projects", "Exploring technology"],
            "strengths": ["Curiosity", "Creativity", "Persistence", "Attention to detail"],
        },
        "jobs": [
            ("Software Developer", "Creates websites, mobile apps and other software."),
            ("Data Scientist", "Uses data, statistics and computing to find useful patterns."),
            ("Cybersecurity Analyst", "Helps protect computer systems, networks and information."),
            ("Robotics Engineer", "Designs and builds robots and automated systems."),
        ],
        "courses": ["Computer Science", "Software Engineering", "Cybersecurity", "Data Science"],
    },
    "Medicine and Healthcare": {
        "matches": {
            "interests": ["Science", "Biology", "Helping people"],
            "abilities": ["Research", "Scientific experiments", "Communication"],
            "hobbies": ["Teaching others", "Reading"],
            "strengths": ["Empathy", "Patience", "Attention to detail", "Discipline"],
        },
        "jobs": [
            ("Doctor", "Assesses, diagnoses and treats patients."),
            ("Nurse", "Provides care, support and health education to patients."),
            ("Pharmacist", "Advises on medicines and their safe use."),
            ("Medical Laboratory Scientist", "Analyses samples to support diagnosis and treatment."),
        ],
        "courses": ["Medicine and Surgery", "Nursing Science", "Pharmacy", "Medical Laboratory Science"],
    },
    "Engineering": {
        "matches": {
            "interests": ["Science", "Mathematics", "Technology", "Building things"],
            "abilities": ["Problem solving", "Mathematics", "Scientific experiments", "Drawing"],
            "hobbies": ["Building projects", "Exploring technology", "Gaming"],
            "strengths": ["Creativity", "Persistence", "Curiosity", "Attention to detail"],
        },
        "jobs": [
            ("Civil Engineer", "Plans and helps construct roads, bridges and buildings."),
            ("Mechanical Engineer", "Designs and improves machines and mechanical systems."),
            ("Electrical Engineer", "Works with electrical power, circuits and electronic systems."),
            ("Aerospace Engineer", "Works on aircraft, spacecraft and related technology."),
        ],
        "courses": ["Civil Engineering", "Mechanical Engineering", "Electrical Engineering", "Mechatronics Engineering"],
    },
    "Business and Management": {
        "matches": {
            "interests": ["Business", "Mathematics", "Helping people"],
            "abilities": ["Communication", "Leadership", "Organising", "Mathematics"],
            "hobbies": ["Debating", "Writing", "Teaching others"],
            "strengths": ["Confidence", "Discipline", "Adaptability", "Leadership", "Teamwork"],
        },
        "jobs": [
            ("Entrepreneur", "Identifies opportunities and builds a business."),
            ("Accountant", "Prepares and analyses financial records."),
            ("Marketing Manager", "Plans how organisations promote products and services."),
            ("Business Analyst", "Studies business needs and recommends improvements."),
        ],
        "courses": ["Accounting", "Business Administration", "Marketing", "Economics"],
    },
    "Arts, Design and Media": {
        "matches": {
            "interests": ["Art and Design", "Music", "Writing"],
            "abilities": ["Drawing", "Creativity", "Writing", "Communication"],
            "hobbies": ["Drawing", "Photography", "Writing", "Music"],
            "strengths": ["Creativity", "Curiosity", "Adaptability"],
        },
        "jobs": [
            ("Graphic Designer", "Creates visual materials for brands and communication."),
            ("Journalist", "Researches, writes and reports news and stories."),
            ("Animator", "Creates moving images for films, games and digital media."),
            ("Content Creator", "Produces useful or entertaining digital content."),
        ],
        "courses": ["Graphic Design", "Mass Communication", "Fine and Applied Arts", "Film and Multimedia"],
    },
    "Law and Social Sciences": {
        "matches": {
            "interests": ["Law", "Helping people", "Writing"],
            "abilities": ["Communication", "Critical thinking", "Research", "Writing"],
            "hobbies": ["Reading", "Debating", "Writing"],
            "strengths": ["Confidence", "Empathy", "Discipline", "Attention to detail"],
        },
        "jobs": [
            ("Lawyer", "Advises clients and represents them in legal matters."),
            ("Psychologist", "Studies behaviour and supports people with psychological needs."),
            ("Diplomat", "Builds relationships and represents a country internationally."),
            ("Social Worker", "Supports individuals, families and communities."),
        ],
        "courses": ["Law", "Psychology", "Political Science", "International Relations", "Sociology"],
    },
    "Education": {
        "matches": {
            "interests": ["Teaching", "Helping people", "Science", "Writing"],
            "abilities": ["Communication", "Leadership", "Writing", "Research"],
            "hobbies": ["Reading", "Teaching others", "Writing"],
            "strengths": ["Patience", "Empathy", "Teamwork", "Discipline"],
        },
        "jobs": [
            ("Teacher", "Helps students learn and develop new skills."),
            ("Educational Consultant", "Supports schools and organisations with learning strategies."),
            ("Lecturer", "Teaches and carries out research at a college or university."),
        ],
        "courses": ["Education", "Educational Psychology", "Your chosen teaching subject"],
    },
}

OPTIONS = {
    "interests": [
        "Technology", "Computers", "Science", "Biology", "Mathematics",
        "Helping people", "Business", "Art and Design", "Writing",
        "Building things", "Teaching", "Law", "Music",
    ],
    "abilities": [
        "Problem solving", "Communication", "Coding", "Critical thinking",
        "Drawing", "Leadership", "Research", "Organising", "Mathematics",
        "Writing", "Creativity", "Scientific experiments",
    ],
    "hobbies": [
        "Reading", "Gaming", "Drawing", "Photography", "Playing sports",
        "Writing", "Building projects", "Debating", "Cooking",
        "Exploring technology", "Teaching others", "Music",
    ],
    "strengths": [
        "Patience", "Confidence", "Creativity", "Discipline", "Empathy",
        "Curiosity", "Attention to detail", "Teamwork", "Persistence",
        "Critical thinking", "Adaptability", "Leadership",
    ],
}

LABELS = {
    "interests": "What subjects or topics interest you?",
    "abilities": "Which abilities describe what you can do well?",
    "hobbies": "What do you enjoy doing in your free time?",
    "strengths": "Which personal strengths describe you?",
}

def calculate_matches(answers):
    """Calculate a weighted match score for each career category."""
    weights = {"interests": 3, "abilities": 3, "hobbies": 2, "strengths": 2}
    scores = {}

    for career, data in CAREERS.items():
        earned = 0
        possible = 0
        for group, weight in weights.items():
            selected = set(answers[group])
            relevant = set(data["matches"][group])
            earned += len(selected & relevant) * weight
            possible += len(selected) * weight

        # Scores are relative to the student's selected answers.
        scores[career] = round((earned / possible) * 100) if possible else 0

    return sorted(scores.items(), key=lambda item: item[1], reverse=True)


# Header
st.markdown("""
<div class="hero">
    <h1>🧭 PATHORA</h1>
    <p><b>Your Future, Your Path.</b><br>
    Discover career possibilities that connect with who you are.</p>
</div>
""", unsafe_allow_html=True)

st.write(
    "Answer the questions below honestly. There are no right or wrong answers. "
    "The more accurately you describe yourself, the more useful your career suggestions can be."
)

with st.form("career_discovery_form"):
    st.markdown("### 01 · About you")
    col1, col2 = st.columns(2)
    with col1:
        student_name = st.text_input("Your name", placeholder="Enter your name")
    with col2:
        education = st.selectbox(
            "Your educational level",
            ["Junior Secondary", "Senior Secondary", "Year 12 / SS3", "University Student", "Other"],
        )

    st.markdown("---")
    st.markdown("### 02 · Discover your profile")

    answers = {}
    for key in ["interests", "abilities", "hobbies", "strengths"]:
        st.markdown(f"**{LABELS[key]}**")
        answers[key] = st.multiselect(
            LABELS[key],
            OPTIONS[key],
            placeholder="Select all that apply",
            key=f"select_{key}",
            label_visibility="collapsed",
        )
        st.write("")

    submitted = st.form_submit_button("✨ Discover my career path", type="primary", use_container_width=True)

if submitted:
    if not student_name.strip():
        st.error("Please enter your name before viewing your recommendations.")
    elif not any(answers.values()):
        st.warning("Please select at least one option so PATHORA can find relevant career matches.")
    else:
        ranked = calculate_matches(answers)
        recommendations = [(name, score) for name, score in ranked if score > 0][:3]

        st.session_state["pathora_result"] = {
            "name": student_name.strip(),
            "education": education,
            "answers": answers,
            "recommendations": recommendations,
        }

if "pathora_result" in st.session_state:
    result = st.session_state["pathora_result"]
    st.markdown("---")
    st.markdown(f"## 🎯 Your career discovery results, {result['name']}!")
    st.caption(f"Educational level: {result['education']}")
    st.write("Based on your answers, these are career areas worth exploring:")

    if not result["recommendations"]:
        st.info("We could not find a strong match yet. Try selecting a few more interests, abilities, hobbies or strengths.")
    else:
        for index, (category, score) in enumerate(result["recommendations"], start=1):
            details = CAREERS[category]
            with st.container(border=True):
                st.markdown(f"### {index}. {category}")
                st.progress(score / 100, text=f"{score}% answer match")
                st.markdown("**Careers to explore**")
                for job, description in details["jobs"]:
                    st.markdown(f"- **{job}:** {description}")
                st.markdown("**Related courses to research**")
                st.write(", ".join(details["courses"]))

    with st.expander("Review the answers you selected"):
        for group, title in [
            ("interests", "Interests"),
            ("abilities", "Abilities"),
            ("hobbies", "Hobbies"),
            ("strengths", "Strengths"),
        ]:
            st.markdown(f"**{title}:** " + (", ".join(result["answers"][group]) or "None selected"))

    st.info(
        "PATHORA is a career exploration tool, not a test that determines your future. "
        "A match percentage shows how your selected answers overlap with this app's career profile; "
        "it is not a scientific aptitude score or a guarantee of success. Research admission requirements, "
        "speak with teachers or career advisers, and explore careers before making a decision."
    )

    if st.button("Start again", use_container_width=True):
        del st.session_state["pathora_result"]
        st.rerun()

st.markdown("---")
st.markdown(
    "<div style='text-align:center;color:#68796f;'>"
    "<b>PATHORA</b> · Your Future, Your Path. · © 2026"
    "</div>",
    unsafe_allow_html=True,
)
