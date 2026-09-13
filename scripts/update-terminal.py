#!/usr/bin/env python3
"""自动更新终端动画里的真实数据：提交总数 + 加入 GitHub 天数。
由 .github/workflows/terminal-stats.yml 每日调用；API 失败时保留旧数字，静默退出。"""
import json
import os
import re
import urllib.request
from datetime import date

JOINED = date(2026, 2, 28)  # GitHub 账号创建日
OWNER = "Yumiko-rin"
FILES = ["assets/terminal-dark.svg", "assets/terminal-light.svg"]

days = (date.today() - JOINED).days
commits = None

try:
    req = urllib.request.Request(
        f"https://api.github.com/search/commits?q=author:{OWNER}&per_page=1",
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {os.environ.get('GITHUB_TOKEN', '')}",
            "User-Agent": "profile-stats-updater",
        },
    )
    commits = json.load(urllib.request.urlopen(req, timeout=30)).get("total_count")
except Exception as e:  # API 失败时天数照常更新，提交数保留旧值
    print(f"warn: fetch commits failed ({e}), keep old value")

changed = []
for name in FILES:
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

print(f"days={days}, commits={commits}, updated={changed or 'none'}")
