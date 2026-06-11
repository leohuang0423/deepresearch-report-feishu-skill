# 从零到上线 SETUP(预计 1 个工作日)

前置:`playbook/setup-checklist.md` 中的账号/收款准备已完成(Shopify 试用账号、PayPal 企业账号)。

## 1. 开店与基础设置(~30 分钟)

1. shopify.com 注册 → 选 **Basic 年付($29/月)**;试用期内先不付费。
2. Settings → Store details:店名、美国市场、货币 USD、时区 America/New_York。
3. Settings → Payments:
   - 激活 **PayPal Express Checkout**(用 PayPal 中国企业账号登录授权)。
   - 不开 Shopify Payments(大陆主体不支持);知悉每单 0.2-2% 第三方网关附加费(Basic 档 2%)。
4. Settings → Checkout:开启邮箱必填、订单后营销勾选框。
5. Settings → Policies:粘贴 `copy/policies-faq.md` 中的 Refund / Shipping / Privacy / ToS 四段。

## 2. 应用安装(~15 分钟)

| 应用 | 用途 | 费用 |
|---|---|---|
| Digital Downloads(Shopify 官方) | Mini Diagnostic 交付 PDF 自动发送 | 免费 |
| Shopify Inbox | 客服聊天(<50 工单/月够用) | 免费 |
| Klaviyo | 邮件弹窗 + 等候名单(B 线) | 免费档起步,~$20/月 |
| CJdropshipping | B 线通过验证后再装(1688 寻源+履约) | 免费 |

## 3. 导入商品(~10 分钟)

1. Products → Import → 上传 `products/products.csv`。
2. 检查:`AI Agent Mini Diagnostic` 为 active、免发货;在 Digital Downloads 中为其挂载交付模板 PDF(首次可挂占位说明文件,实际交付走邮件)。
3. `AI Agent Audit Sprint` 与 `ThermaShell Paddle Sleeve` 保持 **draft**——分别在签下首单、通过 B 线验证门槛后发布。

## 4. 部署主题定制(~30 分钟)

```bash
npm install -g @shopify/cli@latest
shopify theme list --store your-store.myshopify.com      # 找到 Dawn 的 theme ID
shopify theme pull --store your-store.myshopify.com -t <ID> -d dawn-live
cp -r theme/sections/* dawn-live/sections/
cp -r theme/templates/* dawn-live/templates/
shopify theme check -d dawn-live                          # lint
shopify theme push --store your-store.myshopify.com -t <ID> -d dawn-live
```

然后在 Admin:
1. Online Store → Pages → 新建页面 `AI Agent Audit`,模板选 **page.audit**;正文留空(内容来自 sections),文案对照 `copy/a-line-pages.md` 在 Theme Editor 中填入 section 设置。
2. ThermaShell 商品 → Theme template 选 **product.preorder**;在 Theme Editor 中把 `preorder-banner` 的 **Ship-by date** 设为真实日期(FTC 强制,见 copy/b-line-presale.md 顶部警告)。
3. 首页:用 Theme Editor 按 `copy/homepage.md` 配置(Dawn 自带 image-banner + rich-text 即可,首页不需要自定义 section)。

## 5. 上线前检查清单

- [ ] 用 PayPal 沙箱/小额真实订单各走一遍 $499 下单 → 确认 Digital Downloads 邮件触发
- [ ] 预售页 ship-by 日期醒目可见(移动端也检查)
- [ ] 四项政策页可从 footer 访问
- [ ] Klaviyo 弹窗:10% off 首单(B 线)/ 免费样例报告(A 线),目标 opt-in ≥2-5%
- [ ] 移除密码页,绑定域名(~$12/年)
- [ ] Google Analytics / Meta Pixel 暂缓——B 线投流前再装,避免无效数据

## 6. 上线后

按 `playbook/` 各手册执行:A 线获客(`a-line-gtm.md`)→ 交付(`a-line-delivery-sop.md`);B 线验证(`b-line-launch.md`)。
