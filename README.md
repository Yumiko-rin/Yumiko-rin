<!-- ============================================================ -->
<!-- GitHub 个人主页 README                                        -->
<!-- 使用方法：创建与 GitHub 用户名同名的仓库 Yumiko-rin/Yumiko-rin -->
<!-- 将此文件作为 README.md 推送上去即可。                          -->
<!-- ============================================================ -->

<div align="center">

  <!-- 动态打字效果，替换 lines= 后的内容为你想显示的文字，多个用 ; 分隔 -->
  [![Typing SVG](https://readme-typing-svg.demolab.com?font=Press+Start+2P&pause=1200&color=FF69B4&width=500&lines=%E5%96%B5%E5%91%BC~%E4%B8%BB%E4%BA%BA%E4%BD%A0%E6%9D%A5%E5%95%A6%EF%BC%81;%E6%AC%A2%E8%BF%8E%E6%9D%A5%E5%88%B0%E6%88%91%E7%9A%84%E5%B0%8F%E7%AA%9D~;%E4%BB%8A%E5%A4%A9%E4%B9%9F%E8%A6%81%E5%85%83%E6%B0%94%E6%BB%A1%E6%BB%A1%E5%93%A6%EF%BC%81&center=true&size=20)](https://github.com/Yumiko-rin)

  <!-- 访客计数器 -->
  <div>
    <img src="https://komarev.com/ghpvc/?username=Yumiko-rin&label=Views&color=ff69b4&style=flat" alt="访问量统计" />
  </div>

  <div>&nbsp;</div>

  <!-- 可爱风装饰插画 + 贪吃蛇（左右装饰图，中间贪吃蛇） -->
  <img align="left" width="120" alt="左侧可爱装饰" src="https://user-images.githubusercontent.com/74038190/216122065-2f028bae-25d6-4a3c-bc9f-175394ed5011.png" style="border-radius: 12px;" />
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://cdn.jsdelivr.net/gh/Yumiko-rin/Yumiko-rin@output/github-contribution-grid-snake-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://cdn.jsdelivr.net/gh/Yumiko-rin/Yumiko-rin@output/github-contribution-grid-snake.svg" />
    <img style="max-width:calc(100% - 260px);height:auto;" alt="GitHub贡献贪吃蛇" src="https://cdn.jsdelivr.net/gh/Yumiko-rin/Yumiko-rin@output/github-contribution-grid-snake-dark.svg" />
  </picture>
  <img align="right" width="120" alt="右侧可爱装饰" src="https://user-images.githubusercontent.com/74038190/216120986-f2752ca9-fe82-4aa3-befe-0a58db010d85.png" style="border-radius: 12px;" />

  <div style="clear: both;"></div>
  <div>&nbsp;</div>

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
permissions:
  contents: write
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: Platane/snk@v3
        with:
          github_user_name: Yumiko-rin
          outputs: |
            dist/github-contribution-grid-snake-dark.svg?palette=github-dark
            dist/github-contribution-grid-snake.svg?palette=github-light
      - uses: crazy-max/ghaction-github-pages@v4
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
