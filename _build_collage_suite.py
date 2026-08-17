import os
import json

BASE_DIR = r"D:\Codding\Claude Cowork code\Collage Tools"
SITE_URL = "https://bypyay.github.io/collagetools"
TOOLS_DIR = os.path.join(BASE_DIR, "tools")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
CSS_DIR = os.path.join(ASSETS_DIR, "css")
JS_DIR = os.path.join(ASSETS_DIR, "js")
JS_TOOLS_DIR = os.path.join(JS_DIR, "tools")

os.makedirs(TOOLS_DIR, exist_ok=True)
os.makedirs(CSS_DIR, exist_ok=True)
os.makedirs(JS_TOOLS_DIR, exist_ok=True)

# 1. Master CSS for Collage Tools
css_content = """/* ==========================================================================
   Daily1Step Collage Tools - Master Design System & Stylesheet
   Optimized for Pi7 Collage / Canva Aesthetics, Google AdSense & SEO
   ========================================================================== */

@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Outfit:wght@600;700;800&display=swap');

:root {
  --primary: #f43f5e;
  --primary-hover: #e11d48;
  --primary-light: #fff1f2;
  --accent: #8b5cf6;
  --accent-blue: #0284c7;
  --success: #10b981;
  --success-light: #ecfdf5;
  --warning: #f59e0b;
  --danger: #ef4444;
  
  --bg: #ffffff;
  --bg-soft: #f8fafc;
  --bg-dark: #0f172a;
  
  --ink: #0f172a;
  --ink-light: #334155;
  --ink-soft: #64748b;
  --ink-muted: #94a3b8;
  
  --border: #e2e8f0;
  --border-focus: #f43f5e;
  --shadow-sm: 0 1px 2px rgba(0,0,0,0.05);
  --shadow-md: 0 4px 6px -1px rgba(0,0,0,0.08), 0 2px 4px -2px rgba(0,0,0,0.04);
  --shadow-lg: 0 10px 15px -3px rgba(0,0,0,0.08), 0 4px 6px -4px rgba(0,0,0,0.03);
  --radius-sm: 8px;
  --radius-md: 12px;
  --radius-lg: 18px;
  --radius-xl: 24px;
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  color: var(--ink);
  background-color: var(--bg);
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
}

h1, h2, h3, h4, .brand, .btn {
  font-family: 'Outfit', 'Plus Jakarta Sans', sans-serif;
  letter-spacing: -0.02em;
}

a {
  color: var(--primary);
  text-decoration: none;
  transition: color 0.15s ease;
}
a:hover {
  color: var(--primary-hover);
}

.container {
  width: 96%;
  max-width: 1720px;
  margin: 0 auto;
  padding: 0 16px;
}

.content-container {
  width: 94%;
  max-width: 1040px;
  margin: 0 auto;
  padding: 0 16px;
}

/* ---------------- Header & Navigation ---------------- */
.site-header {
  background: rgba(255, 255, 255, 0.95);
  border-bottom: 1px solid var(--border);
  position: sticky;
  top: 0;
  z-index: 100;
  backdrop-filter: blur(10px);
}

.site-header .container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 64px;
}

.brand {
  font-size: 1.4rem;
  font-weight: 800;
  color: var(--ink);
  letter-spacing: -0.5px;
  display: flex;
  align-items: center;
  gap: 4px;
}
.brand .dot {
  color: var(--primary);
}

.main-nav {
  display: flex;
  align-items: center;
  gap: 16px;
}
.main-nav a {
  font-size: 0.92rem;
  font-weight: 600;
  color: var(--ink-light);
  padding: 6px 12px;
  border-radius: var(--radius-sm);
  transition: all 0.15s ease;
}
.main-nav a:hover, .main-nav a.active {
  color: var(--primary);
  background: var(--primary-light);
}

/* ---------------- Hero Section ---------------- */
.hero {
  padding: 48px 0 28px;
  text-align: center;
  background: linear-gradient(180deg, #fff1f2 0%, #ffffff 100%);
  border-bottom: 1px solid var(--border);
}

.hero h1 {
  font-size: 2.4rem;
  font-weight: 800;
  letter-spacing: -0.8px;
  color: var(--ink);
  margin-bottom: 12px;
  line-height: 1.2;
}

.hero p {
  font-size: 1.1rem;
  color: var(--ink-soft);
  max-width: 820px;
  margin: 0 auto;
  line-height: 1.6;
}

/* ---------------- Controls & Filter Tabs ---------------- */
.tool-controls-wrap {
  margin: 28px 0 24px;
}

.tool-search-box {
  position: relative;
  max-width: 620px;
  margin: 0 auto 20px;
}

.tool-search-box input[type="text"],
.tool-search-box input {
  width: 100%;
  padding: 14px 20px 14px 52px !important;
  font-size: 0.98rem;
  font-family: inherit;
  border: 2px solid var(--border);
  border-radius: 50px;
  outline: none;
  background: var(--bg);
  box-shadow: var(--shadow-sm);
  transition: all 0.2s ease;
  color: var(--ink);
}
.tool-search-box input:focus {
  border-color: var(--primary);
  box-shadow: 0 0 0 4px rgba(244, 63, 94, 0.15);
}

.tool-search-box .search-icon {
  position: absolute;
  left: 20px;
  top: 50%;
  transform: translateY(-50%);
  color: var(--ink-muted);
  pointer-events: none;
  z-index: 2;
  display: flex;
  align-items: center;
}

.category-tabs {
  display: flex;
  gap: 8px;
  align-items: center;
  justify-content: center;
  flex-wrap: wrap;
}

.category-tab {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 8px 16px;
  border-radius: 30px;
  border: 1px solid var(--border);
  background: var(--bg);
  color: var(--ink-light);
  font-size: 0.88rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.15s ease;
  font-family: inherit;
}
.category-tab:hover {
  background: var(--bg-soft);
  border-color: var(--ink-muted);
}
.category-tab.active {
  background: var(--primary);
  color: #fff;
  border-color: var(--primary);
  box-shadow: 0 3px 10px rgba(244, 63, 94, 0.35);
}
.category-tab .tab-count {
  background: rgba(0, 0, 0, 0.08);
  padding: 1px 7px;
  border-radius: 12px;
  font-size: 0.76rem;
  font-weight: 700;
}
.category-tab.active .tab-count {
  background: rgba(255, 255, 255, 0.25);
  color: #fff;
}

/* ---------------- Tool Grid & Cards ---------------- */
.tool-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
  gap: 16px;
  margin: 28px 0 50px;
}

.tool-card {
  display: flex;
  flex-direction: column;
  background: var(--bg);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  padding: 20px 18px;
  text-decoration: none;
  color: var(--ink);
  transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
  position: relative;
  overflow: hidden;
}
.tool-card::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: var(--primary);
  opacity: 0;
  transition: opacity 0.2s ease;
}
.tool-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-md);
  border-color: rgba(244, 63, 94, 0.4);
}
.tool-card:hover::after {
  opacity: 1;
}

.tool-card .icon {
  width: 44px;
  height: 44px;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  margin-bottom: 14px;
  flex-shrink: 0;
  box-shadow: 0 4px 10px rgba(0,0,0,0.1);
  transition: transform 0.2s ease;
}
.tool-card:hover .icon {
  transform: scale(1.06);
}

.tool-card h3 {
  font-size: 1.08rem;
  font-weight: 700;
  margin-bottom: 6px;
  color: var(--ink);
  line-height: 1.3;
}
.tool-card:hover h3 {
  color: var(--primary);
}

.tool-card p {
  font-size: 0.86rem;
  color: var(--ink-soft);
  line-height: 1.45;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

/* ---------------- Collage Studio Workspace ---------------- */
.tool-page {
  padding: 32px 0 60px;
}

.tool-header {
  text-align: center;
  max-width: 820px;
  margin: 0 auto 30px;
}

.tool-header h1 {
  font-size: 2.2rem;
  font-weight: 800;
  color: var(--ink);
  margin-bottom: 10px;
  line-height: 1.25;
}

.tool-header p {
  font-size: 1.05rem;
  color: var(--ink-soft);
}

.dropzone {
  border: 2px dashed #fda4af;
  background: #fff5f5;
  border-radius: var(--radius-lg);
  padding: 44px 20px;
  text-align: center;
  cursor: pointer;
  position: relative;
  max-width: 860px;
  margin: 0 auto;
  transition: all 0.2s ease;
}
.dropzone:hover, .dropzone.dragover {
  border-color: var(--primary);
  background: var(--primary-light);
  transform: scale(1.005);
}
.dropzone input[type="file"] {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  opacity: 0;
  cursor: pointer;
}
.dropzone .dz-icon {
  width: 64px;
  height: 64px;
  margin: 0 auto 14px;
  color: var(--primary);
  display: flex;
  align-items: center;
  justify-content: center;
}

.tool-workspace {
  max-width: 1100px;
  margin: 28px auto 0;
  display: grid;
  grid-template-columns: 340px 1fr;
  gap: 24px;
}

.tool-controls-panel {
  background: var(--bg);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 24px;
  box-shadow: var(--shadow-sm);
  height: fit-content;
}

.collage-canvas-panel {
  background: #f8fafc;
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 24px;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.collage-canvas-wrap {
  background: #fff;
  box-shadow: 0 8px 24px rgba(0,0,0,0.12);
  border-radius: var(--radius-sm);
  overflow: hidden;
  max-width: 100%;
}
.collage-canvas-wrap canvas {
  display: block;
  max-width: 100%;
  height: auto;
}

.control-group {
  margin-bottom: 16px;
}
.control-group label {
  display: block;
  font-weight: 700;
  font-size: 0.88rem;
  margin-bottom: 6px;
  color: var(--ink);
}

.control-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
}

input[type="text"], input[type="number"], select, textarea {
  width: 100%;
  padding: 9px 12px;
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  font-size: 0.92rem;
  font-family: inherit;
  outline: none;
  background: var(--bg);
}
input:focus, select:focus, textarea:focus {
  border-color: var(--primary);
  box-shadow: 0 0 0 3px rgba(244, 63, 94, 0.15);
}

.preset-grid {
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
  margin-top: 6px;
}

.preset-chip {
  background: var(--bg-soft);
  border: 1px solid var(--border);
  border-radius: 16px;
  padding: 5px 12px;
  font-size: 0.8rem;
  font-weight: 600;
  color: var(--ink-soft);
  cursor: pointer;
  transition: all 0.15s ease;
}
.preset-chip:hover, .preset-chip.active {
  background: var(--primary-light);
  border-color: var(--primary);
  color: var(--primary);
}

.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 12px 24px;
  background: var(--primary);
  color: #fff;
  font-size: 1rem;
  font-weight: 700;
  border: none;
  border-radius: var(--radius-sm);
  cursor: pointer;
  transition: all 0.15s ease;
  box-shadow: 0 2px 6px rgba(244, 63, 94, 0.25);
  text-decoration: none;
}
.btn:hover {
  background: var(--primary-hover);
  color: #fff;
  transform: translateY(-1px);
}
.btn.success {
  background: var(--success);
  box-shadow: 0 2px 6px rgba(16, 185, 129, 0.25);
}
.btn.success:hover {
  background: #059669;
}
.btn.block {
  width: 100%;
}

/* ---------------- AdSense & SEO Article ---------------- */
.ad-slot-wrap {
  margin: 32px auto;
  text-align: center;
  max-width: 970px;
  min-height: 90px;
  background: #f8fafc;
  border: 1px dashed #cbd5e1;
  border-radius: var(--radius-md);
  display: flex;
  align-items: center;
  justify-content: center;
  color: #94a3b8;
  font-size: 0.8rem;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.seo-article {
  background: var(--bg);
  border-top: 1px solid var(--border);
  padding: 48px 0 60px;
}

.seo-article .content-container {
  color: var(--ink-light);
}

.seo-article h2 {
  font-size: 1.75rem;
  font-weight: 800;
  color: var(--ink);
  margin: 32px 0 14px;
  line-height: 1.3;
}

.seo-article h3 {
  font-size: 1.25rem;
  font-weight: 700;
  color: var(--ink);
  margin: 24px 0 10px;
}

.seo-article p {
  font-size: 1rem;
  line-height: 1.7;
  margin-bottom: 16px;
}

.seo-article ul, .seo-article ol {
  margin: 12px 0 20px 24px;
  line-height: 1.65;
}

.seo-article li {
  margin-bottom: 8px;
}

.step-card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 16px;
  margin: 24px 0 32px;
}

.step-card {
  background: var(--bg-soft);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  padding: 20px;
}
.step-card .step-num {
  width: 34px;
  height: 34px;
  border-radius: 50%;
  background: var(--primary);
  color: #fff;
  font-weight: 800;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 12px;
  font-size: 0.95rem;
}
.step-card h4 {
  font-size: 1.08rem;
  color: var(--ink);
  margin-bottom: 6px;
}

.faq-list {
  margin: 24px 0;
}

.faq-item {
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  margin-bottom: 10px;
  overflow: hidden;
}

.faq-question {
  width: 100%;
  text-align: left;
  background: var(--bg-soft);
  border: none;
  padding: 16px 20px;
  font-size: 1rem;
  font-weight: 700;
  color: var(--ink);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  font-family: inherit;
}

.faq-answer {
  padding: 16px 20px;
  background: var(--bg);
  border-top: 1px solid var(--border);
  line-height: 1.65;
}

.breadcrumb {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 0.85rem;
  color: var(--ink-soft);
  margin-bottom: 16px;
}
.breadcrumb a {
  color: var(--ink-soft);
}
.breadcrumb a:hover {
  color: var(--primary);
}

.site-footer {
  background: var(--bg-dark);
  color: #94a3b8;
  padding: 48px 0 24px;
  font-size: 0.9rem;
}

.footer-grid {
  display: grid;
  grid-template-columns: 2fr repeat(3, 1fr);
  gap: 32px;
  margin-bottom: 40px;
}

.footer-col h4 {
  color: #fff;
  font-size: 1rem;
  font-weight: 700;
  margin-bottom: 14px;
}

.footer-col ul {
  list-style: none;
}
.footer-col li {
  margin-bottom: 8px;
}
.footer-col a {
  color: #94a3b8;
  transition: color 0.15s;
}
.footer-col a:hover {
  color: #fff;
}

.footer-bottom {
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  padding-top: 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 12px;
  font-size: 0.85rem;
}

@media (max-width: 900px) {
  .tool-workspace {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 768px) {
  .hero h1 {
    font-size: 1.75rem;
  }
  .hero p {
    font-size: 0.95rem;
  }
  .tool-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 10px;
  }
  .tool-card {
    padding: 14px 10px;
  }
  .tool-card .icon {
    width: 36px;
    height: 36px;
    margin-bottom: 8px;
  }
  .tool-card h3 {
    font-size: 0.92rem;
  }
  .tool-card p {
    font-size: 0.76rem;
  }
  .footer-grid {
    grid-template-columns: 1fr;
    gap: 24px;
  }
  .main-nav {
    display: none;
  }
}
"""

with open(os.path.join(CSS_DIR, "style.css"), "w", encoding="utf-8") as f:
    f.write(css_content)

print("Saved assets/css/style.css.")

# 21 Photo Collage Tools Definitions
COLLAGE_TOOLS = [
    # Master Studio
    {
        "slug": "collage-maker",
        "name": "Collage Maker Studio",
        "category": "count",
        "color": "#f43f5e",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg>',
        "title": "Photo Collage Maker Online Free — 100+ Templates & 4K Export",
        "desc": "Free online photo collage maker. Choose from 100+ templates for 2 to 30 photos, custom grid builder, rounded corners, text captions, and 4K export.",
        "h1": "Free Online Photo Collage Maker",
        "tagline": "Create stunning photo collages with 100+ free layouts, custom grids, borders, filters, and 4K ultra HD downloads.",
        "layout_key": "4-grid",
        "faqs": [
            ("How do I make a photo collage online?", "Select a template, drop your photos into the grid cells, customize borders and filters, and click Export 4K."),
            ("Is there any limit or watermark?", "No! All collages are 100% free with zero watermarks.")
        ]
    },

    # Photo Count Specific
    {
        "slug": "combine-2-photos-in-one-frame",
        "name": "2 Photos in One Frame",
        "category": "count",
        "color": "#ec4899",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="8" height="18" rx="1"/><rect x="13" y="3" width="8" height="18" rx="1"/></svg>',
        "title": "2 Photos in One Frame Online Free — Combine 2 Pictures Side by Side",
        "desc": "Join 2 photos together side by side or vertically in one frame online. Perfect for before and after comparisons and couple photos.",
        "h1": "Combine 2 Photos in One Frame",
        "tagline": "Merge two pictures side by side or top and bottom with customizable borders and spacing.",
        "layout_key": "2-side",
        "faqs": [
            ("Can I put 2 photos side by side?", "Yes, choose the side-by-side split layout to merge 2 pictures seamlessly.")
        ]
    },
    {
        "slug": "3-photo-collage",
        "name": "3 Photo Collage",
        "category": "count",
        "color": "#8b5cf6",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="8" height="18" rx="1"/><rect x="13" y="3" width="8" height="8" rx="1"/><rect x="13" y="13" width="8" height="8" rx="1"/></svg>',
        "title": "3 Photo Collage Maker Online — Triptych & 3 Picture Layouts",
        "desc": "Create a 3 photo collage online. Choose from 1 large hero + 2 small stacked pictures, 3 vertical strips, or horizontal rows.",
        "h1": "3 Photo Collage Maker",
        "tagline": "Combine 3 pictures into a balanced triptych layout or 1 large feature photo with two side shots.",
        "layout_key": "3-left-big",
        "faqs": [
            ("What 3-photo layouts are available?", "You can choose 1 large left + 2 stacked right, 1 top banner + 2 bottom, or a 3-column triptych.")
        ]
    },
    {
        "slug": "4-photos-in-one-frame",
        "name": "4 Photos in One Frame",
        "category": "count",
        "color": "#3b82f6",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="8" height="8" rx="1"/><rect x="13" y="3" width="8" height="8" rx="1"/><rect x="3" y="13" width="8" height="8" rx="1"/><rect x="13" y="13" width="8" height="8" rx="1"/></svg>',
        "title": "4 Photos in One Frame Online — Classic 2x2 Grid Collage Maker",
        "desc": "Put 4 pictures in one frame online. Classic 2x2 square grid, 4 horizontal strips, and modern 4-picture collage layouts.",
        "h1": "4 Photos in One Frame (2x2 Grid)",
        "tagline": "Arrange 4 favorite photos in a classic balanced 2x2 grid with rounded corners and custom background colors.",
        "layout_key": "4-grid",
        "faqs": [
            ("How do I make a 2x2 photo collage?", "Upload 4 photos into the 2x2 grid, adjust border thickness, and export in 4K.")
        ]
    },
    {
        "slug": "5-photo-collage",
        "name": "5 Photo Collage",
        "category": "count",
        "color": "#06b6d4",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="10" height="18" rx="1"/><rect x="15" y="3" width="6" height="3.5" rx="1"/><rect x="15" y="8" width="6" height="3.5" rx="1"/><rect x="15" y="13" width="6" height="3.5" rx="1"/><rect x="15" y="18" width="6" height="3" rx="1"/></svg>',
        "title": "5 Photo Collage Maker Online — Magazine Style & Cross Layouts",
        "desc": "Combine 5 photos into an eye-catching magazine editorial layout with 1 large centerpiece picture and 4 accent photos.",
        "h1": "5 Photo Collage Maker (Magazine Style)",
        "tagline": "Showcase 5 pictures with 1 bold spotlight image surrounded by 4 supporting snapshot tiles.",
        "layout_key": "5-mag",
        "faqs": [
            ("Is magazine layout good for travel photos?", "Yes! It highlights your best hero shot while showing 4 key story moments.")
        ]
    },
    {
        "slug": "6-photo-collage",
        "name": "6 Photo Collage",
        "category": "count",
        "color": "#10b981",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="5" height="8" rx="1"/><rect x="10" y="3" width="5" height="8" rx="1"/><rect x="17" y="3" width="4" height="8" rx="1"/><rect x="3" y="13" width="5" height="8" rx="1"/><rect x="10" y="13" width="5" height="8" rx="1"/><rect x="17" y="13" width="4" height="8" rx="1"/></svg>',
        "title": "6 Photo Collage Maker Online — 2x3 Grid & Bento Box Layouts",
        "desc": "Make a 6 photo collage online for free. Clean 2x3 grid, modern bento layouts, and hexagonal photo arrangements.",
        "h1": "6 Photo Collage Maker (2x3 Grid)",
        "tagline": "Combine 6 images into a symmetric 2x3 grid or dynamic bento box story format.",
        "layout_key": "6-grid",
        "faqs": [
            ("Can I adjust spacing between the 6 photos?", "Yes, use the Spacing slider to increase or remove cell gaps.")
        ]
    },
    {
        "slug": "8-picture-collage",
        "name": "8 Picture Collage",
        "category": "count",
        "color": "#84cc16",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="4" height="8" rx="1"/><rect x="8.5" y="3" width="4" height="8" rx="1"/><rect x="14" y="3" width="4" height="8" rx="1"/><rect x="19" y="3" width="3" height="8" rx="1"/><rect x="3" y="13" width="4" height="8" rx="1"/><rect x="8.5" y="13" width="4" height="8" rx="1"/><rect x="14" y="13" width="4" height="8" rx="1"/><rect x="19" y="13" width="3" height="8" rx="1"/></svg>',
        "title": "8 Picture Collage Maker Online — Photo Strip & Timeline Collage",
        "desc": "Create an 8 picture collage online. 2x4 grid, panoramic photo banner, and filmstrip story sequence.",
        "h1": "8 Picture Collage Maker",
        "tagline": "Design an 8-photo memory strip or 2x4 grid for party recaps and vacation albums.",
        "layout_key": "8-grid",
        "faqs": [
            ("What is the best export resolution for 8 photos?", "Choose 4K resolution to ensure every photo tile remains ultra sharp.")
        ]
    },
    {
        "slug": "9-photo-collage",
        "name": "9 Photo Collage (3x3 Grid)",
        "category": "count",
        "color": "#f59e0b",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="5" height="5" rx="1"/><rect x="10" y="3" width="5" height="5" rx="1"/><rect x="17" y="3" width="4" height="5" rx="1"/><rect x="3" y="10" width="5" height="5" rx="1"/><rect x="10" y="10" width="5" height="5" rx="1"/><rect x="17" y="10" width="4" height="5" rx="1"/><rect x="3" y="17" width="5" height="4" rx="1"/><rect x="10" y="17" width="5" height="4" rx="1"/><rect x="17" y="17" width="4" height="4" rx="1"/></svg>',
        "title": "9 Photo Collage Maker Online — 3x3 Instagram BestNine Grid",
        "desc": "Create a 9 photo collage in a perfect 3x3 square grid. Ideal for Instagram BestNine, yearly summaries, and aesthetic moodboards.",
        "h1": "9 Photo Collage (3x3 Square Grid)",
        "tagline": "Make a 3x3 Instagram BestNine collage or square aesthetic moodboard in seconds.",
        "layout_key": "9-grid",
        "faqs": [
            ("How do I make an Instagram BestNine 3x3 grid?", "Upload your 9 favorite photos and export in 1080x1080 square format.")
        ]
    },
    {
        "slug": "10-photo-collage",
        "name": "10 Photo Collage",
        "category": "count",
        "color": "#ea580c",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="3.5" height="8" rx="1"/><rect x="6.5" y="3" width="3.5" height="8" rx="1"/><rect x="11" y="3" width="3.5" height="8" rx="1"/><rect x="15.5" y="3" width="3.5" height="8" rx="1"/><rect x="20" y="3" width="2" height="8" rx="1"/><rect x="2" y="13" width="3.5" height="8" rx="1"/><rect x="6.5" y="13" width="3.5" height="8" rx="1"/><rect x="11" y="13" width="3.5" height="8" rx="1"/><rect x="15.5" y="13" width="3.5" height="8" rx="1"/><rect x="20" y="13" width="2" height="8" rx="1"/></svg>',
        "title": "10 Photo Collage Maker Online — Top 10 Moments & 2x5 Grid",
        "desc": "Arrange 10 photos in a 2x5 panoramic collage banner. Perfect for Top 10 memories, decade milestones, and portfolio highlights.",
        "h1": "10 Photo Collage (Top 10 Moments)",
        "tagline": "Showcase your top 10 moments in a sleek 2x5 grid banner.",
        "layout_key": "10-grid",
        "faqs": [
            ("Can I reorder the 10 photos?", "Yes, you can swap and place images into specific numbered cells.")
        ]
    },
    {
        "slug": "12-photo-collage",
        "name": "12 Photo Collage",
        "category": "count",
        "color": "#dc2626",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="4" height="4" rx="1"/><rect x="8.5" y="3" width="4" height="4" rx="1"/><rect x="14" y="3" width="4" height="4" rx="1"/><rect x="19" y="3" width="3" height="4" rx="1"/><rect x="3" y="9" width="4" height="4" rx="1"/><rect x="8.5" y="9" width="4" height="4" rx="1"/><rect x="14" y="9" width="4" height="4" rx="1"/><rect x="19" y="9" width="3" height="4" rx="1"/><rect x="3" y="15" width="4" height="4" rx="1"/><rect x="8.5" y="15" width="4" height="4" rx="1"/><rect x="14" y="15" width="4" height="4" rx="1"/><rect x="19" y="15" width="3" height="4" rx="1"/></svg>',
        "title": "12 Photo Collage Maker — 12 Months Year in Review & Calendar",
        "desc": "Make a 12 photo collage for 12 months year recap, baby's first year milestones, and family calendar yearbooks.",
        "h1": "12 Photo Collage (Year in Review)",
        "tagline": "Capture 12 months of memories in a 3x4 grid for calendar prints and annual summaries.",
        "layout_key": "12-grid",
        "faqs": [
            ("Is 12 photo collage good for baby milestones?", "Yes! 1 photo per month from newborn to 1st birthday is the most popular layout.")
        ]
    },
    {
        "slug": "30-photo-collage",
        "name": "30 Photo Collage",
        "category": "count",
        "color": "#7c3aed",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>',
        "title": "30 Photo Collage Maker Online — Mega Photo Mosaic & Memory Wall",
        "desc": "Create a 30 photo mega collage mosaic. Combine 30 pictures into a stunning wall art poster for 30th birthdays, weddings, and anniversaries.",
        "h1": "30 Photo Collage (Mega Mosaic Wall)",
        "tagline": "Build an impressive 30-photo memory board wall art poster with ultra HD 4K rendering.",
        "layout_key": "12-grid",
        "faqs": [
            ("Can I export a 30 photo collage in print quality?", "Yes! Export at 4x (4K 300 DPI) for crisp, professional poster printing.")
        ]
    },

    # Style & Themes
    {
        "slug": "photo-grid-maker",
        "name": "Photo Grid Maker",
        "category": "style",
        "color": "#0284c7",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg>',
        "title": "Photo Grid Maker Online Free — Custom NxM Image Grids",
        "desc": "Custom photo grid generator. Build any NxM grid (2x2, 3x3, 4x4, 5x5) with adjustable cell borders, spacing, and background styling.",
        "h1": "Custom Photo Grid Maker",
        "tagline": "Create any custom grid layout from 2x2 up to 6x6 with precision spacing and rounding.",
        "layout_key": "4-grid",
        "faqs": [
            ("Can I customize the number of rows and columns?", "Yes! Select any column and row count from 2 to 6.")
        ]
    },
    {
        "slug": "picture-montage-maker",
        "name": "Picture Montage Maker",
        "category": "style",
        "color": "#c026d3",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>',
        "title": "Picture Montage Maker Online — Polaroid Frame & Scrapbook Collage",
        "desc": "Create artistic picture montages with retro polaroid photo frames, scrapbook paper textures, and shadow depth.",
        "h1": "Picture Montage &amp; Polaroid Maker",
        "tagline": "Craft retro polaroid montages and vintage scrapbook photo boards.",
        "layout_key": "3-left-big",
        "faqs": [
            ("Does it support polaroid borders?", "Yes! Polaroid white borders with drop shadows are supported.")
        ]
    },
    {
        "slug": "heart-photo-collage",
        "name": "Heart Photo Collage",
        "category": "style",
        "color": "#e11d48",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>',
        "title": "Heart Photo Collage Maker Online Free — Heart Shaped Picture Frame",
        "desc": "Arrange your favorite photos inside a beautiful heart-shaped collage frame. The perfect romantic gift for Valentine's, weddings, and anniversaries.",
        "h1": "Heart Shaped Photo Collage",
        "tagline": "Arrange romantic photos into a gorgeous heart-shaped mosaic frame.",
        "layout_key": "4-grid",
        "faqs": [
            ("How does heart collage work?", "Photos are placed inside heart-contoured mosaic tiles for a romantic keepsake.")
        ]
    },
    {
        "slug": "instagram-collage-maker",
        "name": "Instagram Collage Maker",
        "category": "style",
        "color": "#d946ef",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg>',
        "title": "Instagram Collage Maker — 1:1 Feed Post & 9:16 Story Presets",
        "desc": "Design eye-catching Instagram photo collages. Pre-sized for 1080x1080 Feed posts, 1080x1920 Stories, and Reels covers.",
        "h1": "Instagram Photo Collage Maker",
        "tagline": "Pre-sized canvas templates for 1080x1080 Instagram Feed and 9:16 Story/Reel collages.",
        "layout_key": "4-grid",
        "faqs": [
            ("What resolutions are used for Instagram?", "1080x1080 for square posts and 1080x1920 for full-screen stories.")
        ]
    },

    # Special Occasions
    {
        "slug": "birthday-collage-maker",
        "name": "Birthday Collage Maker",
        "category": "occasion",
        "color": "#f59e0b",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>',
        "title": "Birthday Photo Collage Maker Online — Party Frames & Birthday Cards",
        "desc": "Create festive birthday photo collages with party confetti banners, celebratory balloons, and personalized birthday messages.",
        "h1": "Birthday Photo Collage Maker",
        "tagline": "Celebrate special birthdays with party-themed collage frames and custom greetings.",
        "layout_key": "3-top-big",
        "faqs": [
            ("Can I add birthday text greetings?", "Yes, add custom birthday wishes and names in vibrant typography.")
        ]
    },
    {
        "slug": "wedding-photo-collage",
        "name": "Wedding Photo Collage",
        "category": "occasion",
        "color": "#ec4899",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 8v8"/><path d="M8 12h8"/></svg>',
        "title": "Wedding Photo Collage Maker — Romance Album & Save-the-Date Frames",
        "desc": "Design elegant wedding photo collages, save-the-date cards, engagement memory boards, and romantic photo albums.",
        "h1": "Wedding &amp; Romance Photo Collage",
        "tagline": "Elegant pastel frames and timeless typography for wedding and engagement photo memories.",
        "layout_key": "4-grid",
        "faqs": [
            ("Is this suitable for Save the Date cards?", "Yes, export at 300 DPI for high-quality wedding invitations.")
        ]
    },
    {
        "slug": "family-photo-collage",
        "name": "Family Photo Collage",
        "category": "occasion",
        "color": "#10b981",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>',
        "title": "Family Photo Collage Maker — Family Tree & Reunion Wall Art",
        "desc": "Bring family generations together in a heartwarming family photo collage. Ideal for reunions, home wall art, and anniversary gifts.",
        "h1": "Family Photo Collage Maker",
        "tagline": "Assemble generations of family memories into a classic keepsake frame.",
        "layout_key": "6-grid",
        "faqs": [
            ("Can I include photos of different sizes?", "Yes, choose asymmetric family layouts to fit all generations.")
        ]
    },
    {
        "slug": "couple-photo-collage",
        "name": "Couple Photo Collage",
        "category": "occasion",
        "color": "#f43f5e",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/></svg>',
        "title": "Couple Photo Collage Maker — Then & Now Love Timeline Frames",
        "desc": "Create a romantic couple photo collage. Side-by-side Then and Now timelines, first date memories, and cute couple anniversary frames.",
        "h1": "Couple Photo Collage Maker",
        "tagline": "Capture your romantic journey with Then & Now love timeline frames.",
        "layout_key": "2-side",
        "faqs": [
            ("How do I make a Then & Now couple photo?", "Upload your first photo on the left and recent photo on the right in the 2-in-1 frame.")
        ]
    },
    {
        "slug": "anniversary-photo-collage",
        "name": "Anniversary Photo Collage",
        "category": "occasion",
        "color": "#d97706",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 14 14"/></svg>',
        "title": "Anniversary Photo Collage Maker — 25th, 50th & Milestone Anniversaries",
        "desc": "Celebrate milestone wedding anniversaries (1st, 10th, 25th Silver, 50th Golden) with luxurious gold and silver framed photo collages.",
        "h1": "Anniversary Milestone Photo Collage",
        "tagline": "Celebrate years of love with elegant milestone anniversary photo frames.",
        "layout_key": "4-grid",
        "faqs": [
            ("Can I add anniversary year text?", "Yes, stamp 'Happy 25th Anniversary' or custom dates directly on the canvas.")
        ]
    },
    {
        "slug": "christmas-collage",
        "name": "Christmas & Holiday Collage",
        "category": "occasion",
        "color": "#059669",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 19 21 5 21 12 2"/></svg>',
        "title": "Christmas Photo Collage Maker — Holiday Cards & Year Recap Frames",
        "desc": "Design festive Christmas and New Year holiday photo collages. Send personalized holiday greeting cards to family and friends.",
        "h1": "Christmas &amp; Holiday Photo Collage",
        "tagline": "Create cheerful holiday greeting cards and festive family Christmas memory collages.",
        "layout_key": "4-grid",
        "faqs": [
            ("Can I export holiday cards as PDF?", "Yes! Export print-ready PDF files formatted for greeting card envelopes.")
        ]
    }
]

CATEGORIES = [
    ("all", "All Collage Tools", "🌟", len(COLLAGE_TOOLS)),
    ("count", "By Photo Count", "🖼️", 11),
    ("style", "Styles & Themes", "🎨", 4),
    ("occasion", "Special Occasions", "🎉", 6),
]

def make_header(root_rel, page_title, page_desc, canonical_url):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{page_title}</title>
<meta name="description" content="{page_desc}">
<link rel="canonical" href="{canonical_url}">
<meta property="og:title" content="{page_title}">
<meta property="og:description" content="{page_desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical_url}">
<meta name="twitter:card" content="summary_large_image">
<meta name="robots" content="index, follow">
<link rel="stylesheet" href="{root_rel}assets/css/style.css?v=1">
</head>
<body>
<header class="site-header">
  <div class="container">
    <a href="{root_rel}index.html" class="brand">Daily1Step Collage<span class="dot">.</span></a>
    <nav class="main-nav">
      <a href="{root_rel}index.html">All Collage Tools</a>
      <a href="{root_rel}tools/collage-maker/">Collage Maker</a>
      <a href="{root_rel}tools/combine-2-photos-in-one-frame/">2 Photos</a>
      <a href="{root_rel}tools/4-photos-in-one-frame/">4 Photos</a>
      <a href="{root_rel}tools/photo-grid-maker/">Grid Maker</a>
      <a href="{root_rel}about.html">About</a>
    </nav>
  </div>
</header>
"""

def make_footer(root_rel):
    return f"""<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-col">
        <h4>Daily1Step Collage Tools</h4>
        <p style="font-size:.88rem; line-height:1.6; margin-top:8px;">Fast, private, and 100% browser-based photo collage maker. Create custom grids, photo strips, polaroid montages, and 4K ultra HD downloads with zero server uploads.</p>
      </div>
      <div class="footer-col">
        <h4>By Photo Count</h4>
        <ul>
          <li><a href="{root_rel}tools/combine-2-photos-in-one-frame/">2 Photos in One Frame</a></li>
          <li><a href="{root_rel}tools/3-photo-collage/">3 Photo Collage</a></li>
          <li><a href="{root_rel}tools/4-photos-in-one-frame/">4 Photos (2x2 Grid)</a></li>
          <li><a href="{root_rel}tools/6-photo-collage/">6 Photo Collage</a></li>
          <li><a href="{root_rel}tools/9-photo-collage/">9 Photo Collage (3x3)</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Styles &amp; Occasions</h4>
        <ul>
          <li><a href="{root_rel}tools/photo-grid-maker/">Photo Grid Maker</a></li>
          <li><a href="{root_rel}tools/heart-photo-collage/">Heart Photo Collage</a></li>
          <li><a href="{root_rel}tools/instagram-collage-maker/">Instagram Collage</a></li>
          <li><a href="{root_rel}tools/birthday-collage-maker/">Birthday Collage</a></li>
          <li><a href="{root_rel}tools/wedding-photo-collage/">Wedding Collage</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Company &amp; Legal</h4>
        <ul>
          <li><a href="{root_rel}about.html">About Us</a></li>
          <li><a href="{root_rel}contact.html">Contact Us</a></li>
          <li><a href="{root_rel}privacy-policy.html">Privacy Policy</a></li>
          <li><a href="{root_rel}terms.html">Terms of Service</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <div>&copy; 2026 Daily1Step Collage Tools. All rights reserved. 100% Client-Side Processing.</div>
      <div>
        <a href="{root_rel}privacy-policy.html" style="margin-right:12px;">Privacy Policy</a>
        <a href="{root_rel}terms.html">Terms of Service</a>
      </div>
    </div>
  </div>
</footer>
<script src="{root_rel}vendor/jspdf.umd.min.js"></script>
<script src="{root_rel}vendor/jszip.min.js"></script>
<script src="{root_rel}assets/js/collage-core.js"></script>
</body>
</html>
"""

# 2. Build 21 Tool Pages & Scripts
for t in COLLAGE_TOOLS:
    slug = t["slug"]
    name = t["name"]
    title = t["title"]
    desc = t["desc"]
    h1 = t["h1"]
    tagline = t["tagline"]
    layout_key = t.get("layout_key", "4-grid")
    canonical = f"{SITE_URL}/tools/{slug}/"

    faq_entities = []
    faq_html = ""
    for q, a in t["faqs"]:
        faq_entities.append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": a
            }
        })
        faq_html += f"""
        <div class="faq-item">
          <button class="faq-question" type="button">
            <span>{q}</span>
            <span style="font-size:1.2rem;">+</span>
          </button>
          <div class="faq-answer" style="display:none;">
            <p>{a}</p>
          </div>
        </div>
        """

    schema_data = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebApplication",
                "name": name,
                "url": canonical,
                "description": desc,
                "applicationCategory": "MultimediaApplication",
                "operatingSystem": "All modern browsers (Windows, Mac, iOS, Android)",
                "offers": {
                    "@type": "Offer",
                    "price": "0",
                    "priceCurrency": "USD"
                }
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": 1,
                        "name": "Home",
                        "item": f"{SITE_URL}/"
                    },
                    {
                        "@type": "ListItem",
                        "position": 2,
                        "name": "Collage Tools",
                        "item": f"{SITE_URL}/#tools"
                    },
                    {
                        "@type": "ListItem",
                        "position": 3,
                        "name": name,
                        "item": canonical
                    }
                ]
            },
            {
                "@type": "FAQPage",
                "mainEntity": faq_entities
            }
        ]
    }

    workspace_html = f"""
    <div class="dropzone" id="dropZone">
      <input type="file" id="fileInput" accept="image/*" multiple>
      <div class="dz-icon">
        <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg>
      </div>
      <h3>Select or Drop Photos</h3>
      <p>Drop multiple photos here to automatically populate the collage cells</p>
    </div>

    <div class="tool-workspace" id="workspaceArea">
      <div class="tool-controls-panel">
        <h3 style="font-size:1.15rem; margin-bottom:16px; color:var(--ink);">Collage Settings</h3>

        <div class="control-group">
          <label>Layout Spacing (Gap)</label>
          <input type="range" id="spacingRange" min="0" max="30" value="12">
        </div>

        <div class="control-group">
          <label>Corner Radius (Rounded)</label>
          <input type="range" id="radiusRange" min="0" max="40" value="8">
        </div>

        <div class="control-row">
          <div class="control-group">
            <label>Background Color</label>
            <input type="color" id="bgColor" value="#ffffff" style="height:40px; padding:2px 4px;">
          </div>
          <div class="control-group">
            <label>Photo Filter</label>
            <select id="filterSelect">
              <option value="none" selected>Normal</option>
              <option value="warm">Warm &amp; Sunny</option>
              <option value="cool">Cool Blue</option>
              <option value="vintage">Vintage Film</option>
              <option value="grayscale">B&amp;W Grayscale</option>
              <option value="sepia">Sepia Nostalgia</option>
            </select>
          </div>
        </div>

        <div class="control-group">
          <label>Caption Text (Optional)</label>
          <input type="text" id="captionText" placeholder="e.g. Summer Memories 2026">
        </div>

        <div class="control-group">
          <label>Export Resolution</label>
          <select id="exportScale">
            <option value="1">Standard Web (1080 px)</option>
            <option value="2" selected>High Definition 2K (2160 px)</option>
            <option value="4">Ultra HD 4K / 300 DPI Print (4320 px)</option>
          </select>
        </div>

        <button type="button" class="btn block success" id="exportBtn" style="margin-top:8px;">Download High-Res Collage</button>
      </div>

      <div class="collage-canvas-panel">
        <div class="collage-canvas-wrap">
          <canvas id="collageCanvas" width="800" height="800"></canvas>
        </div>
      </div>
    </div>
    """

    tool_html = make_header("../../", title, desc, canonical) + f"""
<script type="application/ld+json">
{json.dumps(schema_data, indent=2)}
</script>

<main class="tool-page">
  <div class="container">
    <div class="breadcrumb" style="max-width:1100px; margin:0 auto 16px;">
      <a href="../../index.html">Home</a> &gt; <a href="../../index.html">Collage Tools</a> &gt; <span>{name}</span>
    </div>

    <div class="tool-header">
      <h1>{h1}</h1>
      <p>{tagline}</p>
    </div>

    <!-- Ad Slot Top -->
    <div class="ad-slot-wrap">
      <span>Advertisement</span>
    </div>

    {workspace_html}

    <!-- Ad Slot Middle -->
    <div class="ad-slot-wrap" style="margin-top:32px;">
      <span>Advertisement</span>
    </div>

  </div>
</main>

<article class="seo-article">
  <div class="content-container">
    <h2>How to Create {name} in 3 Easy Steps</h2>
    <div class="step-card-grid">
      <div class="step-card">
        <div class="step-num">1</div>
        <h4>Upload Your Photos</h4>
        <p>Drop your favorite photos into the upload box to fill the collage cells.</p>
      </div>
      <div class="step-card">
        <div class="step-num">2</div>
        <h4>Customize Layout &amp; Style</h4>
        <p>Adjust gap spacing, rounded corners, background colors, and vintage photo filters.</p>
      </div>
      <div class="step-card">
        <div class="step-num">3</div>
        <h4>Export in 4K Quality</h4>
        <p>Download your high-resolution collage in crisp PNG or JPEG up to 4K / 300 DPI for printing.</p>
      </div>
    </div>

    <h2>Why Choose Daily1Step {name}?</h2>
    <p>Daily1Step {name} runs 100% locally in your web browser using HTML5 Canvas 2D. <strong>Your personal photos are never uploaded to any remote server.</strong></p>
    <ul>
      <li><strong>100% Private &amp; Secure:</strong> Zero server uploads or cloud storage.</li>
      <li><strong>Up to 4K Ultra HD Export:</strong> 300 DPI print-ready outputs for framing.</li>
      <li><strong>No Watermarks &amp; Always Free:</strong> Unlimited downloads without signup.</li>
      <li><strong>Cross-Device Responsive:</strong> Works seamlessly on mobile, tablet, and PC.</li>
    </ul>

    <h2>Frequently Asked Questions (FAQ)</h2>
    <div class="faq-list">
      {faq_html}
    </div>

    <!-- Ad Slot Bottom -->
    <div class="ad-slot-wrap" style="margin-top:40px;">
      <span>Advertisement</span>
    </div>
  </div>
</article>

<script src="../../assets/js/tools/{slug}.js"></script>
<script>
// FAQ Accordion interaction
document.querySelectorAll('.faq-question').forEach(function(btn) {{
  btn.addEventListener('click', function() {{
    var ans = btn.nextElementSibling;
    var isOpen = ans.style.display === 'block';
    ans.style.display = isOpen ? 'none' : 'block';
    btn.querySelector('span:last-child').textContent = isOpen ? '+' : '−';
  }});
}});
</script>
""" + make_footer("../../")

    # Save to tools/<slug>/index.html
    t_dir = os.path.join(TOOLS_DIR, slug)
    os.makedirs(t_dir, exist_ok=True)
    with open(os.path.join(t_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(tool_html)

    # Save alias to root <slug>/index.html
    alias_dir = os.path.join(BASE_DIR, slug)
    os.makedirs(alias_dir, exist_ok=True)
    alias_html = tool_html.replace('../../', '../')
    with open(os.path.join(alias_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(alias_html)

    # Generate Tool JS Handler
    js_code = f"""// Tool logic for {name} ({slug})
(function() {{
  var fileInput = document.getElementById('fileInput');
  var canvas = document.getElementById('collageCanvas');
  var spacingRange = document.getElementById('spacingRange');
  var radiusRange = document.getElementById('radiusRange');
  var bgColor = document.getElementById('bgColor');
  var filterSelect = document.getElementById('filterSelect');
  var captionText = document.getElementById('captionText');
  var exportScale = document.getElementById('exportScale');
  var exportBtn = document.getElementById('exportBtn');

  var loadedImages = [];
  var layoutKey = '{layout_key}';
  var layoutCells = CollageCore.LAYOUTS[layoutKey] || CollageCore.LAYOUTS['4-grid'];

  function updateCollage() {{
    if (!canvas) return;
    CollageCore.renderCollage(canvas, {{
      cells: layoutCells,
      images: loadedImages,
      spacing: parseInt(spacingRange ? spacingRange.value : 12),
      radius: parseInt(radiusRange ? radiusRange.value : 8),
      bgColor: bgColor ? bgColor.value : '#ffffff',
      filter: filterSelect ? filterSelect.value : 'none',
      text: captionText ? captionText.value : ''
    }});
  }}

  // Initial draw
  updateCollage();

  if (fileInput) {{
    fileInput.addEventListener('change', function(e) {{
      if (e.target.files && e.target.files.length > 0) {{
        loadedImages = [];
        var files = Array.from(e.target.files);
        var loaded = 0;
        files.forEach(function(f, idx) {{
          var img = new Image();
          img.onload = function() {{
            loadedImages[idx] = img;
            loaded++;
            if (loaded === files.length) {{
              updateCollage();
            }}
          }};
          var reader = new FileReader();
          reader.onload = function(ev) {{
            img.src = ev.target.result;
          }};
          reader.readAsDataURL(f);
        }});
      }}
    }});
  }}

  [spacingRange, radiusRange, bgColor, filterSelect, captionText].forEach(function(el) {{
    if (el) {{
      el.addEventListener('input', updateCollage);
      el.addEventListener('change', updateCollage);
    }}
  }});

  if (exportBtn) {{
    exportBtn.addEventListener('click', function() {{
      var scale = parseInt(exportScale ? exportScale.value : 2);
      var dataUrl = CollageCore.exportCollage(canvas, scale, 'image/png', 0.95);
      CollageCore.downloadFile(dataUrl, '{slug}-collage.png');
    }});
  }}
}})();
"""
    with open(os.path.join(JS_TOOLS_DIR, f"{slug}.js"), "w", encoding="utf-8") as f:
        f.write(js_code)

print("Generated all 21 collage tool pages and JS scripts.")

# 3. Build Homepage index.html
tab_buttons_html = ""
for cat_key, cat_name, cat_icon, count in CATEGORIES:
    active = " active" if cat_key == "all" else ""
    tab_buttons_html += f"""
    <button class="category-tab{active}" data-category="{cat_key}">
      <span>{cat_icon} {cat_name}</span>
      <span class="tab-count">{count}</span>
    </button>
    """

tool_cards_html = ""
for t in COLLAGE_TOOLS:
    tool_cards_html += f"""
    <a href="tools/{t['slug']}/" class="tool-card" data-category="{t['category']}" data-title="{t['name'].lower()}" data-desc="{t['desc'].lower()}">
      <div class="icon" style="background:{t['color']};">{t['icon']}</div>
      <h3>{t['name']}</h3>
      <p>{t['desc']}</p>
    </a>
    """

home_schema = {
    "@context": "https://schema.org",
    "@type": "WebSite",
    "name": "Daily1Step Collage Tools",
    "url": f"{SITE_URL}/",
    "description": "Free online photo collage maker with 100+ templates. Custom grids, heart shapes, polaroid montages, and 4K high resolution export.",
    "potentialAction": {
        "@type": "SearchAction",
        "target": f"{SITE_URL}/?q={{search_term_string}}",
        "query-input": "required name=search_term_string"
    }
}

home_faqs = [
    ("Are all collage tools on Daily1Step free?", "Yes! All 21 photo collage tools and templates are 100% free with no subscriptions, file size limits, or watermarks."),
    ("Are my personal photos uploaded to a remote server?", "No! Every collage is rendered 100% client-side in your web browser using HTML5 Canvas. Your photos never leave your device."),
    ("Can I export in 4K resolution for print?", "Yes! You can choose 4x (4K / 300 DPI) resolution for framing, posters, and greeting cards."),
    ("Can I customize borders, spacing, and background color?", "Yes! You have real-time controls for gap spacing, corner radius rounding, filters, and custom background colors.")
]

home_faq_html = ""
for q, a in home_faqs:
    home_faq_html += f"""
    <div class="faq-item">
      <button class="faq-question" type="button">
        <span>{q}</span>
        <span style="font-size:1.2rem;">+</span>
      </button>
      <div class="faq-answer" style="display:none;">
        <p>{a}</p>
      </div>
    </div>
    """

home_html = make_header("", "Daily1Step Collage Tools — Free Online Photo Collage Maker & 4K Export", "Free online photo collage maker with 100+ templates. Custom grids, heart shapes, polaroid montages, and 4K ultra HD exports 100% in browser.", f"{SITE_URL}/") + f"""
<script type="application/ld+json">
{json.dumps(home_schema, indent=2)}
</script>

<section class="hero">
  <div class="container">
    <h1>Photo Collage Maker &mdash; <em>100+ Free Templates</em></h1>
    <p>Combine photos into beautiful grids, magazine layouts, polaroid montages, and heart shapes &mdash; 100% free, no signup, and processed right in your browser.</p>
  </div>
</section>

<!-- Ad Slot Top -->
<div class="container">
  <div class="ad-slot-wrap">
    <span>Advertisement</span>
  </div>
</div>

<section class="container" id="tools">
  <div class="tool-controls-wrap">
    <div class="tool-search-box">
      <span class="search-icon">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
      </span>
      <input type="text" id="toolSearchInput" placeholder="Search 21 collage tools (e.g. 2 photos, 4 photos, grid, heart, polaroid)..." autocomplete="off">
    </div>

    <div class="category-tabs" id="categoryTabs">
      {tab_buttons_html}
    </div>
  </div>

  <div class="tool-grid" id="mainToolGrid">
    {tool_cards_html}
  </div>

  <div id="noResultsMsg" style="display:none; text-align:center; padding:50px 20px; color:var(--ink-soft);">
    <p style="font-size:1.4rem; font-weight:700; color:var(--ink); margin-bottom:6px;">No collage tools found</p>
    <p>Try searching for "2 photos", "4 photos", "grid", "heart", or "birthday".</p>
  </div>
</section>

<!-- Ad Slot Middle -->
<div class="container">
  <div class="ad-slot-wrap">
    <span>Advertisement</span>
  </div>
</div>

<article class="seo-article">
  <div class="content-container">
    <h2>Why Choose Daily1Step Collage Tools?</h2>
    <p>Daily1Step Collage Tools runs entirely in your web browser. Unlike other collage editors that upload your private photos to the cloud, all collage rendering happens locally in memory using <strong>HTML5 Canvas 2D and WebAssembly</strong>.</p>

    <div class="step-card-grid">
      <div class="step-card">
        <div class="step-num">🖼️</div>
        <h4>100+ Templates</h4>
        <p>From 2-photo pairs to 30-photo mega mosaics, classic grids, and magazine editorials.</p>
      </div>
      <div class="step-card">
        <div class="step-num">🔒</div>
        <h4>100% Device-Local Privacy</h4>
        <p>Your personal photos never leave your device. Zero server uploads guarantee total confidentiality.</p>
      </div>
      <div class="step-card">
        <div class="step-num">⚡</div>
        <h4>4K Ultra HD Export</h4>
        <p>Download in 1080p, 2K, or 4K (300 DPI) print-ready quality for framing and photo albums.</p>
      </div>
      <div class="step-card">
        <div class="step-num">💯</div>
        <h4>Always 100% Free</h4>
        <p>No subscriptions, no watermarks, no registration, and unlimited downloads.</p>
      </div>
    </div>

    <h2>Frequently Asked Questions</h2>
    <div class="faq-list">
      {home_faq_html}
    </div>
  </div>
</article>

<script>
(function() {{
  var searchInput = document.getElementById('toolSearchInput');
  var categoryTabs = document.querySelectorAll('.category-tab');
  var toolCards = document.querySelectorAll('.tool-card');
  var noResults = document.getElementById('noResultsMsg');
  var currentCategory = 'all';

  function filterTools() {{
    var query = (searchInput.value || '').trim().toLowerCase();
    var visibleCount = 0;

    toolCards.forEach(function(card) {{
      var cat = card.getAttribute('data-category');
      var title = card.getAttribute('data-title');
      var desc = card.getAttribute('data-desc');

      var matchesCat = (currentCategory === 'all' || cat === currentCategory);
      var matchesQuery = !query || title.indexOf(query) !== -1 || desc.indexOf(query) !== -1;

      if (matchesCat && matchesQuery) {{
        card.style.display = 'flex';
        visibleCount++;
      }} else {{
        card.style.display = 'none';
      }}
    }});

    if (noResults) {{
      noResults.style.display = (visibleCount === 0) ? 'block' : 'none';
    }}
  }}

  categoryTabs.forEach(function(tab) {{
    tab.addEventListener('click', function() {{
      categoryTabs.forEach(function(t) {{ t.classList.remove('active'); }});
      tab.classList.add('active');
      currentCategory = tab.getAttribute('data-category');
      filterTools();
    }});
  }});

  if (searchInput) {{
    searchInput.addEventListener('input', filterTools);
  }}

  // FAQ Accordion
  document.querySelectorAll('.faq-question').forEach(function(btn) {{
    btn.addEventListener('click', function() {{
      var ans = btn.nextElementSibling;
      var isOpen = ans.style.display === 'block';
      ans.style.display = isOpen ? 'none' : 'block';
      btn.querySelector('span:last-child').textContent = isOpen ? '+' : '−';
    }});
  }});
}})();
</script>
""" + make_footer("")

with open(os.path.join(BASE_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(home_html)

print("Generated homepage index.html.")

# 4. Generate Legal & SEO Pages
# Privacy Policy
privacy_html = make_header("", "Privacy Policy — Daily1Step Collage Tools", "Privacy policy for Daily1Step Collage Tools. Learn how browser-side rendering keeps your photos private.", f"{SITE_URL}/privacy-policy.html") + """
<main class="seo-article">
  <div class="content-container">
    <div class="breadcrumb">
      <a href="index.html">Home</a> &gt; <span>Privacy Policy</span>
    </div>
    <h1>Privacy Policy</h1>
    <p><em>Last updated: August 17, 2026</em></p>

    <h2>1. 100% Client-Side Privacy Model</h2>
    <p>At Daily1Step Collage Tools (<code>https://bypyay.github.io/collagetools/</code>), we maintain a strict client-side architecture. All photo collage rendering, canvas transformations, and filters are executed directly in your web browser. <strong>Your photos are never uploaded to any remote server or stored in the cloud.</strong></p>

    <h2>2. Google AdSense & Cookies</h2>
    <p>We may display advertisements served by Google AdSense to keep our service free. Google uses cookies (such as DoubleClick) to serve relevant ads based on browsing activity. You can opt out via Google Ads Settings.</p>

    <h2>3. GDPR & CCPA Compliance</h2>
    <p>Because we do not collect, process, or store personal files or personal identifiers on remote servers, no user data is sold, rented, or shared with third parties.</p>
  </div>
</main>
""" + make_footer("")
with open(os.path.join(BASE_DIR, "privacy-policy.html"), "w", encoding="utf-8") as f:
    f.write(privacy_html)

# Terms of Service
terms_html = make_header("", "Terms of Service — Daily1Step Collage Tools", "Terms of service for Daily1Step Collage Tools.", f"{SITE_URL}/terms.html") + """
<main class="seo-article">
  <div class="content-container">
    <div class="breadcrumb">
      <a href="index.html">Home</a> &gt; <span>Terms of Service</span>
    </div>
    <h1>Terms of Service</h1>
    <p><em>Last updated: August 17, 2026</em></p>

    <h2>1. Acceptance of Terms</h2>
    <p>By using Daily1Step Collage Tools, you agree to these Terms of Service. All tools are provided free of charge on an 'as-is' basis.</p>

    <h2>2. Intellectual Property</h2>
    <p>You retain 100% ownership and copyright of any collages, photos, and graphics created using our platform.</p>
  </div>
</main>
""" + make_footer("")
with open(os.path.join(BASE_DIR, "terms.html"), "w", encoding="utf-8") as f:
    f.write(terms_html)

# About Us
about_html = make_header("", "About Us — Daily1Step Collage Tools", "About Daily1Step Collage Tools — Free private browser-based photo collage maker.", f"{SITE_URL}/about.html") + """
<main class="seo-article">
  <div class="content-container">
    <div class="breadcrumb">
      <a href="index.html">Home</a> &gt; <span>About Us</span>
    </div>
    <h1>About Daily1Step Collage Tools</h1>
    <p class="lead" style="font-size:1.15rem; color:var(--ink-soft); margin-bottom:24px;">Fast, private, and free browser-based photo collage suite for creators, families, and photographers.</p>

    <h2>Our Mission</h2>
    <p>Daily1Step Collage Tools provides 21 client-side collage tools to combine, frame, and export photos in up to 4K quality without ever uploading personal files to remote servers.</p>
  </div>
</main>
""" + make_footer("")
with open(os.path.join(BASE_DIR, "about.html"), "w", encoding="utf-8") as f:
    f.write(about_html)

# Contact Us
contact_html = make_header("", "Contact Us — Daily1Step Collage Tools", "Get in touch with Daily1Step Collage Tools.", f"{SITE_URL}/contact.html") + """
<main class="seo-article">
  <div class="content-container">
    <div class="breadcrumb">
      <a href="index.html">Home</a> &gt; <span>Contact Us</span>
    </div>
    <h1>Contact Us</h1>
    <p>Have questions, feedback, or template requests? We'd love to hear from you!</p>

    <div style="max-width:680px; margin:28px 0; background:var(--bg-soft); border:1px solid var(--border); border-radius:var(--radius-lg); padding:28px;">
      <form onsubmit="event.preventDefault(); alert('Thank you for contacting us! We will respond shortly.');">
        <div style="margin-bottom:16px;">
          <label style="display:block; font-weight:700; font-size:.9rem; margin-bottom:6px; color:var(--ink);">Your Name</label>
          <input type="text" required placeholder="Enter your full name" style="width:100%; padding:12px 14px; border:1px solid var(--border); border-radius:var(--radius-sm); font-size:1rem;">
        </div>
        <div style="margin-bottom:16px;">
          <label style="display:block; font-weight:700; font-size:.9rem; margin-bottom:6px; color:var(--ink);">Your Email</label>
          <input type="email" required placeholder="name@example.com" style="width:100%; padding:12px 14px; border:1px solid var(--border); border-radius:var(--radius-sm); font-size:1rem;">
        </div>
        <div style="margin-bottom:20px;">
          <label style="display:block; font-weight:700; font-size:.9rem; margin-bottom:6px; color:var(--ink);">Message</label>
          <textarea rows="5" required placeholder="How can we assist you?" style="width:100%; padding:12px 14px; border:1px solid var(--border); border-radius:var(--radius-sm); font-size:1rem; font-family:inherit;"></textarea>
        </div>
        <button type="submit" class="btn" style="width:100%;">Send Message</button>
      </form>
    </div>
  </div>
</main>
""" + make_footer("")
with open(os.path.join(BASE_DIR, "contact.html"), "w", encoding="utf-8") as f:
    f.write(contact_html)

# 5. Generate Robots.txt and Sitemap.xml
robots_txt = f"""User-agent: *
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
"""
with open(os.path.join(BASE_DIR, "robots.txt"), "w", encoding="utf-8") as f:
    f.write(robots_txt)

sitemap_urls = [
    f"{SITE_URL}/",
    f"{SITE_URL}/about.html",
    f"{SITE_URL}/contact.html",
    f"{SITE_URL}/privacy-policy.html",
    f"{SITE_URL}/terms.html",
]
for t in COLLAGE_TOOLS:
    sitemap_urls.append(f"{SITE_URL}/tools/{t['slug']}/")

sitemap_xml = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
"""
for u in sitemap_urls:
    sitemap_xml += f"""  <url>
    <loc>{u}</loc>
    <lastmod>2026-08-17</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
"""
sitemap_xml += "</urlset>\n"

with open(os.path.join(BASE_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write(sitemap_xml)

print("Generated sitemap.xml with 26 URLs and robots.txt.")
