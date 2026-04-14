import streamlit as st

st.set_page_config(page_title="삼괴고 2학년 선택과목 가이드", page_icon="📚", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700&display=swap');
    html, body, .stApp { font-family: 'Noto Sans KR', sans-serif; }
    .main-header { text-align: center; padding: 1.2rem 0 0.8rem; }
    .main-header h1 { font-size: 1.8rem; font-weight: 700; color: #1a365d; margin-bottom: 0.2rem; }
    .main-header p { color: #64748b; font-size: 0.9rem; }
    .semester-title { font-size: 1.3rem; font-weight: 700; color: #0f3460; border-bottom: 3px solid #0f3460; padding-bottom: 0.3rem; margin: 1.5rem 0 0.8rem; }
    .group-title { font-size: 1rem; font-weight: 600; color: #334155; margin: 1rem 0 0.5rem; padding: 0.4rem 0.8rem; background: #f1f5f9; border-radius: 8px; display: inline-block; }
    .course-card { background: #fff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 1rem 1.2rem; margin-bottom: 0.6rem; }
    .course-card:hover { box-shadow: 0 4px 12px rgba(0,0,0,0.07); }
    .course-card.rec { border-left: 4px solid #2563eb; background: #f0f7ff; }
    .course-name { font-size: 1.05rem; font-weight: 700; color: #1e293b; margin-bottom: 0.3rem; }
    .course-desc { font-size: 0.85rem; color: #475569; line-height: 1.55; margin-bottom: 0.4rem; }
    .badge { display: inline-block; padding: 0.15rem 0.5rem; border-radius: 20px; font-size: 0.72rem; font-weight: 500; margin-right: 0.3rem; margin-bottom: 0.2rem; }
    .badge-rec { background: #dbeafe; color: #1d4ed8; font-weight: 700; }
    .badge-group { background: #f0fdf4; color: #15803d; }
    .badge-eval-rel { background: #fef3c7; color: #92400e; }
    .badge-eval-abs { background: #ede9fe; color: #6d28d9; }
    .badge-track { background: #fce7f3; color: #9d174d; }
    .badge-univ { background: #dbeafe; color: #1e40af; font-size: 0.75rem; }
    .combo-box { background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 1.2rem; margin-bottom: 1rem; }
    .combo-title { font-size: 1.1rem; font-weight: 700; color: #1a365d; margin-bottom: 0.6rem; }
    .combo-sem { font-weight: 600; color: #0f3460; margin: 0.6rem 0 0.3rem; font-size: 0.95rem; }
    .combo-item { font-size: 0.88rem; color: #334155; padding: 0.15rem 0; line-height: 1.5; }
    .ai-profile-banner { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border-radius: 12px; padding: 1.2rem 1.5rem; margin-bottom: 1.2rem; }
    .ai-profile-banner h3 { color: white; margin-bottom: 0.5rem; font-size: 1.1rem; }
    .ai-profile-banner p { color: rgba(255,255,255,0.9); font-size: 0.88rem; margin: 0.2rem 0; }
    .ai-card { background: #fff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 1rem 1.2rem; margin-bottom: 0.8rem; }
    .ai-card.top { border-left: 4px solid #7c3aed; background: #faf5ff; }
    .ai-score { font-size: 1.3rem; font-weight: 700; margin-right: 0.5rem; }
    .ai-score.high { color: #059669; }
    .ai-score.mid { color: #d97706; }
    .ai-score.low { color: #9ca3af; }
    .ai-reason { font-size: 0.82rem; color: #475569; line-height: 1.6; margin: 0.3rem 0; }
    .ai-warning { font-size: 0.82rem; color: #dc2626; line-height: 1.6; }
    .ai-univ-note { font-size: 0.82rem; color: #1e40af; background: #eff6ff; border-radius: 6px; padding: 0.5rem 0.8rem; margin-top: 0.4rem; line-height: 1.55; }
    .score-bar-bg { background: #e5e7eb; border-radius: 6px; height: 8px; width: 100%; }
    .score-bar-fill { border-radius: 6px; height: 8px; }
    .score-bar-fill.high { background: linear-gradient(90deg, #059669, #34d399); }
    .score-bar-fill.mid { background: linear-gradient(90deg, #d97706, #fbbf24); }
    .score-bar-fill.low { background: linear-gradient(90deg, #9ca3af, #d1d5db); }
    .univ-guide-box { background: #f0f9ff; border: 1px solid #bae6fd; border-left: 5px solid #0284c7; border-radius: 10px; padding: 1rem 1.3rem; margin-bottom: 1.2rem; }
    .univ-guide-box .guide-title { font-size: 1rem; font-weight: 700; color: #0c4a6e; margin-bottom: 0.4rem; }
    .univ-guide-box .guide-prereq { font-size: 0.88rem; color: #0369a1; line-height: 1.6; margin-bottom: 0.3rem; }
    .univ-guide-box .guide-3rd { font-size: 0.88rem; color: #334155; line-height: 1.6; }
    .block-container {
    max-width: 1200px;
    padding-left: 2rem;
    padding-right: 2rem;
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# 2학년 선택과목 데이터
# ============================================================
COURSES = {
    # ── 2학년 1학기 택1 (제2외국어/수학심화) ──
    "중국어": {"sem":"2-1","grp":"택1","cr":3,"eval":"5등급 상대평가","desc":"중국어의 기초 발음, 문법, 회화를 학습하여 기본적인 의사소통 능력을 기릅니다.","tracks":["어문계","국제외교","상경계"],"kw":["중국어","중국","통역","번역","무역","글로벌"],
        "aff":{"국어":0.2,"수학":0.0,"영어":0.2,"과학":0.0,"사회":0.4},"diff":3,"mem":0.5,"und":0.3,"pra":0.2,"wl":3,"gc":"보통","rmg":{},
        "univ_note":"서울대 인문계열은 제2외국어/한문 1과목 이상 이수를 권장해요. 3학년 '중국 문화→심화 중국어'로 이어갈 수 있어요."},
    "일본어": {"sem":"2-1","grp":"택1","cr":3,"eval":"5등급 상대평가","desc":"일본어의 기초 발음, 문법, 회화를 학습하여 기본적인 의사소통 능력을 기릅니다.","tracks":["어문계","국제외교"],"kw":["일본어","일본","통역","번역","무역","관광"],
        "aff":{"국어":0.2,"수학":0.0,"영어":0.2,"과학":0.0,"사회":0.4},"diff":3,"mem":0.5,"und":0.3,"pra":0.2,"wl":3,"gc":"보통","rmg":{},
        "univ_note":"서울대 인문계열 제2외국어 권장과목. 3학년 '일본 문화→심화 일본어'로 이어갈 수 있어요."},
    "기하": {"sem":"2-1","grp":"택1","cr":3,"eval":"5등급 상대평가","desc":"공간도형, 벡터, 이차곡선 등 기하학의 핵심 개념을 학습합니다.","tracks":["이공계","자연과학","의약계"],"kw":["수학","기하","벡터","공간","공학","물리","건축"],
        "aff":{"국어":0.0,"수학":1.0,"영어":0.0,"과학":0.2,"사회":0.0},"diff":4,"mem":0.2,"und":0.7,"pra":0.1,"wl":4,"gc":"높음","rmg":{"수학":2},
        "univ_note":"서울대·고려대 등 자연계열 대부분이 '기하+미적분Ⅱ' 이수를 권장합니다. 이공·의약계 지원자는 반드시 이수하세요!"},

    # ── 2학년 1학기 택3 (일반선택 과목) ──
    "세계사": {"sem":"2-1","grp":"택3","cr":3,"eval":"5등급 상대평가","desc":"동서양 문명의 형성과 발전, 근현대 세계의 변화를 폭넓게 학습합니다.","tracks":["인문사회","국제외교","교육"],"kw":["역사","세계사","문명","근대","현대사","전쟁","혁명"],
        "aff":{"국어":0.3,"수학":0.0,"영어":0.1,"과학":0.0,"사회":0.9},"diff":3,"mem":0.6,"und":0.3,"pra":0.1,"wl":3,"gc":"보통","rmg":{"사회":3},
        "univ_note":"동국대·숙명여대 인문사회 범주에서 '역사' 교과를 역량 영역으로 지정. 인문·사회·국제 계열의 기초 과목이에요."},
    "세계시민과 지리": {"sem":"2-1","grp":"택3","cr":3,"eval":"5등급 상대평가","desc":"세계 여러 지역의 자연환경과 인문환경, 글로벌 이슈를 지리적 관점에서 탐구합니다.","tracks":["인문사회","국제외교","환경도시"],"kw":["지리","세계","환경","기후","도시","글로벌","국제"],
        "aff":{"국어":0.2,"수학":0.0,"영어":0.2,"과학":0.2,"사회":0.8},"diff":2,"mem":0.4,"und":0.4,"pra":0.2,"wl":2,"gc":"보통","rmg":{"사회":3}},
    "윤리와 사상": {"sem":"2-1","grp":"택3","cr":3,"eval":"5등급 상대평가","desc":"동서양의 윤리 사상과 현대 사회의 윤리적 쟁점을 탐구합니다.","tracks":["인문사회","철학윤리","교육"],"kw":["윤리","철학","사상","동양","서양","도덕","인권","정의"],
        "aff":{"국어":0.4,"수학":0.0,"영어":0.1,"과학":0.0,"사회":0.8},"diff":3,"mem":0.5,"und":0.4,"pra":0.1,"wl":3,"gc":"보통","rmg":{"사회":3}},
    "경제": {"sem":"2-1","grp":"택3","cr":3,"eval":"5등급 상대평가","desc":"시장경제의 원리, 국민경제, 국제경제 등 경제학의 기본 개념을 학습합니다.","tracks":["상경계","경제금융","법·정치"],"kw":["경제","시장","금융","무역","경영","회계","세무","GDP"],
        "aff":{"국어":0.2,"수학":0.4,"영어":0.1,"과학":0.0,"사회":0.8},"diff":3,"mem":0.3,"und":0.5,"pra":0.2,"wl":3,"gc":"보통","rmg":{"사회":3},
        "univ_note":"숙명여대 경영·경제 범주에서 사회 교과를 2단계 교과영역으로 지정. 상경계열 진학 시 경제 기초가 필수예요."},
    "물리학": {"sem":"2-1","grp":"택3","cr":3,"eval":"5등급 상대평가","desc":"힘과 운동, 에너지, 파동, 전기와 자기 등 물리학의 기본 원리를 학습합니다.","tracks":["이공계","자연과학","의약계"],"kw":["물리","역학","에너지","파동","전기","자기","공학","반도체"],
        "aff":{"국어":0.0,"수학":0.7,"영어":0.1,"과학":0.9,"사회":0.0},"diff":4,"mem":0.2,"und":0.6,"pra":0.2,"wl":4,"gc":"높음","rmg":{"수학":3,"과학":3},
        "univ_note":"서울대·고려대 공학계열은 물리학 진로선택 2~3과목 이수를 권장. 2학기 '역학과 에너지'로 이어지는 필수 기초예요."},
    "생명과학": {"sem":"2-1","grp":"택3","cr":3,"eval":"5등급 상대평가","desc":"세포, 유전, 진화, 생태계 등 생명 현상의 기본 원리를 학습합니다.","tracks":["의약계","자연과학","보건간호"],"kw":["생명과학","세포","유전","진화","생태","의대","약대","간호"],
        "aff":{"국어":0.0,"수학":0.3,"영어":0.1,"과학":0.9,"사회":0.0},"diff":3,"mem":0.5,"und":0.4,"pra":0.1,"wl":3,"gc":"보통","rmg":{"과학":3},
        "univ_note":"의약계 지원자 필수! 서울대 의대는 '세포와 물질대사, 생물의 유전' 포함 과학 진로선택 3과목 이상 권장. 이 과목이 그 기초예요."},
    "화학": {"sem":"2-1","grp":"택3","cr":3,"eval":"5등급 상대평가","desc":"물질의 구조, 화학 반응, 에너지 변화 등 화학의 기본 개념을 학습합니다.","tracks":["이공계","자연과학","의약계"],"kw":["화학","물질","반응","원소","화합물","약학","화공","신소재"],
        "aff":{"국어":0.0,"수학":0.5,"영어":0.1,"과학":0.9,"사회":0.0},"diff":4,"mem":0.4,"und":0.5,"pra":0.1,"wl":4,"gc":"높음","rmg":{"수학":3,"과학":3},
        "univ_note":"약학·화공·신소재 계열 필수. 2학기 '물질과 에너지'로 이어지고 3학년 '고급 화학'의 기초가 돼요."},
    "지구과학": {"sem":"2-1","grp":"택3","cr":3,"eval":"5등급 상대평가","desc":"지구의 구조, 대기와 해양, 천체와 우주 등을 탐구합니다.","tracks":["자연과학","환경도시","이공계"],"kw":["지구과학","기상","천문","지질","해양","환경","우주","기후"],
        "aff":{"국어":0.0,"수학":0.2,"영어":0.1,"과학":0.8,"사회":0.1},"diff":2,"mem":0.4,"und":0.4,"pra":0.2,"wl":2,"gc":"보통","rmg":{"과학":3}},

    # ── 2학년 2학기 택1-가 (제2외국어/수학심화) ──
    "중국어 회화": {"sem":"2-2","grp":"택1-가","cr":3,"eval":"5등급 상대평가","desc":"중국어 듣기·말하기 능력을 집중적으로 훈련하여 실용적 회화 능력을 기릅니다.","tracks":["어문계","국제외교","상경계"],"kw":["중국어","회화","중국","통역","무역","관광"],
        "aff":{"국어":0.2,"수학":0.0,"영어":0.2,"과학":0.0,"사회":0.3},"diff":3,"mem":0.4,"und":0.3,"pra":0.3,"wl":3,"gc":"보통","rmg":{},
        "univ_note":"1학기 '중국어'와 연계 이수하면 제2외국어 심화를 보여줄 수 있어요. 서울대 인문계열 제2외국어 권장에 해당해요."},
    "일본어 회화": {"sem":"2-2","grp":"택1-가","cr":3,"eval":"5등급 상대평가","desc":"일본어 듣기·말하기 능력을 집중적으로 훈련하여 실용적 회화 능력을 기릅니다.","tracks":["어문계","국제외교"],"kw":["일본어","회화","일본","통역","무역","관광"],
        "aff":{"국어":0.2,"수학":0.0,"영어":0.2,"과학":0.0,"사회":0.3},"diff":3,"mem":0.4,"und":0.3,"pra":0.3,"wl":3,"gc":"보통","rmg":{},
        "univ_note":"1학기 '일본어'와 연계 이수. 3학년 '일본 문화→심화 일본어'까지 이어가면 제2외국어 이수 깊이가 확실해져요."},
    "인공지능 수학": {"sem":"2-2","grp":"택1-가","cr":3,"eval":"5등급 상대평가","desc":"인공지능의 기초가 되는 수학적 개념(행렬, 확률, 최적화 등)을 학습합니다.","tracks":["IT","이공계","상경계"],"kw":["AI","인공지능","수학","행렬","확률","데이터","프로그래밍","코딩"],
        "aff":{"국어":0.0,"수학":0.9,"영어":0.1,"과학":0.2,"사회":0.0},"diff":3,"mem":0.2,"und":0.6,"pra":0.2,"wl":3,"gc":"보통","rmg":{"수학":3},
        "univ_note":"IT·AI 분야 지원자에게 차별화 포인트. 숙명여대는 수학/컴퓨터·경영 범주에서도 정보 교과를 핵심으로 제시해요."},

    # ── 2학년 2학기 택3 (진로선택 과목) ──
    "동아시아 역사 기행": {"sem":"2-2","grp":"택3","cr":3,"eval":"5등급 상대평가","desc":"한국·중국·일본 등 동아시아 국가들의 역사와 문화를 비교 탐구합니다.","tracks":["인문사회","국제외교","어문계"],"kw":["역사","동아시아","한국","중국","일본","문화교류","국제"],
        "aff":{"국어":0.3,"수학":0.0,"영어":0.1,"과학":0.0,"사회":0.9},"diff":2,"mem":0.5,"und":0.4,"pra":0.1,"wl":2,"gc":"보통","rmg":{}},
    "사회와 문화": {"sem":"2-2","grp":"택3","cr":3,"eval":"5등급 상대평가","desc":"사회 구조, 문화, 사회 변동, 사회 불평등 등 사회학의 기본 개념을 학습합니다.","tracks":["인문사회","교육","법·정치"],"kw":["사회","문화","사회학","불평등","계층","사회변동","다문화"],
        "aff":{"국어":0.3,"수학":0.1,"영어":0.1,"과학":0.0,"사회":0.9},"diff":3,"mem":0.4,"und":0.5,"pra":0.1,"wl":3,"gc":"보통","rmg":{"사회":3},
        "univ_note":"동국대·숙명여대 사회과학/교육/법학 범주에서 사회 교과를 1단계 교과영역으로 지정. 사회과학 계열 필수 기초예요."},
    "현대사회와 윤리": {"sem":"2-2","grp":"택3","cr":3,"eval":"5등급 상대평가","desc":"현대 사회의 윤리적 쟁점(생명윤리, 정보윤리, 환경윤리 등)을 다양한 관점에서 탐구합니다.","tracks":["인문사회","철학윤리","교육"],"kw":["윤리","현대사회","생명윤리","정보윤리","환경윤리","인권","정의"],
        "aff":{"국어":0.4,"수학":0.0,"영어":0.1,"과학":0.1,"사회":0.8},"diff":2,"mem":0.3,"und":0.6,"pra":0.1,"wl":2,"gc":"보통","rmg":{}},
    "한국지리 탐구": {"sem":"2-2","grp":"택3","cr":3,"eval":"5등급 상대평가","desc":"한국의 자연환경, 인구, 도시, 산업 등을 지리적 관점에서 심화 탐구합니다.","tracks":["인문사회","환경도시","관광"],"kw":["한국","지리","도시","인구","환경","국토","관광"],
        "aff":{"국어":0.2,"수학":0.1,"영어":0.0,"과학":0.2,"사회":0.8},"diff":2,"mem":0.4,"und":0.4,"pra":0.2,"wl":2,"gc":"보통","rmg":{}},
    "역학과 에너지": {"sem":"2-2","grp":"택3","cr":3,"eval":"5등급 상대평가","desc":"뉴턴 역학, 에너지 보존, 운동량 등 역학의 핵심 개념을 심화 학습합니다.","tracks":["이공계","자연과학"],"kw":["물리","역학","에너지","뉴턴","운동","힘","공학","반도체","기계"],
        "aff":{"국어":0.0,"수학":0.8,"영어":0.1,"과학":0.9,"사회":0.0},"diff":4,"mem":0.2,"und":0.7,"pra":0.1,"wl":4,"gc":"높음","rmg":{"수학":2,"과학":2},
        "univ_note":"서울대·고려대 공학계열 권장 과학 진로선택 핵심 과목! 3학년 '고급 물리학'의 필수 전제예요."},
    "생물의 유전": {"sem":"2-2","grp":"택3","cr":3,"eval":"5등급 상대평가","desc":"유전의 원리, DNA, 유전자 발현, 유전공학 등을 심화 학습합니다.","tracks":["의약계","자연과학","보건간호"],"kw":["유전","DNA","유전공학","생명과학","의대","약대","바이오","생명공학"],
        "aff":{"국어":0.0,"수학":0.3,"영어":0.1,"과학":0.9,"사회":0.0},"diff":4,"mem":0.4,"und":0.5,"pra":0.1,"wl":4,"gc":"높음","rmg":{"과학":2},
        "univ_note":"서울대 의대 권장 필수 과목! '세포와 물질대사'와 함께 의약계 과학 진로선택 3과목 요건의 핵심이에요."},
    "물질과 에너지": {"sem":"2-2","grp":"택3","cr":3,"eval":"5등급 상대평가","desc":"화학 결합, 반응 에너지, 화학 평형 등 화학의 심화 개념을 탐구합니다.","tracks":["이공계","자연과학","의약계"],"kw":["화학","물질","에너지","반응","결합","약학","화공","신소재"],
        "aff":{"국어":0.0,"수학":0.5,"영어":0.1,"과학":0.9,"사회":0.0},"diff":4,"mem":0.3,"und":0.6,"pra":0.1,"wl":4,"gc":"높음","rmg":{"수학":3,"과학":2},
        "univ_note":"약학·화공 계열 핵심 진로선택. 3학년 '고급 화학'의 기초가 되며 대학별 과학 이수 요건 충족에 필수예요."},
    "지구시스템과학": {"sem":"2-2","grp":"택3","cr":3,"eval":"5등급 상대평가","desc":"지구 시스템의 상호작용, 지질 현상, 기후 변화 등을 심화 탐구합니다.","tracks":["자연과학","환경도시","이공계"],"kw":["지구과학","지질","기후","환경","해양","대기","지구시스템"],
        "aff":{"국어":0.0,"수학":0.2,"영어":0.1,"과학":0.8,"사회":0.1},"diff":3,"mem":0.3,"und":0.5,"pra":0.2,"wl":3,"gc":"보통","rmg":{"과학":3}},

    # ── 2학년 2학기 택1-나 (수학 필수선택) ──
    "미적분Ⅱ": {"sem":"2-2","grp":"택1-나","cr":4,"eval":"5등급 상대평가","desc":"다변수 함수, 급수, 적분법의 확장 등 미적분학의 심화 내용을 학습합니다.","tracks":["이공계","자연과학","의약계"],"kw":["수학","미적분","적분","급수","공학","물리","의대"],
        "aff":{"국어":0.0,"수학":1.0,"영어":0.0,"과학":0.2,"사회":0.0},"diff":5,"mem":0.2,"und":0.7,"pra":0.1,"wl":5,"gc":"높음","rmg":{"수학":2},
        "univ_note":"서울대·고려대·경희대 등 자연계열 거의 전부가 '기하+미적분Ⅱ' 이수를 권장합니다. 이공·의약계 지원자는 반드시 선택하세요!"},
    "실용 통계": {"sem":"2-2","grp":"택1-나","cr":4,"eval":"5등급 상대평가","desc":"데이터 수집, 정리, 분석, 해석의 기본 원리와 실생활 활용을 학습합니다.","tracks":["상경계","인문사회","IT"],"kw":["통계","데이터","확률","분석","조사","경제","경영","사회조사"],
        "aff":{"국어":0.1,"수학":0.7,"영어":0.1,"과학":0.1,"사회":0.3},"diff":2,"mem":0.3,"und":0.5,"pra":0.2,"wl":2,"gc":"보통","rmg":{"수학":3},
        "univ_note":"인문·상경계열 학생에게 추천! 미적분Ⅱ가 부담되는 인문계열 학생이 수학 교과를 유지하면서 데이터 역량을 보여줄 수 있어요."},
}

# ============================================================
# 2학년 맥락 대입 안내
# ============================================================
TRACK_UNIV_GUIDE = {
    "이공계 (공학·반도체·전기전자·기계)": {
        "icon": "⚙️",
        "prereq": "서울대·고려대 등은 <b>기하 + 미적분Ⅱ</b>, 과학 진로선택(역학과 에너지, 전자기와 양자 등) <b>2~3과목 이상</b> 이수를 권장합니다.",
        "third": "2학년에서 <b>기하, 물리학, 화학 → 미적분Ⅱ, 역학과 에너지, 물질과 에너지</b> 순서로 이수하면 3학년 '고급 물리학/화학'으로 자연스럽게 이어져요.",
    },
    "IT·컴퓨터·AI": {
        "icon": "💻",
        "prereq": "이공계와 동일하게 <b>기하 + 미적분Ⅱ</b> 이수가 권장돼요. 숙명여대는 정보 교과(인공지능 기초, 데이터 과학)도 핵심으로 제시합니다.",
        "third": "2학년에서 <b>기하 + 인공지능 수학 + 미적분Ⅱ</b>를 챙기고, 과학은 물리학 중심으로 이수하세요.",
    },
    "의약계 (의대·치대·한의대·약대·수의대)": {
        "icon": "🏥",
        "prereq": "서울대 의대는 <b>기하 + 미적분Ⅱ + 세포와 물질대사·생물의 유전 포함</b> 과학 진로선택 3과목 이상을 권장합니다.",
        "third": "2학년에서 <b>기하, 생명과학, 화학 → 미적분Ⅱ, 생물의 유전, 물질과 에너지</b>를 반드시 이수하세요. 이게 3학년 '고급 생명과학/화학'의 기초예요.",
    },
    "보건·간호": {
        "icon": "💊",
        "prereq": "간호학과 등은 <b>생명과학·화학</b> 관련 진로선택 3과목 이상 이수를 권장하는 대학이 많아요.",
        "third": "2학년에서 <b>생명과학 + 화학 → 생물의 유전 + 물질과 에너지</b>를 이수하면 과학 이수 요건을 채울 수 있어요.",
    },
    "자연과학 (수학·물리·화학·생명·지구과학)": {
        "icon": "🔬",
        "prereq": "<b>기하 + 미적분Ⅱ</b> + 해당 분야 과학 진로선택 이수가 기본이에요.",
        "third": "2학년에서 해당 분야 일반선택(물리학/화학/생명과학/지구과학) + 진로선택을 반드시 이어서 이수하세요.",
    },
    "인문·사회 (인문학·사회학·심리학)": {
        "icon": "📖",
        "prereq": "서울대 <b>제2외국어/한문 1과목 이상</b> 권장. 동국대·숙명여대는 <b>국어·영어·사회</b>를 1단계 교과영역으로 지정해요.",
        "third": "2학년에서 <b>사회 교과 3과목(세계사/윤리와 사상/경제 등)</b> + <b>제2외국어(중국어/일본어)</b>를 챙기세요. 수학은 '실용 통계'로 커버 가능해요.",
    },
    "법·정치·행정": {
        "icon": "⚖️",
        "prereq": "동국대·숙명여대는 사회과학/법학 계열에서 <b>사회 교과</b>를 1단계 관련 영역으로 강조합니다.",
        "third": "2학년에서 <b>경제, 윤리와 사상, 세계사</b> 등 사회 교과를 폭넓게 이수하고, 2학기에 <b>사회와 문화</b>까지 이어가세요.",
    },
    "상경계 (경영·경제·금융·회계)": {
        "icon": "📊",
        "prereq": "부산대 등은 <b>확률과 통계, 미적분Ⅰ, 미적분Ⅱ 중 1과목 이상</b> 이수를 권장합니다. 숙명여대는 수학·영어를 1단계로 지정해요.",
        "third": "2학년에서 <b>경제</b>(사회 교과) + <b>미적분Ⅱ 또는 실용 통계</b>(수학 교과)를 반드시 이수하세요. 경희대 수학 5과목 가산점 기준도 챙기면 좋아요.",
    },
    "교육 (사범대·교직)": {
        "icon": "🎓",
        "prereq": "사범대는 전공 교과 심화가 중요해요. 숙명여대 교육학부는 국어·영어·사회를 1단계로 지정합니다.",
        "third": "2학년에서 희망 교과(국어/영어/수학/과학/사회) 관련 과목을 집중 이수하세요. 과학교육이면 과학 택3을, 사회교육이면 사회 택3을 중심으로!",
    },
    "어문·외국어 (영문·국문·통번역)": {
        "icon": "🌐",
        "prereq": "서울대 <b>제2외국어/한문 1과목 이상</b> 권장. 숙명여대는 국어·영어를 1단계로 지정합니다.",
        "third": "2학년에서 <b>중국어/일본어 → 중국어 회화/일본어 회화</b>로 제2외국어를 이어가고, 사회 교과도 인문학적 소양 차원에서 챙기세요.",
    },
    "국제·외교 (국제학·외교·국제기구)": {
        "icon": "🌍",
        "prereq": "서울대 <b>제2외국어/한문 1과목 이상</b> 권장. 사회·영어 교과 심화가 중요해요.",
        "third": "2학년에서 <b>세계사/경제 + 중국어(→회화)</b>를 이수하고, 2학기에 <b>사회와 문화/동아시아 역사 기행</b>으로 국제 시야를 넓히세요.",
    },
    "환경·도시·건축": {
        "icon": "🏗️",
        "prereq": "건축·환경공학은 <b>기하 + 미적분Ⅱ</b>, 물리·화학 진로선택 이수가 권장돼요.",
        "third": "2학년에서 <b>기하 + 물리학/화학 → 미적분Ⅱ + 역학과 에너지</b>를 이수하고, 사회 교과에서 '세계시민과 지리'도 고려해보세요.",
    },
    "미디어·언론·광고": {
        "icon": "📺",
        "prereq": "숙명여대·동국대는 국어·영어·사회를 1단계 교과영역으로 지정해요.",
        "third": "2학년에서 <b>사회 교과(세계사/경제/윤리와 사상)</b>를 폭넓게 이수하세요. 수학은 '실용 통계'로 데이터 역량을 보여줄 수 있어요.",
    },
    "관광·호텔·항공": {
        "icon": "✈️",
        "prereq": "외국어 교과 심화가 경쟁력이에요. 숙명여대 문화관광학전공은 영어·사회를 핵심으로 제시합니다.",
        "third": "2학년에서 <b>중국어/일본어 → 회화</b>로 제2외국어를 이어가고, <b>세계시민과 지리</b>로 글로벌 시야를 보여주세요.",
    },
    "예체능 (음악·체육·미술)": {
        "icon": "🎨",
        "prereq": "예체능 계열은 실기가 핵심이라 교과 이수 권장 사항이 별도로 없는 경우가 많아요.",
        "third": "2학년에서는 기본 교과를 충실히 이수하면서 본인의 실기 역량 개발에 집중하세요.",
    },
}

# ============================================================
# 진로별 추천 조합 (2학년용)
# ============================================================
TRACK_COMBOS = {
    "이공계 (공학·반도체·전기전자·기계)": {
        "desc": "공학, 반도체, 전기전자, 기계공학, 항공우주, 컴퓨터공학 등",
        "1학기": {"택1": "기하", "택3": ["물리학", "화학", "지구과학"]},
        "2학기": {"택1-가": "인공지능 수학", "택3": ["역학과 에너지", "물질과 에너지", "지구시스템과학"], "택1-나": "미적분Ⅱ"},
    },
    "IT·컴퓨터·AI": {
        "desc": "컴퓨터과학, 소프트웨어, 인공지능, 데이터사이언스 등",
        "1학기": {"택1": "기하", "택3": ["물리학", "화학", "경제"]},
        "2학기": {"택1-가": "인공지능 수학", "택3": ["역학과 에너지", "물질과 에너지", "사회와 문화"], "택1-나": "미적분Ⅱ"},
    },
    "의약계 (의대·치대·한의대·약대·수의대)": {
        "desc": "의학, 치의학, 한의학, 약학, 수의학 등",
        "1학기": {"택1": "기하", "택3": ["생명과학", "화학", "물리학"]},
        "2학기": {"택1-가": "인공지능 수학", "택3": ["생물의 유전", "물질과 에너지", "역학과 에너지"], "택1-나": "미적분Ⅱ"},
    },
    "보건·간호": {
        "desc": "간호학, 보건학, 물리치료, 임상병리 등 보건의료 계열",
        "1학기": {"택1": "기하", "택3": ["생명과학", "화학", "윤리와 사상"]},
        "2학기": {"택1-가": "인공지능 수학", "택3": ["생물의 유전", "물질과 에너지", "현대사회와 윤리"], "택1-나": "미적분Ⅱ"},
    },
    "자연과학 (수학·물리·화학·생명·지구과학)": {
        "desc": "기초과학 연구, 수학과, 물리학과, 화학과, 생명과학, 지구과학 등",
        "1학기": {"택1": "기하", "택3": ["물리학", "화학", "생명과학"]},
        "2학기": {"택1-가": "인공지능 수학", "택3": ["역학과 에너지", "물질과 에너지", "생물의 유전"], "택1-나": "미적분Ⅱ"},
    },
    "인문·사회 (인문학·사회학·심리학)": {
        "desc": "국문학, 사학, 철학, 사회학, 심리학, 사회복지 등",
        "1학기": {"택1": "중국어", "택3": ["세계사", "윤리와 사상", "경제"]},
        "2학기": {"택1-가": "중국어 회화", "택3": ["사회와 문화", "동아시아 역사 기행", "현대사회와 윤리"], "택1-나": "실용 통계"},
    },
    "법·정치·행정": {
        "desc": "법학, 정치외교학, 행정학, 공공정책, 공무원 등",
        "1학기": {"택1": "중국어", "택3": ["경제", "윤리와 사상", "세계사"]},
        "2학기": {"택1-가": "중국어 회화", "택3": ["사회와 문화", "현대사회와 윤리", "동아시아 역사 기행"], "택1-나": "실용 통계"},
    },
    "상경계 (경영·경제·금융·회계)": {
        "desc": "경영학, 경제학, 금융, 회계, 무역, 세무 등",
        "1학기": {"택1": "중국어", "택3": ["경제", "세계사", "세계시민과 지리"]},
        "2학기": {"택1-가": "중국어 회화", "택3": ["사회와 문화", "동아시아 역사 기행", "현대사회와 윤리"], "택1-나": "미적분Ⅱ"},
    },
    "교육 (사범대·교직)": {
        "desc": "초등교육, 국어교육, 영어교육, 수학교육, 특수교육, 유아교육 등",
        "1학기": {"택1": "중국어", "택3": ["세계사", "윤리와 사상", "경제"]},
        "2학기": {"택1-가": "중국어 회화", "택3": ["사회와 문화", "현대사회와 윤리", "한국지리 탐구"], "택1-나": "실용 통계"},
    },
    "어문·외국어 (영문·국문·통번역)": {
        "desc": "영어영문학, 국어국문학, 통번역, 언어학 등",
        "1학기": {"택1": "중국어", "택3": ["세계사", "윤리와 사상", "세계시민과 지리"]},
        "2학기": {"택1-가": "중국어 회화", "택3": ["사회와 문화", "동아시아 역사 기행", "현대사회와 윤리"], "택1-나": "실용 통계"},
    },
    "국제·외교 (국제학·외교·국제기구)": {
        "desc": "국제학, 정치외교학, 국제통상, 국제기구, NGO 등",
        "1학기": {"택1": "중국어", "택3": ["경제", "세계사", "세계시민과 지리"]},
        "2학기": {"택1-가": "중국어 회화", "택3": ["사회와 문화", "동아시아 역사 기행", "현대사회와 윤리"], "택1-나": "실용 통계"},
    },
    "환경·도시·건축": {
        "desc": "환경공학, 도시계획, 건축학, 조경, 토목 등",
        "1학기": {"택1": "기하", "택3": ["물리학", "화학", "세계시민과 지리"]},
        "2학기": {"택1-가": "인공지능 수학", "택3": ["역학과 에너지", "물질과 에너지", "지구시스템과학"], "택1-나": "미적분Ⅱ"},
    },
    "미디어·언론·광고": {
        "desc": "신문방송학, 미디어학, 광고홍보, 영상, 콘텐츠 등",
        "1학기": {"택1": "중국어", "택3": ["경제", "세계사", "윤리와 사상"]},
        "2학기": {"택1-가": "중국어 회화", "택3": ["사회와 문화", "현대사회와 윤리", "동아시아 역사 기행"], "택1-나": "실용 통계"},
    },
    "관광·호텔·항공": {
        "desc": "관광경영, 호텔경영, 항공서비스 등",
        "1학기": {"택1": "일본어", "택3": ["경제", "세계시민과 지리", "세계사"]},
        "2학기": {"택1-가": "일본어 회화", "택3": ["사회와 문화", "동아시아 역사 기행", "한국지리 탐구"], "택1-나": "실용 통계"},
    },
    "예체능 (음악·체육·미술)": {
        "desc": "음악, 체육, 미술, 실용음악, 체육교육, 무용 등",
        "1학기": {"택1": "중국어", "택3": ["윤리와 사상", "세계사", "세계시민과 지리"]},
        "2학기": {"택1-가": "중국어 회화", "택3": ["현대사회와 윤리", "사회와 문화", "동아시아 역사 기행"], "택1-나": "실용 통계"},
    },
}

GRP_COUNT = {"택1": 1, "택3": 3, "택1-가": 1, "택1-나": 1}
GRP_ORDER_1 = ["택1", "택3"]  # 1학기
GRP_ORDER_2 = ["택1-가", "택3", "택1-나"]  # 2학기
GRP_LABELS = {"택1": "택1 — 1개 선택", "택3": "택3 — 3개 선택", "택1-가": "택1-가 (제2외국어/수학심화) — 1개 선택", "택1-나": "택1-나 (수학 필수선택) — 1개 선택"}
SEM_INFO = [("📘 2학년 1학기", "2-1", "1학기"), ("📗 2학년 2학기", "2-2", "2학기")]

def get_grp_order(sem_filter):
    return GRP_ORDER_1 if sem_filter == "2-1" else GRP_ORDER_2

# ============================================================
# 희망 직업 → 진로 계열 매핑
# ============================================================
JOB_TO_TRACKS = {
    "의사": ["의약계", "자연과학"], "간호사": ["보건간호", "의약계"],
    "프로그래머": ["IT", "이공계"], "개발자": ["IT", "이공계"],
    "변호사": ["법·정치", "인문사회"], "교사": ["교육", "인문사회"],
    "회계사": ["상경계", "경제금융"], "기자": ["미디어", "인문사회"],
    "건축": ["환경도시", "이공계"], "외교관": ["국제외교", "법·정치"],
    "약사": ["의약계", "자연과학"], "치과의사": ["의약계", "자연과학"],
    "한의사": ["의약계", "자연과학"], "수의사": ["의약계", "자연과학"],
    "물리치료사": ["보건간호", "의약계"], "방사선사": ["보건간호", "의약계"],
    "임상병리사": ["보건간호", "의약계"], "영양사": ["보건간호", "생활과학"],
    "공무원": ["행정", "법·정치"], "경찰": ["법·정치", "행정"],
    "소방관": ["행정", "보건간호"], "군인": ["행정", "이공계"],
    "판사": ["법·정치", "인문사회"], "검사": ["법·정치", "인문사회"],
    "세무사": ["상경계", "경제금융"], "관세사": ["상경계", "국제외교"],
    "은행원": ["상경계", "경제금융"], "펀드매니저": ["상경계", "경제금융"],
    "경영": ["상경계", "경제금융"], "마케팅": ["상경계", "미디어"],
    "디자이너": ["예체능", "미디어"], "작가": ["어문계", "인문사회"],
    "아나운서": ["미디어", "어문계"], "PD": ["미디어", "예체능"],
    "영화감독": ["미디어", "예체능"], "배우": ["예체능", "미디어"],
    "음악가": ["예체능", "교육"], "체육": ["예체능", "교육"],
    "통역사": ["어문계", "국제외교"], "번역가": ["어문계", "국제외교"],
    "상담사": ["교육", "인문사회"], "심리학자": ["인문사회", "교육"],
    "사회복지사": ["인문사회", "교육"], "연구원": ["자연과학", "이공계"],
    "교수": ["교육", "자연과학"], "과학자": ["자연과학", "이공계"],
    "엔지니어": ["이공계", "자연과학"], "반도체": ["이공계", "자연과학"],
    "로봇": ["이공계", "IT"], "항공": ["이공계", "관광"],
    "조종사": ["이공계", "관광"], "승무원": ["관광", "어문계"],
    "호텔리어": ["관광", "어문계"], "관광가이드": ["관광", "어문계"],
    "환경": ["환경도시", "자연과학"], "도시계획": ["환경도시", "건축"],
    "조경": ["환경도시", "자연과학"], "토목": ["환경도시", "이공계"],
    "데이터": ["IT", "상경계"], "AI": ["IT", "이공계"],
    "보험": ["상경계", "경제금융"], "유튜버": ["미디어", "IT"],
    "웹디자이너": ["IT", "미디어"], "게임": ["IT", "예체능"],
    "수학": ["이공계", "자연과학"], "과학": ["자연과학", "이공계"],
    "물리": ["이공계", "자연과학"], "화학": ["자연과학", "의약계"],
    "생명": ["의약계", "자연과학"], "지구": ["환경도시", "자연과학"],
    "국어": ["어문계", "인문사회"], "영어": ["어문계", "국제외교"],
    "역사": ["인문사회"], "지리": ["인문사회", "관광"],
    "사회": ["인문사회"], "윤리": ["인문사회", "철학윤리"],
    "음악": ["예체능", "교육"], "미술": ["예체능", "교육"],
    "체육": ["예체능", "교육"], "정보": ["IT", "이공계", "교육"],
    "컴퓨터": ["IT", "이공계", "교육"], "보건": ["보건간호", "의약계", "교육"],
}

SUBJECTS = ["국어", "수학", "영어", "과학", "사회"]

# ============================================================
# AI 점수 엔진 (3학년과 동일 로직)
# ============================================================
def score_career(course_name, course, profile):
    if not profile["career_tracks"]:
        return 50
    
    # 1순위: TRACK_COMBOS 추천 목록에 직접 포함된 과목 → 100
    for trk in profile["career_tracks"]:
        if trk in TRACK_COMBOS:
            combo = TRACK_COMBOS[trk]
            for sem in combo:
                if sem in ["desc"]: continue
                for grp in combo[sem]:
                    items = combo[sem][grp]
                    if isinstance(items, list):
                        if course_name in items: return 100
                    else:
                        if course_name == items: return 100

    # 2순위: 희망 직업 키워드 매칭 → 90
    job = profile.get("dream_job", "").strip().replace(" ", "")
    if job:
        kw_all = course.get("kw", []) + [course_name]
        if any(job in kw or kw in job for kw in kw_all):
            return 90

    # 3순위: track 태그만 겹치는 과목 → 70 (기존 100에서 하향)
    p_tracks_str = " ".join(profile["career_tracks"])
    for t in course["tracks"]:
        if t in p_tracks_str:
            return 70

    return 0

def score_affinity(course, profile):
    aff = course["aff"]
    score, total_w = 0, 0
    for subj, weight in aff.items():
        if weight == 0: continue
        total_w += weight
        grade_norm = (6 - profile["grades"].get(subj, 3)) / 5
        like_bonus = 0.3 if subj in profile["likes"] else 0
        dislike_pen = -0.4 if subj in profile["dislikes"] else 0
        score += (grade_norm + like_bonus + dislike_pen) * weight
    return max(0, min(100, (score / total_w) * 100)) if total_w else 80

def score_learning_style(course, profile):
    style = profile["learning_style"]
    if style == "골고루": return 70
    style_map = {"암기": "mem", "이해": "und", "실습": "pra"}
    return course.get(style_map.get(style, "und"), 0.5) * 100

def score_eval(course, profile):
    pref = profile["eval_pref"]
    if pref == "상관없어요": return 70
    is_abs = "절대" in course["eval"]
    if pref == "절대평가가 편해요" and is_abs: return 100
    if pref == "상대평가도 괜찮아요" and not is_abs: return 80
    if pref == "절대평가가 편해요" and not is_abs: return 30
    return 60

def score_workload(course, profile):
    diff = abs(course["wl"] - profile["workload_pref"])
    return max(0, 100 - diff * 25)

def score_grade_comp(course, profile):
    sens = profile["grade_sens"]
    gc_map = {"낮음": 90, "보통": 60, "높음": 30}
    base = gc_map.get(course["gc"], 60)
    return 70 + (base - 70) * (sens / 5)

def calc_total_score(course_name, course, profile):
    weights = {"career": 0.35, "affinity": 0.25, "style": 0.10, "eval": 0.10, "workload": 0.10, "grade": 0.10}
    scores = {
        "career": score_career(course_name, course, profile),
        "affinity": score_affinity(course, profile),
        "style": score_learning_style(course, profile),
        "eval": score_eval(course, profile),
        "workload": score_workload(course, profile),
        "grade": score_grade_comp(course, profile),
    }
    total = sum(scores[k] * weights[k] for k in weights)
    if profile["career_tracks"] and scores["career"] == 0:
        total *= 0.7
    job = profile.get("dream_job", "").strip().replace(" ", "")
    if job:
        kw_all = course.get("kw", []) + [course_name]
        if any(kw in job or job in kw for kw in kw_all):
            total = min(100, total + 15)
    # TRACK_COMBOS 추천 목록 순서에 따른 미세 가산점 (동점 방지)
    combo_bonus = 0
    for trk in profile.get("career_tracks", []):
        if trk in TRACK_COMBOS:
            combo = TRACK_COMBOS[trk]
            for sem in ["1학기", "2학기"]:
                for grp in combo[sem]:
                    items = combo[sem][grp]
                    if isinstance(items, list):
                        if course_name in items:
                            idx = items.index(course_name)
                            combo_bonus = max(combo_bonus, (len(items) - idx) * 0.5)
                    else:
                        if course_name == items:
                            combo_bonus = max(combo_bonus, 1.0)
    total = min(100, total + combo_bonus)
    return round(total, 1), scores

def generate_explanation(course_name, course, scores, profile):
    reasons, warnings = [], []
    if scores["career"] >= 70:
        reasons.append("선택한 진로 계열과 높은 연관성이 있어요")
    if scores["affinity"] >= 70:
        top_subj = max(course["aff"], key=course["aff"].get)
        reasons.append(f"{top_subj} 실력이 뒷받침되어 잘 맞아요")
    elif scores["affinity"] >= 50:
        reasons.append("기초 과목 성적과 적절히 매칭돼요")
    if scores["style"] >= 70:
        reasons.append("선호하는 학습 방식과 잘 맞아요")
    if scores["eval"] >= 80:
        reasons.append("선호하는 평가 방식이에요")
    if scores["grade"] >= 80 and profile["grade_sens"] >= 3:
        reasons.append("등급 받기에 비교적 유리해요")
    if scores["workload"] >= 80:
        reasons.append("원하는 공부 부담 수준과 잘 맞아요")
    if not reasons:
        reasons.append("전반적으로 균형 잡힌 선택이에요")
    univ_note = course.get("univ_note", "")
    if univ_note and scores["career"] >= 70:
        reasons.append(f"🎓 {univ_note}")
    for subj, min_g in course.get("rmg", {}).items():
        student_g = profile["grades"].get(subj, 3)
        if student_g > min_g:
            warnings.append(f"{subj} 현재 {student_g}등급 — 기초가 부족하면 어려울 수 있어요")
    if scores["workload"] < 40:
        warnings.append("원하는 부담 수준보다 학습량이 많을 수 있어요")
    if course["diff"] >= 4 and scores["affinity"] < 50:
        warnings.append("난이도가 높은 과목이라 관련 기초 과목 성적을 확인해보세요")
    if profile["career_tracks"] and scores["career"] == 0:
        warnings.append("선택하신 희망 진로 계열과 무관한 과목입니다. 단순 성적 관리가 목적이 아니라면 재고해보세요.")
    return reasons, warnings

# ============================================================
# 렌더링 함수
# ============================================================
def render_card(name, info, is_rec=False):
    cls = "course-card rec" if is_rec else "course-card"
    ev_cls = "badge-eval-rel" if "상대" in info["eval"] else "badge-eval-abs"
    rec = '<span class="badge badge-rec">⭐ 추천</span> ' if is_rec else ""
    tracks = "".join(f'<span class="badge badge-track">{t}</span>' for t in info["tracks"])
    univ_html = ""
    if info.get("univ_note"):
        univ_html = f'<div class="ai-univ-note">🎓 {info["univ_note"]}</div>'
    st.markdown(f"""<div class="{cls}">
<div class="course-name">{rec}{name}</div>
<div style="margin-bottom:0.4rem;"><span class="badge badge-group">{info["grp"]} · {info["cr"]}학점</span><span class="badge {ev_cls}">{info["eval"]}</span></div>
<div class="course-desc">{info["desc"]}</div><div>{tracks}</div>
{univ_html}
</div>""", unsafe_allow_html=True)

def render_group(sem_filter, grp, rec_names):
    items = {k: v for k, v in COURSES.items() if v["sem"] == sem_filter and v["grp"] == grp}
    recs = {k: v for k, v in items.items() if k in rec_names}
    others = {k: v for k, v in items.items() if k not in rec_names}
    for n, i in recs.items():
        render_card(n, i, True)
    if others:
        with st.expander(f"나머지 {len(others)}개 과목 보기"):
            for n, i in others.items():
                render_card(n, i, False)

def get_rec_names(combo):
    names = set()
    for sk in ["1학기", "2학기"]:
        s = combo[sk]
        for grp in s:
            items = s[grp]
            if isinstance(items, list):
                names.update(items)
            else:
                names.add(items)
    return names

def render_ai_card(rank, name, info, total_score, scores, reasons, warnings, is_top=False):
    cls = "ai-card top" if is_top else "ai-card"
    sc_cls = "high" if total_score >= 70 else ("mid" if total_score >= 50 else "low")
    ev_cls = "badge-eval-rel" if "상대" in info["eval"] else "badge-eval-abs"
    tracks_html = "".join(f'<span class="badge badge-track">{t}</span>' for t in info["tracks"])
    reasons_html = "".join(f"<li>{r}</li>" for r in reasons)
    warnings_html = "".join(f"<li>⚠️ {w}</li>" for w in warnings)
    warn_block = f'<div class="ai-warning"><ul style="margin:0;padding-left:1.2rem;">{warnings_html}</ul></div>' if warnings else ""
    univ_note = info.get("univ_note", "")
    univ_block = ""
    if univ_note and not any("🎓" in r for r in reasons):
        univ_block = f'<div class="ai-univ-note">🎓 {univ_note}</div>'
    st.markdown(f"""<div class="{cls}">
<div style="display:flex;align-items:center;margin-bottom:0.4rem;">
<span class="ai-score {sc_cls}">{total_score}점</span>
<span class="course-name" style="margin-bottom:0;">{name}</span>
</div>
<div style="margin-bottom:0.5rem;">
<div class="score-bar-bg"><div class="score-bar-fill {sc_cls}" style="width:{total_score}%;"></div></div>
</div>
<div style="margin-bottom:0.4rem;">
<span class="badge badge-group">{info["grp"]} · {info["cr"]}학점</span>
<span class="badge {ev_cls}">{info["eval"]}</span>
{tracks_html}
</div>
<div class="course-desc">{info["desc"]}</div>
<div class="ai-reason"><b>추천 이유:</b><ul style="margin:0.2rem 0 0;padding-left:1.2rem;">{reasons_html}</ul></div>
{warn_block}
{univ_block}
</div>""", unsafe_allow_html=True)

def render_univ_guide_boxes(career_tracks):
    guides_shown = []
    for trk in career_tracks:
        if trk in TRACK_UNIV_GUIDE:
            guides_shown.append((trk, TRACK_UNIV_GUIDE[trk]))
    if not guides_shown: return
    for trk_name, guide in guides_shown[:3]:
        st.markdown(f"""<div class="univ-guide-box">
<div class="guide-title">{guide["icon"]} {trk_name} — 대입 참고사항</div>
<div class="guide-prereq">📌 <b>대학별 권장:</b> {guide["prereq"]}</div>
<div class="guide-3rd">💡 <b>2학년 선택 포인트:</b> {guide["third"]}</div>
</div>""", unsafe_allow_html=True)

# ============================================================
# 기본 세팅
# ============================================================
if "profile" not in st.session_state:
    st.session_state.profile = {
        "dream_job": "", "career_tracks": [],
        "grades": {subj: 3 for subj in SUBJECTS},
        "likes": [], "dislikes": [],
        "learning_style": "골고루", "eval_pref": "상관없어요",
        "workload_pref": 3, "grade_sens": 3,
    }

# ============================================================
# 사이드바 프로필 폼
# ============================================================
st.sidebar.markdown("### 🤖 나의 프로필 설정")
st.sidebar.caption("프로필을 입력하면 AI 맞춤 추천을 받을 수 있어요!")

with st.sidebar.form("profile_form"):
    st.markdown("**🎯 진로**")
    dream_job = st.text_input("희망 직업", placeholder="예: 프로그래머, 간호사, 교사 ...")
    career_tracks = st.multiselect("관심 계열 (복수 선택 가능)", list(TRACK_COMBOS.keys()))
    st.markdown("---")
    st.markdown("**📊 현재 성적 (1학년 기준)**")
    grades = {}
    gcols = st.columns(len(SUBJECTS))
    for i, subj in enumerate(SUBJECTS):
        with gcols[i]:
            grades[subj] = st.selectbox(subj, list(range(1, 6)), index=2, key=f"g_{subj}")
    st.markdown("---")
    st.markdown("**💡 과목 호불호**")
    likes = st.multiselect("좋아하는/잘하는 영역", SUBJECTS, key="likes")
    dislikes = st.multiselect("싫어하는/어려운 영역", SUBJECTS, key="dislikes")
    st.markdown("---")
    st.markdown("**📝 학습 스타일**")
    learning_style = st.radio("선호하는 학습 방식", ["암기", "이해", "실습", "골고루"], index=3, horizontal=True)
    eval_pref = st.radio("평가 방식 선호", ["상대평가도 괜찮아요", "절대평가가 편해요", "상관없어요"], index=2)
    workload_pref = st.slider("공부 부담 수준", 1, 5, 3, help="1=여유롭게, 5=빡빡하게")
    grade_sens = st.slider("내신 등급 중요도", 1, 5, 3, help="1=배우고 싶은 거 위주, 5=등급 유리한 과목 위주")
    submitted = st.form_submit_button("🚀 AI 추천 받기", use_container_width=True)

if submitted:
    auto_tracks = set()
    for job_kw, trk_list in JOB_TO_TRACKS.items():
        if dream_job and job_kw in dream_job:
            auto_tracks.update(trk_list)
    all_track_names = set(career_tracks)
    for at in auto_tracks:
        for tk in TRACK_COMBOS:
            if at in tk:
                all_track_names.add(tk)
    st.session_state.profile = {
        "dream_job": dream_job, "career_tracks": list(all_track_names),
        "grades": grades, "likes": likes, "dislikes": dislikes,
        "learning_style": learning_style, "eval_pref": eval_pref,
        "workload_pref": workload_pref, "grade_sens": grade_sens,
    }

# ============================================================
# UI
# ============================================================
st.markdown("""<div class="main-header"><h1>📚 삼괴고 2학년 선택과목 가이드</h1>
<p>2026학년도 입학생 교육과정 편제 기준 · 진로별 추천 조합 & AI 맞춤 추천</p></div>""", unsafe_allow_html=True)

st.markdown("""
<div style="background-color: #fffbeb; border: 1px solid #fef3c7; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 1.2rem 1.5rem; margin-bottom: 2rem;">
    <div style="font-size: 1.15rem; font-weight: 700; color: #b45309; margin-bottom: 0.4rem;">
        ⚠️ 과목 선택 전 반드시 읽어주세요!
    </div>
    <div style="color: #92400e; font-size: 0.95rem; line-height: 1.6;">
        본 가이드 및 AI 맞춤 추천 결과는 학생 여러분의 선택을 돕기 위한 <b>참고자료</b>일 뿐입니다.<br>
        2학년 과목 선택은 <b>3학년 심화 과목의 기초</b>가 되며, <b>대학별 권장 이수 과목</b>과 직결됩니다.<br>
        최종 과목 선택은 본인의 희망 진로, 목표 대학의 입시 요강을 꼼꼼히 확인하고, <b>교과 담당 선생님 및 담임 선생님, 부모님 등과 충분한 상담을 통해 신중하게 결정</b>하시기 바랍니다.
    </div>
</div>
""", unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["🤖 AI 맞춤 추천", "🎯 진로별 추천 조합", "🔍 키워드 검색", "📋 전체 과목 보기"])

# ── 탭1: AI 맞춤 추천 ──
with tab1:
    profile = st.session_state.get("profile")
    if not profile:
        st.markdown("""<div style="text-align:center;padding:3rem 1rem;">
            <div style="font-size:3rem;margin-bottom:1rem;">🤖</div>
            <h3 style="color:#1a365d;">AI 맞춤 추천을 받아보세요!</h3>
            <p style="color:#64748b;font-size:0.95rem;max-width:500px;margin:0.5rem auto;">
                왼쪽 사이드바에서 <b>나의 프로필</b>을 설정하면<br>
                나에게 딱 맞는 과목을 추천해 드립니다.</p></div>""", unsafe_allow_html=True)
    else:
        strong_subjs = sorted(profile["grades"].items(), key=lambda x: x[1])[:2]
        strong_text = ", ".join(f"{s} {g}등급" for s, g in strong_subjs)
        track_text = ", ".join(profile["career_tracks"][:3]) if profile["career_tracks"] else "미선택"
        job_text = profile["dream_job"] if profile["dream_job"] else "미입력"
        st.markdown(f"""<div class="ai-profile-banner">
            <h3>📊 나의 프로필 분석 결과</h3>
            <p>🎯 희망 직업: <b>{job_text}</b> | 관심 계열: <b>{track_text}</b></p>
            <p>💪 강점 과목: <b>{strong_text}</b> | 학습 성향: <b>{profile["learning_style"]}</b> 중심</p>
            <p>📈 등급 중요도: <b>{"★" * profile["grade_sens"]}{"☆" * (5 - profile["grade_sens"])}</b> | 부담 수준: <b>{"▮" * profile["workload_pref"]}{"▯" * (5 - profile["workload_pref"])}</b></p>
        </div>""", unsafe_allow_html=True)

        if profile["career_tracks"]:
            render_univ_guide_boxes(profile["career_tracks"])

        all_scores = {}
        for name, info in COURSES.items():
            total, breakdown = calc_total_score(name, info, profile)
            reasons, warnings = generate_explanation(name, info, breakdown, profile)
            all_scores[name] = {"total": total, "breakdown": breakdown, "reasons": reasons, "warnings": warnings}

        for sem_label, sem_filter, _ in SEM_INFO:
            st.markdown(f'<div class="semester-title">{sem_label}</div>', unsafe_allow_html=True)
            for grp in get_grp_order(sem_filter):
                grp_courses = {k: v for k, v in COURSES.items() if v["sem"] == sem_filter and v["grp"] == grp}
                if not grp_courses: continue
                sorted_courses = sorted(grp_courses.keys(), key=lambda x: all_scores[x]["total"], reverse=True)
                pick_count = GRP_COUNT[grp]
                if len(sorted_courses) >= pick_count:
                    cut_off_score = all_scores[sorted_courses[pick_count - 1]]["total"]
                else:
                    cut_off_score = -1
                top_courses = [c for c in sorted_courses if all_scores[c]["total"] >= cut_off_score]
                remaining = [c for c in sorted_courses if all_scores[c]["total"] < cut_off_score]
                st.markdown(f'<div class="group-title">📌 {GRP_LABELS[grp]}</div>', unsafe_allow_html=True)
                if len(top_courses) > pick_count:
                    st.caption(f"🏆 상위 추천 과목 (동점 포함 총 {len(top_courses)}개)")
                else:
                    st.caption(f"🏆 상위 {pick_count}개 추천 과목")
                for rank, cname in enumerate(top_courses, 1):
                    sc = all_scores[cname]
                    render_ai_card(rank, cname, COURSES[cname], sc["total"], sc["breakdown"], sc["reasons"], sc["warnings"], is_top=True)
                if remaining:
                    with st.expander(f"나머지 {len(remaining)}개 과목 보기"):
                        for i, cname in enumerate(remaining):
                            rank = len(top_courses) + i + 1
                            sc = all_scores[cname]
                            render_ai_card(rank, cname, COURSES[cname], sc["total"], sc["breakdown"], sc["reasons"], sc["warnings"], is_top=False)

# ── 탭2: 진로별 추천 조합 ──
with tab2:
    sel = st.selectbox("관심 진로를 선택하세요", list(TRACK_COMBOS.keys()))
    combo = TRACK_COMBOS[sel]
    rec_names = get_rec_names(combo)

    if sel in TRACK_UNIV_GUIDE:
        guide = TRACK_UNIV_GUIDE[sel]
        st.markdown(f"""<div class="univ-guide-box">
<div class="guide-title">{guide["icon"]} 2028 대입 참고사항</div>
<div class="guide-prereq">📌 <b>대학별 권장:</b> {guide["prereq"]}</div>
<div class="guide-3rd">💡 <b>2학년 선택 포인트:</b> {guide["third"]}</div>
</div>""", unsafe_allow_html=True)

    st.markdown(f'<div class="combo-box"><div class="combo-title">🎯 {sel}</div><div class="course-desc" style="margin-bottom:0.8rem;">{combo["desc"]}</div>', unsafe_allow_html=True)
    for sk in ["1학기", "2학기"]:
        sem_data = combo[sk]
        st.markdown(f'<div class="combo-sem">{"📘" if sk == "1학기" else "📗"} 2학년 {sk}</div>', unsafe_allow_html=True)
        for grp in sem_data:
            items = sem_data[grp]
            if isinstance(items, list):
                items_str = ", ".join(items)
            else:
                items_str = items
            st.markdown(f'<div class="combo-item"><b>{grp}:</b> {items_str}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("#### 과목 상세 정보")
    st.caption("⭐ 추천 과목이 상단에, 같은 그룹의 나머지 과목은 펼쳐서 볼 수 있습니다.")

    for sem_label, sem_filter, _ in SEM_INFO:
        st.markdown(f'<div class="semester-title">{sem_label}</div>', unsafe_allow_html=True)
        for grp in get_grp_order(sem_filter):
            st.markdown(f'<div class="group-title">📌 {GRP_LABELS[grp]}</div>', unsafe_allow_html=True)
            render_group(sem_filter, grp, rec_names)

# ── 탭3: 키워드 검색 ──
with tab3:
    q = st.text_input("키워드를 입력하세요", placeholder="예: 의대, 반도체, 외교, 중국어, 유전 ...")
    st.caption("쉼표로 여러 키워드를 입력할 수 있어요")
    if q.strip():
        qs = [x.strip().lower() for x in q.split(",") if x.strip()]
        matched = set()
        for name, info in COURSES.items():
            txt = (name + " " + info["desc"] + " " + " ".join(info["kw"]) + " " + " ".join(info["tracks"])).lower()
            if any(kw in txt for kw in qs):
                matched.add(name)
        st.markdown(f'<p style="color:#64748b;font-size:0.9rem;">총 <b>{len(matched)}개</b> 과목이 검색되었습니다.</p>', unsafe_allow_html=True)
        if matched:
            for sem_label, sem_filter, _ in SEM_INFO:
                sem_match = {k for k in matched if COURSES[k]["sem"] == sem_filter}
                if not sem_match: continue
                st.markdown(f'<div class="semester-title">{sem_label}</div>', unsafe_allow_html=True)
                grps_in_sem = []
                for grp in get_grp_order(sem_filter):
                    if any(COURSES[k]["grp"] == grp for k in sem_match):
                        grps_in_sem.append(grp)
                for grp in grps_in_sem:
                    st.markdown(f'<div class="group-title">📌 {GRP_LABELS[grp]}</div>', unsafe_allow_html=True)
                    render_group(sem_filter, grp, matched)
        else:
            st.warning("검색 조건에 맞는 과목이 없습니다. 다른 키워드를 시도해보세요.")
    else:
        st.info("👆 키워드를 입력하면 관련 과목을 검색하고, 같은 선택 그룹의 나머지 과목도 함께 보여줍니다.")

# ── 탭4: 전체 과목 보기 ──
with tab4:
    for sem_label, sem_filter, _ in SEM_INFO:
        st.markdown(f'<div class="semester-title">{sem_label}</div>', unsafe_allow_html=True)
        for grp in get_grp_order(sem_filter):
            st.markdown(f'<div class="group-title">📌 {GRP_LABELS[grp]}</div>', unsafe_allow_html=True)
            for name, info in COURSES.items():
                if info["sem"] != sem_filter or info["grp"] != grp: continue
                render_card(name, info)

st.markdown("""<div style="text-align:center;color:#94a3b8;font-size:0.8rem;padding:1rem 0;">
삼괴고등학교 교육과정부 · 2025학년도 입학생 교육과정 편제표 기준<br>
해당 내용은 어디까지나 참고 자료일 뿐, 꼭 해당 과목으로 선택해야 하는 것은 아닙니다<br>
※ 과목별 상세 내용은 담당 교과 선생님께 문의하세요</div>""", unsafe_allow_html=True)
