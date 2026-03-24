---
name: research-feishu-report-cocreate
description: Use for high-standard topic reports that need creator-first evidence, explicit audience and decision framing, non-consensus synthesis, structured dossiers, and optional Feishu or HTML delivery. Trigger when the user needs a deep report, build/no-build memo, high-rework-cost synthesis, a local-only method playbook, or a shareable research package rather than lightweight research or generic writing.
metadata:
  short-description: Topic report cocreation
  production-synthesis: true
  synthesized-from:
    - v16_round02
    - v16_round02_prod_visual_feishu
    - rb01_h08
    - rb02_h01
    - rb03_h06
    - rb03_h08
    - rb03_h15
---

# Research Feishu Report Cocreation

Use this skill only for one task class:

- high-standard topic-sharing report
- multiple evidence objects
- explicit audience and decision value
- high-rework-cost convergence
- optional dossier / Feishu / HTML delivery

It is not for:

- generic writing
- lightweight research
- automatic product judgment or thesis generation
- vague brainstorming without a report contract

## Trigger check

Use this skill only if at least three are true:

- the topic still needs to be clarified
- evidence comes from more than one source or case
- the target audience is explicit
- the output must help readers make a concrete judgment
- delivery quality matters
- rework cost is high

If any of these are missing, stop and ask before drafting:

- target audience
- decision the report should help with
- deliverable shape
- evidence boundary

## Mandatory clarification loop

Before deep research or drafting, do one short first pass:

- frame the task
- sketch the initial plan
- scan the obvious evidence boundary

Then ask the user `2-3 high-leverage clarification questions` and wait for confirmation.

Those questions must target the variables most likely to change the result. Prioritize:

- who the real audience is
- what ideal-state result standard the user will judge the work against; make this as specific, evaluable, measurable, and quantifiable as possible
- what decision, goal, or quality bar the report must serve
- what scope, source boundary, delivery shape, or must-include / must-exclude constraints apply

Do not ask a long laundry list. Ask only the smallest set of questions that can materially change the report.

The clarification loop must explicitly align on what "excellent" looks like for this report. Push for concrete acceptance criteria, evaluation dimensions, thresholds, examples, or numeric targets instead of vague style preferences.

If the user already gave all of this clearly, restate the frozen assumptions instead of asking again.

## Mode route

- `light`: use the four-stage skeleton only
- `mid`: expand one or two checkpoints
- `local_only_synthesis`: keep the contract, but compress intermediate states into the requested final artifacts and do not pretend to have external validation
- `heavy_topic_report`: load contracts and follow the report-first path

## Read first

- `contracts/mode_policy.yaml`
- `contracts/gates.yaml`
- `references/workflow_v2.md`

If mode is `heavy_topic_report`, also read:

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

Load these on demand:

- `references/native_dossier_rules.md`
- `references/feishu_publish_qa_rules.md`
- `references/interactive_html_render_rules.md`
- `references/main_doc_review_rules.md`
- `references/eval_rules.md`

## Required gates for heavy topic reports

- `brief_gate`
- `pre_research_gate`
- `pre_draft_gate`
- `post_draft_gate`
- `publish_gate`

Do not enter full draft or publish until the required gate passes.

Required heavy-mode panels:

- `ideal_state_panel`
- `evidence_panel`
- `acceptance_panel`

Mandatory execution path for heavy topic reports:

- `brief`
- `research_question`
- `thesis_card`
- `evidence_map`
- `outline_freeze`
- `figure_plan`
- `draft`
- `review_panel`
- `acceptance_panel`

Mandatory execution path for `local_only_synthesis`:

- `brief`
- `research_question`
- `thesis_card`
- `compressed_evidence_map`
- `outline_freeze`
- `draft`
- `review_panel`

Required artifacts for every heavy-topic-report run:

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

Required artifacts for every `local_only_synthesis` run:

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

Templates:

- `assets/topic_report_brief_template.yaml`
- `assets/thesis_card_template.md`
- `assets/evidence_map_template.md`
- `assets/figure_manifest_template.yaml`
- `assets/case_packet_template.yaml`
- `assets/render_manifest_template.yaml`
- `assets/report_structure_template.md`
- `assets/review_output_template.md`
- `assets/acceptance_scorecard_template.md`

## Non-negotiables

- Do not replace the user's product judgment.
- Do not continue into full research or drafting until you have asked `2-3 high-leverage clarification questions` after the initial first pass, unless the user already made those answers explicit.
- Do not treat "good quality" as sufficient alignment; freeze an ideal-state result standard that is as specific, evaluable, measurable, or quantifiable as the task allows.
- Do not skip `brief -> research_question -> thesis_card -> evidence_map -> outline_freeze -> figure_plan`.
- Do not enter full draft without creator-first evidence, a frozen evidence map, and at least one core figure role.
- If the task is `local_only_synthesis`, do not fake external evidence, do not require publish assets, and preserve compressed intermediate states inside appendix or run log.
- Do not let market conclusions borrow certainty from mechanism evidence.
- Do not ship consensus-only insight as if it were original insight.
- Do not explain difficult mechanisms without concrete case packets.
- Do not treat Feishu or HTML rendering as a substitute for research quality.
