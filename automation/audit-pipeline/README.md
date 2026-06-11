# Audit Pipeline — A 线交付半自动化

把客户的对话日志变成交付物(失败模式图谱 + 客户报告初稿),覆盖 Audit Sprint 交付 SOP(`playbook/a-line-delivery-sop.md`)中 60-80% 的机械工作。Mini Diagnostic($499)几乎全程走这条流水线。

```
客户导出 (JSONL/CSV)
  → ingest.py            # 归一化为 conversations.jsonl
  → cluster_failures.py  # Claude 按 12 类失败分类法逐对话诊断 + 聚合
  → gen_report.py        # 生成客户报告初稿 (markdown → 人工润色 → PDF)
```

## 用法

```bash
export ANTHROPIC_API_KEY=sk-ant-...
pip install -r ../../mining-pipeline/requirements.txt   # 同一套依赖 (anthropic, pydantic)

python ingest.py raw_export.csv -o data/conversations.jsonl
python cluster_failures.py data/conversations.jsonl -o data/failures.json
python gen_report.py data/failures.json --client "Acme Inc" -o data/report.md
```

成本参考:500 条对话 ≈ $20-40 token(Mini Diagnostic);2,000 条 ≈ $80-150(Sprint)。

## 输入格式

- **JSONL**:每行 `{"conversation_id": "...", "messages": [{"role": "user|assistant", "content": "..."}]}`,
  或常见平台导出(Intercom/OpenAI threads)——`ingest.py` 会尽力识别 `role`/`content` 字段。
- **CSV**:列 `conversation_id, role, content`(按时间排序)。

## 注意

- 分类法在 `taxonomy.md`——这是私有资产,每单交付后把新发现的失败模式回写进去(复利)。
- 客户数据放 `data/`(已 gitignore),交付后 30 天删除(隐私政策承诺)。
- `gen_report.py` 产出的是**初稿**:Top-3 修复建议必须人工验证后再交付,报告中的占位段落(`[REVIEW]` 标记)逐条处理。
