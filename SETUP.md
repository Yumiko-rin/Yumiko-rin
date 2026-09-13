# 🚀 主页配置指南

深空夜航主题 GitHub 个人主页 —— 全部动画素材均为手写 SVG，无任何脚本依赖，可放心修改。

---

## ⚡ 三步上手

### 第 1 步 · 确认用户名（已完成 ✓）

用户名已配置为 `Yumiko-rin`，可直接跳到第 2 步。

> 如需更换：在 `README.md` 中全局搜索 `Yumiko-rin` 替换为新的用户名即可。两个 workflow 里用的是 `${{ github.repository_owner }}`，会自动适配，无需修改。

### 第 2 步 · 创建同名仓库并推送

1. 在 GitHub 上新建一个**与你用户名同名**的仓库（例如用户名是 `Yumiko-rin`，就建 `Yumiko-rin/Yumiko-rin`），**不要**勾选自动生成 README；
2. 推送本项目所有文件：

```bash
git init
git add .
git commit -m "feat: 初始化个人主页"
git branch -M main
git remote add origin https://github.com/你的用户名/你的用户名.git
git push -u origin main
```

3. 打开你的个人主页 `https://github.com/你的用户名`，README 已经生效 🎉

### 第 3 步 · 激活两个自动化（让蛇和 metrics 动起来）

1. **Metrics（需要一个 Token）**：
   - 打开 [Generate new token (classic)](https://github.com/settings/tokens/new?scopes=repo,read:user)，勾选 `repo` 和 `read:user`，生成后复制；
   - 仓库 → Settings → Secrets and variables → Actions → New repository secret，名称填 `METRICS_TOKEN`，值为刚才的 token；
   - 配置好后，**每次推送 main 会自动生成**（也支持每日定时与手动触发），生成 4 张自托管数据卡到 `github-metrics/`；
2. **贪吃蛇（零配置）**：仓库 → Actions → `Generate Snake` → Enable workflow → 右侧 `Run workflow` 手动跑一次（之后每日自动更新）。

两者首次运行后，刷新个人主页即可看到贪吃蛇和数据卡（jsDelivr 缓存约 12 小时，等不及见下方 FAQ）。

---

## 🎨 自定义指南

### 修改动画文案与配色（assets/ 目录）

| 文件 | 内容 | 常见改动 |
|---|---|---|
| `terminal-dark/light.svg` | 终端打字机：逐字输入 + 光标跟随 + 循环（明/暗自适应） | 改"命令"请同步调整对应 `clipPath` 里的 `to="宽度"`（每字符约 8.4px） |
| `wave-dark/light.svg` | 波浪分隔线（明/暗自适应） | 改 `fill` 色值 |
| `footer-dark/light.svg` | 页脚：THANKS FOR VISITING + 心跳（明/暗自适应） | 改文字即可 |

统一色板：背景 `#0d1117` · 青 `#39d2c0` · 蓝 `#58a6ff` · 琥珀 `#ffb86c` · 红 `#ff7b72` · 灰 `#8b949e`

### 修改打字机问候语

`README.md` 中 typing-svg 链接的 `lines=` 参数，用 [URL 编码工具](https://www.urlencoder.org/) 转换中文后替换。

### 换统计卡主题

连续提交卡（streak-stats）把 URL 里的 `theme=tokyonight` / `theme=default` 换成任意[可用主题](https://github.com/JuliaCiubotariu/git-heat-map#readme)即可；其余统计卡由本仓库 workflow 自行生成，样式可在 `metrics.yml` 里调整插件参数。

### 修改技术栈图标

到 [skillicons.dev](https://skillicons.dev) 挑选图标，替换 `icons?i=` 后面的英文缩写。

---

## ❓ 常见问题

**Q：图片显示不出来 / 一直是旧的？**
jsDelivr 有约 12 小时缓存。强制刷新：浏览器打开
`https://pur.jsdelivr.net/gh/你的用户名/你的用户名@main/assets/banner.svg`
（换成想刷新的文件路径）即可清除该文件缓存。

**Q：SVG 在本地会动，传上去不动了？**
GitHub 的图片代理会缓存，等缓存过期或用上面的 purge 链接刷新；另外确认文件确实推到了 `main` 分支。

**Q：贪吃蛇区域裂图？**
`output` 分支还没生成。去 Actions 手动跑一次 `Generate Snake`，确认运行成功后再刷新缓存。

**Q：Metrics 卡片报错？**
检查 `METRICS_TOKEN` 是否过期（classic PAT 默认 30 天，可在生成时设 No expiration），以及是否包含 `repo` 和 `read:user` 权限。到仓库 Actions 页查看 `GitHub Metrics` 最近一次运行日志定位原因。

**Q：为什么不用 github-readme-stats / trophy 这类在线统计卡？**
它们托管在 vercel.app 公共实例上，长期存在限流与间歇性不可用问题（README 上会随机裂图）。本主页改用 GitHub Actions 在自己仓库里生成数据卡（`github-metrics/` 目录），经 jsDelivr 分发，100% 稳定且数据更丰富。

**Q：如何预览明暗两种主题？**
GitHub → 头像 → Switch appearance。本地预览直接打开 `preview.html`，右上角可切换明暗。

---

## 📁 文件结构

```
.
├── README.md                 # 主页本体（推送到 GitHub 后自动展示）
├── SETUP.md                  # 本文件
├── preview.html              # 本地动画预览页（不会被主页引用）
├── scripts/
│   └── update-terminal.py    # 每日数据脚本：终端数字、项目徽章、项目卡片
├── assets/                   # 全部手写动画 SVG（均明暗自适应）
│   ├── terminal-dark.svg     # 终端打字机（暗色）
│   ├── terminal-light.svg    # 终端打字机（亮色）
│   ├── wave-dark.svg         # 波浪（暗色主题）
│   ├── wave-light.svg        # 波浪（亮色主题）
│   ├── footer-dark.svg       # 页脚（暗色主题）
│   ├── footer-light.svg      # 页脚（亮色主题）
│   ├── badge-dafeiyu.svg     # 项目最近更新日期徽章（脚本自动生成）
│   ├── card-dafeiyu-pet-dark.svg   # 项目卡片（脚本依据仓库真实数据生成）
│   └── card-dafeiyu-pet-light.svg  # 项目卡片（亮色）
└── .github/workflows/
    ├── snake.yml             # 每日生成贪吃蛇 → output 分支
    ├── metrics.yml           # 每日生成数据卡 → github-metrics/
    └── terminal-stats.yml    # 每日更新终端动画里的提交数与天数
```
