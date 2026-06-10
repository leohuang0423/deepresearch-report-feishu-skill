# A5 — Shopify Implementation Facts for a Solo Technical Founder (2026) + Unit-Economics Benchmarks

Research date: 2026-06-10. Sources searched via live web; each claim carries a source URL, source date (where determinable), and confidence rating (high / medium / low). "High" = official docs or multiple independent corroborating sources; "medium" = single reputable third-party source; "low" = single blog/secondary source or directional estimate.

---

## 1. Shopify Plans & Costs (2026)

### 1.1 Monthly pricing

| Plan | Monthly (month-to-month) | Monthly (annual billing) | Online card rate (Shopify Payments) |
|---|---|---|---|
| Starter | $5/mo | — | ~5% (social/link selling only) |
| Basic | $39/mo | $29/mo | 2.9% + $0.30 |
| Grow | $105/mo | $79/mo | 2.7% + $0.30 (≈$3.00 on $100) |
| Advanced | $399/mo | $299/mo | 2.5% + $0.30 (≈$2.80 on $100) |
| Plus | from ~$2,300/mo | (3-yr term) | negotiated |

- Five US plans in 2026: Starter $5, Basic $39, Grow $105, Advanced $399, Plus from ~$2,300/mo. Annual billing gives ~25% off Basic/Grow/Advanced (Basic $29, Grow $79, Advanced $299). Sources: https://costbench.com/software/ecommerce/shopify/ , https://www.demandsage.com/shopify-pricing/ , https://www.charleagency.com/articles/shopify-pricing/ (all 2026). **Confidence: high** (multiple 2026 sources agree; minor variance in some listings showing Basic $49/Grow $135 likely reflects regional pricing or month-to-month vs. promotional differences — verify on shopify.com/pricing at signup).
- Basic plan with Shopify Payments: 2.9% + 30¢ per online transaction (a $100 sale costs $3.20); Grow ≈ $3.00; Advanced ≈ $2.80 per $100. Source: https://costbench.com/software/ecommerce/shopify/ (2026). **Confidence: high**.

### 1.2 Third-party gateway penalty fee

- If you do NOT use Shopify Payments, Shopify adds a surcharge of **0.2%–2.0% per transaction** on top of your gateway's own fees (commonly cited: 2% Basic, 1% Grow, 0.6% Advanced). Sources: https://commerce-ui.com/insights/shopify-pricing , https://www.websitebuilderexpert.com/ecommerce-website-builders/shopify-pricing/ (2026). **Confidence: high**. This penalty matters a lot for a founder who can't use Shopify Payments (see below) — budget ~2% extra on Basic.

### 1.3 Shopify Payments availability — can a China-based founder use it?

- **No — mainland China is not a supported country for Shopify Payments.** The 2026 supported list (~39 countries) includes the US, UK, EU/EEA states, Australia, Canada, Japan, Mexico, New Zealand, Norway, Switzerland — and notably **Hong Kong and Singapore**, but not mainland China. Sources: https://help.shopify.com/en/manual/payments/shopify-payments/supported-countries (official, current; page returned 403 to automated fetch but list corroborated by) https://www.letstalkshop.com/blog/shopify-payment-gateways-comparison-by-country (2026), https://www.digismoothie.com/blog/shopify-payments-11-new-countries . **Confidence: high** for mainland-China exclusion; **medium** on the exact 39-country count.
- Eligibility is tied to where your **business entity and bank account** are registered, not citizenship. A China-based founder with a **US LLC + EIN + US bank account + US address** can register the store to the US entity and use Shopify Payments (this is the standard workaround). Sources: https://globallinkconsulting.sg/en/article/payment-solution/set-up-shopify-payments (2026), https://mazinooyolo.com/blog/how-to-use-stripe-in-unsupported-countries/ (2026). **Confidence: medium-high** (widely documented practice; Shopify/Stripe KYC may still ask for beneficial-owner ID — a foreign passport is accepted for the UBO).
- In countries where Shopify Payments IS available, you generally **cannot connect a separate Stripe account** (Shopify Payments is itself powered by Stripe). Where it isn't available, third-party gateways (PayPal, 2Checkout, Authorize.net, regional gateways) are the route. Source: https://statrys.com/blog/shopify-payment-gateways (2026), https://help.shopify.com/en/manual/payments/third-party-providers/payment-gateway-availability . **Confidence: high**.

### 1.4 Alternatives for a China-based founder

- **Stripe direct: not possible from mainland China.** Stripe does not offer merchant accounts in mainland China due to regulatory restrictions (Stripe supports ~46 countries in 2026). Sources: https://stripe.com/global , https://crolytics.ai/stripe-in-asia-in-2026/ , https://dodopayments.com/blogs/stripe-supported-countries-alternatives (2026). **Confidence: high**.
- **Stripe via US LLC**: form a US LLC, get an EIN, US address, US phone, and US bank account, then open Stripe under the US entity. This is the documented standard path for founders in unsupported countries. Source: https://mazinooyolo.com/blog/how-to-use-stripe-in-unsupported-countries/ (2026), https://rapidr.io/blog/stripe-atlas/ . **Confidence: high**.
- **PayPal China (PPCN)**: PayPal operates a licensed China cross-border payments service; a China-resident can open a business account with government ID + Chinese bank account. Cross-border receiving fees are high: ~4.4% + fixed fee on international transactions (vs 2.99% + fixed domestic US), plus 0–2% cross-border surcharge and currency-conversion spread. Sources: https://www.doola.com/paypal-guide/how-to-open-a-paypal-account-in-china/ (2026), https://www.paypal.com/c2/business/paypal-business-fees , https://wise.com/us/blog/paypal-cross-border-fee . **Confidence: medium-high**. Practical note: a PayPal-only Shopify checkout converts worse than card checkout (directional, widely reported) — **low confidence** on magnitude.

### 1.5 US LLC + EIN formation costs for non-residents (2026)

- **Stripe Atlas: $500 one-time** (Delaware LLC or C-corp), includes state filing fees, EIN handling, first-year registered agent; **$100/yr registered-agent renewal** thereafter; includes $2,500 in Stripe credits and partner perks. Sources: https://stripe.com/atlas (official), https://sparklaun.ch/compare/stripe-atlas (2026), https://support.stripe.com/questions/stripe-atlas . **Confidence: high**.
- **Firstbase: $399 formation**, positioned for non-US founders (EIN without SSN, US business address product, banking intros, Form 5472 support); optional tax-filing package ~$899/yr. Sources: https://www.firstbase.io/pricing , https://www.globalsolo.global/blog/stripe-atlas-vs-firstbase-vs-doola-pricing-comparison-2026 (2026). **Confidence: medium-high** (third-party comparison + vendor page).
- **3-year all-in cost estimates**: Stripe Atlas ≈ $3,100–4,600 incl. external CPA; Firstbase ≈ $3,276 incl. tax filing. Source: https://www.globalsolo.global/blog/stripe-atlas-vs-firstbase-vs-doola-pricing-comparison-2026 (2026). **Confidence: medium** (single comparison site; real cost depends on CPA choice and state).
- **EIN timing for foreign-owned LLC**: typically issued within ~10 days of submitting signed forms via these services (without an SSN it goes by fax/mail to IRS — can stretch to several weeks in busy periods). Source: https://www.firstbase.io/guide/important-details-for-owners-of-a-us-company . **Confidence: medium**.
- **Ongoing compliance to budget**: foreign-owned single-member LLC must file IRS Form 5472 + pro-forma 1120 annually (penalty for non-filing is $25,000), plus Delaware franchise tax (~$300/yr for LLC) and registered agent (~$100/yr). Sources: https://www.firstbase.io/guide/important-details-for-owners-of-a-us-company , https://ecommerceparadise.com/best-llc-services-for-non-us-residents-in-2026-form-your-us-business-from-anywhere/ (2026). **Confidence: medium-high**.

---

## 2. Selling Digital Products & Services on Shopify

- **Native support exists**: Shopify supports digital/service products by marking the product as not requiring shipping. Official path: product page → Shipping section → deactivate "Physical product" / enable "Not a physical product" → Save. No shipping is charged or requested at checkout. Source: https://help.shopify.com/en/manual/products/digital-service-product/selling-services-or-digital-products (official). **Confidence: high**.
- **Digital Downloads app (free, first-party)**: upload files (up to 5 GB each) and attach them to products/variants; buyers get a download link by email and on the order status page; supports download limits and manual re-sends. Sources: https://apps.shopify.com/digital-downloads , https://help.shopify.com/en/manual/products/digital-service-product/digital-downloads (official). **Confidence: high**.
- **Stronger third-party alternatives** (if you need streaming, license keys, PDF stamping, unlimited bandwidth): Fileflare (https://apps.shopify.com/digital-assets), Sky Pilot, ByteBox, Sellkite — all on the App Store; most have free tiers and paid plans roughly $10–30/mo. Source: Shopify App Store listings above (2025-2026). **Confidence: medium** (pricing tiers change frequently).
- **Concrete setup path (validated against official docs)**: (1) create product; (2) uncheck "This is a physical product"; (3) install Digital Downloads, attach file to the variant; (4) in Checkout settings, no shipping address will be collected for carts of only non-physical items; (5) for taxes on digital goods, enable digital-goods VAT collection if selling to EU. **Confidence: high** for steps 1–4 (official docs), **medium** for tax step specifics.
- **Subscriptions**: Shopify has a free first-party **Shopify Subscriptions** app (basic recurring billing on Shopify Checkout); third-party apps built on the official Subscriptions API: **Seal Subscriptions** (free up to 150 subscribers, paid from $5.95/mo, no transaction fees), **Appstle** (from $10/mo, 0% transaction fees), **Recharge** (from $99/mo + 1.25% + $0.19/txn — overkill for a solo founder at start). Sources: https://www.getonecart.com/shopify-subscription-apps/ (2026), https://apps.shopify.com/subscriptions-by-appstle , https://www.recurpay.com/subscription-apps-for-shopify (2026). **Confidence: medium-high**. Note: subscriptions require Shopify Checkout + a supported payment gateway (Shopify Payments or PayPal Express; many third-party gateways don't support recurring) — another reason the US-LLC/Shopify Payments route matters. **Confidence: medium**.

---

## 3. Shopify Theme Development Toolchain (2026)

- **Horizon replaced Dawn as the default theme** for new stores, launched May 2025 at Shopify Editions Summer '25. Sources: https://blog.devmoek.com/horizon-replaces-dawn-as-the-new-default-theme-in-shopify/ (2025), https://ed.codes/blog/shopify-horizon-theme-and-blocks (2025), https://themes.shopify.com/themes/horizon/presets/horizon . **Confidence: high**.
- **Horizon framework = Theme Blocks**: nested, reusable blocks (up to 8 levels) that can be placed anywhere, replacing Dawn/OS 2.0's flatter section-based model; includes AI block generation via Shopify Magic. A family of 10 free Horizon-framework themes shipped (Horizon, Ritual, Atelier, Fabric, Tinker, Savor, Heritage, Dwell, Pitch, Vessel). Sources: https://ed.codes/blog/shopify-horizon-theme-and-blocks , https://bsscommerce.com/shopify/shopify-horizon-theme-review/ (2025). **Confidence: high**.
- **Dawn + Online Store 2.0 JSON templates remain fully supported** — OS 2.0 JSON templates/sections are still the architecture for Dawn-derived themes, and Dawn remains a valid, simpler base for custom dev; Horizon is recommended for new merchant-customizable builds. Sources: https://omnithemes.com/blog/theme-comparison/shopify-horizon-theme-vs-dawn/ (2025), https://shopify.dev/docs/storefronts/themes/tools/cli . **Confidence: high** for continued Dawn/OS2.0 support; **medium** on "which to pick" guidance (editorial).
- **Shopify CLI is the current canonical theme workflow** (Theme Kit is legacy): `shopify theme init`, `shopify theme dev` (local dev server with hot reload of CSS/sections against a development theme), `shopify theme push` / `pull`, `shopify theme check` (Theme Check linter is bundled in the CLI), `shopify theme publish/share/list`. Sources: https://shopify.dev/docs/api/shopify-cli/theme (official), https://shopify.dev/docs/storefronts/themes/tools/cli (official), https://www.practicalecommerce.com/set-up-a-shopify-theme-dev-environment-in-2025 (2025). **Confidence: high**.
- **2025 changes to know**: multi-environment theme commands — configure environments (store, theme ID, flags) in `shopify.theme.toml` at repo root and run `check/push/pull/publish/list/...` across several environments at once. Source: https://shopify.dev/changelog/multi-environment-theme-commands-shopify-cli (official changelog, 2025). **Confidence: high**.
- Practical solo-founder stack: VS Code + Shopify Liquid extension, GitHub integration for theme version control, `shopify theme dev --store=<store>` for live preview, Theme Check in CI. Source: https://www.codilar.com/shopify-theme-developer-cheatsheet-2025-edition/ (2025). **Confidence: medium** (editorial best practice).

---

## 4. Store Conversion / Unit-Economics Benchmarks (2025-2026 sources)

- **Average Shopify store conversion rate: ~1.4%–1.8%**; top ~20% of stores exceed ~3.2%; 2.5–3% is a strong target; 4%+ is excellent. Sources: https://redstagfulfillment.com/average-conversion-rate-for-shopify-stores/ (2026), https://blendcommerce.com/blogs/shopify/ecommerce-conversion-rate-benchmarks-2026 (2026), https://popupsmart.com/blog/shopify-conversion-rate-statistics (2025). **Confidence: medium-high** (consistent across sources, but none are Shopify-official; Shopify doesn't publish an official figure).
- **Conversion by category (2026 industry benchmarks)**: Food & Beverage 4.5–6.0%; Beauty & Cosmetics 3.0–4.0%; Apparel 2.0–3.0%; Luxury & Jewelry 0.8–1.2%. Source: https://convertibles.dev/blogs/optimization/increase-ecommerce-conversion-rate (2026). **Confidence: medium** (single aggregator).
- **Email capture (popup opt-in) rates**: standard discount popup 2–5% of visitors; gamified/spin-wheel popups 6–12% (2–3x lift). Source: https://popupsmart.com/blog/shopify-conversion-rate-statistics (2025). **Confidence: medium** (vendor data, popup vendor has incentive to flatter gamified numbers).
- **AOV benchmarks**: average ecommerce order value ≈ **$80–$120** across categories; an observed pattern in a 21-store dataset: every store converting above 4% had AOV under $80 (high conversion and high AOV trade off). Sources: https://www.dtcpages.com/blog/ecommerce-conversion-rate-benchmarks-2026 (2026), https://easyappsecom.com/guides/shopify-ecommerce-statistics (2026). **Confidence: medium** (small datasets; use as planning heuristic, not gospel).
- Planning math for a solo store: at 1.5% CVR, $90 AOV, you need ~740 sessions per $1,000 revenue; email list converting at 3–5% of visitors becomes the main owned channel. **Confidence: derived/low** (arithmetic on the medium-confidence benchmarks above).

---

## 5. Automation Stack for Hands-Off Operation

### 5.1 Fulfillment apps for China/1688 sourcing

- **DSers** (AliExpress official partner): free plan (3 stores, ~3,000 products, core automation); Advanced ~$19.90/mo; Pro ~$49.90/mo. Bulk/one-click AliExpress order placement is its core strength. AliExpress-centric — it does **not** natively source from 1688. Sources: https://ecommerce-platforms.com/articles/dsers-vs-zendrop (2026), https://www.autods.com/blog/dropshipping-tips-strategies/subscription-costs-comparison-autods-cjdropshipping-zendrop/ (2026). **Confidence: medium-high**.
- **CJdropshipping**: core service is **free** (you pay product + shipping only); optional memberships Plus $15.99/mo, Prime $19.99/mo, Advanced $59.99/mo (coupons, more sourcing requests, order priority). Sources: https://cjdropshipping.com/blogs/cj-news/Zendrop-or-CJdropshipping (2026), https://www.autods.com/blog/dropshipping-tips-strategies/subscription-costs-comparison-autods-cjdropshipping-zendrop/ . **Confidence: medium-high**.
- **How 1688 sourcing actually works through CJ**: you submit a **sourcing request** (paste a 1688/Taobao/Tmall URL via the CJ web app or Chrome extension); CJ's China team finds/quotes the supplier, typically responding in **24–48 hours** (longer in peak season); once quoted, the product is listed in your CJ account, connects to your Shopify store, and orders auto-route: customer orders → CJ buys from the 1688 supplier → CJ's warehouse QCs and ships internationally with tracking pushed back to Shopify. Sourcing is free; new users get 5 sourcing requests/day (scales to unlimited at higher levels). Sources: https://blog.cjdropshipping.com/detail/how-to-use-1688-com-or-taobao-com-for-drop-shipping-sourcing/ , https://cjdropshipping.com/article-details/8 , https://app.cjdropshipping.com/blog/post/the-easiest-way-ever-to-buy-source-from-aliexpress-1688-and-taobao-for-dropshipping/ (official CJ docs/blog). **Confidence: high** for mechanics (vendor-official), **medium** for response-time SLAs.
- **Zendrop**: free plan exists but auto-fulfillment, bulk import, branded invoicing sit behind paid tiers from **$29/mo** (Plus commonly $49/mo for full automation); differentiator is curated suppliers + US warehouses with 3–5-day domestic delivery. Sources: https://ecommerce-platforms.com/articles/dsers-vs-zendrop (2026), https://cjdropshipping.com/blogs/cj-news/Zendrop-or-CJdropshipping (2026 — note: competitor-authored, treat comparisons cautiously). **Confidence: medium**.
- Solo-founder takeaway: CJ is the only one of the three with first-party 1688/Taobao sourcing; DSers is cheapest for pure AliExpress; Zendrop buys US shipping speed. **Confidence: medium** (synthesis).

### 5.2 Customer-service AI

- **Shopify Inbox**: free, native; adequate under ~50 tickets/mo. Source: https://www.ringly.io/blog/shopify-customer-service (2026). **Confidence: medium**.
- **Tidio + Lyro AI**: free plan; paid from ~$29/mo; Lyro AI add-on $39–$289/mo by conversation volume; Lyro auto-answers order-tracking/shipping/product FAQs from your docs. Best value under ~500 tickets/mo. Sources: https://apps.shopify.com/tidio-chat , https://stormy.ai/blog/tidio-vs-gorgias-2026-shopify-ai-agent (2026). **Confidence: medium-high**.
- **Gorgias**: helpdesk plans $60–$750+/mo by ticket volume plus ~$0.90–$1.00 per AI-resolved ticket; automates ~60% of WISMO/WISMR-type inquiries; built for larger ecommerce teams — overkill at launch. Sources: https://www.hellorep.ai/blog/gorgias-pricing (2026), https://chatarmin.com/en/blog/gorgias-pricing (2026). **Confidence: medium-high**.

### 5.3 Email automation — Klaviyo free tier

- **Klaviyo free plan (2026): 250 active profiles, 500 email sends/month, 150 SMS credits/mo**; includes flows/automations, segmentation, drag-and-drop editor; sending halts when limits are exceeded until upgrade or next cycle. Paid: Email from $20/mo; Email+SMS from $35/mo (scales with profile count). Sources: https://www.klaviyo.com/pricing (official), https://help.klaviyo.com/hc/en-us/articles/360050759151 (official), https://www.omnisend.com/blog/klaviyo-pricing/ (2026). **Confidence: high**.
- Practical note: 250 profiles is exhausted fast with a 3–5% capture rate (~5–8k visitors); budget the $20/mo tier within the first months. **Confidence: derived**.

---

## 6. TikTok Organic + TikTok Shop as Low-Budget Channel

### 6.1 TikTok Shop US eligibility for non-US founders (2026)

- **Hard requirement: a US-resident Primary Business Representative with a valid US government ID and verifiable US residential address.** A non-resident cannot serve as their own representative; the Ultimate Beneficial Owner (≥25% ownership) can be the foreign founder verified with a foreign passport, but the PBR must be a real US person. Sources: https://clemta.com/blog/how_to_start_tiktok_shop_us_non_resident/ (2026), https://flatfeecorp.com/articles/the-ultimate-guide-to-us-business-registration-for-non-residents-setting-up-a-tiktok-shop , https://ads.tiktok.com/help/article/requirements-to-register-as-a-seller-on-tiktok-shop (official). **Confidence: high** on the US-representative requirement; **medium** on exact UBO mechanics.
- Additional friction: TikTok Shop US requires a **Form W-9** (US taxpayer form) even though a foreign-owned single-member LLC is technically a W-8 filer — a documented compliance contradiction that traps many non-resident sellers; name on ID, bank account, and business registration must match exactly; INFORM Consumers Act verification applies. Sources: https://globalfy.com/blog/register-tiktok-shop-usa-as-international-seller/ (2026), https://seller-us.tiktok.com/university/essay?knowledge_id=1411491405465390&lang=en (official). **Confidence: medium-high**.
- Net assessment for a China-based solo founder: TikTok Shop US is **effectively closed without a trusted US partner or paid representation service** (which carries account-ban and tax risk). Driving TikTok **organic traffic to your own Shopify store** (link-in-bio) has no such residency gate. **Confidence: medium** (synthesis of above).

### 6.2 Affiliate / UGC model economics (if Shop access is solved, or via a US partner)

- Affiliate-first playbook: set an Open Plan commission (~10% to start, lowering toward 5% as GMV grows); creator commission of 10–15% implies an all-in affiliate cost-of-sale of ~18–23% before product costs. Sources: https://useclip.com/tiktok-shop-ugc-what-brands-need-to-know-in-2026 (2026), https://www.shortformnation.com/blog/social-commerce-trends-2026-what-s-actually-working-on-tiktok-shop-and-what-s-not (2026). **Confidence: medium**.
- Nano-creator seeding beats big sponsorships: seed samples ($5–10/sample to hundreds of creators); promote top performers (≥2–3% conversion) to retained affiliates ($200–500/mo + commission); cut creators below ~1.5% conversion. Reported program cost at scale: $6–8k/mo — but seeding can start at a few hundred dollars with 20–50 creators. Sources: https://tiksly.com/scale-tiktok-shop-ugc-guide/ (2026), https://www.kolsprite.com/blog/tiktok-creator-economy-2026 (2026). **Confidence: medium** (agency content; case-study numbers like "$100K/mo from 6 organic posts" are outliers — **low confidence** on such claims).
- UGC trust premium: consumers trust UGC ~2.4x more than brand content; UGC assets are reused across Spark Ads, product pages, and email. Source: https://influee.co/blog/tiktok-ugc (2026). **Confidence: medium** (survey-based, vendor-cited).

---

## 7. Bottom-Line Implications for the Venture

1. The **US LLC route ($399–500 one-time + ~$400–900/yr compliance)** unlocks the trifecta: Shopify Payments (saves the 2% third-party-gateway penalty), Stripe, and (with a US partner) TikTok Shop. Without it, the founder is limited to PayPal PPCN at ~4.4%+ fees and a degraded checkout. **Confidence: medium-high** (synthesis).
2. Digital products are trivially supported natively (free Digital Downloads app, untick "physical product"); subscriptions cheapest via Seal (free→$5.95/mo) but require Shopify Payments/PayPal Express for recurring billing. **Confidence: medium-high**.
3. Theme dev in 2026 = Shopify CLI (`theme dev/push/check`) + Git; build on Horizon (Theme Blocks) for merchant-editable stores or Dawn/OS2.0 for simplest custom code. **Confidence: high**.
4. Plan unit economics around 1.4–1.8% baseline CVR, $80–120 AOV, 3–5% email capture (6–12% gamified), Klaviyo free until ~250 profiles. **Confidence: medium**.
5. For physical goods sourced from 1688, **CJdropshipping (free, sourcing-request workflow)** is the only mainstream app with native 1688/Taobao sourcing; total automation stack can run ~$0–50/mo at launch (CJ free + Klaviyo free + Tidio free + Shopify Inbox). **Confidence: medium-high**.
