<!-- ============================================================ -->

<!-- GitHub 个人主页 README                                        -->

<!-- 使用方法：创建与 GitHub 用户名同名的仓库 Yumiko-rin/Yumiko-rin -->

<!-- 将此文件作为 README.md 推送上去即可。                          -->

<!-- ============================================================ -->

<div align="center">

  <!-- 动态打字效果，替换 lines= 后的内容为你想显示的文字，多个用 ; 分隔 -->

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code\&pause=1000\&width=435\&lines=console.log\(%22Hello%2C+World%22\);%E6%AC%A2%E8%BF%8E%E6%9D%A5%E5%88%B0%E6%88%91%E7%9A%84%E4%B8%BB%E9%A1%B5!\&center=true\&size=27)](https://github.com/Yumiko-rin)

  <!-- GitHub 贡献贪吃蛇动画，需配置 GitHub Action 定期生成 SVG，见底部说明 -->

  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://cdn.jsdelivr.net/gh/Yumiko-rin/Yumiko-rin@output/github-contribution-grid-snake-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://cdn.jsdelivr.net/gh/Yumiko-rin/Yumiko-rin@output/github-contribution-grid-snake.svg" />
    <img style="max-width:100%;height:auto;" alt="GitHub贡献贪吃蛇" src="https://cdn.jsdelivr.net/gh/Yumiko-rin/Yumiko-rin@output/github-contribution-grid-snake-dark.svg" />
  </picture>

  <!-- GitHub Metrics 信息卡片，需配置 GitHub Action 生成 SVG，见底部说明 -->
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://cdn.jsdelivr.net/gh/Yumiko-rin/Yumiko-rin/github-metrics/base-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://cdn.jsdelivr.net/gh/Yumiko-rin/Yumiko-rin/github-metrics/base-light.svg" />
    <img style="max-width:100%;height:auto;" alt="GitHub Metrics" src="https://cdn.jsdelivr.net/gh/Yumiko-rin/Yumiko-rin/github-metrics/base-dark.svg" />
  </picture>

</div>

<!--
================================================================
  附：GitHub Action 配置说明
================================================================

【1】贪吃蛇动画 — .github/workflows/snake.yml

name: Generate Snake
on:
  schedule:
    - cron: "0 0 * * *"
  workflow_dispatch:
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: Platane/sink@main
        with:
          github_user_name: Yumiko-rin
          outputs: |
            dist/github-contribution-grid-snake-dark.svg?palette=github-dark
            dist/github-contribution-grid-snake.svg?palette=github-light
      - uses: crazy-max/ghaction-github-pages@v3
        with:
          target_branch: output
          build_dir: dist
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

----------------------------------------------------------------

【2】GitHub Metrics — .github/workflows/metrics.yml

  需先创建 Personal Access Token：
  GitHub Settings → Developer settings → Personal access tokens (classic)
  → Generate new token → 勾选 repo, read:user → 复制 token
  → 仓库 Settings → Secrets and variables → Actions → New repository secret
  → Name: METRICS_TOKEN → Value: 粘贴刚才的 token

name: GitHub Metrics
on:
  schedule:
    - cron: "0 0 * * *"
  workflow_dispatch:
jobs:
  github-metrics:
    runs-on: ubuntu-latest
    steps:
      - uses: lowlighter/metrics@latest
        with:
          token: ${{ secrets.METRICS_TOKEN }}
          filename: github-metrics/base-dark.svg
          base: header, activity, community, repositories, metadata
          config_timezone: Asia/Shanghai
          config_display: large

      - uses: lowlighter/metrics@latest
        with:
          token: ${{ secrets.METRICS_TOKEN }}
          filename: github-metrics/base-light.svg
          base: header, activity, community, repositories, metadata
          config_timezone: Asia/Shanghai
          config_display: large
          output_base: ""

  注意：Metrics 默认推送到仓库根目录的 github-metrics/ 目录下。
  深色版输出 base-dark.svg，浅色版输出 base-light.svg。
  README 中通过 jsdelivr CDN 引用这两个文件，深浅模式自动切换。
--> 
