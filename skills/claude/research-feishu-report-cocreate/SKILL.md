---
name: research-feishu-report-cocreate
description: Contract-first topic-report cocreation for creator-first evidence gathering, non-consensus synthesis, reader-first reporting, structured dossiers, optional Feishu or HTML delivery, and local-only synthesis packets.
allowed-tools: Bash,Read,Write,Edit
---

# Research Feishu Report Cocreation

Use only for high-standard topic-sharing reports with explicit audience, decision value, and structured delivery.

Start with:

- `contracts/mode_policy.yaml`
- `contracts/gates.yaml`
- `references/workflow_v2.md`

If mode is `heavy_topic_report`, also load:

- `contracts/topic_report_brief.schema.yaml`
- `contracts/expert_panels.yaml`
- `contracts/rubric.yaml`
- `contracts/state_machine.yaml`
- `references/research_cocreate_rules.md`
- `references/creator_first_source_rules.md`
- `references/non_consensus_insight_rules.md`
- `references/reader_first_narrative_rules.md`
- `references/case_packet_rules.md`
- `references/report_visual_rules.md`
- `references/local_only_synthesis_rules.md`

Load on demand:

- `references/native_dossier_rules.md`
- `references/feishu_publish_qa_rules.md`
- `references/interactive_html_render_rules.md`
- `references/main_doc_review_rules.md`
- `references/eval_rules.md`

## Mandatory clarification loop

Before deep research, figure planning, or drafting:

- do one short framing pass
- sketch the initial plan
- scan the evidence boundary

Then ask the user `2-3 high-leverage clarification questions` and wait for confirmation.

Prioritize:

- audience
- ideal-state result standard; make it as specific, evaluable, measurable, and quantifiable as possible
- decision goal or quality bar
- scope, source boundary, delivery shape, and must-include constraints

The clarification loop must align on what "excellent" looks like for this report using concrete acceptance criteria, evaluation dimensions, thresholds, examples, or numeric targets whenever possible.

## Mode route

- `light`: use the four-stage skeleton only
- `mid`: expand one or two checkpoints
- `local_only_synthesis`: keep the contract, compress intermediate states into final artifacts, and stay explicit about bounded evidence
- `heavy_topic_report`: load contracts and follow the report-first path

Required heavy-mode panels:

- `ideal_state_panel`
- `evidence_panel`
- `acceptance_panel`

Required heavy-mode sequence:

- `brief`
- `research_question`
- `thesis_card`
- `evidence_map`
- `outline_freeze`
- `figure_plan`
- `draft`
- `review_panel`
- `acceptance_panel`

Required `local_only_synthesis` sequence:

- `brief`
- `research_question`
- `thesis_card`
- `compressed_evidence_map`
- `outline_freeze`
- `draft`
- `review_panel`

Required heavy-mode artifacts:

- `brief.yaml`
- `thesis_card.md`
- `evidence_map.md`
- `atomic_evidence.jsonl`
- `case_packets/`
- `figure_manifest.yaml`
- `render_manifest.yaml`
- `main_report.md`
- `appendix.md`
- `run_log.json`

Required `local_only_synthesis` artifacts:

- `brief.yaml`
- `main_report.md`
- `appendix.md`
- `run_log.json`

## Modules

- `topic_to_report`
- `creator_source_mining`
- `non_consensus_synthesis`
- `narrative_architecture`
- `case_packeting`
- `report_visuals`
- `local_only_synthesis`
- `native_dossier`
- `feishu_publish_qa`
- `interactive_html_report`

## Boundaries

- not a generic writing command
- not a generic research command
- not a replacement for user judgment
- not allowed to skip expert-panel checkpoints in heavy mode
- not allowed to continue into full research or drafting until `2-3 high-leverage clarification questions` have been asked after the initial first pass, unless the user already made them explicit
- not allowed to treat "good quality" as sufficient alignment; the ideal-state result standard must be frozen as specifically and measurably as the task allows
- not allowed to skip the brief-to-outline path before drafting
- not allowed to fake external validation or full publish assets in `local_only_synthesis`
- not allowed to let market conclusions borrow certainty from mechanism evidence
- not allowed to output a final report without appendix, creator-first evidence traceability, case packets, and explicit go / no-go thresholds
