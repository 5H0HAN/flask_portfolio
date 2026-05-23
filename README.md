<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Flask-3.1.3-black?style=for-the-badge&logo=flask" alt="Flask">
  <img src="https://img.shields.io/badge/license-MIT-green?style=for-the-badge" alt="License">
</p>

<h1 align="center">📂 Flask Portfolio</h1>

<p align="center">
  <strong>A modern, dark-mode portfolio website built with Flask</strong>
  <br>
  Showcasing projects, skills, services, blog articles, and a contact form
</p>

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🌗 **Dark/Light Mode** | Persistent theme toggle saved to `localStorage` |
| 📱 **Fully Responsive** | Mobile-first design adapts to all screen sizes |
| 🎞️ **GSAP Animations** | Scroll-triggered reveals for sections and cards |
| 🏷️ **Project Filtering** | Category-based tabs (AI, Backend, Tools) |
| 📰 **Blog Filtering** | Category tabs (AI & ML, Programming, Infrastructure, Tutorials) |
| ✉️ **Contact Form** | POST endpoint with success feedback |
| 💼 **Freelance Services** | Service listings with pricing & Fiverr integration |
| 🖼️ **Image Placeholders** | Ready for real assets with styled fallbacks |

---

## 🗺️ Pages

| Page | Route | Description |
|------|-------|-------------|
| 🏠 **Home** | `/` | Hero section, about preview, featured projects, services teaser, skills snapshot, testimonials, blog preview, CTA |
| 👤 **About** | `/about` | Biography, education timeline, technical interests, expertise areas, tools grid, resume download CTA |
| 💻 **Projects** | `/projects` | Filterable project grid (AI / Backend / Tools) with overlay links |
| 🛠️ **Skills** | `/skills` | Language proficiency bars, framework cards, tool grid, infrastructure expertise, skill legend |
| 🛒 **Services** | `/services` | Service detail cards with pricing, Fiverr gigs, client testimonials |
| 📝 **Blog** | `/blog` | Featured post, filterable article grid, newsletter signup |
| 📬 **Contact** | `/contact` | Contact info, social links, message form, FAQ section |

---

## 🧰 Tech Stack

| Layer | Technology | Badge |
|-------|-----------|-------|
| **Backend** | [Flask](https://flask.palletsprojects.com/) (Python) | <img src="https://img.shields.io/badge/Flask-000000?logo=flask&logoColor=white"> |
| **Templating** | Jinja2 | <img src="https://img.shields.io/badge/Jinja2-B41717?logo=jinja&logoColor=white"> |
| **Frontend** | HTML5, CSS3, JavaScript (ES6) | <img src="https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white"> <img src="https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white"> <img src="https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black"> |
| **Animations** | [GSAP](https://gsap.com/) + ScrollTrigger | <img src="https://img.shields.io/badge/GSAP-88CE02?logo=greensock&logoColor=white"> |
| **Icons** | [Font Awesome 6](https://fontawesome.com/) | <img src="https://img.shields.io/badge/Font_Awesome-528DD7?logo=fontawesome&logoColor=white"> |
| **Fonts** | Inter + JetBrains Mono | <img src="https://img.shields.io/badge/Google_Fonts-4285F4?logo=googlefonts&logoColor=white"> |

---

## 📁 Project Structure

```
flask_portfolio/
├── portfolio/
│   ├── app.py                  # Flask routes & application
│   ├── requirements.txt        # Python dependencies
│   ├── static/
│   │   └── css/
│   │       └── style.css       # Global styles (1080 lines)
│   └── templates/
│       ├── base.html           # Base layout (nav, footer, GSAP CDN)
│       ├── index.html          # Home page
│       ├── about.html          # About page
│       ├── projects.html       # Projects page
│       ├── skills.html         # Skills page
│       ├── services.html       # Services page
│       ├── blog.html           # Blog page
│       └── contact.html        # Contact page
├── requirements.txt            # Root deps for Render deployment
├── README.md
├── .gitignore
├── .env                        # Local environment variables (gitignored)
└── .env.example                # Environment variable template
```

---

## 🚀 Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/5H0HAN/flask_portfolio.git
cd flask_portfolio

# 2. Install dependencies
pip install -r portfolio/requirements.txt

# 3. Run the development server
cd portfolio && python app.py

# 4. Open in your browser
open http://127.0.0.1:5000
```

---

## 🌐 Deployment (Render)

| Setting | Value |
|---------|-------|
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn portfolio.app:app` |
| **Runtime** | Python 3 (auto-detected) |

---

## 🤝 Contact

| Platform | Link |
|----------|------|
| 🖐️ **Fiverr** | [fiverr.com/theshohan](https://www.fiverr.com/theshohan) |
| 🐙 **GitHub** | [github.com/5H0HAN](https://github.com/5H0HAN) |
| 📍 **Location** | Dhaka, Bangladesh |
| 🕐 **Timezone** | GMT+6 |

---

<p align="center">Built with ❤️ using Flask</p>
