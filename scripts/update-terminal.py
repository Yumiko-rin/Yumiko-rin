#!/usr/bin/env python3
"""自动更新主页自绘数据：终端动画的提交数/天数 + 项目徽章的最近更新日期。
由 .github/workflows/terminal-stats.yml 每日调用；API 失败时保留旧数据，静默退出。"""
import json
import os
import re
import urllib.request
from datetime import date

JOINED = date(2026, 2, 28)  # GitHub 账号创建日
OWNER = "Yumiko-rin"
REPO = "dafeiyu-pet"
TERMINALS = ["assets/terminal-dark.svg", "assets/terminal-light.svg"]
BADGE = "assets/badge-dafeiyu.svg"


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

print(f"days={days}, commits={commits}, updated={changed or 'none'}")
