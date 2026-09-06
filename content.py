

NAME = "Scott Hodgins"
TAGLINE = "Data Analyst & Data Scientist"


CONTACT = {
    "email": "mailto:scott.hodgins05@gmail.com",      
    "linkedin": "https://www.linkedin.com/in/scott-hodgins/",   
    "github": "https://github.com/ScottHodg",    
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
    "title": "Honest Validation of a Real-Time Abandoned-Luggage Detection System",
    "subtitle": "Computer vision \u00b7 MBAI capstone (MBAI 5600G) \u00b7 Ontario Tech University \u00b7 Summer 2026",
    "framing": (
        "A transit-security system has to flag an unattended bag before it becomes a "
        "problem, and it has to be right, or operators stop trusting it. I reproduced "
        "a published YOLOv8s-based abandoned-luggage detector, paired it with ByteTrack "
        "for tracking and a location-based ownership rule for the abandonment decision, "
        "and then put the original paper's own evaluation under a microscope."
    ),
    "stat_before_label": "Originally reported",
    "stat_before_value": "0.937",
    "stat_before_sub": "mAP@0.50, single train/test split",
    "stat_after_label": "After group-aware cross-validation",
    "stat_after_value": "0.708",
    "stat_after_sub": "mAP@0.50 (bag-class AP alone fell 0.966 \u2192 0.651)",
    "narrative": (
        "A three-level validation protocol, single split, group-aware 5-fold "
        "cross-validation holding whole videos out, and an out-of-domain benchmark, "
        "exposed frame-level data leakage in the original evaluation: the ABODA "
        "training source contained frames from the same videos used for testing. "
        "Once that leakage was controlled for, mAP fell from an inflated 0.937 to an "
        "honest 0.708, a reduction confirmed statistically significant with one-sample "
        "t-tests for every class (mAP: t=-6.35, p=0.0031; bag AP: t=-4.01, p=0.0160; "
        "person AP: t=-7.22, p=0.0020). The bag class, the harder and rarer of the two, "
        "took the biggest hit, falling from 0.966 to 0.651, while person AP fell more "
        "modestly, evidence the model had partly memorized specific bags rather than "
        "learning the general category."
        "\n\n"
        "On the unseen AVSS2007 benchmark, the complete system reached a 0.50 "
        "abandonment-event recall (it caught one of two unseen abandonment events; a "
        "small enough sample that the report treats this as suggestive rather than a "
        "firm estimate, not a fully powered result). Error analysis traced the failure "
        "to object unfamiliarity, not object size: a large, obvious suitcase, roughly "
        "eight times the size at which in-domain recall was 0.955, was still missed, "
        "because upright rolling suitcases were essentially absent from training. "
        "Separately, robustness testing across 17 degradations in 7 families found "
        "the model tolerant of lighting and compression changes but catastrophically "
        "sensitive to sensor noise, an 88% performance loss, tracing directly to the "
        "absence of noise augmentation during training."
        "\n\n"
        "I used NSGA-II multi-objective optimization (pymoo) to tune the ownership "
        "rule's own parameters, detection radius, dwell time, and movement tolerance, "
        "which the original paper had left as future work, and found a wide, stable "
        "operating region rather than a fragile sweet spot. A break-even analysis "
        "framed the economics concretely: at roughly CAD 1,267 per camera per year in "
        "fixed cost, the system pays for itself even at the validated 0.50 recall if "
        "it catches about one real abandonment event every two years per camera under "
        "a conservative CAD 5,000-per-incident scenario. So cost was never the "
        "obstacle. Reliability was. My recommendation was against full autonomous or "
        "night-time deployment, but in favor of a restricted, human-supervised, "
        "daytime rollout, an honest middle ground between 'it works' and 'scrap it.'"
    ),
    "tools": [
        "YOLOv8s (Ultralytics)", "ByteTrack", "pymoo / NSGA-II", "SciPy",
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
