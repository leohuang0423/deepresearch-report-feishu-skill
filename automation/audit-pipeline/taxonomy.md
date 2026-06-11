# Agent 失败模式分类法 v1(12 类)

私有资产:每个 engagement 结束后回写新模式/新例证。分类 ID 与 `cluster_failures.py` 中的枚举一一对应。

| ID | 名称 | 定义 | 典型证据 |
|---|---|---|---|
| `hallucination` | 事实捏造 | 陈述不存在的事实/政策/价格/功能 | 与知识库或产品事实冲突的断言 |
| `lost_context` | 上下文丢失 | 忘记用户已提供的信息,重复提问 | "我刚才已经说过了" |
| `wrong_tool_call` | 工具误用 | 调错工具、参数错误、该调不调 | 查询参数与用户意图不符 |
| `retrieval_miss` | 检索失败 | RAG 召回不相关/过期文档,或答案在库中却没召回 | "根据文档…"后内容驴唇不对马嘴 |
| `instruction_violation` | 指令违背 | 违反 system prompt 中的明确规则(语气/范围/禁区) | 越权承诺退款、讨论禁区话题 |
| `dead_end_loop` | 死循环/死胡同 | 重复同样的回答或反复要求换措辞 | 同一回复连续出现 ≥2 次 |
| `premature_handoff` | 过早转人工 | 能力范围内的问题直接甩给人工 | 简单 FAQ 触发 escalation |
| `missed_handoff` | 该转不转 | 用户明确要求人工/情绪升级仍不转 | "let me talk to a human" 后继续机答 |
| `format_failure` | 格式/渲染失败 | 输出截断、markdown 泄漏、JSON 暴露给用户 | 用户看到 `{"tool":...}` |
| `over_refusal` | 过度拒答 | 把正常请求误判为违规而拒绝 | 合理问题被"I can't help with that" |
| `verbosity_mismatch` | 冗长/敷衍 | 回答长度与场景严重不匹配 | 一句话问题得到 500 词论文 |
| `language_tone` | 语言/语气失配 | 答错语言、语气与品牌冲突 | 用户用西语提问得到英语回答 |

严重度定义(打分用):
- **S1 营收级**:导致用户流失/错误承诺/合规风险
- **S2 信任级**:用户明显沮丧、重试或贬损产品
- **S3 体验级**:可察觉但用户自行恢复
