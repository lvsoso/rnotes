#!/usr/bin/env python3
"""Validate explicitly synthetic tutorial data; this is not the human-review gate.

No third-party dependencies. Refuses human-reviewed provenance claims.
"""
import argparse
import csv
import hashlib
import json
import unicodedata
from collections import Counter
from pathlib import Path

LABELS = ['digital_human', 'translation', 'agent_workflow', 'clarify', 'other']
COUNTS = {'train': 150, 'dev': 50, 'calibration': 50, 'test': 50, 'challenge': 20}
REVIEWER = 'AI-generated tutorial; not human-reviewed'
POLICY = 'tutorial-intent-v1.0'


def check(condition, message):
    if not condition:
        raise ValueError(message)


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalized(text):
    return ''.join(unicodedata.normalize('NFKC', text).casefold().split())


def validate(root):
    ids, group_splits, text_splits = set(), {}, {}
    allrows, manifests = [], {}
    expected_ins = None
    expected_crit = None
    for split, count in COUNTS.items():
        path = root / (split + '.jsonl')
        rows = [json.loads(line) for line in path.read_text(encoding='utf-8').splitlines() if line.strip()]
        check(len(rows) == count, f'{split}: expected {count} rows, got {len(rows)}')
        class_counts, language_counts, group_counts = Counter(), Counter(), Counter()
        for row in rows:
            rid = row.get('id')
            check(isinstance(rid, str) and rid and rid not in ids, f'{split}: missing/duplicate id {rid}')
            ids.add(rid)
            check(row.get('split') == split, f'{rid}: incorrect split')
            group = row.get('source_group_id')
            check(isinstance(group, str) and group, f'{rid}: missing source_group_id')
            check(group_splits.setdefault(group, split) == split, f'{rid}: source group crosses splits')
            group_counts[group] += 1
            state = row.get('state')
            check(isinstance(state, dict) and isinstance(state.get('text'), str) and state['text'].strip(), f'{rid}: invalid state.text')
            norm = normalized(state['text'])
            check(text_splits.setdefault(norm, split) == split, f'{rid}: normalized text repeats across splits')
            qs = row.get('qs')
            check(isinstance(qs, list) and len(qs) == 1, f'{rid}: expected one question')
            q = qs[0]
            check(q.get('id') == 'intent' and q.get('t') == 'choice', f'{rid}: wrong question schema')
            check(isinstance(q.get('crit'), dict) and list(q['crit']) == LABELS, f'{rid}: wrong candidate order')
            if expected_crit is None:
                expected_crit = q['crit']
                expected_ins = q.get('ins')
            check(q['crit'] == expected_crit and q.get('ins') == expected_ins and isinstance(expected_ins, str) and expected_ins.strip(), f'{rid}: policy prompt/candidates drift')
            check(type(q.get('y')) is int and 0 <= q['y'] < len(LABELS), f'{rid}: invalid hard label')
            check('soft' not in q, f'{rid}: this tutorial intentionally has no soft labels')
            m = row.get('metadata')
            check(isinstance(m, dict), f'{rid}: missing metadata')
            check(m.get('review_status') == 'assistant_reviewed_pilot', f'{rid}: wrong synthetic review flag')
            check(m.get('reviewer') == REVIEWER, f'{rid}: wrong reviewer disclosure')
            check(m.get('label_source') == 'synthetic_tutorial', f'{rid}: wrong synthetic label source')
            check(m.get('label_policy_version') == POLICY, f'{rid}: policy version mismatch')
            check(m.get('intended_use') == 'educational_only_not_benchmark', f'{rid}: intended-use disclosure missing')
            for key in ('lang', 'tag', 'rationale'):
                check(isinstance(m.get(key), str) and m[key].strip(), f'{rid}: missing {key}')
            class_counts[LABELS[q['y']]] += 1
            language_counts[m['lang']] += 1
        check(dict(class_counts) == {label: count // 5 for label in LABELS}, f'{split}: class imbalance {class_counts}')
        manifests[split] = {'records': len(rows), 'groups': len(group_counts), 'class_counts': {label: class_counts[label] for label in LABELS}, 'language_counts': dict(sorted(language_counts.items())), 'sha256': sha256(path)}
        allrows.extend(rows)
    combined = (root / 'train.jsonl').read_bytes() + (root / 'dev.jsonl').read_bytes()
    check((root / 'train-dev.jsonl').read_bytes() == combined, 'train-dev.jsonl must exactly concatenate train and dev, preserving split fields')
    with (root / 'data_preview.csv').open(encoding='utf-8-sig', newline='') as f:
        preview = list(csv.DictReader(f))
    check(len(preview) == len(allrows), 'CSV row count mismatch')
    expected_rows = {r['id']: r for r in allrows}
    check({r['id'] for r in preview} == set(expected_rows), 'CSV ids mismatch')
    for p in preview:
        r = expected_rows[p['id']]
        check(p['text'] == r['state']['text'] and p['label'] == LABELS[r['qs'][0]['y']] and p['split'] == r['split'] and p['rationale'] == r['metadata']['rationale'], f"CSV content mismatch: {p['id']}")
    check(json.loads((root / 'label_order.json').read_text()) == LABELS, 'label_order.json mismatch')
    manifest = {'dataset': 'Jev five-intent synthetic tutorial', 'version': POLICY, 'created_utc': '2026-10-03', 'review_status': 'assistant_reviewed_pilot', 'reviewer': REVIEWER, 'label_source': 'synthetic_tutorial', 'warning': 'Educational synthetic pilot only. Not human-reviewed and not a benchmark. Passing this validator does not establish semantic independence, label correctness, calibration reliability, or production suitability.', 'candidate_order': LABELS, 'total_records_including_challenge': len(allrows), 'total_groups': len(group_splits), 'splits': manifests, 'train-dev': {'records': 200, 'sha256': sha256(root / 'train-dev.jsonl')}, 'csv': {'records': len(preview), 'sha256': sha256(root / 'data_preview.csv')}}
    (root / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return manifest


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dir', required=True, type=Path)
    args = parser.parse_args()
    print(json.dumps(validate(args.dir), ensure_ascii=False, indent=2))
    print('PASS: synthetic tutorial schema, class balance, exact text/group disjointness, provenance, and CSV parity. Human review is still absent.')
