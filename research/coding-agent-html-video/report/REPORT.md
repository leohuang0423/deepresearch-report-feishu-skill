# 用 Coding Agent 写 HTML 做电商短视频，到底行不行？
## ——与「图生视频 agent 工作流」的可复现实测对比

**作者**：Claude Code（agent 自主完成）  ·  **日期**：2026-06-19  ·  **类型**：研究 + 真实产物对比

---

## 0. 一句话结论

**行，而且在"带货型电商短视频"这个具体场景里，coding agent 写 HTML/CSS/JS 直出视频的路线，质量、可控性、成本、可批量性整体优于图生视频工作流；但在"要实拍质感/真人/情绪"的品牌片场景里，图生视频反超。最优解是两者混合。**

这不是纸上判断：本仓库用 coding agent 真的写了一支 HTML 广告并**渲染成了可投放的 MP4**
（`output/ecommerce-ad-1080x1920.mp4`，1080×1920 / 30fps / 15s / H.264），你可以直接播放核验。

---

## 1. 为什么这个问题值得认真做

电商投放团队每天要产**大量**短视频：同一商品 N 个卖点切片、N 个价格/赠品版本、N 种语言、N 个达人话术。
两条技术路线在抢这件事：

- **路线 A｜代码直出**：coding agent（如 Claude Code）写 HTML/CSS/JS（或 React + Remotion 这类框架），
  用无头浏览器逐帧截图 + ffmpeg 编码成 MP4。本质是"把视频生产变成软件工程"。
- **路线 B｜图生视频 agent 工作流**：把产品图/脚本喂给 Sora / Veo / Kling / Runway / 即梦(Seedance) 这类
  生成模型，由 agent 编排 prompt、reroll、拼接、配音。

谁更适合"专业电商经营 + 投广告"的短视频？这份报告给出**可复现**的答案。

---

## 2. 本次"真实测试"做了什么（路线 A 的实测产物）

我没有停留在讨论，而是端到端跑通了路线 A：

1. **coding agent 写代码**：一个自包含的 `scenes/ecommerce-ad.html`——六段分镜、确定性时间线、
   纯代码渲染的精华瓶（无任何外部图片依赖）、Noto Sans SC 中文排版、暖橙金高级调性。
2. **确定性渲染管线**：`render.mjs` 用 Puppeteer 无头 Chrome，把动画**按帧号**驱动
   （`window.seek(frame)`，不依赖墙钟时间），逐帧截图，再用 `ffmpeg`(libx264) 编码。
3. **真实产出**：

| 产物 | 规格 |
| --- | --- |
| `output/ecommerce-ad-1080x1920.mp4` | 1080×1920，30fps，15.00s，H.264 High/yuv420p，约 3.2MB |
| `output/ecommerce-ad-1080x1920-with-audio.mp4` | 同上 + 程序化背景乐床（scratch，可替换） |
| `output/ecommerce-ad-1080x1920-poster.jpg` | 自动导出的封面帧 |

**实测要点（可核验）**：
- 渲染耗时：450 帧捕获约 **418 秒**（本容器、单线程、无 GPU），再 ffmpeg 编码数秒；
  即"一次成片 ≈ 7 分钟、0 API 费用"。
- 文字/价格/品牌信息：`¥199→¥149`、`+30%`、`4.9`、`12,000+`、`20% 高浓度VC` 等**全部像素级精确**，
  因为画面里的字就是代码里你打的字——**不存在"AI 把字写糊/写错"的可能**。
- 可复现性：同一份 HTML 渲染两次，逐帧 bit 级一致。改一个价格 = 改一行 = 重渲染即更新。
- 中文与 emoji：容器内用 Noto Sans SC（已随项目自带子集字体）+ Noto Color Emoji，渲染清晰无豆腐块。

> 这一节的所有结论都来自**真实运行**，不是预期。封面与逐帧可在 `output/` 与交互报告 `report.html` 里看到。

---

## 3. 路线 A 的工程范式（为什么它对电商特别合适）

- **声明式 + 数据驱动**：视频 = 模板(HTML/组件) + 数据(JSON)。把商品名/价格/卖点抽成参数，
  一套模板批量出千条变体——这正是 Remotion 在 2026 年被规模化用于广告生产的核心理由：
  "把视频生产从手工剪辑变成可扩展的软件工程"，并可用 Remotion Lambda 在云上**大规模并行渲染** [1][2]。
- **像素级可控**：排版、动效曲线、安全区、品牌色、首帧 3 秒钩子，全部精确到帧到像素。
- **确定性/可审计**：每一帧是帧号的纯函数 → 可复现、可 diff、可回归测试、合规可审计。
- **零素材幻觉**：产品图就是你上传的真图（或本例的纯代码绘制），不会被模型"脑补"变形。
- **上限**：纯 CSS/DOM **做不出**实拍真人、真实光影物理、电影感 b-roll——这是范式天花板。

---

## 4. 路线 B 现状：图生视频 2026（基于公开资料）

到 2026 年中，图生视频已是成熟工具层，第一梯队大致是
**Google Veo 3.1、快手 Kling 3.0、OpenAI Sora 2、字节 Seedance 2.0、Runway Gen-4.5** [3][4][5]：

- **时长**：原生 8–20 秒（Seedance 2.0 约 15–20s、Sora 2 约 12–20s），Veo 用"场景延展"可串到 60s+ [3]。
- **价格**：约 **$0.10–0.75/秒**（Kling≈$0.10、Veo fast≈$0.15、Sora 2≈$0.75）[3]，且不含 reroll/QA 成本。
- **原生音频**：头部模型（Veo 3.1 / Kling 3.0 / Sora 2 / Seedance 2.0）已普遍支持原生音画同步 [3][6]。
- **电商适配**：2026 年"图生视频"已**超过**"文生视频"成为电商首选，因为它能保住真实产品的视觉完整性；
  新一代用"空间一致性"算法减少产品在动画中变形 [4]。
- **仍存硬伤**：
  - **文字渲染**：长期痛点是把品牌字/价格/招牌生成得糊或乱；Kling 3.0 主打"原生文字渲染"号称可清晰
    生成 logo/字幕，但 Runway Gen-4、Kling 2.0 等仍会在 2–3 秒内出现文字退化 [7]。
  - **一致性/物理/手部**：产品跨镜一致性、物理合理性、手部仍是公认短板 [4]。
  - **可控性是"抽卡"**：靠 prompt/motion brush/参考图逼近，但**不是**像素级精确，需多次 reroll。

> 重要诚实声明：本容器**没有** AI 视频 API 密钥、且出网受白名单限制，**未在本地实跑 B 组**。
> B 组的能力与分数来自上方公开资料 + 范式特性判断。把它变成"完全实测对比"的方法见第 6 节。

---

## 5. 对比结论（来自 `comparison-scorecard.md`）

用同一份 brief、同一把 10 维评分卡（1–5 分）打分，按**用途**换权重，结论会翻转：

| 用途 | HTML/代码 | 图生视频 AI | 谁赢 |
| --- | ---: | ---: | --- |
| 带货/转化信息流广告（重准确·可控·成本·规模） | **4.34** | 3.29 | **代码路线** |
| 品牌故事/实拍质感 TVC（重真实感·情绪·原生音画） | 3.68 | **3.76** | **图生视频** |

**为什么 performance 广告里代码路线赢**：转化广告的命门是"信息层零错误 + 可大批量 + 边际成本趋零"。
价格写错一个数、赠品规则糊一帧，投放就是事故；而代码路线在这几维直接拿满分，AI 在文字/可控/可复现上结构性吃亏。

**为什么品牌片里图生视频赢**：当 KPI 变成"像真的拍出来的质感、情绪、镜头语言"，真实感权重压倒一切，
纯 CSS 的天花板就暴露了。

**真正的最优解是混合工作流**（见第 7 节）。

---

## 6. 如何把它跑成"完全实测对比"（复现步骤）

A 组（本仓库已能一键复现）：

```bash
cd research/coding-agent-html-video/pipeline
npm install                 # 装 puppeteer + ffmpeg-static（Chrome 由 puppeteer 自动下载）
npm run render:ad           # 渲染 -> ../output/ecommerce-ad-1080x1920.mp4
# 想快速看分镜关键帧：
node preview.mjs scenes/ecommerce-ad.html "1.2,3.6,6.5,9.8,11.9,14.2"
```

B 组（你来跑，得到对称数据）：
1. 打开 `assets/shared-brief.md`，把第 5 节"prompt 包"整段贴给你的图生视频 agent/工具。
2. 产出成片后，用 `report/comparison-scorecard.md` 的 **C 客观指标表**逐格回填。
3. 两组用**同一张评分卡**打分，即得到你自己环境下的对称结论。

> 这样设计的意义：A 组是已落地的真产物，B 组给出**对称、可复现**的测试协议——
> 任何人都能在自己有 API 的环境里补齐 B 组，得到口径一致的对比，而不是各说各话。

---

## 7. 推荐：生产级混合工作流（coding agent 当"导演 + 合成层"）

把两条路线的长处叠起来，是 2026 年最务实的电商视频产线：

1. **AI 生成"难拍的料"**：用图生视频产出实拍质感的 b-roll、模特上脸、质地特写、氛围镜头。
2. **coding agent 当合成与信息层**：用 HTML/CSS/JS（或 Remotion）把这些片段 + 真实产品图 + **逐字准确的
   价格/卖点/CTA/字幕/品牌包装** 合成为成片——信息层绝不交给生成模型去"写字"。
3. **数据驱动批量**：把价格、赠品、语言、达人话术抽成参数表，一套模板批量渲染千条变体（A/B/多 SKU/多地区）。
4. **确定性收尾**：所有合成与字幕在代码侧完成 → 可复现、可审计、可回归，投放零事故。

一句话：**让 AI 负责"像真的"，让代码负责"准且多"。**

---

## 8. 局限与边界（诚实）

- 本容器无 GPU、单线程，450 帧渲染≈7 分钟；生产中用 GPU/并行/Lambda 会快很多。
- 纯 CSS 绘制的精华瓶是"高级矢量风"，不是实拍照片级；真实电商里通常**合成真实产品图**，质感更高。
- 背景音乐是程序化 scratch 床，仅作占位；正式投放应替换授权音乐或平台热门音轨。
- B 组未实跑（见第 4 节声明）；模型版本/价格变动很快，第 4 节数据请在采购前再核。
- 评分权重应按你自己的投放结构调整，结论会随之移动——这正是评分卡设计成"可调权重"的原因。

---

## 参考文献

- [1] Remotion 官网 — Make videos programmatically. https://www.remotion.dev/
- [2] "Remotion (2026): The React Framework for Programmatic Video", toolworthy.ai. https://www.toolworthy.ai/tool/remotion
- [3] "Best AI Video Models 2026 — VEO vs Kling vs Sora vs Seedance", vexub. https://vexub.com/blog/best-ai-video-models-2026-comparison
- [4] "Best AI Video Generator for E-Commerce Ads (2026 Guide)", digen.ai. https://resource.digen.ai/ai-video-generator-for-ecommerce-ads-2026/
- [5] "AI Video Generation 2026: Sora 2 vs Veo 3.1 vs Kling 3.0", lushbinary. https://lushbinary.com/blog/ai-video-generation-sora-veo-kling-seedance-comparison/
- [6] "Best AI Video Generators 2026: Veo 3.1, Kling, Sora 2, Seedance & More", AI/ML API Blog. https://aimlapi.com/blog/best-ai-video-generators-2026-veo-3-1-kling-sora-2-seedance-more-compared
- [7] "How to Choose the Best AI Video Generator of 2026", Kling AI blog. https://kling.ai/blog/best-ai-video-generator-2026-kling-ai

> 注：[3]–[7] 为 2026 年公开评测/厂商资料，用于校准路线 B 现状；模型迭代极快，数字以采购日实测为准。
