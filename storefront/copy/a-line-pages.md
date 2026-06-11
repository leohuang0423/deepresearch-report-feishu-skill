# A 线页面文案(英文,对照填入 Theme Editor)

## /pages/ai-agent-audit(模板 page.audit)

Hero、流程、引流块文案已内置在 `theme/templates/page.audit.json` 默认值中,Theme Editor 里确认即可。唯一必填:**hero 的 CTA link 指向你的 Calendly 链接**。

### 补充 FAQ(用 Dawn collapsible-content section 追加在页尾)

**What do you need from us?**
Read access to your agent (API key or staging endpoint) and an export of 1,000+ recent conversations (JSONL or CSV). We sign an NDA first; data is deleted 30 days after the engagement.

**Which stacks do you cover?**
Any LLM-backed agent: customer support bots, internal copilots, voice agents, RAG assistants — built on OpenAI, Anthropic, LangChain/LangGraph, Voiceflow, Intercom Fin, or custom stacks.

**What does it cost?**
The Audit Sprint is a fixed **$4,500**. The Mini Diagnostic is **$499** and credits in full toward a sprint within 30 days. No hourly billing, no scope creep.

**What if you find nothing serious?**
Then you get documented proof your agent is healthy — and the regression eval suite so it stays that way. That hasn't happened yet.

**Who's behind this?**
A solo AI engineer who builds and evaluates LLM agents full-time. You work directly with the person doing the analysis — no account managers.

## Mini Diagnostic 商品页

商品描述已在 `products/products.csv` 内。下单后自动邮件(Settings → Notifications → Order confirmation 末尾追加):

> **Next step:** reply to this email with your conversation export (JSONL or CSV, ≥500 conversations). Need an NDA first? Just say so — we'll send ours within hours. Your report lands within 5 business days of receiving the data.

## 预约电话确认邮件(Calendly 自动发送)

> Before our call, if you can, reply with 3–5 example conversations where your agent disappointed you. We'll review at least one live on the call — you'll leave with something useful even if we never work together.
