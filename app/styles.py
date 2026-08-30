"""
MediAssist AI - Premium Healthcare UI Styles
A polished medical AI design system inspired by modern healthcare products.
"""


def get_main_css() -> str:
    """Return the complete premium CSS stylesheet for MediAssist AI."""
    return """
    <style>
    /* =============================================
       GOOGLE FONTS - Inter for clean medical feel
       ============================================= */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    /* =============================================
       CSS CUSTOM PROPERTIES
       ============================================= */
    :root {
        /* Primary - Medical Blue Palette */
        --ma-blue-900: #0C2D48;
        --ma-blue-800: #0D3B5E;
        --ma-blue-700: #0F4C75;
        --ma-blue-600: #1B6CA8;
        --ma-blue-500: #2196C8;
        --ma-blue-400: #4DB8D9;
        --ma-blue-300: #7ECCE6;
        --ma-blue-200: #B3E1F0;
        --ma-blue-100: #DBF1F8;
        --ma-blue-50: #EEF8FC;

        /* Teal / Cyan Accent */
        --ma-teal-600: #0D9488;
        --ma-teal-500: #14B8A6;
        --ma-teal-400: #2DD4BF;
        --ma-teal-100: #CCFBF1;

        /* Navy */
        --ma-navy-900: #0A1628;
        --ma-navy-800: #0F2240;
        --ma-navy-700: #162D50;

        /* Neutral Gray */
        --ma-gray-900: #111827;
        --ma-gray-800: #1F2937;
        --ma-gray-700: #374151;
        --ma-gray-600: #4B5563;
        --ma-gray-500: #6B7280;
        --ma-gray-400: #9CA3AF;
        --ma-gray-300: #D1D5DB;
        --ma-gray-200: #E5E7EB;
        --ma-gray-100: #F3F4F6;
        --ma-gray-50: #F9FAFB;

        /* Semantic */
        --ma-green-500: #10B981;
        --ma-green-100: #D1FAE5;
        --ma-red-500: #EF4444;
        --ma-red-100: #FEE2E2;
        --ma-amber-500: #F59E0B;
        --ma-amber-100: #FEF3C7;
        --ma-amber-800: #92400E;

        /* Surfaces */
        --surface-primary: #FFFFFF;
        --surface-secondary: #F8FAFC;
        --surface-tertiary: #F1F5F9;
        --surface-chat: #FAFBFD;

        /* Shadows */
        --shadow-xs: 0 1px 2px rgba(10, 22, 40, 0.04);
        --shadow-sm: 0 1px 3px rgba(10, 22, 40, 0.06), 0 1px 2px rgba(10, 22, 40, 0.04);
        --shadow-md: 0 4px 6px -1px rgba(10, 22, 40, 0.06), 0 2px 4px -1px rgba(10, 22, 40, 0.04);
        --shadow-lg: 0 10px 15px -3px rgba(10, 22, 40, 0.06), 0 4px 6px -2px rgba(10, 22, 40, 0.04);
        --shadow-xl: 0 20px 25px -5px rgba(10, 22, 40, 0.08), 0 10px 10px -5px rgba(10, 22, 40, 0.03);
        --shadow-blue: 0 4px 14px rgba(33, 150, 200, 0.15);
        --shadow-card: 0 1px 3px rgba(10, 22, 40, 0.05), 0 0 0 1px rgba(10, 22, 40, 0.03);

        /* Radius */
        --radius-sm: 6px;
        --radius-md: 10px;
        --radius-lg: 14px;
        --radius-xl: 20px;
        --radius-2xl: 24px;
        --radius-full: 9999px;

        /* Font */
        --font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }

    /* =============================================
       GLOBAL RESET & BASE
       ============================================= */
    * {
        font-family: var(--font-family) !important;
    }

    html, body, [class*="css"] {
        font-family: var(--font-family) !important;
    }

    /* Prevent any inline SVG from expanding beyond its container */
    svg {
        max-width: 100%;
        height: auto;
    }

    /* Hide Streamlit chrome */
    #MainMenu {visibility: hidden !important;}
    footer {visibility: hidden !important;}
    header[data-testid="stHeader"] {background: transparent !important; height: 0 !important;}
    header {visibility: hidden !important; height: 0 !important;}

    .stApp {
        background: linear-gradient(170deg, #E3F2FD 0%, #EBF5FB 25%, #F0F8FF 50%, #E8F4FD 75%, #E1F0FA 100%) !important;
        background-color: #E8F4FD !important;
    }

    .stApp > header {
        background: linear-gradient(135deg, #FAFCFE 0%, #E3F2FD 50%, #BBDEFB 100%) !important;
    }

    /* Remove default Streamlit padding */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 0 !important;
        max-width: 100% !important;
        background: transparent !important;
    }

    /* Main content area background */
    .stMain {
        background: linear-gradient(170deg, #E3F2FD 0%, #EBF5FB 25%, #F0F8FF 50%, #E8F4FD 75%, #E1F0FA 100%) !important;
        background-color: #E8F4FD !important;
    }

    section.main .block-container {
        background: transparent !important;
    }

    /* =============================================
       TOP HEADER BAR
       ============================================= */
    .top-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0.75rem 1.5rem;
        background: linear-gradient(135deg, #FAFCFE 0%, #E3F2FD 50%, #BBDEFB 100%);
        border-bottom: 2px solid rgba(21, 101, 192, 0.15);
        margin: -1rem -1rem 0 -1rem;
        position: sticky;
        top: 0;
        z-index: 100;
    }

    .top-header-left {
        display: flex;
        align-items: center;
        gap: 0.75rem;
    }

    .top-header-logo {
        width: 36px;
        height: 36px;
        min-width: 36px;
        max-width: 36px;
        background: linear-gradient(135deg, var(--ma-blue-600), var(--ma-teal-500));
        border-radius: var(--radius-md);
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 1.1rem;
        font-weight: 700;
        box-shadow: var(--shadow-blue);
        overflow: hidden;
    }

    .top-header-logo svg {
        width: 20px;
        height: 20px;
        flex-shrink: 0;
    }

    .top-header-title {
        font-size: 1.05rem;
        font-weight: 700;
        color: var(--ma-gray-900);
        letter-spacing: -0.3px;
    }

    .top-header-subtitle {
        font-size: 0.75rem;
        color: var(--ma-gray-400);
        font-weight: 400;
    }

    .top-header-right {
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    .status-pill {
        display: inline-flex;
        align-items: center;
        gap: 0.35rem;
        padding: 0.3rem 0.7rem;
        border-radius: var(--radius-full);
        font-size: 0.72rem;
        font-weight: 500;
        border: 1px solid transparent;
    }

    .status-pill.connected {
        background: var(--ma-green-100);
        color: #065F46;
        border-color: #A7F3D0;
    }

    .status-pill.disconnected {
        background: var(--ma-red-100);
        color: #991B1B;
        border-color: #FECACA;
    }

    .status-pill .dot {
        width: 6px;
        height: 6px;
        border-radius: 50%;
        flex-shrink: 0;
    }

    .status-pill.connected .dot { background: var(--ma-green-500); }
    .status-pill.disconnected .dot { background: var(--ma-red-500); }

    /* =============================================
       SIDEBAR - PREMIUM MEDICAL BLUE
       ============================================= */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1565C0 0%, #1976D2 25%, #1E88E5 50%, #2196F3 80%, #42A5F5 100%) !important;
        background-color: #1976D2 !important;
    }

    [data-testid="stSidebar"] > div {
        background: linear-gradient(180deg, #1565C0 0%, #1976D2 25%, #1E88E5 50%, #2196F3 80%, #42A5F5 100%) !important;
        background-color: #1976D2 !important;
    }

    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1565C0 0%, #1976D2 25%, #1E88E5 50%, #2196F3 80%, #42A5F5 100%) !important;
        background-color: #1976D2 !important;
    }

    section[data-testid="stSidebar"] > div {
        background: linear-gradient(180deg, #1565C0 0%, #1976D2 25%, #1E88E5 50%, #2196F3 80%, #42A5F5 100%) !important;
    }

    section[data-testid="stSidebar"] > div > div {
        background: linear-gradient(180deg, #1565C0 0%, #1976D2 25%, #1E88E5 50%, #2196F3 80%, #42A5F5 100%) !important;
    }

    section[data-testid="stSidebar"] [data-testid="stVerticalBlockBorderWrapper"] {
        background: transparent !important;
    }

    /* Force sidebar background via CSS custom property injection */
    :root {
        --sidebar-background-color: #1976D2;
        --sidebar-text-color: #FFFFFF;
        --secondary-background-color: #E8F4FD;
        --background-color: #E3F2FD;
    }

    [data-testid="stSidebar"][style] {
        background: linear-gradient(180deg, #1565C0 0%, #1976D2 25%, #1E88E5 50%, #2196F3 80%, #42A5F5 100%) !important;
    }

    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {
        color: rgba(255,255,255,0.95) !important;
    }

    [data-testid="stSidebar"] .stMarkdown p,
    [data-testid="stSidebar"] .stMarkdown h1,
    [data-testid="stSidebar"] .stMarkdown h2,
    [data-testid="stSidebar"] .stMarkdown h3,
    [data-testid="stSidebar"] .stMarkdown span,
    [data-testid="stSidebar"] .stMarkdown li {
        color: rgba(255,255,255,0.92) !important;
    }

    .sb-brand {
        text-align: center;
        padding: 1.8rem 1rem 1.4rem;
        border-bottom: 1px solid rgba(255,255,255,0.1);
        margin-bottom: 0.5rem;
    }

    .sb-brand-icon {
        width: 52px;
        height: 52px;
        min-width: 52px;
        max-width: 52px;
        background: linear-gradient(135deg, var(--ma-blue-500), var(--ma-teal-500));
        border-radius: var(--radius-lg);
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 0.75rem;
        box-shadow: 0 4px 20px rgba(33, 150, 200, 0.3);
        overflow: hidden;
    }

    .sb-brand-icon svg {
        width: 28px;
        height: 28px;
        flex-shrink: 0;
    }

    .sb-brand h1 {
        color: #FFFFFF !important;
        font-size: 1.2rem !important;
        font-weight: 700 !important;
        margin: 0 !important;
        letter-spacing: -0.3px;
    }

    .sb-brand .sb-tagline {
        color: rgba(255,255,255,0.55) !important;
        font-size: 0.78rem !important;
        margin-top: 0.2rem !important;
        font-weight: 400 !important;
    }

    .sb-section {
        padding: 0.6rem 0;
        margin-bottom: 0;
    }

    .sb-section-label {
        color: rgba(255,255,255,0.55) !important;
        font-size: 0.65rem !important;
        text-transform: uppercase !important;
        letter-spacing: 1.2px !important;
        font-weight: 600 !important;
        padding: 0 1rem;
        margin-bottom: 0.5rem;
    }

    .sb-item {
        display: flex;
        align-items: center;
        gap: 0.6rem;
        padding: 0.5rem 1rem;
        font-size: 0.85rem;
        color: rgba(255,255,255,0.75);
        border-radius: var(--radius-sm);
        margin: 0.1rem 0.5rem;
        transition: background 0.15s ease;
    }

    .sb-item:hover {
        background: rgba(255,255,255,0.08);
    }

    .sb-item .sb-icon {
        font-size: 0.9rem;
        width: 20px;
        text-align: center;
        flex-shrink: 0;
    }

    .sb-status-row {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.35rem 0.5rem 0.35rem 1rem;
        font-size: 0.82rem;
    }

    .sb-status-dot {
        width: 7px;
        height: 7px;
        border-radius: 50%;
        flex-shrink: 0;
    }

    .sb-status-dot.green { background: var(--ma-green-500); box-shadow: 0 0 6px rgba(16, 185, 129, 0.4); }
    .sb-status-dot.red { background: var(--ma-red-500); box-shadow: 0 0 6px rgba(239, 68, 68, 0.4); }
    .sb-status-dot.amber { background: var(--ma-amber-500); box-shadow: 0 0 6px rgba(245, 158, 11, 0.4); }

    .sb-divider {
        height: 1px;
        background: rgba(255,255,255,0.08);
        margin: 0.5rem 1rem;
    }

    .sb-disclaimer {
        margin: auto 0.75rem 1rem;
        padding: 0.75rem;
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: var(--radius-md);
        font-size: 0.72rem;
        color: rgba(255,255,255,0.45) !important;
        line-height: 1.45;
    }

    /* Sidebar buttons */
    [data-testid="stSidebar"] .stButton > button {
        background: rgba(255,255,255,0.18) !important;
        color: rgba(255,255,255,0.95) !important;
        border: 1px solid rgba(255,255,255,0.25) !important;
        border-radius: var(--radius-md) !important;
        font-size: 0.85rem !important;
        font-weight: 500 !important;
        padding: 0.55rem 1rem !important;
        transition: all 0.2s ease !important;
        width: calc(100% - 1rem) !important;
        margin: 0 0.5rem !important;
    }

    [data-testid="stSidebar"] .stButton > button:hover {
        background: rgba(255,255,255,0.28) !important;
        border-color: rgba(255,255,255,0.35) !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.15) !important;
    }

    /* =============================================
       WELCOME / TWO-COLUMN HERO SCREEN
       ============================================= */
    .ma-welcome-left {
        padding: 1.5rem 0;
    }

    .ma-welcome-title {
        font-size: 2rem !important;
        font-weight: 800 !important;
        color: var(--ma-gray-900) !important;
        margin-bottom: 0.5rem !important;
        letter-spacing: -0.6px !important;
        line-height: 1.2 !important;
    }

    .ma-welcome-title .gradient-text {
        background: linear-gradient(135deg, var(--ma-blue-600), var(--ma-teal-500));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    .ma-welcome-subtitle {
        font-size: 1.05rem !important;
        color: var(--ma-gray-500) !important;
        margin-bottom: 0.75rem !important;
        font-weight: 400 !important;
    }

    .ma-welcome-desc {
        font-size: 0.88rem !important;
        color: var(--ma-gray-400) !important;
        line-height: 1.55 !important;
        margin-bottom: 1rem !important;
    }

    .ma-welcome-visual {
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 1rem 0;
    }

    /* Hero card - controlled size, visually impressive */
    .ma-hero-card {
        width: 280px;
        height: 280px;
        position: relative;
        border-radius: var(--radius-2xl);
        overflow: hidden;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        box-shadow: var(--shadow-xl), 0 0 0 1px rgba(33, 150, 200, 0.08), 0 0 40px rgba(27, 108, 168, 0.25);
        margin: 0 auto;
        animation: hero-glow 4s ease-in-out infinite;
    }

    .ma-hero-card-bg {
        position: absolute;
        inset: 0;
        background: linear-gradient(145deg, var(--ma-blue-600) 0%, var(--ma-blue-700) 40%, var(--ma-teal-600) 100%);
        z-index: 0;
    }

    .ma-hero-card-icon {
        position: relative;
        z-index: 2;
        width: 100%;
        display: flex;
        justify-content: center;
    }

    .ma-hero-card-icon svg {
        width: 100%;
        height: 100%;
        position: absolute;
        top: 0;
        left: 0;
        border-radius: var(--radius-2xl);
        animation: hero-cross-glow 3s ease-in-out infinite;
    }

    .ma-hero-card-icon svg path[stroke-linecap="round"] {
        stroke-dasharray: 200;
        animation: hero-wave-flow 3s linear infinite;
    }

    .ma-hero-card-icon svg g[transform] {
        animation: hero-cross-glow 2.5s ease-in-out infinite;
    }

    .ma-hero-card-ring {
        position: absolute;
        border-radius: 50%;
        border: 1.5px solid rgba(255,255,255,0.15);
        z-index: 1;
        animation: hero-pulse 3s ease-in-out infinite;
    }

    .ring-1 {
        width: 200px; height: 200px;
        top: 40px; left: 40px;
        animation-delay: 0s;
    }

    .ring-2 {
        width: 150px; height: 150px;
        top: 65px; left: 65px;
        animation-delay: 0.5s;
    }

    .ring-3 {
        width: 100px; height: 100px;
        top: 90px; left: 90px;
        animation-delay: 1s;
    }

    .ma-hero-card-label {
        position: relative;
        z-index: 3;
        color: rgba(255,255,255,0.9);
        font-size: 0.8rem;
        font-weight: 600;
        letter-spacing: 0.3px;
        text-shadow: 0 1px 4px rgba(0,0,0,0.2);
    }

    @keyframes hero-pulse {
        0%, 100% { transform: scale(1); opacity: 0.8; }
        50% { transform: scale(1.12); opacity: 0.3; }
    }

    @keyframes hero-glow {
        0%, 100% { box-shadow: var(--shadow-xl), 0 0 0 1px rgba(33, 150, 200, 0.08), 0 0 40px rgba(27, 108, 168, 0.2); }
        50% { box-shadow: var(--shadow-xl), 0 0 0 1px rgba(33, 150, 200, 0.12), 0 0 60px rgba(20, 184, 166, 0.35); }
    }

    @keyframes hero-cross-glow {
        0%, 100% { filter: drop-shadow(0 0 4px rgba(255,255,255,0.3)); }
        50% { filter: drop-shadow(0 0 12px rgba(255,255,255,0.6)); }
    }

    @keyframes hero-wave-flow {
        0% { stroke-dashoffset: 200; }
        100% { stroke-dashoffset: 0; }
    }

    /* Feature badges */
    .ma-hero-badges {
        display: flex;
        gap: 0.5rem;
        flex-wrap: wrap;
        margin-top: 0.5rem;
    }

    .ma-hero-badge {
        display: inline-flex;
        align-items: center;
        gap: 0.35rem;
        padding: 0.35rem 0.7rem;
        background: var(--surface-primary);
        border: 1px solid var(--ma-gray-200);
        border-radius: var(--radius-full);
        font-size: 0.75rem;
        color: var(--ma-gray-600);
        font-weight: 500;
        box-shadow: var(--shadow-xs);
    }

    .ma-hero-badge .badge-icon {
        display: flex;
        align-items: center;
        color: var(--ma-blue-500);
    }

    .ma-hero-badge .badge-icon svg {
        width: 14px;
        height: 14px;
    }

    /* =============================================
       SUGGESTION CARDS
       ============================================= */
    .ma-suggestions-heading {
        font-size: 0.72rem !important;
        text-transform: uppercase !important;
        letter-spacing: 1.5px !important;
        color: var(--ma-gray-400) !important;
        font-weight: 600 !important;
        margin-bottom: 1rem !important;
        text-align: center !important;
    }

    .ma-suggestion-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 0.75rem;
        margin-bottom: 2.5rem;
    }

    .ma-suggestion-card {
        background: var(--surface-primary);
        border: 1px solid var(--ma-gray-200);
        border-radius: var(--radius-lg);
        padding: 1rem 1.15rem;
        text-align: left;
        cursor: pointer;
        transition: all 0.2s ease;
        box-shadow: var(--shadow-card);
        display: flex;
        align-items: flex-start;
        gap: 0.75rem;
    }

    .ma-suggestion-card:hover {
        border-color: var(--ma-blue-400);
        box-shadow: var(--shadow-md), 0 0 0 1px rgba(33, 150, 200, 0.1);
        transform: translateY(-1px);
    }

    .ma-suggestion-icon {
        width: 36px;
        height: 36px;
        border-radius: var(--radius-md);
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        font-size: 1rem;
    }

    .ma-suggestion-icon.blue { background: var(--ma-blue-50); color: var(--ma-blue-600); }
    .ma-suggestion-icon.teal { background: var(--ma-teal-100); color: var(--ma-teal-600); }
    .ma-suggestion-icon.amber { background: var(--ma-amber-100); color: var(--ma-amber-800); }
    .ma-suggestion-icon.red { background: var(--ma-red-100); color: var(--ma-red-500); }

    .ma-suggestion-text {
        font-size: 0.85rem !important;
        color: var(--ma-gray-700) !important;
        font-weight: 500 !important;
        line-height: 1.4 !important;
    }

    /* =============================================
       DISCLAIMER BANNER (welcome page)
       ============================================= */
    .ma-disclaimer {
        background: linear-gradient(135deg, #FFFBEB 0%, #FEF3C7 100%);
        border: 1px solid #FDE68A;
        border-radius: var(--radius-lg);
        padding: 1rem 1.25rem;
        text-align: left;
        font-size: 0.8rem;
        color: var(--ma-amber-800);
        line-height: 1.55;
        max-width: 740px;
        margin: 0 auto 2rem;
    }

    .ma-disclaimer strong {
        color: var(--ma-amber-800);
    }

    /* =============================================
       CHAT AREA
       ============================================= */
    .stChatMessage {
        border-radius: var(--radius-lg) !important;
        border: 1px solid transparent !important;
        box-shadow: none !important;
        margin: 0.25rem 0 !important;
        padding: 1rem 1.25rem !important;
        background: transparent !important;
    }

    /* User messages - right aligned style */
    [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) {
        background: var(--ma-blue-50) !important;
        border: 1px solid var(--ma-blue-100) !important;
        border-radius: var(--radius-lg) !important;
    }

    /* Assistant messages - white card */
    [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]) {
        background: var(--surface-primary) !important;
        border: 1px solid var(--ma-gray-200) !important;
        border-radius: var(--radius-lg) !important;
        box-shadow: var(--shadow-sm) !important;
    }

    /* Avatar styling */
    [data-testid="chatAvatarIcon-assistant"] {
        background: linear-gradient(135deg, var(--ma-blue-600), var(--ma-teal-500)) !important;
    }

    [data-testid="chatAvatarIcon-user"] {
        background: var(--ma-gray-600) !important;
    }

    /* =============================================
       SOURCES EXPANDER
       ============================================= */
    .ma-sources-section {
        margin-top: 0.75rem;
        padding-top: 0.75rem;
        border-top: 1px solid var(--ma-gray-100);
    }

    .ma-source-card {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.45rem 0.7rem;
        background: var(--surface-secondary);
        border: 1px solid var(--ma-gray-200);
        border-radius: var(--radius-sm);
        margin: 0.3rem 0;
        font-size: 0.78rem;
        color: var(--ma-gray-600);
    }

    .ma-source-card .source-num {
        background: var(--ma-blue-500);
        color: white;
        width: 18px;
        height: 18px;
        border-radius: var(--radius-sm);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 0.65rem;
        font-weight: 600;
        flex-shrink: 0;
    }

    .ma-source-card .source-page {
        margin-left: auto;
        background: var(--ma-gray-100);
        padding: 0.1rem 0.45rem;
        border-radius: var(--radius-sm);
        font-size: 0.7rem;
        color: var(--ma-gray-500);
        font-weight: 500;
    }

    .ma-context-preview {
        font-size: 0.82rem;
        color: var(--ma-gray-500);
        background: var(--surface-secondary);
        padding: 0.75rem;
        border-radius: var(--radius-md);
        border-left: 3px solid var(--ma-blue-400);
        margin-top: 0.75rem;
        line-height: 1.5;
    }

    /* =============================================
       MEDICAL SAFETY WARNING
       ============================================= */
    .ma-safety-warning {
        background: linear-gradient(135deg, #FEF2F2 0%, #FEE2E2 100%);
        border: 1px solid #FECACA;
        border-left: 4px solid var(--ma-red-500);
        border-radius: var(--radius-md);
        padding: 0.85rem 1rem;
        margin: 0.75rem 0;
        font-size: 0.85rem;
        color: #991B1B;
        line-height: 1.5;
    }

    .ma-safety-warning .safety-title {
        font-weight: 600;
        color: #DC2626;
        font-size: 0.88rem;
        margin-bottom: 0.25rem;
    }

    /* =============================================
       ERROR & INSUFFICIENT INFO
       ============================================= */
    .ma-error {
        background: var(--ma-red-100);
        border: 1px solid #FECACA;
        border-left: 4px solid var(--ma-red-500);
        border-radius: var(--radius-md);
        padding: 0.85rem 1rem;
        margin: 0.5rem 0;
    }

    .ma-error .error-title {
        color: #DC2626;
        font-weight: 600;
        font-size: 0.88rem;
        margin-bottom: 0.2rem;
    }

    .ma-error .error-message {
        color: #991B1B;
        font-size: 0.82rem;
        line-height: 1.5;
    }

    .ma-limited {
        background: var(--ma-blue-50);
        border: 1px solid var(--ma-blue-200);
        border-left: 4px solid var(--ma-blue-400);
        border-radius: var(--radius-md);
        padding: 0.85rem 1rem;
        margin: 0.5rem 0;
        font-size: 0.85rem;
        color: var(--ma-blue-700);
        line-height: 1.55;
    }

    .ma-limited strong {
        color: var(--ma-blue-800);
    }

    /* =============================================
       FOOTER DISCLAIMER
       ============================================= */
    .ma-footer-disclaimer {
        text-align: center;
        padding: 1.25rem 1rem;
        margin-top: 1.5rem;
        border-top: 1px solid var(--ma-gray-200);
        font-size: 0.75rem;
        color: var(--ma-gray-400);
        line-height: 1.5;
    }

    /* =============================================
       BUTTONS
       ============================================= */
    .stButton > button {
        border-radius: var(--radius-md) !important;
        font-weight: 500 !important;
        font-size: 0.85rem !important;
        transition: all 0.15s ease !important;
        border: 1px solid var(--ma-gray-200) !important;
        background: var(--surface-primary) !important;
        color: var(--ma-gray-700) !important;
    }

    .stButton > button:hover {
        border-color: var(--ma-blue-400) !important;
        color: var(--ma-blue-600) !important;
        box-shadow: var(--shadow-sm) !important;
    }

    /* Primary buttons */
    .stButton > button[kind="primary"],
    .stButton > button[data-testid="stBaseButton-primary"] {
        background: linear-gradient(135deg, var(--ma-blue-600), var(--ma-blue-500)) !important;
        color: white !important;
        border: none !important;
        box-shadow: var(--shadow-blue) !important;
    }

    /* =============================================
       CHAT INPUT
       ============================================= */
    .stChatInput {
        border-radius: var(--radius-xl) !important;
    }

    [data-testid="stChatInput"] {
        border: 1px solid var(--ma-gray-200) !important;
        border-radius: var(--radius-xl) !important;
        box-shadow: var(--shadow-md) !important;
        background: var(--surface-primary) !important;
    }

    [data-testid="stChatInput"]:focus-within {
        border-color: var(--ma-blue-400) !important;
        box-shadow: var(--shadow-md), 0 0 0 3px rgba(33, 150, 200, 0.1) !important;
    }

    /* =============================================
       LOADING / THINKING
       ============================================= */
    .ma-thinking {
        display: flex;
        align-items: center;
        gap: 0.6rem;
        padding: 0.75rem 1rem;
        color: var(--ma-gray-400);
        font-size: 0.85rem;
    }

    .ma-thinking-dots {
        display: flex;
        gap: 3px;
    }

    .ma-thinking-dots span {
        width: 6px;
        height: 6px;
        border-radius: 50%;
        background: var(--ma-blue-400);
        animation: thinking-bounce 1.4s infinite both;
    }

    .ma-thinking-dots span:nth-child(2) { animation-delay: 0.16s; }
    .ma-thinking-dots span:nth-child(3) { animation-delay: 0.32s; }

    @keyframes thinking-bounce {
        0%, 80%, 100% { transform: scale(0.6); opacity: 0.4; }
        40% { transform: scale(1); opacity: 1; }
    }

    /* =============================================
       RESPONSIVE
       ============================================= */
    @media (max-width: 768px) {
        .ma-welcome-title { font-size: 1.6rem !important; }
        .ma-welcome-subtitle { font-size: 0.95rem !important; }
        .ma-hero-card { width: 220px !important; height: 220px !important; }
        .ma-hero-card-icon svg { width: 60px !important; height: 60px !important; }
        .ring-1 { width: 160px !important; height: 160px !important; top: 30px !important; left: 30px !important; }
        .ring-2 { width: 120px !important; height: 120px !important; top: 50px !important; left: 50px !important; }
        .ring-3 { width: 80px !important; height: 80px !important; top: 70px !important; left: 70px !important; }
        .ma-hero-badges { gap: 0.35rem !important; }
        .ma-hero-badge { font-size: 0.7rem !important; padding: 0.3rem 0.55rem !important; }
        .top-header { padding: 0.5rem 1rem !important; }
        .top-header-subtitle { display: none !important; }
    }

    @media (max-width: 480px) {
        .ma-welcome-title { font-size: 1.4rem !important; }
        .ma-hero-card { width: 180px !important; height: 180px !important; }
        .ma-hero-card-icon svg { width: 48px !important; height: 48px !important; }
        .ring-1 { width: 130px !important; height: 130px !important; top: 25px !important; left: 25px !important; }
        .ring-2 { width: 100px !important; height: 100px !important; top: 40px !important; left: 40px !important; }
        .ring-3 { width: 70px !important; height: 70px !important; top: 55px !important; left: 55px !important; }
        .ma-hero-card-label { font-size: 0.7rem !important; }
    }

    /* =============================================
       SCROLLBAR STYLING
       ============================================= */
    ::-webkit-scrollbar { width: 6px; }
    ::-webkit-scrollbar-track { background: transparent; }
    ::-webkit-scrollbar-thumb { background: var(--ma-gray-300); border-radius: 3px; }
    ::-webkit-scrollbar-thumb:hover { background: var(--ma-gray-400); }

    /* =============================================
       MARKDOWN IN CHAT - IMPROVED READABILITY
       ============================================= */
    [data-testid="stChatMessage"] h1,
    [data-testid="stChatMessage"] h2,
    [data-testid="stChatMessage"] h3 {
        color: var(--ma-gray-900) !important;
        margin-top: 0.75rem !important;
        margin-bottom: 0.4rem !important;
    }

    [data-testid="stChatMessage"] h2 {
        font-size: 1.05rem !important;
    }

    [data-testid="stChatMessage"] h3 {
        font-size: 0.95rem !important;
    }

    [data-testid="stChatMessage"] ul,
    [data-testid="stChatMessage"] ol {
        margin: 0.4rem 0 !important;
        padding-left: 1.2rem !important;
    }

    [data-testid="stChatMessage"] li {
        margin: 0.2rem 0 !important;
        line-height: 1.55 !important;
    }

    [data-testid="stChatMessage"] strong {
        color: var(--ma-gray-900) !important;
    }

    [data-testid="stChatMessage"] code {
        background: var(--ma-gray-100) !important;
        padding: 0.1rem 0.35rem !important;
        border-radius: 4px !important;
        font-size: 0.85em !important;
    }

    [data-testid="stChatMessage"] blockquote {
        border-left: 3px solid var(--ma-blue-400) !important;
        padding-left: 0.75rem !important;
        color: var(--ma-gray-600) !important;
        margin: 0.5rem 0 !important;
    }

    /* Streamlit expander styling override */
    .streamlit-expanderHeader {
        font-size: 0.82rem !important;
        font-weight: 500 !important;
        color: var(--ma-gray-600) !important;
        border-radius: var(--radius-md) !important;
    }

    /* Suggestion button styling - make them feel like cards */
    [data-testid="stButton"] button {
        text-align: left !important;
        padding: 0.7rem 1rem !important;
        border-radius: var(--radius-md) !important;
        border: 1px solid var(--ma-gray-200) !important;
        background: var(--surface-primary) !important;
        box-shadow: var(--shadow-xs) !important;
        transition: all 0.2s ease !important;
        font-size: 0.85rem !important;
        color: var(--ma-gray-700) !important;
    }

    [data-testid="stButton"] button:hover {
        border-color: var(--ma-blue-300) !important;
        box-shadow: var(--shadow-sm) !important;
        background: var(--ma-blue-50) !important;
    }

    [data-testid="stButton"] button:active {
        transform: scale(0.99) !important;
    }
    </style>
    """
