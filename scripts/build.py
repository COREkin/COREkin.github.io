#!/usr/bin/env python3
"""포트폴리오 3개 언어 페이지(/, /ja/, /ko/)를 생성한다.

콘텐츠 정본은 MyPortfolio(portfolio-website/content/{en,ja,ko}/*.md)다. 그쪽을 고치면 아래 CONTENT를 맞추고
`python3 scripts/build.py`를 실행한다. 표준 라이브러리만 쓴다. 개인정보처리방침(kinboard/privacy/)은 이 스크립트가
만들지 않는다.
"""
from __future__ import annotations

import json
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://corekin.github.io"
EMAIL = "aaaa8757@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/dongsikk/"
GITHUB = "https://github.com/COREkin"
BLOG = "https://kin-archive.tistory.com/"

# Material Symbols에서 쓰는 아이콘. Google Fonts의 icon_names는 알파벳순이어야 한다.
ICONS = sorted({
    "article", "cloud", "cloud_done", "code", "cloud_queue", "database", "description", "history_edu",
    "language", "link", "location_on", "psychology", "router", "school", "science", "settings_suggest",
    "smartphone", "stars", "sync", "translate", "verified", "web", "workspace_premium",
})
FONT_LINKS = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
    '  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
    '  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&amp;display=swap">\n'
    '  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0'
    f'&amp;icon_names={",".join(ICONS)}&amp;display=block">'
)

LOCALES = [
    # (code, path, html lang, menu label)
    ("en", "/", "en", "English"),
    ("ja", "/ja/", "ja", "日本語"),
    ("ko", "/ko/", "ko", "한국어"),
]

SKILLS = [
    ("Cloud Platforms", "cloud_queue", ["Azure", "AWS", "GCP"]),
    ("Database", "database", ["MySQL", "Aurora MySQL", "RDS MySQL", "SQL Server", "MariaDB", "PostgreSQL", "AWS DMS"]),
    ("Programming", "code", ["Python", "TypeScript", "JavaScript", "PHP"]),
    ("Frontend", "web", ["Vue 3", "Vue.js", "Nuxt.js", "WordPress"]),
    ("Mobile", "smartphone", ["Flutter"]),
    ("CI/CD", "sync", ["GitHub Actions", "CircleCI"]),
    ("Infrastructure as Code", "settings_suggest", ["Terraform", "AWS CDK", "CloudFormation"]),
    ("AI & GenAI", "psychology", ["Amazon Bedrock", "Kiro AI", "Prompt Engineering", "Claude (Anthropic)", "Stable Diffusion"]),
]

AZURE = [
    "Microsoft Certified - Azure Virtual Desktop Specialty",
    "Microsoft Certified - Azure Solutions Architect Expert",
    "Microsoft Certified - DevOps Engineer Expert",
    "Microsoft Certified - Azure Administrator Associate",
    "Microsoft Certified - Azure Developer Associate",
    "Microsoft Certified - Azure Fundamentals",
    "Microsoft Certified - Azure AI Fundamentals",
    "Microsoft Certified - Azure Data Fundamentals",
]


def certifications(ipa: str) -> list[tuple[str, str, list[str]]]:
    return [
        ("Azure", "workspace_premium", AZURE),
        ("AWS", "verified", ["AWS Certified Cloud Practitioner"]),
        ("GCP", "stars", ["Google Cloud Associate Cloud Engineer", "Google Cloud Digital Leader"]),
        ("Alibaba", "stars", ["ACA Cloud Computing Certification"]),
        ("Specialty", "stars", [ipa]),
        ("Language", "translate", ["JLPT N1 (2013.12)", "TOEIC 880 (2020.12)"]),
    ]


TOKYO_TECH = [
    "SysML (Activity, State Machine, Parametric Diagrams)",
    "Lattice Theory, Causal Modeling",
    "MATLAB / Python",
    "Factory Automation, Fault Detection and Diagnosis",
]
TOKYO_DETAIL = "https://otalab.race.t.u-tokyo.ac.jp/wpdir/wp-content/uploads/2022/05/2022_Intro_Japanese_Shirafuji2.pdf"

CONTENT = {
    "en": {
        "name": "Kim Dongsik",
        "headline": "Cloud Native &amp; Database Expert",
        "experiences": [
            {
                "company": "Amazon Web Services Japan G.K.", "role": "Cloud Support Engineer", "location": "Tokyo, Japan",
                "start": "2023-07", "end": None,
                "items": [
                    "Support AWS Database services including Aurora/RDS MySQL, SQL Server, MariaDB, PostgreSQL, and AWS DMS",
                    "Support database tasks like database architecture design, troubleshooting, issue resolution, data migration, and optimization",
                    "Specialize in MySQL, SQL Server, and DMS, with experience in MariaDB and PostgreSQL",
                    "Assisting customers with cloud-native architecture design",
                ],
            },
            {
                "company": "SoftBank Corp.", "role": "DevOps Engineer", "location": "Tokyo, Japan",
                "start": "2022-04", "end": "2023-06",
                "items": [
                    "Designed and implemented CI/CD pipelines using GitHub Actions and CircleCI",
                    "Managed multi-cloud infrastructure across Azure, AWS, and GCP",
                    "Automated infrastructure provisioning with Terraform",
                    "Led cloud migration projects for enterprise clients",
                ],
            },
        ],
        "education": [
            {
                "institution": "The University of Tokyo", "degree": "Master of Engineering", "field": "Precision Engineering",
                "location": "Tokyo, Japan", "start": "2020-04", "end": "2022-03", "grade": "3.857/4.0",
                "lab": "Mobile Robotics Laboratory", "lab_url": "https://otalab.race.t.u-tokyo.ac.jp/",
                "title": "Modeling and Generalizing Causal Relationships in Production Lines for Knowledge Description",
                "summary": 'To address the shortage of skilled workers in manufacturing, I formalized the "tacit knowledge" of experts by combining SysML with the mathematical theory of "Lattices." By modeling the causal relationships between equipment in complex automated production lines, I visualized the process of diagnosing failure causes and provided a framework to quantitatively analyze the differences in cognitive patterns between experts and novices.',
                "tech": TOKYO_TECH, "detail": TOKYO_DETAIL,
                "papers": [("Master's Thesis", "/papers/master-thesis.pdf"), ("RSJ 2021 Conference Paper", "/papers/rsj2021.pdf")],
            },
            {
                "institution": "Yokohama National University", "degree": "Bachelor of Engineering", "field": "Mechanical Engineering",
                "location": "Yokohama, Japan", "start": "2016-04", "end": "2020-03", "grade": "3.783/4.5",
                "lab": "Maeda Laboratory", "lab_url": "https://iir.ynu.ac.jp/index-j.html",
                "title": "Robot Teaching Support System Using AR Smart Glasses",
                "summary": 'To address the challenges faced by unskilled workers in "online programming" of industrial robots, I developed a teaching support system using AR (Augmented Reality) smart glasses. By visualizing the robot\'s movable range, joint limits, and distances between poses as 3D models in real-time, the system enables operators to intuitively understand the robot\'s status and perform teaching tasks safely and efficiently.',
                "tech": ["Unity, Vuforia (AR Implementation)", "ROS (Robot Operating System)", "C#, C++", "SolidWorks (3D Modeling)", "DENSO COBOTTA, Epson MOVERIO BT-30E"],
                "papers": [("Bachelor's Thesis", "/papers/bachelor-thesis.pdf")],
                "scholarship": "Japan-Korea Joint Scholarship Program for Science and Engineering Students (2015 - 2022)",
            },
        ],
        "ipa": "IPA Applied Information Technology Engineer",
        "languages": [("🇰🇷", "Korean", "Native", None), ("🇯🇵", "Japanese", "Fluent", "JLPT N1 (2013.12)"), ("🇺🇸", "English", "Business Level", "TOEIC 880 (2020.12)")],
        "privacy": "Kin Board Privacy Policy",
        "more": "Summary &amp; Tech Stack",
    },
    "ja": {
        "name": "金 棟植",
        "headline": "クラウドネイティブ &amp; データベースエキスパート",
        "experiences": [
            {
                "company": "Amazon Web Services Japan G.K.", "role": "Cloud Support Engineer", "location": "Tokyo, Japan",
                "start": "2023-07", "end": None,
                "items": [
                    "Aurora/RDS MySQL、SQL Server、MariaDB、PostgreSQL、AWS DMSを含むAWSデータベースサービスのサポート",
                    "データベースアーキテクチャ設計、トラブルシューティング、問題解決、データ移行、最適化などのデータベース作業のサポート",
                    "MySQL、SQL Server、DMSを専門とし、MariaDB、PostgreSQLの経験を保有",
                    "クラウドネイティブアーキテクチャ設計の支援",
                ],
            },
            {
                "company": "ソフトバンク株式会社", "role": "DevOps Engineer", "location": "Tokyo, Japan",
                "start": "2022-04", "end": "2023-06",
                "items": [
                    "GitHub ActionsとCircleCIを使用したCI/CDパイプラインの設計と実装",
                    "Azure、AWS、GCPにわたるマルチクラウドインフラの管理",
                    "Terraformによるインフラプロビジョニングの自動化",
                    "エンタープライズクライアント向けクラウド移行プロジェクトのリード",
                ],
            },
        ],
        "education": [
            {
                "institution": "東京大学", "degree": "工学修士", "field": "精密工学",
                "location": "Tokyo, Japan", "start": "2020-04", "end": "2022-03", "grade": "3.857/4.0",
                "lab": "移動ロボティクス研究室", "lab_url": "https://otalab.race.t.u-tokyo.ac.jp/",
                "title": "生産ラインにおける因果関係のモデル化と一般化による知識の記述",
                "summary": "製造現場における熟練工不足を解決するため、熟練者の「暗黙知」を数学的な「束（Lattice）」論とSysMLを組み合わせて形式化。複雑な自動化生産ライン内の設備間の因果関係をモデリングし、システムの故障原因を特定するプロセスを可視化。熟練者と初心者の思考パターンの違いを定量的に分析できる基盤を構築。",
                "tech": TOKYO_TECH, "detail": TOKYO_DETAIL,
                "papers": [("修士論文", "/papers/master-thesis.pdf"), ("RSJ 2021 学会発表", "/papers/rsj2021.pdf")],
            },
            {
                "institution": "横浜国立大学", "degree": "工学士", "field": "機械工学",
                "location": "Yokohama, Japan", "start": "2016-04", "end": "2020-03", "grade": "3.783/4.5",
                "lab": "前田研究室", "lab_url": "https://iir.ynu.ac.jp/index-j.html",
                "title": "スマートグラスを用いたロボット指示支援システムの実装",
                "summary": "産業用ロボットの「オンライン教示」において、非熟練者が直面する課題を解決するため、AR（拡張現実）スマートグラスを用いた教示支援システムを開発。ロボットの可動範囲、各関節の限界角、姿勢間の距離などを3Dモデルでリアルタイムに可視化し、作業者が直感的にロボットの状態を把握し、安全かつ効率的に操作できるシステムを実装。",
                "tech": ["Unity, Vuforia (AR実装)", "ROS (Robot Operating System)", "C#, C++", "SolidWorks (3Dモデリング)", "DENSO COBOTTA, Epson MOVERIO BT-30E"],
                "papers": [("卒業論文", "/papers/bachelor-thesis.pdf")],
                "scholarship": "日韓共同理工系学部留学生 (2015 - 2022)",
            },
        ],
        "ipa": "IPA 応用情報技術者",
        "languages": [("🇰🇷", "韓国語", "ネイティブ", None), ("🇯🇵", "日本語", "流暢レベル", "JLPT N1 (2013.12)"), ("🇺🇸", "英語", "ビジネスレベル", "TOEIC 880 (2020.12)")],
        "privacy": "Kin Board プライバシーポリシー",
        "more": "研究概要・技術スタック",
    },
    "ko": {
        "name": "김동식",
        "headline": "클라우드 네이티브 &amp; 데이터베이스 전문가",
        "experiences": [
            {
                "company": "Amazon Web Services Japan G.K.", "role": "Cloud Support Engineer", "location": "Tokyo, Japan",
                "start": "2023-07", "end": None,
                "items": [
                    "Aurora/RDS MySQL, SQL Server, MariaDB, PostgreSQL, AWS DMS를 포함한 AWS 데이터베이스 서비스 지원",
                    "데이터베이스 아키텍처 설계, 트러블슈팅, 문제 해결, 데이터 마이그레이션, 최적화 등의 데이터베이스 작업 지원",
                    "MySQL, SQL Server, DMS를 전문으로 하며, MariaDB, PostgreSQL 경험 보유",
                    "클라우드 네이티브 아키텍처 설계 지원",
                ],
            },
            {
                "company": "소프트뱅크 주식회사", "role": "DevOps Engineer", "location": "Tokyo, Japan",
                "start": "2022-04", "end": "2023-06",
                "items": [
                    "GitHub Actions 및 CircleCI를 사용한 CI/CD 파이프라인 설계 및 구현",
                    "Azure, AWS, GCP에 걸친 멀티 클라우드 인프라 관리",
                    "Terraform을 사용한 인프라 프로비저닝 자동화",
                    "엔터프라이즈 고객을 위한 클라우드 마이그레이션 프로젝트 리드",
                ],
            },
        ],
        "education": [
            {
                "institution": "도쿄대학교", "degree": "공학 석사", "field": "정밀공학",
                "location": "Tokyo, Japan", "start": "2020-04", "end": "2022-03", "grade": "3.857/4.0",
                "lab": "이동 로보틱스 연구실", "lab_url": "https://otalab.race.t.u-tokyo.ac.jp/",
                "title": "생산 라인의 인과 관계 모델링 및 지식 기술",
                "summary": "제조 현장의 숙련공 부족 문제를 해결하기 위해, 숙련자의 '암묵지(경험과 직관)'를 수학적 '속(Lattice)' 이론과 SysML을 결합하여 형식화. 복잡한 자동화 생산 라인 내 장비 간의 인과 관계를 모델링하여 시스템의 고장 원인을 추론하는 과정을 가시화하고, 숙련자와 초보자의 사고 패턴 차이를 정량적으로 분석할 수 있는 기반을 마련.",
                "tech": TOKYO_TECH, "detail": TOKYO_DETAIL,
                "papers": [("석사 논문", "/papers/master-thesis.pdf"), ("RSJ 2021 학회 발표", "/papers/rsj2021.pdf")],
            },
            {
                "institution": "요코하마 국립대학교", "degree": "공학 학사", "field": "기계공학",
                "location": "Yokohama, Japan", "start": "2016-04", "end": "2020-03", "grade": "3.783/4.5",
                "lab": "마에다 연구실", "lab_url": "https://iir.ynu.ac.jp/index-j.html",
                "title": "AR 스마트글라스를 활용한 로봇 교시 지원 시스템",
                "summary": "산업용 로봇의 '온라인 프로그래밍(직접 교시)' 시 발생하는 비숙련자의 어려움을 해결하기 위해, AR(증강현실) 스마트글라스를 활용한 교시 지원 시스템을 개발. 로봇의 가동 범위, 관절 한계, 자세 간 거리 등을 3D 모델로 실시간 시각화하여 작업자가 직관적으로 로봇의 상태를 파악하고 안전하게 조작할 수 있도록 구현.",
                "tech": ["Unity, Vuforia (AR 구현)", "ROS (Robot Operating System)", "C#, C++", "SolidWorks (3D 모델링)", "DENSO COBOTTA, Epson MOVERIO BT-30E"],
                "papers": [("학사 논문", "/papers/bachelor-thesis.pdf")],
                "scholarship": "한일 이공계 학부 유학생 (2015 - 2022)",
            },
        ],
        "ipa": "IPA 응용정보기술자",
        "languages": [("🇰🇷", "한국어", "모국어", None), ("🇯🇵", "일본어", "유창함", "JLPT N1 (2013.12)"), ("🇺🇸", "영어", "비즈니스 레벨", "TOEIC 880 (2020.12)")],
        "privacy": "Kin Board 개인정보처리방침",
        "more": "연구 요약·기술 스택",
    },
}

NAV = [("experience", "Experience"), ("education", "Education"), ("skills", "Skills"),
       ("certifications", "Certifications"), ("languages", "Languages")]


def e(text: str) -> str:
    """텍스트를 HTML 이스케이프한다. CONTENT 안의 `&amp;`처럼 이미 이스케이프된 값은 쓰지 않는 필드에만 쓴다."""
    return escape(text, quote=True)


def mmyyyy(ym: str | None) -> str:
    if ym is None:
        return "Present"
    year, month = ym.split("-")
    return f"{month}/{year}"


def icon(name: str, cls: str = "") -> str:
    assert name in ICONS, f"icon_names에 없는 아이콘: {name}"
    extra = f" {cls}" if cls else ""
    return f'<span class="material-symbols-outlined{extra}" aria-hidden="true">{name}</span>'


def section_header(title: str, heading_id: str) -> str:
    return (f'<div class="section-header"><h2 class="section-title" id="{heading_id}">{title}</h2>'
            '<div class="section-divider"></div></div>')


def lang_menu(current: str) -> str:
    items = []
    for code, path, _, label in LOCALES:
        cur = ' aria-current="page"' if code == current else ""
        items.append(f'<li><a href="{path}" hreflang="{code}" lang="{code}" data-lang="{code}"{cur}>{label}</a></li>')
    return (
        '<details class="lang-menu">'
        f'<summary aria-label="Language">{icon("language")}<span class="lang-code">{current.upper()}</span></summary>'
        f'<ul class="lang-list">{"".join(items)}</ul></details>'
    )


def render(code: str) -> str:
    c = CONTENT[code]
    lang = next(l for l in LOCALES if l[0] == code)
    html_lang = lang[2]

    # Experience
    exp_items = []
    for i, x in enumerate(c["experiences"]):
        first = i == 0
        lis = "".join(
            f'<li><span class="list-marker{" active" if first else ""}" aria-hidden="true">■</span><span>{e(t)}</span></li>'
            for t in x["items"]
        )
        exp_items.append(
            '<div class="timeline-item">'
            f'<div class="timeline-icon-wrapper"><div class="timeline-icon{" active" if first else ""}">'
            f'{icon("cloud" if first else "router")}</div><div class="timeline-line"></div></div>'
            '<div class="timeline-content">'
            f'<div class="timeline-header"><h3 class="timeline-title{" text-primary" if first else ""}">{e(x["company"])} — {e(x["role"])}</h3>'
            f'<span class="timeline-date">{mmyyyy(x["start"])} — {mmyyyy(x["end"])}</span></div>'
            f'<div class="timeline-meta"><p class="timeline-subtitle">{e(x["role"])}</p>'
            f'<p class="timeline-location">{icon("location_on", "location-icon")}{e(x["location"])}</p></div>'
            f'<ul class="timeline-list">{lis}</ul>'
            '</div></div>'
        )

    # Education
    edu_cards = []
    for i, x in enumerate(c["education"]):
        links = []
        if x.get("detail"):
            links.append(f'<a class="research-link-btn" href="{e(x["detail"])}" target="_blank" rel="noopener noreferrer">'
                         f'{icon("description")}<span>Research Details</span></a>')
        for title, url in x["papers"]:
            links.append(f'<a class="research-link-btn" href="{e(url)}" target="_blank" rel="noopener noreferrer">'
                         f'{icon("article")}<span>{e(title)}</span></a>')
        chips = "".join(f'<li class="tech-chip">{e(t)}</li>' for t in x["tech"])
        scholarship = ""
        if x.get("scholarship"):
            scholarship = f'<p class="education-scholarship">{icon("school", "scholarship-icon")}{e(x["scholarship"])}</p>'
        edu_cards.append(
            '<article class="card education-card">'
            f'<div class="education-header">{icon("school" if i == 0 else "history_edu", "education-icon")}'
            '<div class="education-info">'
            f'<div class="education-title-row"><h3 class="education-institution">{e(x["institution"])}</h3>'
            f'<span class="education-date">{mmyyyy(x["start"])} — {mmyyyy(x["end"])}</span></div>'
            f'<p class="education-degree">{e(x["degree"])} in {e(x["field"])}</p>'
            f'<div class="education-meta"><p class="education-grade">Grade: {e(x["grade"])}</p>'
            f'<p class="education-location">{icon("location_on", "location-icon")}{e(x["location"])}</p></div>'
            '</div></div>'
            '<div class="education-research"><span class="research-label">Research:</span>'
            f'<div class="research-lab">{icon("science", "lab-icon")}'
            f'<a class="lab-link" href="{e(x["lab_url"])}" target="_blank" rel="noopener noreferrer">{e(x["lab"])}</a></div>'
            f'<p class="research-title">{e(x["title"])}</p>'
            f'<div class="research-links">{"".join(links)}</div>'
            f'<details class="research-more"><summary>{c["more"]}</summary>'
            f'<p class="research-summary">{e(x["summary"])}</p>'
            f'<h4 class="tech-stack-title">Tech Stack</h4><ul class="tech-chips">{chips}</ul></details>'
            '</div>'
            f'{scholarship}'
            '</article>'
        )

    # Skills
    skill_cards = ""
    for cat, ic, items in SKILLS:
        tags = "".join('<li class="skill-tag">' + e(s) + "</li>" for s in items)
        skill_cards += (f'<article class="card skill-card"><div class="skill-header">{icon(ic)}'
                        f'<h3 class="skill-category">{e(cat)}</h3></div><ul class="skill-tags">{tags}</ul></article>')

    # Certifications
    cert_cards = ""
    for p, ic, names in certifications(c["ipa"]):
        lis = "".join("<li>" + e(n) + "</li>" for n in names)
        cert_cards += (f'<article class="card cert-card"><div class="cert-header">{icon(ic)}'
                       f'<h3 class="cert-provider">{e(p)}</h3></div><ul class="cert-list">{lis}</ul></article>')

    # Languages
    lang_cards = "".join(
        f'<article class="card language-card"><div class="language-flag" aria-hidden="true">{flag}</div>'
        f'<h3 class="language-name">{e(name)}</h3><p class="language-level">{e(level)}</p>'
        + (f'<p class="language-cert">{e(cert)}</p>' if cert else "")
        + '</article>'
        for flag, name, level, cert in c["languages"]
    )

    nav_links = "".join(f'<a class="nav-link" href="#{sid}">{label}</a>' for sid, label in NAV)
    sitemap = "".join(f'<li><a href="#{sid}">{label}</a></li>' for sid, label in NAV[:4])
    alternates = "\n  ".join(f'<link rel="alternate" hreflang="{l[0]}" href="{SITE}{l[1]}">' for l in LOCALES)
    canonical = f"{SITE}{lang[1]}"
    asset = "/assets/style.css"

    person = {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": "Dongsik Kim",
        "url": canonical,
        "image": f"{SITE}/images/profile.webp",
        "jobTitle": "Cloud Support Engineer",
        "worksFor": {"@type": "Organization", "name": "Amazon Web Services Japan G.K."},
        "email": EMAIL,
        "sameAs": [LINKEDIN, GITHUB, BLOG],
        "knowsAbout": ["Cloud Computing", "AWS", "Azure", "Google Cloud Platform", "Database Administration", "DevOps",
                       "Infrastructure as Code"],
        "alumniOf": [{"@type": "CollegeOrUniversity", "name": "The University of Tokyo"},
                     {"@type": "CollegeOrUniversity", "name": "Yokohama National University"}],
    }

    # 루트(영어)에서만: 첫 방문이면 브라우저 언어로 /ja/·/ko/로 보낸다. 사용자가 고른 언어는 localStorage에 남긴다.
    redirect = ""
    if code == "en":
        redirect = (
            "<script>(function(){try{var p=localStorage.getItem('preferred-language');"
            "if(p===null){var n=(navigator.language||'').toLowerCase();"
            "if(n.indexOf('ko')===0){location.replace('/ko/');}else if(n.indexOf('ja')===0){location.replace('/ja/');}}"
            "}catch(e){}})();</script>\n  "
        )

    return f"""<!doctype html>
<html lang="{html_lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  {redirect}<title>Dongsik Kim - Cloud Native &amp; Database Expert</title>
  <meta name="description" content="Cloud Support Engineer at AWS Japan specializing in cloud-native solutions and database technologies. 14 cloud certifications across Azure, AWS, GCP, and Alibaba Cloud.">
  <meta property="og:title" content="Dongsik Kim - Cloud Native &amp; Database Expert">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{SITE}/images/profile.webp">
  <meta property="og:description" content="Cloud Support Engineer at AWS Japan specializing in cloud-native solutions and database technologies.">
  <link rel="canonical" href="{canonical}">
  {alternates}
  <link rel="alternate" hreflang="x-default" href="{SITE}/">
  {FONT_LINKS}
  <link rel="stylesheet" href="{asset}">
  <script type="application/ld+json">{json.dumps(person, ensure_ascii=False)}</script>
</head>
<body id="top">
<a class="skip-link" href="#main">Skip to content</a>
<nav class="fixed-nav" aria-label="Main">
  <div class="nav-container">
    <a href="#top" class="nav-brand">{icon("cloud_done")}<span class="brand-name">DONGSIK KIM</span></a>
    <div class="nav-links">{nav_links}</div>
    <div class="nav-actions">{lang_menu(code)}</div>
  </div>
</nav>

<main id="main">
  <section class="hero-section" aria-label="Profile">
    <div class="container">
      <div class="hero-content">
        <div class="profile-wrapper">
          <div class="profile-border-effect" aria-hidden="true"></div>
          <div class="profile-image-container">
            <img src="/images/profile.webp" alt="{e(c['name'])} Profile" class="profile-image" width="320" height="320" loading="eager">
          </div>
        </div>
        <div class="hero-text">
          <p class="hero-subtitle">{c["headline"]}</p>
          <h1 class="hero-title">{e(c["name"])}</h1>
          <p class="hero-description">Cloud Support Engineer at Amazon Web Services Japan G.K.</p>
          <div class="hero-actions">
            <a class="btn btn-primary" href="{LINKEDIN}" target="_blank" rel="noopener noreferrer">{icon("link")}LinkedIn</a>
            <a class="btn btn-secondary" href="mailto:{EMAIL}">Contact Me</a>
            <div class="location-info">{icon("location_on")}<span>Tokyo, Japan</span></div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section id="experience" class="section section-alt" aria-labelledby="experience-title">
    <div class="container">
      {section_header("WORK EXPERIENCE", "experience-title")}
      <div class="timeline">{"".join(exp_items)}</div>
    </div>
  </section>

  <section id="education" class="section" aria-labelledby="education-title">
    <div class="container">
      {section_header("EDUCATION", "education-title")}
      <div class="grid-2">{"".join(edu_cards)}</div>
    </div>
  </section>

  <section id="skills" class="section section-alt" aria-labelledby="skills-title">
    <div class="container">
      {section_header("TECHNICAL SKILLS", "skills-title")}
      <div class="skills-grid">{skill_cards}</div>
    </div>
  </section>

  <section id="certifications" class="section" aria-labelledby="certifications-title">
    <div class="container">
      {section_header("CERTIFICATIONS", "certifications-title")}
      <div class="grid-3">{cert_cards}</div>
    </div>
  </section>

  <section id="languages" class="section section-alt" aria-labelledby="languages-title">
    <div class="container">
      {section_header("LANGUAGES", "languages-title")}
      <div class="grid-3">{lang_cards}</div>
    </div>
  </section>
</main>

<footer class="footer">
  <div class="container">
    <div class="footer-top">
      <div>
        <div class="footer-brand">{icon("cloud_done")}<span class="brand-name">DONGSIK KIM</span></div>
        <p class="footer-copy">© 2026 Dongsik Kim. All rights reserved.</p>
      </div>
      <div class="footer-built"><span class="footer-label">Built with</span><span class="footer-tech">GitHub Pages · HTML/CSS · Kiro AI</span></div>
    </div>
    <div class="footer-columns">
      <nav class="footer-col" aria-labelledby="f-sitemap"><span class="footer-label" id="f-sitemap">Sitemap</span><ul>{sitemap}</ul></nav>
      <nav class="footer-col" aria-labelledby="f-resources"><span class="footer-label" id="f-resources">Resources</span><ul>
        <li><a href="{BLOG}" target="_blank" rel="noopener noreferrer">Blog (Korean)</a></li>
        <li><a href="{GITHUB}" target="_blank" rel="noopener noreferrer">GitHub</a></li>
        <li><a href="{LINKEDIN}" target="_blank" rel="noopener noreferrer">LinkedIn</a></li>
        <li><a href="mailto:{EMAIL}">Email</a></li>
      </ul></nav>
      <nav class="footer-col" aria-labelledby="f-apps"><span class="footer-label" id="f-apps">Apps</span><ul>
        <li><a href="/kinboard/privacy/#{code}">{c["privacy"]}</a></li>
      </ul></nav>
    </div>
  </div>
</footer>
<script>
  // 언어 메뉴에서 고른 언어를 기억해 루트 자동 이동을 멈춘다.
  document.querySelectorAll('[data-lang]').forEach(function (a) {{
    a.addEventListener('click', function () {{ try {{ localStorage.setItem('preferred-language', a.dataset.lang); }} catch (e) {{}} }});
  }});
</script>
</body>
</html>
"""


def main() -> None:
    for code, path, _, _ in LOCALES:
        out = ROOT / path.strip("/") / "index.html" if path != "/" else ROOT / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render(code), encoding="utf-8")
        print(f"wrote {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
