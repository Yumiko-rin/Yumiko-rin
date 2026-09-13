#!/usr/bin/env python3
"""自动更新主页自绘数据：终端动画的提交数/天数 + 项目徽章 + 项目卡片。
由 .github/workflows/terminal-stats.yml 每日调用；API 失败时保留旧数据，静默退出。"""
import glob
import json
import os
import re
import urllib.request
from datetime import date
from xml.sax.saxutils import escape

JOINED = date(2026, 2, 28)  # GitHub 账号创建日
OWNER = "Yumiko-rin"
REPO = "dafeiyu-pet"
TERMINALS = ["assets/terminal-dark.svg", "assets/terminal-light.svg"]
BADGE = "assets/badge-dafeiyu.svg"
CARD = "assets/card-{name}-{variant}.svg"

LANG_COLORS = {
    "Python": "#3572A5", "TypeScript": "#3178c6", "JavaScript": "#f1e05a",
    "HTML": "#e34c26", "CSS": "#663399", "PLpgSQL": "#336790",
    "Batchfile": "#C1F12E", "C": "#555555", "C++": "#f34b7d", "Go": "#00ADD8",
    "Java": "#b07219", "Rust": "#dea584", "Shell": "#89e051", "Vue": "#41b883",
}
DEFAULT_LANG_COLOR = "#8b949e"


def api(url):
    req = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {os.environ.get('GITHUB_TOKEN', '')}",
            "User-Agent": "profile-stats-updater",
        },
    )
    return json.load(urllib.request.urlopen(req, timeout=30))


def trunc(s, n):
    s = (s or "").strip()
    return s if len(s) <= n else s[: n - 1] + "…"


def build_badge(pushed: str) -> str:
    """生成仿 shields flat-square 样式的最近更新日期徽章。"""
    lw, vw = 64, 82
    w = lw + vw
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="20" role="img" aria-label="最近更新: {pushed}">
  <linearGradient id="s" x2="0" y2="100%"><stop offset="0" stop-color="#bbb" stop-opacity=".1"/><stop offset="1" stop-opacity=".1"/></linearGradient>
  <clipPath id="r"><rect width="{w}" height="20" rx="3" fill="#fff"/></clipPath>
  <g clip-path="url(#r)">
    <rect width="{lw}" height="20" fill="#24292f"/>
    <rect x="{lw}" width="{vw}" height="20" fill="#1f6feb"/>
    <rect width="{w}" height="20" fill="url(#s)"/>
  </g>
  <g fill="#fff" text-anchor="middle" font-family="Verdana,Geneva,'DejaVu Sans',sans-serif" font-size="11">
    <text x="{lw // 2}" y="15">最近更新</text>
    <text x="{lw + vw // 2}" y="15">{pushed}</text>
  </g>
</svg>
'''


def build_card(repo: dict, variant: str) -> str:
    """根据仓库真实数据生成项目卡片 SVG（dark / light 两套配色）。"""
    name = repo["name"]
    desc = trunc(escape(repo.get("description") or "暂无简介"), 28)
    lang = repo.get("language") or "Markdown"
    dot = LANG_COLORS.get(lang, DEFAULT_LANG_COLOR)
    stars = repo.get("stargazers_count", 0)
    pushed = (repo.get("pushed_at") or "")[:10]
    updated = "今天" if pushed == date.today().isoformat() else pushed

    if variant == "dark":
        bg, border, title, desc_c, meta_c = "#101828", "#2b3d52", "#58a6ff", "#8b949e", "#8b949e"
    else:
        bg, border, title, desc_c, meta_c = "#ffffff", "#a9c3dd", "#0550ae", "#57606a", "#6a7683"

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="460" height="96" viewBox="0 0 460 96" role="img" aria-label="{escape(name)}: {desc}">
  <rect x="1" y="1" width="458" height="94" rx="10" fill="{bg}" stroke="{border}" stroke-width="2"/>
  <text x="20" y="32" font-family="'Segoe UI','Microsoft YaHei',sans-serif" font-size="15" font-weight="bold" fill="{title}">{escape(name)}</text>
  <text x="20" y="57" font-family="'Segoe UI','Microsoft YaHei',sans-serif" font-size="12.5" fill="{desc_c}">{desc}</text>
  <circle cx="24" cy="76" r="5" fill="{dot}"/>
  <text x="34" y="80" font-family="'Segoe UI','Microsoft YaHei',sans-serif" font-size="11.5" fill="{meta_c}">{escape(lang)}&#160;&#160;·&#160;&#160;★ {stars}&#160;&#160;·&#160;&#160;更新 {updated}</text>
</svg>
'''


changed = []

# ① 终端动画：提交总数 + 加入天数
days = (date.today() - JOINED).days
commits = None
try:
    commits = api(f"https://api.github.com/search/commits?q=author:{OWNER}&per_page=1").get("total_count")
except Exception as e:  # API 失败时天数照常更新，提交数保留旧值
    print(f"warn: fetch commits failed ({e}), keep old value")

for name in TERMINALS:
    with open(name, encoding="utf-8") as f:
        s = f.read()
    orig = s
    s = re.sub(r">(\d+) days</tspan>", f">{days} days</tspan>", s)
    if commits is not None:
        s = re.sub(r"已推送 \d+\+? 个提交", f"已推送 {commits}+ 个提交", s)
    if s != orig:
        with open(name, "w", encoding="utf-8") as f:
            f.write(s)
        changed.append(name)

# ② 项目徽章：最近更新日期
try:
    pushed = api(f"https://api.github.com/repos/{OWNER}/{REPO}").get("pushed_at", "")[:10]
    if pushed:
        svg = build_badge(pushed)
        if not os.path.exists(BADGE) or open(BADGE, encoding="utf-8").read() != svg:
            with open(BADGE, "w", encoding="utf-8") as f:
                f.write(svg)
            changed.append(BADGE)
except Exception as e:
    print(f"warn: fetch repo badge failed ({e}), keep old value")

# ③ 项目卡片：从公开仓库列表生成（排除个人资料仓库），数据全部来自 API
try:
    repos = api(f"https://api.github.com/users/{OWNER}/repos?per_page=100")
    projects = [r for r in repos if r.get("name") != OWNER and not r.get("fork")]
    generated = set()
    for r in projects:
        for variant in ("dark", "light"):
            path = CARD.format(name=r["name"], variant=variant)
            svg = build_card(r, variant)
            if not os.path.exists(path) or open(path, encoding="utf-8").read() != svg:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(svg)
                changed.append(path)
            generated.add(os.path.basename(path))
    # 清理已删除仓库的残留卡片
    for path in glob.glob("assets/card-*-dark.svg") + glob.glob("assets/card-*-light.svg"):
        if os.path.basename(path) not in generated:
            os.remove(path)
            changed.append(f"-{path}")
    print(f"projects: {[r['name'] for r in projects]}")
except Exception as e:
    print(f"warn: fetch repos failed ({e}), keep old cards")

print(f"days={days}, commits={commits}, updated={changed or 'none'}")
