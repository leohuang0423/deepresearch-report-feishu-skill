# 小红书「猫砂垫避坑测评」攻略视频 · 选品 + 脚本 + 成片

一条龙：**研究选品 → 1688 选品规格 → 真实痛点 → 2-3 分钟小红书视频成片 → 发布套件**。
视频刻意做成"避坑测评"形态：精准人群/场景、独特攻略 + 真实体验、带挂载素材、不假不硬广。

## TL;DR

- **选品**：猫砂垫（养猫人/铲屎官，开放盆+玄关+木地板+小户型场景）——理由见 `RESEARCH.md`。
- **成片**：`output/xhs-cat-litter-mat.mp4`（1080×1440 / 3:4 / 24fps / **2:34** / H.264 + 轻量 BGM）。
- **结构**：钩子 → 精准人群 → 结论(4指标) → 4个误区 → 我的用法 → 1688选品参数 → 选垫公式 → 挂素材。
- **发布套件**：标题/正文/话题/挂载素材/封面建议，全在 `RESEARCH.md` 第 5 节，可直接复制发布。

## 目录

```
xiaohongshu-guide-video/
├─ README.md                              本文件
├─ RESEARCH.md                            选品研究 + 1688 选品规格 + 发布套件 + 质量自检
├─ output/
│  ├─ xhs-cat-litter-mat.mp4              成片（含字幕 + BGM）
│  └─ xhs-cat-litter-mat-poster.jpg       封面帧（信息型封面，可直接做小红书封面）
└─ pipeline/
   ├─ render.mjs                          并行确定性渲染器（多 worker + ffmpeg）
   ├─ preview.mjs                         抽取关键帧 QA
   ├─ scenes/xhs-cat-litter-mat.html      视频源（15段时间线 + 字幕 + 线描图，数据驱动）
   └─ lib/fonts/                          自带 Noto Sans SC 子集
```

## 复现

```bash
cd pipeline
npm install
./make-bgm.sh          # 生成轻量背景乐 .bgm.wav（可选；不要可去掉下面 --music）
node render.mjs --scene scenes/xhs-cat-litter-mat.html --out ../output/xhs-cat-litter-mat.mp4 \
  --width 1080 --height 1440 --fps 24 --workers 4 --jpeg --music .bgm.wav
# 仅看关键帧：
node preview.mjs "4,26,40,86,120,152"
```

> 渲染很快：4 个并行 worker 约 90 秒抓完 ~3700 帧，再 ffmpeg 编码即出片。

## 把真实 1688 素材替换进去（重要）

本视频用代码渲染的"测评示意图"呈现，因为运行环境出网受白名单限制、**无法抓取 1688 真实商品图/视频**
（1688/alicdn/小红书域名均返回 403）。管线是**数据驱动**的，替换很简单：

1. 在可联网环境按 `RESEARCH.md` 第 4 节参数到 1688 选定货，下载真实产品图/短视频到 `pipeline/assets/`。
2. 在 `scenes/xhs-cat-litter-mat.html` 的对应分镜里，把线描 `ART` 占位换成 `<img src="../assets/你的图.jpg">`
   （或把真实短视频片段用 ffmpeg 插入对应时间段）。
3. 重新 `node render.mjs ...` 即可——文字/字幕/时间轴/排版全部保持不变。

这样既保证了"现在就有一支可发的成片"，又保留了"随时换成真实 1688 素材"的能力。

## 质量自检

逐条对照目标的自检清单见 `RESEARCH.md` 第 7 节（人群/场景、独特攻略、真实体验、挂素材、去营销感、时长等均已核验）。
诚实边界：1688 真实图文/视频素材因出网封锁未接入，已用可替换的代码示意替代。
