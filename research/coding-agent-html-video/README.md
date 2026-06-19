# Coding Agent 写 HTML 做电商短视频 · 实测 + 对比

这是一份**带真实产物**的研究：验证"用 coding agent 写 HTML/CSS/JS 直出专业电商短视频"是否可行，
并与"图生视频 agent 工作流"做**可复现**的对比。

## TL;DR

- **可行，已实跑。** 本目录用 coding agent 写了一支 9:16 美妆带货短视频并真渲染成 MP4：
  `output/ecommerce-ad-1080x1920.mp4`（1080×1920 / 30fps / 15s / H.264）。
- **带货广告场景：代码路线赢**（信息逐字准确、可控、低成本、可批量）。
- **实拍质感品牌片：图生视频赢**。最优解是**混合工作流**。
- 完整结论见 `report/REPORT.md`；可视化看 `report/report.html`；评分口径见 `report/comparison-scorecard.md`。

## 目录结构

```
coding-agent-html-video/
├─ README.md                      本文件
├─ report/
│  ├─ REPORT.md                   主研究报告（结论 + 实测 + 对比 + 决策框架 + 参考文献）
│  ├─ comparison-scorecard.md     可复现 10 维评分卡 + 客观指标表 + 方法学
│  └─ report.html                 交互式报告（内嵌成片 + 分镜 + 评分卡）
├─ assets/
│  ├─ shared-brief.md             两条路线的同一输入 brief（含给图生视频的 prompt 包）
│  └─ frames/                     六段分镜关键帧（供报告内嵌）
├─ pipeline/                      可复用的确定性渲染管线
│  ├─ render.mjs                  HTML→逐帧截图→ffmpeg 编码 MP4（按帧驱动，确定性）
│  ├─ preview.mjs                 快速抓取指定时间点关键帧
│  ├─ scenes/ecommerce-ad.html    广告场景（自包含：字体/样式/时间线）
│  └─ lib/                        动画助手 + 自带 Noto Sans SC 子集字体
└─ output/                        渲染产物（MP4 + 封面）
```

## 一键复现（路线 A）

```bash
cd pipeline
npm install          # 安装 puppeteer + ffmpeg-static（Chrome 由 puppeteer 自动下载）
npm run render:ad    # 渲染 -> ../output/ecommerce-ad-1080x1920.mp4（本机约 7 分钟）
node preview.mjs scenes/ecommerce-ad.html "1.2,3.6,6.5,9.8,11.9,14.2"   # 仅看关键帧
```

改文案/价格 = 改 `scenes/ecommerce-ad.html` 里的文本，重渲染即更新；要换商品做批量，
把卖点/价格抽成参数即可（见报告第 7 节"数据驱动批量"）。

## 补齐路线 B（图生视频）做完全对称对比

把 `assets/shared-brief.md` 第 5 节的 prompt 包贴给 Sora / Veo / Kling / Runway / 即梦，
产出成片后用 `report/comparison-scorecard.md` 的客观指标表回填——两组同一把尺子，得到你环境下的结论。

## 技术栈与原理

- **渲染**：Puppeteer（无头 Chromium）逐帧截图；动画**按帧号**驱动（`window.seek(frame)`，
  不依赖墙钟时间）→ 100% 可复现、可 diff、可回归。
- **编码**：`ffmpeg-static`（libx264，yuv420p，+faststart）→ 全平台可播、可投放。
- **零外部素材**：示例产品瓶纯 CSS 绘制；中文用项目自带 Noto Sans SC 子集，无网络依赖即可渲染。

## 诚实边界

路线 A 全部为**真实渲染产物**，可逐帧核验。路线 B 因本环境无 AI 视频 API 密钥、出网受白名单限制
而**未实跑**，其分数基于 2026 年公开评测 + 范式特性判断（来源见 `report/REPORT.md` 参考文献）。
