import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Project Timeline",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for tighter spacing and smaller week headings
st.markdown("""
    <style>
    .tight-line {
        line-height: 1.0;  /* Adjust line height for tighter spacing */
        margin-bottom: 0.5em;  /* Reduce margin between bullet points */
    }
    .section-spacing {
        margin-bottom: 1.0em;  /* Reduce space between sections */
    }
    h2 {
        font-size: 1.2em;  /* Reduce the size of week headings */
        margin-bottom: 0.5em;  /* Adjust spacing after week headings */
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar table of contents
st.sidebar.title("Table of Contents")
toc_items = [
    ("Week 1: Project Kickoff", "week1"),
    ("Week 2: Design Phase", "week2"),
    ("Week 3: Data Collection", "week3"),
    ("Week 4: Feedback & Refinement Phase", "week4"),
    ("Week 5: Data Cleaning & Preprocessing", "week5"),
    ("Week 6: Feature Engineering", "week6"),
    ("Week 7: Model Selection & Development", "week7"),
    ("Week 8: Model Tuning & Optimization & Evaluation", "week8"),
    ("Week 9: Final Analysis & Presentation Preparation", "week9"),
    ("Week 10: Thanksgiving Break", "week10"),
    ("Week 11: Final Presentation Run Through", "week11")
]

# Creating sidebar with links
for item in toc_items:
    st.sidebar.markdown(f"[{item[0]}](#{item[1]})")

# Main content
st.title("Project Requirements Document")
st.write("Mentors: Arden Kim, John Oh")
st.markdown("<br>", unsafe_allow_html=True)

# Function to display content for each week
def show_content(week_id, title, points):
    st.markdown(f'<div id="{week_id}"></div>', unsafe_allow_html=True)
    st.markdown(f"## {title}")
    for point in points:
        st.markdown(f'<p class="tight-line">- {point}</p>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

# Week 1: Project Kickoff
show_content("week1", "Week 1: Project Kickoff", [
    "Preliminary research on the topic",
    "Review the project timeline and deliverables",
    "Set up necessary tools and environment"
])

# Week 2: Design Phase
show_content("week2", "Week 2: Design Phase", [
    "Develop a high-level project design, including data flow and model architecture",
    "Establish a project repository with initial structure and dependencies"
])

# Week 3: Data Collection
show_content("week3", "Week 3: Data Collection", [
    "Gather relevant data for the project",
    "Research related works or case studies",
    "Collect data and begin exploring/understanding the data"
])

# Week 4: Feedback & Refinement Phase
show_content("week4", "Week 4: Feedback & Refinement Phase", [
    "Review initial data collection and preprocessing results",
    "Refine the project scope and design based on data insights",
    "Update project timeline and deliverables based on feedback"
])

# Week 5: Data Cleaning & Preprocessing
show_content("week5", "Week 5: Data Cleaning & Preprocessing", [
    "Handle missing values, outliers, and inconsistent data",
    "Perform data normalization or transformation as needed",
    "Validate the cleaned data with initial tests and exploratory analysis"
])

# Week 6: Feature Engineering
show_content("week6", "Week 6: Feature Engineering", [
    "Create new features that improve the model's predictive power",
    "Evaluate and select important features using techniques like correlation analysis or feature importance scores"
])

# Week 7: Model Selection & Development
show_content("week7", "Week 7: Model Selection & Development", [
    "Research different algorithms suited for the problem",
    "Implement and evaluate baseline models on the preprocessed data",
    "Split data into training and testing sets and evaluate initial model performance using appropriate metrics"
])

# Week 8: Model Tuning & Optimization & Evaluation
show_content("week8", "Week 8: Model Tuning & Optimization & Evaluation", [
    "Improve the model's performance through multiple tuning methods",
    "Assess model fairness and bias through cross-validation",
    "Compare different models and select the best-performing one",
    "Document the evaluation process"
])

# Week 9: Final Analysis & Presentation Preparation
show_content("week9", "Week 9: Final Analysis & Presentation Preparation", [
    "Summarize the project's findings and identify any limitations or areas for further study",
    "Prepare a comprehensive slide deck detailing the project's approach, findings, and implications",
    "Create visualizations and charts that effectively communicate the results"
])

# Week 10: Thanksgiving Break
show_content("week10", "Week 10: Thanksgiving Break", [
    "Reflect on the project's progress and any remaining tasks",
    "Plan for the final presentation and any last-minute model adjustments",
    "Enjoy your break :))"
])

# Week 11: Final Presentation Run Through
show_content("week11", "Week 11: Final Presentation Run Through", [
    "Schedule a 1:1 meeting if necessary",
    "Revise presentation/slide deck based on feedback from mentors/peers"
])