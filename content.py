# All site content lives here. Edit this file, then run `python generate_site.py`
# to rebuild index.html. No HTML editing required for text changes.

NAME = "Scott Hodgins"
TAGLINE = "Data Analyst & Data Scientist"

# Set these to real strings when ready, e.g. "mailto:scott@example.com".
# Leave any value as None to omit it from the generated page (it will render
# as an HTML comment placeholder so it's easy to find later).
CONTACT = {
    "email": "mailto:scott.hodgins05@gmail.com",      # e.g. "mailto:scott.hodgins@example.com"
    "linkedin": "https://www.linkedin.com/in/scott-hodgins/",   # e.g. "https://linkedin.com/in/scotthodgins"
    "github": "https://github.com/ScottHodg",     # e.g. "https://github.com/scotthodgins"
}

ABOUT = (
    "I'm a data analyst and incoming data scientist finishing a Master's in Business "
    "Analytics and Artificial Intelligence at Ontario Tech University. Before graduate "
    "school, I spent two years at Deloitte in eDiscovery, doing forensic analysis on "
    "legal case data, which taught me to treat every number with suspicion until I've "
    "checked it myself. That habit followed me into my graduate capstone, where it led "
    "me to catch a serious data leakage problem in a published computer-vision system, "
    "one that had made its reported accuracy look far better than it actually was. "
    "I care about analysis that stays honest even when the honest answer isn't the one "
    "anyone was hoping for, and about turning messy data into decisions people can "
    "actually act on."
)

EXPERIENCE = [
    {
        "year": "2025 \u2013 2026",
        "title": "Master of Business Analytics and Artificial Intelligence",
        "org": "Ontario Tech University",
        "body": (
            "Coursework in artificial intelligence programming, big data systems design, "
            "business analytics, data visualization, digital transformation, and the "
            "ethical and legal dimensions of AI."
        ),
    },
    {
        "year": "2022 \u2013 2025",
        "title": "Career Break",
        "org": None,
        "body": (
            "Managed family responsibilities while continuing to build technical skills "
            "in data analytics, financial modeling, and project management, ahead of "
            "graduate study."
        ),
    },
    {
        "year": "2020 \u2013 2022",
        "title": "Data Analyst, eDiscovery",
        "org": "Deloitte, Toronto",
        "body": (
            "Ran forensic analysis on diverse legal case data, translating findings into "
            "actionable input for legal teams. Built and maintained workflows for "
            "managing large volumes of electronic case files, and helped define the KPIs "
            "used to track team performance. Known for keeping one of the lowest error "
            "rates on the team."
        ),
    },
]

PROJECT = {
    "title": "Real-Time Abandoned-Luggage Detection",
    "subtitle": "Computer vision \u00b7 MBAI capstone \u00b7 Ontario Tech University",
    "framing": (
        "A transit-security system has to flag an unattended bag before it becomes a "
        "problem, and it has to be right. I reproduced a published YOLOv8-based "
        "abandoned-luggage detector, built out its tracking and dwell-time logic, and "
        "then put its own evaluation under a microscope."
    ),
    "stat_before_label": "Originally reported",
    "stat_before_value": "0.937",
    "stat_before_sub": "mAP, single train/test split",
    "stat_after_label": "After my validation",
    "stat_after_value": "0.708",
    "stat_after_sub": "mAP, group-aware cross-validation",
    "narrative": (
        "A three-level validation pipeline, single split, group-aware k-fold, and an "
        "out-of-domain benchmark, exposed data leakage in the original evaluation. On "
        "footage the model had never seen, event recall dropped to 0.50. Paired t-tests, "
        "Wilcoxon, and Levene's tests confirmed the gap was real, not noise. Further "
        "error analysis showed the out-of-domain failures came from object "
        "unfamiliarity rather than genuine task difficulty. I tuned the detection and "
        "tracking parameters with NSGA-II multi-objective optimization, then ran a "
        "cost-benefit break-even analysis to answer the only question that actually "
        "mattered: was this ready to deploy. It wasn't, not because of cost, but "
        "because reliability wasn't there yet, and I said so."
    ),
    "tools": [
        "YOLOv8 (Ultralytics)", "ByteTrack", "pymoo / NSGA-II", "SciPy",
        "PyTorch", "OpenCV", "Streamlit",
    ],
}

SKILLS = [
    {
        "group": "Analysis & Statistics",
        "items": ["Statistical hypothesis testing", "Model validation & experimental design", "Data wrangling", "SQL"],
    },
    {
        "group": "Machine Learning",
        "items": ["Predictive modeling", "Computer vision (YOLOv8, ByteTrack)", "NLP & sentiment analysis", "Multi-objective optimization"],
    },
    {
        "group": "Tools",
        "items": ["Python (pandas, PyTorch, SciPy, OpenCV)", "Power BI & Tableau", "Streamlit", "Excel"],
    },
]

FOOTER_NOTE = "Built with Python \u00b7 hosted on GitHub Pages"
