# Agent Guidelines for JRE Podcast Scraper

## Project Overview
This is a Python web scraper that fetches Joe Rogan Experience podcast episodes from jrepodcast.com and generates a static HTML site. The site is deployed to Cloudflare Pages and GitHub Pages.

## Build & Development Commands

### Environment Setup
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Upgrade pip and install
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Running the Scraper
```bash
# Run the main scraper script
python app.py

# Check generated files
ls -la *.html
```

### Testing
**Note**: No formal test suite exists. Testing is done manually:
1. Run `python app.py`
2. Check `index.html` and `scrape.html` are generated
3. Verify HTML structure and content
4. Open `index.html` in browser to confirm rendering

### Linting & Formatting
No linters are configured. Follow the existing code style.

### Deployment Commands
```bash
# GitHub Actions will handle deployment automatically
# Manual deployment triggers available in GitHub UI:
# 1. "Scheduled JRE Scraper" workflow (scrapes and commits)
# 2. "Deploy to GitHub Pages" workflow (deploys to GitHub Pages)

# Cloudflare Pages deployment is automatic via Git integration
```

## Code Style Guidelines

### Python Style
- **Indentation**: 4 spaces (no tabs)
- **Line length**: No strict limit, but keep reasonable
- **Imports**: Group standard library first, then third-party
- **Naming**: snake_case for variables/functions, PascalCase not used

### Import Order (as seen in app.py)
1. Standard library imports
2. Third-party imports
3. Local imports (none currently)

Example:
```python
from datetime import date
import requests
from bs4 import BeautifulSoup
```

### Variable Naming
- Use descriptive names: `url`, `res`, `soup`, `titles`, `dates`, `intro`
- Avoid abbreviations unless clear: `res` for response is acceptable
- HTML file handles: `file`, `scrape`, `index`

### Error Handling
- Minimal error handling in current code
- Consider adding try-except for network requests
- File operations use `with` statements where possible
- Check file existence before operations

### HTML Generation Style
- Inline CSS in `<style>` tags
- Basic responsive design with viewport meta tag
- Semantic HTML where possible
- Direct string concatenation for HTML generation
- Include "Last checked" timestamp

### File Operations
- Use `with open()` context managers for writing
- Manual `open()`/`close()` for append operations
- Compare file contents before overwriting
- Generate `scrape.html` first, then copy to `index.html` if changed

## Project Structure Conventions

### File Organization
```
app.py              # Main scraper script
index.html          # Generated static site (deployed)
scrape.html         # Raw scraped output (intermediate)
requirements.txt    # Python dependencies
.github/workflows/  # GitHub Actions
  action.yml       # Scheduled scraper
  github-pages.yml # GitHub Pages deployment
```

### Workflow Patterns
1. **Scraping**: Fetch → Parse → Generate HTML
2. **Change Detection**: Compare new vs existing content
3. **Deployment**: Commit changes → Trigger workflows → Deploy to platforms

### Dependencies Management
- Pin versions in `requirements.txt`
- Include both `beautifulsoup4` and `bs4` (bs4 is wrapper)
- Use `lxml` parser for performance
- `requests` for HTTP calls

## Agent-Specific Instructions

### When Modifying Code
1. **Preserve existing patterns**: Follow the simple, direct style
2. **No over-engineering**: Keep code minimal and functional
3. **Test manually**: Run `python app.py` and check output
4. **Verify deployments**: Changes should trigger automatic deployments

### Adding Features
1. **Backward compatibility**: Don't break existing scraping
2. **Incremental changes**: Small, testable modifications
3. **Document changes**: Update README.md if functionality changes

### Error Recovery
1. **Network failures**: Consider retry logic for requests
2. **HTML structure changes**: Monitor CSS selector compatibility
3. **Deployment failures**: Check GitHub Actions logs

## Deployment Architecture

### Primary: Cloudflare Pages
- Static files served directly
- No build process required
- Automatic from Git repository
- URL: https://jrescrape.pages.dev

### Secondary: GitHub Pages
- Generated via GitHub Actions
- Creates `_site/` directory during workflow
- Serves from `username.github.io/JRE_claudflare/`

### Workflow Triggers
- **Push to main**: Triggers GitHub Pages deployment
- **Scheduled (every 2 days)**: Runs scraper, commits if changes
- **Manual**: Both workflows can be triggered from GitHub UI

## Common Tasks for Agents

### 1. Update Scraping Logic
- Modify CSS selectors in `app.py` if website structure changes
- Test with `python app.py` and verify HTML output
- Commit changes to trigger deployment

### 2. Add Error Handling
- Wrap `requests.get()` in try-except
- Add timeout for network requests
- Validate HTML parsing results

### 3. Improve HTML Output
- Enhance CSS styling in `<style>` section
- Add meta tags for SEO
- Improve responsive design

### 4. Monitor and Maintain
- Check GitHub Actions for failures
- Verify Cloudflare Pages deployment
- Update dependencies as needed

## Notes for Future Development
- Consider adding configuration file for URLs/selectors
- Add logging for debugging
- Create simple test script
- Consider caching to reduce requests
- Add health check endpoint

## Quick Reference
```bash
# Run everything
python app.py && open index.html

# Check dependencies
pip list | grep -E "(beautifulsoup|requests|lxml)"

# View workflow status
# Check https://github.com/wojtek108/JRE_claudflare/actions
```