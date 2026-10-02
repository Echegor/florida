def get_head():
    return """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
  <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
  <meta http-equiv="Pragma" content="no-cache">
  <meta http-equiv="Expires" content="0">
  <title>Florida Grand Expedition: Keys, Glades & Theme Park Thrills | Master Field Guide</title>
  <meta name="description" content="Comprehensive 8-day / 7-night road trip guide across Florida connecting Miami, the Overseas Highway (US-1), Key West, Everglades National Park, and Orlando's premier theme parks (Universal & Disney). Complete with open-jaw flight analysis, zero-alcohol dining, and unified couple budget.">
  <meta name="theme-color" content="#b47b2c">
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><circle cx='50' cy='50' r='46' fill='%230f172a' stroke='%23b47b2c' stroke-width='6'/><polygon points='50,18 58,45 85,50 58,55 50,82 42,55 15,50 42,45' fill='%23b47b2c'/></svg>">
  <meta property="og:title" content="Florida Grand Expedition: Keys, Glades & Theme Park Thrills">
  <meta property="og:description" content="8-day / 7-night road trip guide connecting Miami, the Overseas Highway, Everglades, Universal Studios, and Disney World.">
  <meta property="og:image" content="images/slide02_hero.jpg">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Florida Grand Expedition: Keys, Glades & Theme Park Thrills">
  <meta name="twitter:description" content="Comprehensive 8-day expedition across Florida connecting the Overseas Highway, Everglades, Universal Studios, and Disney World.">
  <meta name="twitter:image" content="images/slide02_hero.jpg">
  
  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&family=Playfair+Display:ital,wght@0,600;0,700;1,600&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">

  <style>
    /* ==========================================================================
       LUXURY EDITORIAL MULTI-THEME DESIGN SYSTEM
       ========================================================================== */
    :root, [data-theme="linen"] {
      --bg-dark: #f8f9fa;
      --bg-surface: #ffffff;
      --bg-card: #ffffff;
      --bg-card-hover: #fcfcfd;
      --border-subtle: rgba(15, 23, 42, 0.08);
      --border-gold: rgba(180, 123, 44, 0.35);
      
      --text-title: #0f172a;
      --sand-light: #1e293b;
      --sand-muted: #64748b;
      --sand-dark: #334155;
      
      --gold-primary: #b47b2c;
      --gold-glow: #8c5d18;
      --terracotta: #c2410c;
      --terracotta-soft: rgba(194, 65, 12, 0.08);
      --teal-ocean: #0f766e;
      --teal-soft: rgba(15, 118, 110, 0.08);
      
      --card-shadow: 0 10px 30px rgba(15, 23, 42, 0.05), 0 1px 3px rgba(15, 23, 42, 0.03);
      --stat-bg: #f1f5f9;
      --stat-border: rgba(15, 23, 42, 0.06);
      --pill-bg: #f8fafc;
      --pill-border: rgba(15, 23, 42, 0.08);
      --field-alert-bg: rgba(194, 65, 12, 0.08);
      --field-alert-text: #7c2d12;
      --header-bg: rgba(248, 249, 250, 0.94);
      --footer-bg: rgba(248, 249, 250, 0.94);
      --header-border: transparent;
      --nav-btn-bg: rgba(15, 23, 42, 0.06);
      --nav-btn-color: #0f172a;
      --dot-bg: rgba(15, 23, 42, 0.16);

      --font-serif: 'Playfair Display', Georgia, serif;
      --font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-mono: 'JetBrains Mono', monospace;

      --transition-standard: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }

    [data-theme="coastal"] {
      --bg-dark: #0a1422;
      --bg-surface: #0f1f33;
      --bg-card: rgba(18, 35, 56, 0.92);
      --bg-card-hover: rgba(24, 46, 74, 0.95);
      --border-subtle: rgba(255, 255, 255, 0.1);
      --border-gold: rgba(234, 179, 8, 0.45);
      
      --text-title: #ffffff;
      --sand-light: #f8fafc;
      --sand-muted: #94a3b8;
      --sand-dark: #cbd5e1;
      
      --gold-primary: #eab308;
      --gold-glow: #facc15;
      --terracotta: #fb923c;
      --terracotta-soft: rgba(251, 146, 60, 0.15);
      --teal-ocean: #2dd4bf;
      --teal-soft: rgba(45, 212, 191, 0.15);
      
      --card-shadow: 0 20px 50px rgba(0, 0, 0, 0.55);
      --stat-bg: rgba(0, 0, 0, 0.35);
      --stat-border: rgba(255, 255, 255, 0.1);
      --pill-bg: rgba(0, 0, 0, 0.4);
      --pill-border: rgba(255, 255, 255, 0.08);
      --field-alert-bg: rgba(251, 146, 60, 0.16);
      --field-alert-text: #ffe0d6;
      --header-bg: rgba(10, 20, 34, 0.94);
      --footer-bg: rgba(10, 20, 34, 0.94);
      --header-border: transparent;
      --nav-btn-bg: rgba(255, 255, 255, 0.08);
      --nav-btn-color: #ffffff;
      --dot-bg: rgba(255, 255, 255, 0.2);
    }

    [data-theme="obsidian"] {
      --bg-dark: #07090c;
      --bg-surface: #0e1218;
      --bg-card: rgba(18, 24, 32, 0.9);
      --bg-card-hover: rgba(24, 32, 42, 0.95);
      --border-subtle: rgba(255, 255, 255, 0.1);
      --border-gold: rgba(212, 175, 55, 0.45);
      
      --text-title: #ffffff;
      --sand-light: #ffffff;
      --sand-muted: #c8d1dc;
      --sand-dark: #9aa7b6;
      
      --gold-primary: #d4af37;
      --gold-glow: #f0cf6b;
      --terracotta: #e0683e;
      --terracotta-soft: rgba(224, 104, 62, 0.2);
      --teal-ocean: #2ec4b6;
      --teal-soft: rgba(46, 196, 182, 0.2);
      
      --card-shadow: 0 20px 50px rgba(0, 0, 0, 0.7);
      --stat-bg: rgba(0, 0, 0, 0.45);
      --stat-border: rgba(255, 255, 255, 0.1);
      --pill-bg: rgba(0, 0, 0, 0.4);
      --pill-border: rgba(255, 255, 255, 0.08);
      --field-alert-bg: rgba(224, 104, 62, 0.16);
      --field-alert-text: #ffe0d6;
      --header-bg: rgba(7, 9, 12, 0.94);
      --footer-bg: rgba(7, 9, 12, 0.94);
      --header-border: transparent;
      --nav-btn-bg: rgba(255, 255, 255, 0.08);
      --nav-btn-color: #ffffff;
      --dot-bg: rgba(255, 255, 255, 0.2);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-font-smoothing: antialiased;
    }

    body {
      background-color: var(--bg-dark);
      color: var(--sand-light);
      font-family: var(--font-sans);
      overflow: hidden;
      width: 100vw;
      height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      user-select: none;
      transition: background-color 0.4s ease, color 0.4s ease;
    }

    .viewport-ambient {
      position: absolute;
      inset: 0;
      pointer-events: none;
      background: 
        radial-gradient(circle at 10% 15%, rgba(194, 65, 12, 0.06), transparent 45%),
        radial-gradient(circle at 90% 85%, rgba(15, 118, 110, 0.06), transparent 50%),
        radial-gradient(circle at 50% 50%, var(--bg-surface), var(--bg-dark) 95%);
      z-index: 1;
      transition: background 0.4s ease;
    }

    .deck-container {
      width: 100vw;
      height: 100vh;
      max-width: 177.78vh;
      max-height: 56.25vw;
      aspect-ratio: 16 / 9;
      position: relative;
      background: var(--bg-surface);
      box-shadow: 0 30px 100px rgba(0, 0, 0, 0.15);
      border: 1px solid var(--border-subtle);
      border-radius: 8px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      z-index: 2;
      transition: background 0.4s ease, border-color 0.4s ease;
    }

    .deck-header {
      height: 64px;
      padding: 0 2.5rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid var(--border-subtle);
      background: var(--header-bg);
      backdrop-filter: blur(12px);
      z-index: 20;
      transition: var(--transition-standard);
    }

    .header-brand {
      display: flex;
      align-items: center;
      gap: 14px;
    }

    .brand-symbol {
      width: 22px;
      height: 22px;
      background: var(--gold-primary);
      clip-path: polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%);
      box-shadow: 0 0 14px var(--gold-glow);
    }

    .brand-title {
      font-family: var(--font-mono);
      font-size: 0.82rem;
      letter-spacing: 0.22em;
      text-transform: uppercase;
      color: var(--text-title);
      font-weight: 700;
    }

    .header-controls {
      display: flex;
      align-items: center;
      gap: 1rem;
    }

    .slide-counter {
      font-family: var(--font-mono);
      font-size: 0.85rem;
      letter-spacing: 0.15em;
      color: var(--gold-primary);
      font-weight: 700;
    }

    .btn-fs {
      background: var(--nav-btn-bg);
      border: 1px solid var(--border-subtle);
      color: var(--nav-btn-color);
      padding: 6px 14px;
      border-radius: 4px;
      font-family: var(--font-mono);
      font-size: 0.72rem;
      letter-spacing: 0.12em;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: var(--transition-standard);
    }
    .btn-fs:hover {
      border-color: var(--gold-primary);
      color: var(--gold-primary);
      background: rgba(180, 123, 44, 0.12);
    }

    .slides-wrapper {
      flex: 1;
      position: relative;
      overflow: hidden;
      width: 100%;
      height: 100%;
    }

    .slide {
      position: absolute;
      inset: 0;
      padding: 2.2rem 3.2rem;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      opacity: 0;
      visibility: hidden;
      transform: translateY(12px) scale(0.995);
      transition: opacity 0.4s cubic-bezier(0.16, 1, 0.3, 1),
                  transform 0.4s cubic-bezier(0.16, 1, 0.3, 1),
                  visibility 0.4s;
      overflow-y: auto;
      scrollbar-width: thin;
    }

    .slide.active {
      opacity: 1;
      visibility: visible;
      transform: translateY(0) scale(1);
    }

    .slide-header {
      margin-bottom: 1rem;
    }

    .slide-eyebrow {
      font-family: var(--font-mono);
      font-size: 0.78rem;
      letter-spacing: 0.28em;
      text-transform: uppercase;
      color: var(--gold-primary);
      margin-bottom: 0.35rem;
      display: flex;
      align-items: center;
      gap: 8px;
      font-weight: 700;
    }

    .slide-eyebrow::before {
      content: "";
      display: inline-block;
      width: 18px;
      height: 2px;
      background: var(--gold-primary);
    }

    .slide-title {
      font-family: var(--font-serif);
      font-size: 2.2rem;
      font-weight: 700;
      line-height: 1.15;
      color: var(--text-title);
      letter-spacing: -0.015em;
    }

    .slide-subtitle {
      font-size: 1.02rem;
      line-height: 1.45;
      color: var(--sand-muted);
      font-weight: 400;
      max-width: 980px;
      margin-bottom: 1.2rem;
    }

    .content-area {
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: center;
    }

    .grid-2col {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 2.2rem;
      align-items: stretch;
      height: 100%;
    }

    .grid-2col-wide-left {
      display: grid;
      grid-template-columns: 1.25fr 0.75fr;
      gap: 2.2rem;
      align-items: stretch;
      height: 100%;
    }

    .grid-2col-wide-right {
      display: grid;
      grid-template-columns: 0.8fr 1.2fr;
      gap: 2.2rem;
      align-items: stretch;
      height: 100%;
    }

    .glass-card {
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 10px;
      padding: 1.6rem 1.8rem;
      box-shadow: var(--card-shadow);
      backdrop-filter: blur(14px);
      transition: var(--transition-standard);
      position: relative;
    }

    .glass-card.gold-trim {
      border-top: 4px solid var(--gold-primary);
    }

    .glass-card.terracotta-trim {
      border-top: 4px solid var(--terracotta);
    }

    .glass-card.teal-trim {
      border-top: 4px solid var(--teal-ocean);
    }

    .card-label {
      font-family: var(--font-mono);
      font-size: 0.82rem;
      text-transform: uppercase;
      letter-spacing: 0.16em;
      color: var(--gold-primary);
      margin-bottom: 0.45rem;
      font-weight: 700;
    }

    .card-heading {
      font-family: var(--font-serif);
      font-size: 1.55rem;
      font-weight: 700;
      color: var(--text-title);
      margin-bottom: 0.75rem;
      line-height: 1.25;
    }

    .card-body {
      font-size: 1.02rem;
      line-height: 1.6;
      color: var(--sand-muted);
    }

    .tag {
      display: inline-flex;
      align-items: center;
      padding: 4px 10px;
      border-radius: 4px;
      font-family: var(--font-mono);
      font-size: 0.75rem;
      font-weight: 700;
      letter-spacing: 0.06em;
    }
    .tag-gold {
      background: rgba(180, 123, 44, 0.15);
      color: var(--gold-primary);
      border: 1px solid rgba(180, 123, 44, 0.4);
    }
    .tag-terracotta {
      background: var(--terracotta-soft);
      color: var(--terracotta);
      border: 1px solid rgba(194, 65, 12, 0.4);
    }
    .tag-teal {
      background: var(--teal-soft);
      color: var(--teal-ocean);
      border: 1px solid rgba(15, 118, 110, 0.4);
    }

    .stat-box {
      background: var(--stat-bg);
      border: 1px solid var(--stat-border);
      border-radius: 8px;
      padding: 1rem 1.2rem;
    }
    .stat-number {
      font-family: var(--font-serif);
      font-size: 2.1rem;
      font-weight: 700;
      color: var(--text-title);
      line-height: 1.1;
      margin-bottom: 4px;
    }
    .stat-number.gold { color: var(--gold-primary); }
    .stat-number.terracotta { color: var(--terracotta); }
    .stat-number.teal { color: var(--teal-ocean); }
    .stat-caption {
      font-family: var(--font-mono);
      font-size: 0.74rem;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--sand-muted);
    }

    .editorial-media {
      position: relative;
      border-radius: 8px;
      overflow: hidden;
      height: 100%;
      min-height: 270px;
      box-shadow: var(--card-shadow);
      border: 1px solid var(--border-subtle);
    }
    .editorial-media img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transition: transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .editorial-media:hover img {
      transform: scale(1.03);
    }
    .media-overlay {
      position: absolute;
      inset: 0;
      background: linear-gradient(to top, rgba(7, 9, 12, 0.88) 0%, rgba(7, 9, 12, 0.25) 55%, transparent 100%);
      display: flex;
      flex-direction: column;
      justify-content: flex-end;
      padding: 1.5rem;
      pointer-events: none;
    }
    .media-title {
      font-family: var(--font-serif);
      font-size: 1.4rem;
      font-weight: 700;
      color: #ffffff;
      margin-bottom: 0.3rem;
    }
    .media-caption {
      font-size: 0.88rem;
      line-height: 1.45;
      color: #cbd5e1;
    }

    .highlight-list {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 0.7rem;
    }
    .highlight-list li {
      display: flex;
      align-items: flex-start;
      gap: 10px;
      font-size: 0.96rem;
      line-height: 1.5;
      color: var(--sand-light);
    }
    .highlight-list li::before {
      content: "◆";
      font-size: 0.7rem;
      color: var(--gold-primary);
      margin-top: 4px;
      flex-shrink: 0;
    }

    .deck-footer {
      height: 58px;
      padding: 0 2.5rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-top: 1px solid var(--border-subtle);
      background: var(--footer-bg);
      backdrop-filter: blur(12px);
      z-index: 20;
    }

    .nav-buttons {
      display: flex;
      gap: 8px;
    }
    .nav-btn {
      background: var(--nav-btn-bg);
      border: 1px solid var(--border-subtle);
      color: var(--nav-btn-color);
      padding: 7px 18px;
      border-radius: 4px;
      font-family: var(--font-mono);
      font-size: 0.78rem;
      font-weight: 700;
      letter-spacing: 0.12em;
      cursor: pointer;
      transition: var(--transition-standard);
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .nav-btn:hover:not(:disabled) {
      background: rgba(180, 123, 44, 0.14);
      border-color: var(--gold-primary);
      color: var(--gold-primary);
    }
    .nav-btn:disabled {
      opacity: 0.35;
      cursor: not-allowed;
    }

    .progress-dots {
      display: flex;
      gap: 4px;
      align-items: center;
    }
    .dot {
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: var(--dot-bg);
      transition: var(--transition-standard);
      cursor: pointer;
    }
    .dot.active {
      width: 20px;
      border-radius: 3px;
      background: var(--gold-primary);
      box-shadow: 0 0 10px var(--gold-glow);
    }

    /* Native select picker */
    .brand-nav-container {
      position: relative;
      display: inline-flex;
      align-items: center;
    }
    .native-slide-select {
      display: none;
    }

    /* Slide Navigation Drawer */
    .drawer-overlay {
      position: fixed;
      inset: 0;
      z-index: 1000;
      display: none;
      align-items: flex-end;
      justify-content: center;
    }
    .drawer-overlay.active {
      display: flex;
    }
    .drawer-backdrop {
      position: absolute;
      inset: 0;
      background: rgba(7, 9, 12, 0.65);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
    }
    .drawer-sheet {
      position: relative;
      width: 100%;
      max-width: 720px;
      max-height: 85vh;
      background: var(--bg-surface);
      border: 1px solid var(--border-gold);
      border-bottom: none;
      border-radius: 20px 20px 0 0;
      box-shadow: 0 -20px 60px rgba(0, 0, 0, 0.35);
      display: flex;
      flex-direction: column;
      overflow: hidden;
      z-index: 1001;
      animation: drawerSlideUp 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }
    @keyframes drawerSlideUp {
      from { transform: translateY(100%); }
      to { transform: translateY(0); }
    }
    .drawer-drag-bar {
      width: 100%;
      padding: 10px 0 4px 0;
      display: flex;
      justify-content: center;
      cursor: grab;
    }
    .drawer-drag-pill {
      width: 44px;
      height: 5px;
      border-radius: 999px;
      background: var(--sand-muted);
      opacity: 0.45;
    }
    .drawer-header {
      padding: 0.8rem 1.6rem 0.6rem 1.6rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid var(--border-subtle);
    }
    .drawer-eyebrow {
      font-family: var(--font-mono);
      font-size: 0.72rem;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: var(--gold-primary);
      font-weight: 700;
    }
    .drawer-title {
      font-family: var(--font-serif);
      font-size: 1.4rem;
      font-weight: 700;
      color: var(--text-title);
    }
    .drawer-close-btn {
      background: var(--nav-btn-bg);
      border: 1px solid var(--border-subtle);
      color: var(--text-title);
      width: 32px;
      height: 32px;
      border-radius: 50%;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1rem;
    }
    .drawer-search-row {
      padding: 0.8rem 1.6rem;
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      flex-direction: column;
      gap: 0.6rem;
    }
    .drawer-search-wrapper {
      position: relative;
      display: flex;
      align-items: center;
    }
    .drawer-search-icon {
      position: absolute;
      left: 12px;
      font-size: 0.9rem;
      color: var(--sand-muted);
    }
    .drawer-search-input {
      width: 100%;
      background: var(--stat-bg);
      border: 1px solid var(--border-subtle);
      border-radius: 8px;
      padding: 8px 36px 8px 36px;
      font-family: var(--font-sans);
      font-size: 0.9rem;
      color: var(--text-title);
      outline: none;
    }
    .drawer-search-input:focus {
      border-color: var(--gold-primary);
    }
    .drawer-search-clear {
      position: absolute;
      right: 12px;
      background: transparent;
      border: none;
      color: var(--sand-muted);
      cursor: pointer;
      font-size: 0.9rem;
    }
    .drawer-filter-pills {
      display: flex;
      gap: 6px;
      overflow-x: auto;
      padding-bottom: 2px;
    }
    .drawer-filter-pill {
      background: var(--pill-bg);
      border: 1px solid var(--pill-border);
      color: var(--sand-muted);
      padding: 4px 10px;
      border-radius: 999px;
      font-family: var(--font-mono);
      font-size: 0.72rem;
      cursor: pointer;
      white-space: nowrap;
    }
    .drawer-filter-pill.active {
      background: var(--gold-primary);
      color: #ffffff;
      border-color: var(--gold-primary);
    }
    .drawer-list {
      flex: 1;
      overflow-y: auto;
      padding: 0.8rem 1.6rem 2rem 1.6rem;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }
    .drawer-slide-item {
      display: flex;
      align-items: center;
      gap: 14px;
      padding: 10px 14px;
      border-radius: 8px;
      background: var(--stat-bg);
      border: 1px solid var(--border-subtle);
      cursor: pointer;
      transition: var(--transition-standard);
    }
    .drawer-slide-item:hover, .drawer-slide-item.active {
      border-color: var(--gold-primary);
      background: rgba(180, 123, 44, 0.09);
    }
    .drawer-slide-num {
      font-family: var(--font-mono);
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--gold-primary);
      min-width: 32px;
    }
    .drawer-slide-content {
      flex: 1;
    }
    .drawer-slide-meta {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 2px;
    }
    .drawer-slide-tag {
      font-family: var(--font-mono);
      font-size: 0.65rem;
      text-transform: uppercase;
      font-weight: 700;
      color: var(--sand-muted);
    }
    .drawer-slide-current-badge {
      font-family: var(--font-mono);
      font-size: 0.65rem;
      color: var(--gold-primary);
      font-weight: 700;
    }
    .drawer-slide-title {
      font-family: var(--font-serif);
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--text-title);
    }
    .drawer-slide-desc {
      font-size: 0.8rem;
      color: var(--sand-muted);
    }
    .drawer-slide-arrow {
      color: var(--sand-muted);
      font-size: 1rem;
    }

    /* Mobile Drawer Badge */
    .brand-drawer-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: var(--stat-bg);
      border: 1px solid var(--border-gold);
      border-radius: 999px;
      padding: 5px 12px;
      cursor: pointer;
      font-family: var(--font-mono);
      font-size: 0.74rem;
      color: var(--text-title);
      font-weight: 700;
    }

    /* Table styling */
    .table-editorial {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.92rem;
    }
    .table-editorial th {
      font-family: var(--font-mono);
      font-size: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 0.1em;
      color: var(--sand-muted);
      padding: 8px 12px;
      border-bottom: 2px solid var(--border-subtle);
      text-align: left;
    }
    .table-editorial td {
      padding: 10px 12px;
      border-bottom: 1px solid var(--border-subtle);
      color: var(--sand-light);
    }
    .table-editorial tr:last-child td {
      border-bottom: none;
    }

    /* Transit Option Selector */
    .transit-options-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 10px;
      margin-bottom: 1rem;
    }
    .transit-option-card {
      background: var(--stat-bg);
      border: 1px solid var(--border-subtle);
      border-radius: 8px;
      padding: 10px 12px;
      cursor: pointer;
      transition: var(--transition-standard);
      text-align: left;
    }
    .transit-option-card:hover, .transit-option-card.active {
      border-color: var(--gold-primary);
      background: rgba(180, 123, 44, 0.1);
    }
    .transit-option-card strong {
      display: block;
      font-family: var(--font-serif);
      font-size: 0.92rem;
      color: var(--text-title);
      margin-bottom: 2px;
    }
    .transit-option-card p {
      font-size: 0.76rem;
      color: var(--sand-muted);
      line-height: 1.3;
    }

    /* Waypoint Selector */
    .waypoint-selector {
      display: flex;
      gap: 6px;
      margin-bottom: 0.8rem;
      flex-wrap: wrap;
    }
    .stage-pill {
      background: var(--pill-bg);
      border: 1px solid var(--pill-border);
      padding: 5px 11px;
      border-radius: 4px;
      font-family: var(--font-mono);
      font-size: 0.75rem;
      cursor: pointer;
      color: var(--sand-muted);
      transition: var(--transition-standard);
    }
    .stage-pill:hover, .stage-pill.active {
      background: var(--gold-primary);
      color: #ffffff;
      border-color: var(--gold-primary);
    }

    /* Responsive adjustments */
    @media (max-width: 900px) {
      .deck-container {
        max-width: 100vw !important;
        max-height: 100vh !important;
        aspect-ratio: auto !important;
        border-radius: 0 !important;
        border: none !important;
      }
      .slide {
        padding-top: calc(52px + max(0.6rem, env(safe-area-inset-top))) !important;
        padding-bottom: calc(60px + max(0.8rem, env(safe-area-inset-bottom))) !important;
        padding-left: 1.2rem !important;
        padding-right: 1.2rem !important;
        display: flex !important;
        flex-direction: column !important;
        gap: 1.2rem !important;
        justify-content: flex-start !important;
      }
      .slide-title {
        font-size: 1.7rem !important;
      }
      .grid-2col, .grid-2col-wide-left, .grid-2col-wide-right {
        grid-template-columns: 1fr !important;
        gap: 1.2rem !important;
      }
      .editorial-media {
        height: 220px !important;
        min-height: 200px !important;
      }
      .transit-options-grid {
        grid-template-columns: 1fr 1fr !important;
      }
      .native-slide-select {
        display: block !important;
        position: absolute !important;
        inset: 0 !important;
        width: 100% !important;
        height: 100% !important;
        opacity: 0.001 !important;
        cursor: pointer !important;
        z-index: 9999 !important;
      }
      .progress-dots {
        display: none !important;
      }
    }

    /* Print & PDF Dossier */
    @media print {
      body, html {
        background: #ffffff !important;
        color: #0f172a !important;
        height: auto !important;
        overflow: visible !important;
      }
      .deck-header, .deck-footer, .viewport-ambient, .drawer-overlay {
        display: none !important;
      }
      .deck-container {
        box-shadow: none !important;
        border: none !important;
        max-width: 100% !important;
        aspect-ratio: auto !important;
        height: auto !important;
      }
      .slide {
        display: block !important;
        opacity: 1 !important;
        visibility: visible !important;
        transform: none !important;
        page-break-after: always !important;
        break-after: page !important;
        min-height: 90vh !important;
        padding: 2.5rem 2rem !important;
        border-bottom: 2px solid #e2e8f0 !important;
      }
      .slide:last-of-type {
        page-break-after: auto !important;
        break-after: auto !important;
        border-bottom: none !important;
      }
    }
  </style>
</head>
<body data-theme="linen">
  <div class="viewport-ambient"></div>

  <div class="deck-container" id="deckContainer">
    <!-- Header -->
    <header class="deck-header">
      <div class="header-brand">
        <div class="brand-symbol"></div>
        <div class="brand-nav-container">
          <div class="brand-drawer-badge" id="deckDrawerTrigger" role="button" tabindex="0" title="Open Slide Directory">
            <span>📋</span>
            <span>SLIDE DIRECTORY</span>
          </div>
          <!-- Native Slide Picker for Mobile -->
          <select id="nativeSlidePicker" class="native-slide-select" aria-label="Select Expedition Milestone">
            <optgroup label="🗺️ ACT I: STRATEGIC ORIENTATION (SLIDES 1–7)">
              <option value="0" selected>Slide 01 • Cover & Expedition Metrics</option>
              <option value="1">Slide 02 • Strategic Corridor: Open-Jaw EWR->MIA / MCO->EWR</option>
              <option value="2">Slide 03 • Interactive Florida Cartography & GPS Command</option>
              <option value="3">Slide 04 • Florida Meteorology & Microclimate Navigation</option>
              <option value="4">Slide 05 • Highway Logistics, SunPass & Rental Transponders</option>
              <option value="5">Slide 06 • Subtropical Wildlife & Wetland Safety Protocols</option>
              <option value="6">Slide 07 • Technical Packing & Theme Park Field Kit</option>
            </optgroup>
            <optgroup label="🌴 ACT II: MIAMI & OVERSEAS HIGHWAY (SLIDES 8–13)">
              <option value="7">Slide 08 • Day 1: Inbound EWR->MIA & Cultural Gateway</option>
              <option value="8">Slide 09 • Night 1: Miami Boutique Art Deco / Coral Gables</option>
              <option value="9">Slide 10 • Night 1: Authentic Cuban Ropa Vieja & Cafecito</option>
              <option value="10">Slide 11 • Day 2: Overseas Highway US-1 & Key Largo Coral Reefs</option>
              <option value="11">Slide 12 • Day 2: Bahia Honda State Park & Seven Mile Bridge</option>
              <option value="12">Slide 13 • Night 2: Key West Historic Old Town Guesthouse</option>
            </optgroup>
            <optgroup label="🐊 ACT III: KEY WEST & EVERGLADES (SLIDES 14–19)">
              <option value="13">Slide 14 • Day 3: Key West Historic Peninsula & Fort Zachary</option>
              <option value="14">Slide 15 • Day 3: Authentic Conch & Tart Key Lime Pie</option>
              <option value="15">Slide 16 • Night 3: Upper Keys Ocean Retreat (Marathon/Islamorada)</option>
              <option value="16">Slide 17 • Day 4: Everglades National Park (Shark Valley Tram)</option>
              <option value="17">Slide 18 • Day 4: Florida Turnpike Northbound Transit</option>
              <option value="18">Slide 19 • Night 4: Orlando Theme Park Base (3★/4★ Resort)</option>
            </optgroup>
            <optgroup label="⚡ ACT IV: ORLANDO THEME PARK THRILLS (SLIDES 20–25)">
              <option value="19">Slide 20 • Day 5: The Universal Day (Islands & Studios)</option>
              <option value="20">Slide 21 • Day 5: Universal Ride Strategy & Butterbeer</option>
              <option value="21">Slide 22 • Night 5: Orlando Base Continuation & Pool Recovery</option>
              <option value="22">Slide 23 • Day 6: The Disney Day (Magic Kingdom)</option>
              <option value="23">Slide 24 • Day 6: Lightning Lane, Virtual Queue & Fireworks</option>
              <option value="24">Slide 25 • Night 6: Orlando Base Continuation</option>
            </optgroup>
            <optgroup label="🏆 ACT V: EXPEDITION FINALE & SCORECARD (SLIDES 26–30)">
              <option value="25">Slide 26 • Day 7: Park-Free Canals & Disney Springs</option>
              <option value="26">Slide 27 • Day 7: Southern Smokehouse Feast & Citrus Finale</option>
              <option value="27">Slide 28 • Day 8: MCO Departure Protocol & Flight to EWR</option>
              <option value="28">Slide 29 • Master Scorecard & Shared Financial Ledger ($3,520)</option>
              <option value="29">Slide 30 • Zero-Fail Field Directory & Emergency Hotlines</option>
            </optgroup>
          </select>
        </div>
        <div class="brand-title">FLORIDA EXPEDITION DECK</div>
      </div>
      <div class="header-controls">
        <button class="btn-fs" id="themeBtn" title="Click to Cycle Color Scheme">🎨 PALETTE: Porcelain & Slate</button>
        <div class="slide-counter" id="slideCounter">SLIDE 01 / 30</div>
        <button class="btn-fs" id="fullscreenBtn" title="Toggle Fullscreen">⛶ EXPAND</button>
      </div>
    </header>

    <!-- Slide Navigation Drawer -->
    <div class="drawer-overlay" id="drawerOverlay" aria-hidden="true">
      <div class="drawer-backdrop" id="drawerBackdrop" title="Close Directory"></div>
      <aside class="drawer-sheet" id="drawerSheet" role="dialog" aria-modal="true" aria-labelledby="drawerTitle">
        <div class="drawer-drag-bar" id="drawerDragBar">
          <div class="drawer-drag-pill"></div>
        </div>
        <div class="drawer-header">
          <div>
            <div class="drawer-eyebrow">FLORIDA EXPEDITION DOSSIER • 30 MILESTONES</div>
            <h3 class="drawer-title" id="drawerTitle">Slide Directory</h3>
          </div>
          <button class="drawer-close-btn" id="drawerCloseBtn" type="button" aria-label="Close Slide Directory">✕</button>
        </div>
        <div class="drawer-search-row">
          <div class="drawer-search-wrapper">
            <span class="drawer-search-icon">🔍</span>
            <input type="text" class="drawer-search-input" id="drawerSearchInput" placeholder="Search milestone, park, beach, or hotel..." autocomplete="off">
            <button class="drawer-search-clear" id="drawerSearchClear" type="button" style="display: none;">✕</button>
          </div>
          <div class="drawer-filter-pills" id="drawerFilterPills">
            <button class="drawer-filter-pill active" data-filter="all" type="button">All (30)</button>
            <button class="drawer-filter-pill" data-filter="overview" type="button">Strategy (7)</button>
            <button class="drawer-filter-pill" data-filter="keys" type="button">Keys & Coast (6)</button>
            <button class="drawer-filter-pill" data-filter="glades" type="button">Everglades (2)</button>
            <button class="drawer-filter-pill" data-filter="parks" type="button">Theme Parks (6)</button>
            <button class="drawer-filter-pill" data-filter="retreat" type="button">Lodging (5)</button>
            <button class="drawer-filter-pill" data-filter="dining" type="button">Gastronomy (4)</button>
          </div>
        </div>
        <div class="drawer-list" id="drawerList">
          <!-- Dynamically populated by JS -->
        </div>
      </aside>
    </div>

    <!-- Slides Wrapper -->
    <main class="slides-wrapper" id="slidesWrapper">
"""
