import streamlit as st
from google import genai
from google.genai import types

st.set_page_config(
    page_title="EDU Revolution Assistant",
    page_icon="🎓",
    layout="centered",
)

MANUAL = """
1. Introduction to EDU Revolution
EDU Revolution is an LPU initiative designed to recognize and reward students for learning and achievements beyond regular classroom education.

It encourages students to:
- Earn while they learn.
- Develop practical and professional skills.
- Participate in internships, projects and hackathons.
- Complete additional certifications.
- Explore entrepreneurship and revenue generation.
- Gain academic benefits through real-world achievements.
The main objective is to connect classroom learning with industry experience and career development.

2. Academic Benefits Available
EDU Revolution offers several academic benefits.
Academic benefit | Meaning
Course Equivalence | Exemption from classes and evaluation based on approved achievements or learning.
Grade Upgradation | Improvement of an existing course grade through approved achievements.
Attendance Benefit | Up to 10% attendance relaxation for eligible students under the relevant policy.
Duty Leave | Attendance relaxation for approved activities during class hours.
Recognition of Prior Learning (RPL) | Recognition of knowledge and skills acquired before applying.
Evaluation Benefits | Relaxation or benefits in Continuous Assessment (CA) and Mid-Term Tests (MTT).
Transcript Recognition | Achievements beyond the regular curriculum can be recorded in the academic transcript.

3. Processing of Student Nominations
Students can apply under different EDU Revolution categories.

Criteria Sheet: A document defining eligibility, required proofs, evaluation parameters and academic benefits.

Standing Committee: A committee formed by the Head of School (HOS), consisting of 5–7 members.

Its responsibilities include:
- Evaluating student applications.
- Checking certificates and supporting documents.
- Verifying eligibility.
- Recommending suitable academic benefits.
- Ensuring fair and transparent decisions.
The final benefits depend on the committee's evaluation and applicable approvals.

4. Revenue Generation
Revenue Generation allows students to earn money through entrepreneurial, professional, technical, creative or service-based activities.

It follows LPU's concept of Earn Your Fee.

Eligibility conditions:
- Revenue must come from university-approved activities.
- There is no minimum CGPA requirement.
- Academic benefits apply only to courses in which the student has passed.
- Students applying for attendance benefits must maintain at least 60% attendance, excluding bonus attendance and Duty Leave.
- Revenue from family-owned businesses is not accepted.
Important rules:
- Students must appear for the End Term Examination (ETE), irrespective of the benefit claimed.
- Course mapping is performed only by the Head of School.
- Revenue proofs must be submitted at least 15 days before the last teaching day.
- Courses involving third-party evaluation, dissertations, internships or projects cannot be mapped.
Revenue and corresponding benefits
Revenue generated | Academic benefit
Less than ₹5,000–₹10,000 | 1 CA equivalence
₹10,000–₹24,999 | 2 CA equivalence
More than ₹25,000 | Grade upgradation as per criteria sheet
₹50,000–₹1,00,000 | 10% overall attendance benefit
₹1,00,000–₹5,00,000 | 15% overall attendance benefit
More than ₹5,00,000 | 20% overall attendance benefit
More than ₹1,25,000 | Complete equivalence of 1 non-core course

Note: These are the revenue thresholds stated in the guide. All benefits remain subject to verification and approval.

5. NPTEL / Proctored MOOCs / Certifications
Students can receive academic recognition for completing additional courses through recognized and university-approved platforms.

Eligibility:
- Course must be completed through an approved platform.
- Minimum CGPA of 7.0 is required for complete course equivalence.
- No minimum CGPA is required for partial course equivalence.
- Course content must be relevant to the university course being mapped.
- Students must provide registration and completion proof.
Benefits:
- Complete course equivalence.
- Partial course equivalence for 40% of courses, as per the applicable UGC policy.
The Head of School or designated academic authority handles course mapping.

6. Projects
A project is an activity undertaken to solve a real-world problem, develop innovation or conduct research under guided supervision.

Eligibility:
- Minimum CGPA: 6.0.
- For Duty Leave benefits, minimum 65% attendance is required, excluding bonus attendance and Duty Leave.
- Prior approval is required if the project involves scheduled class hours and Duty Leave is claimed.
- Supporting documents must be verified.
Students can either:
1. Select projects from the EDU Revolution Portal.
2. Propose their own projects for approval.
Types of eligible projects
1. Industry and Corporate Projects.
2. Government and National-Level Institutional Projects.
3. Hackathons and Innovation Challenges.
4. Academic Projects, including field research and surveys.
5. Entrepreneurship and Startup Projects.
6. Government Schemes and Fellowship Projects.
7. Technology Development and Prototype Projects.
Academic benefits
Benefit | Maximum benefit
Course Equivalence | Maximum 2 courses
CA Equivalence | 1 or 2 CA equivalences, maximum 3 courses
Attendance Benefit | 10%
Duty Leave | 30 hours
Evaluation may involve an ETP Neutral Panel or viva voce by the respective course faculty, depending on the benefit.

7. Internship Beyond Curriculum
An internship provides practical work experience, professional skills and industry exposure beyond the regular curriculum.

Eligibility:
- Standard minimum CGPA: 6.0.
- Students below 6.0 may be considered in exceptional cases.
- Prior approval is necessary if the internship requires attending work during class hours and the student wants Duty Leave.
- Minimum 65% attendance is required for Duty Leave benefits.
- Students are encouraged to complete internships during breaks, weekends or off-hours.
Internship benefits
Benefits depend on three factors:
1. Monthly stipend.
2. Internship duration.
3. Type of organization.
Organizations are classified as:
- Local companies, startups and NGOs.
- State or national agencies.
- Premier institutes and organizations.
Possible academic benefits include:
- Full marks in one or more CAs.
- Full marks in all CAs.
- MTE benefits.
- Grade upgradation in mapped courses.
Stipend categories
The guide provides different benefit combinations for these stipend ranges:
- No stipend
- Up to ₹5,000
- ₹5,001–₹10,000
- ₹10,001–₹24,999
- ₹25,000–₹49,999
- ₹50,000–₹1,00,000
For internships with a total stipend exceeding ₹1,00,000, students may be considered for a complete course waiver against a course approved by the Standing Committee.
The organization’s reputation, annual turnover and scale are also considered while deciding benefits.

8. Recognition of Prior Learning (RPL)
RPL recognizes knowledge and skills students have already acquired through formal education, professional experience, training or informal learning.

In simple words, if you already know something and can prove your knowledge, LPU may recognize it academically.

Eligibility:
- Must be an active university student.
- Minimum CGPA: 5.0.
- Must provide relevant and verifiable evidence.
- Supporting certificates should generally reflect at least 12 hours of learning, wherever applicable.
- Application must be submitted before the academic term begins or within two weeks of the start of classes.
- Maximum two applications per academic term.
- Course exemption can be granted for only one course per term.
Additional eligibility for CPE courses
Students may qualify through either:
- At least 80% marks in a relevant Class 10, Class 12 or graduation subject for first-year students.
- Overall CGPA of 6.5 or above and average grade B+ or above in mapped courses.
Examples of acceptable prior learning
- IELTS, TOEFL, JLPT and other language certifications.
- AWS, Google Cloud, Microsoft, Cisco and other technical certifications.
- Internships and professional work experience.
- NPTEL and SWAYAM courses.
- Professional workshops and training programmes.
Academic benefit: Complete course waiver after application approval and successful performance of at least B+ in the RPL examination.

IMPORTANT: This text is a revision tool.
"""

SYSTEM_INSTRUCTION = """
You are the EDU Revolution student assistant.
Answer only using the supplied EDU Revolution manual.
If the answer is not available in the manual, reply exactly:
"Information not available in the manual."
Use simple, clear language. Do not invent policies, exceptions, dates, or benefits.
If the manual is ambiguous or appears inconsistent, say so and recommend checking the official criteria sheet or relevant university authority.
"""

st.title("🎓 EDU Revolution Assistant")
st.caption("Ask questions about the EDU Revolution manual. Answers are restricted to the information provided below.")

with st.sidebar:
    st.header("About this assistant")
    st.write("This chatbot answers questions using the EDU Revolution revision manual supplied with the app.")
    st.info("For final eligibility and approvals, always check the latest official criteria sheet or contact the relevant LPU authority.")
    if st.button("Clear chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# Streamlit reads secrets from .streamlit/secrets.toml.
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    model_name = st.secrets.get("GEMINI_MODEL", "gemini-2.5-flash")
except Exception:
    st.error(
        "API key not configured. Open `.streamlit/secrets.toml`, add your Google AI Studio API key, "
        "save the file, and restart the app."
    )
    st.code('GOOGLE_API_KEY = "YOUR_GOOGLE_API_KEY"\nGEMINI_MODEL = "gemini-2.5-flash"', language="toml")
    st.stop()

if not api_key or api_key == "YOUR_GOOGLE_API_KEY":
    st.error("Please replace YOUR_GOOGLE_API_KEY in `.streamlit/secrets.toml` with your actual API key.")
    st.stop()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Ask a question about EDU Revolution...")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Finding the answer in the manual..."):
            try:
                client = genai.Client(api_key=api_key)
                # Include the previous conversation for follow-up questions, while
                # re-supplying the manual and rules on every request.
                conversation = []
                for item in st.session_state.messages:
                    role = "user" if item["role"] == "user" else "model"
                    conversation.append(types.Content(
                        role=role,
                        parts=[types.Part.from_text(text=item["content"])]
                    ))

                response = client.models.generate_content(
                    model=model_name,
                    contents=[
                        types.Content(
                            role="user",
                            parts=[types.Part.from_text(
                                text=f"MANUAL:\n{MANUAL}\n\nConversation and latest question follow."
                            )]
                        ),
                        *conversation,
                    ],
                    config=types.GenerateContentConfig(
                        system_instruction=SYSTEM_INSTRUCTION,
                        temperature=0.2,
                    ),
                )
                answer = response.text or "Information not available in the manual."
            except Exception as exc:
                answer = (
                    "I couldn't generate a response. Please check that your API key is valid, "
                    "your internet connection is working, and the selected model is available. "
                    f"\n\nTechnical details: `{exc}`"
                )

            st.markdown(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})
