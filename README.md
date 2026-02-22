# JRE Podcast Scraper & Static Site Generator

[![Scheduled Scraper](https://github.com/wojtek108/JRE_claudflare/actions/workflows/action.yml/badge.svg)](https://github.com/wojtek108/JRE_claudflare/actions/workflows/action.yml)
[![GitHub Pages Deployment](https://github.com/wojtek108/JRE_claudflare/actions/workflows/github-pages.yml/badge.svg)](https://github.com/wojtek108/JRE_claudflare/actions/workflows/github-pages.yml)

A Python-based web scraper that automatically fetches the latest Joe Rogan Experience podcast episodes and generates a static website. The site is deployed to both GitHub Pages and Cloudflare Pages for redundancy and performance.

## 🎯 Project Overview

This project automatically scrapes the official JRE podcast website (jrepodcast.com) to extract:
- Recent episode titles
- Episode descriptions/excerpts  
- Publication dates
- Generates a clean, static HTML page with the latest episodes
- Deploys automatically to multiple platforms

## 🏗️ Architecture & Logic

### Core Components

1. **Web Scraper (`app.py`)**
   - Uses `BeautifulSoup` and `requests` to parse jrepodcast.com
   - Extracts episode data using CSS selectors
   - Generates `scrape.html` with raw scraped content
   - Updates `index.html` only when new content is detected

2. **Static Site Generator**
   - Creates clean, styled HTML output
   - Includes timestamp of last check
   - Minimal CSS for readability
   - Responsive design

3. **Automation Workflows**
   - GitHub Actions for scheduled scraping
   - Automatic deployment pipelines
   - Change detection to avoid unnecessary updates

### How It Works

```
Scraping Process:
1. Fetch HTML from jrepodcast.com
2. Parse with BeautifulSoup using specific CSS classes:
   - `.card__title` for episode titles
   - `.card__excerpt` for descriptions  
   - `.entry-date.published` for dates
3. Generate HTML file with styled output
4. Compare with existing index.html
5. Update only if content changed

Deployment Process:
1. Scraper runs (scheduled or manual)
2. If changes detected → commit to repository
3. Push triggers deployment workflows
4. Static site deployed to GitHub Pages & Cloudflare Pages
```

## 🚀 Deployment Platforms

### Cloudflare Pages (Primary)
- **URL**: [jrescrape.pages.dev](https://jrescrape.pages.dev)
- **Build Command**: (Not required - static files)
- **Build Output Directory**: `/` (root)
- **Environment Variables**: None required
- **Benefits**: Global CDN, DDoS protection, free SSL, fast edge network

### GitHub Pages (Secondary/Backup)
- **URL**: `https://wojtek108.github.io/JRE_claudflare/`
- **Automated via**: GitHub Actions workflow
- **Benefits**: Integrated with GitHub, automatic on push

## ⚙️ GitHub Actions Workflows

### 1. **Scheduled JRE Scraper** (`action.yml`)
**Purpose**: Automatically scrape latest episodes and update the site

**Triggers**:
- **Scheduled**: Every 2 days at 6:00 AM UTC (`cron: '0 6 */2 * *'`)
- **Manual**: Can be triggered manually from GitHub Actions UI

**What it does**:
1. Checks out repository
2. Sets up Python 3.9 environment
3. Installs dependencies (`requests`, `beautifulsoup4`, `lxml`)
4. Runs `app.py` to scrape latest episodes
5. Checks if new content was found
6. If changes detected → commits and pushes to repository
7. Push triggers deployment workflows

**Manual Trigger Instructions**:
1. Go to GitHub repository → **Actions** tab
2. Select **"Scheduled JRE Scraper"** workflow
3. Click **"Run workflow"** button
4. Select branch (usually `main`) and run

### 2. **GitHub Pages Deployment** (`github-pages.yml`)
**Purpose**: Deploy static site to GitHub Pages

**Triggers**:
- **Automatic**: On push to `main` branch
- **Manual**: Can be triggered manually from GitHub Actions UI

**What it does**:
1. Checks out repository (with scraped content)
2. Creates `.nojekyll` file (disables Jekyll processing)
3. Prepares `_site/` directory with deployment files
4. Uploads artifact for GitHub Pages
5. Deploys to `https://wojtek108.github.io/JRE_claudflare/`

**Manual Trigger Instructions**:
1. Go to GitHub repository → **Actions** tab  
2. Select **"Deploy to GitHub Pages"** workflow
3. Click **"Run workflow"** button
4. Select branch (usually `main`) and run

## 🛠️ Local Development

### Prerequisites
- Python 3.9+
- Git

### Setup
```bash
# Clone repository
git clone https://github.com/wojtek108/JRE_claudflare.git
cd JRE_claudflare

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run scraper manually
python app.py

# View generated site
open index.html  # Or open in browser
```

### Project Structure
```
JRE_claudflare/
├── app.py                    # Main scraper script
├── index.html               # Generated static site
├── scrape.html              # Raw scraped output
├── requirements.txt         # Python dependencies
├── .github/workflows/       # GitHub Actions workflows
│   ├── action.yml          # Scheduled scraper
│   └── github-pages.yml    # GitHub Pages deployment
├── wrangler.jsonc          # Cloudflare Workers configuration
└── netlify.toml            # Legacy Netlify config (not used)
```

## 🔧 Technical Details

### Dependencies
```txt
beautifulsoup4==4.11.1  # HTML parsing
requests==2.28.1        # HTTP requests
lxml==5.3.0            # XML/HTML processing
```

### CSS Selectors Used
```python
# Episode titles
titles = soup.find_all('h3', attrs={'class': 'card__title'})

# Episode descriptions  
intro = soup.find_all('div', attrs={'class': 'card__excerpt'})

# Publication dates
dates = soup.find_all('time', attrs={'class': 'entry-date published'})
```

### Change Detection Logic
The script compares newly scraped content with existing `index.html`:
- Only updates if content differs
- Prevents unnecessary commits and deployments
- Includes "Last checked" timestamp

## 📊 Monitoring & Maintenance

### Status Badges
- **Scheduled Scraper**: Shows last run status
- **GitHub Pages**: Shows deployment status

### Manual Operations
1. **Force re-scrape**: Manually trigger `action.yml` workflow
2. **Force re-deploy**: Manually trigger `github-pages.yml` workflow  
3. **Local testing**: Run `python app.py` and check `index.html`

### Troubleshooting
- **Scraping fails**: Check if jrepodcast.com structure changed
- **Deployment fails**: Check GitHub Actions logs
- **Site not updating**: Clear browser cache, check workflow runs

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make changes and test locally
4. Submit a pull request

## 📄 License

MIT License - see LICENSE file for details

## 🙏 Acknowledgments

- Data sourced from [jrepodcast.com](https://www.jrepodcast.com/)
- Built with Python, BeautifulSoup, and GitHub Actions
- Deployed on Cloudflare Pages and GitHub Pages

---

**Last Updated**: February 2025  
**Maintainer**: wojtek108  
**Live Sites**: 
- [Cloudflare Pages](https://jrescrape.pages.dev)
- [GitHub Pages](https://wojtek108.github.io/JRE_claudflare/)