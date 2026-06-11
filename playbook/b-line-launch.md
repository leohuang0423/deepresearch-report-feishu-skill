# B 线启动手册:ThermaShell 验证与预售

> 角色定位:**验证方法论的实验线**,验证期不背营收 KPI。形态是"TikTok 自然流 → 预售页 → 批量履约",不投广告、不单件直发。

## 阶段 1:素材与账号(样品到手即开始,4-6 周)

**TikTok 账号**:垂直人设"pickleball gear nerd",不是品牌号。前 10 条不带任何链接,先攒人群标签。

**内容支柱(每周 2-3 条,A4 调研验证过的痛点叙事):**
1. **测温实拍**(核心):红外测温枪拍仪表台/后备箱 160°F+ → "this is what's killing your paddle"
2. **科普恐吓**:球拍分层(delamination)特写、品牌保修条款里的"heat damage not covered"截图
3. **解决方案对比**:无隔热软套 vs 硬壳 vs ThermaShell 样品的内外温差测试
4. **透明造物**:1688 打样过程、改版细节("v2 加了挂扣因为评论区说要挂球包上")

**评论区运营**:所有问"where to buy"的回复统一引导主页链接(等候名单页)。

## 阶段 2:等候名单(预售页发布前)

- Shopify 建一个简单页面 + Klaviyo 表单:"Batch #1 drops soon — first 50 get launch price $27.99"
- 门槛(playbook/README.md 决策门):**任一视频 ≥10k 播放,或累计 500 访问 + 100 邮件**→ 发布预售页
- 没过门槛:不发布,换 `research/raw/A4` 榜单下一个候选(高尔夫护网),素材方法论复用

## 阶段 3:预售(14 天)

1. 把 `thermashell-paddle-sleeve` 商品从 draft 改 active,模板确认为 `product.preorder`,**ship-by 日期按 `automation/fulfillment/cj-presale-sop.md` 公式倒推后填入**
2. 等候名单邮件 3 连发:开售日 / 第 7 天("一半名额没了"只在真实时才说)/ 截单前 48h
3. TikTok 同步:开售视频置顶,评论区挂链接
4. 每日检查 PayPal:预售模式下盯防资金冻结信号(发货前别动用预售款,留全额退款能力)

## 阶段 4:履约与复盘

- 按 `cj-presale-sop.md` 阶段 2-3 执行
- 批次复盘进 `data/batch-log.csv`:实际 COGS、头程、税费、纠纷数、净贡献
- **决策**:净贡献/单 ≥$12 且纠纷 0 → 第 2 批转 CJ 美仓常备库存 + 开 TikTok 联盟(10% 佣金 + 纳米创作者寄样);否则砍线,方法论沉淀进 mining-pipeline 的下一轮

## 红线

- ship-by 日期一旦可能失守:**当天**邮件全员给退款选项(FTC 强制,也是纠纷率保险)
- 纠纷率 >0.9% 或 PayPal 出现资金审查:立即停售,先清存量订单
- 单批投入(货+头程)上限 $500,验证期总投入上限 $1,500
