"""通过 system-one-adapter 调用 DeepSeek，生成兼容现有评测工具的 JSONL。"""

import argparse
import json
import os
import time
from pathlib import Path


def main():
    """读取选择题数据，调用 DeepSeek，并逐条保存预测结果。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', required=True)
    parser.add_argument('--output', required=True)
    parser.add_argument('--model', default='deepseek-chat')
    parser.add_argument('--base-url', default='https://api.deepseek.com')
    args = parser.parse_args()

    api_key = os.environ.get('DEEPSEEK_API_KEY')
    if not api_key:
        parser.error('请设置环境变量 DEEPSEEK_API_KEY')
    out = Path(args.output)
    if out.exists():
        parser.error('输出文件已存在，请使用新的输出路径')
    rows = [
        json.loads(line)
        for line in Path(args.input).read_text(encoding='utf-8').splitlines()
        if line.strip()
    ]
    if not rows:
        parser.error('输入文件不能为空')

    from system_one_adapter import Choice, SystemOneAdapterClient
    from system_one_adapter.providers.openai import OpenAIProvider
    from typesafe_sdk import RetryPolicy

    provider = OpenAIProvider(
        args.model,
        base_url=args.base_url,
        api_key=api_key,
        api='chat_completions',
    )
    try:
        out.parent.mkdir(parents=True, exist_ok=True)
        with SystemOneAdapterClient(
            structured_outputs=False,
            llm_answer_mode='probabilities',
            normalize_probabilities=True,
            n_retry_malformed_structure=1,
            retry=RetryPolicy(max_retries=0),
        ) as client, out.open('x', encoding='utf-8') as stream:
            for row in rows:
                start = time.perf_counter()
                try:
                    question = row['qs'][0]
                    if question['t'] != 'choice':
                        raise ValueError('仅支持 qs[0] 为 choice 的数据')
                    response = client.system_one(
                        state=row['state'],
                        questions={
                            question['id']: Choice(
                                instructions=question['ins'],
                                criteria=question['crit'],
                            )
                        },
                        model=provider,
                    )
                    ms = (time.perf_counter() - start) * 1000
                    answer = response.choices[question['id']]
                    labels = list(question['crit'])
                    record = {
                        'id': row['id'],
                        'labels': labels,
                        'probabilities': [float(answer.probabilities[k]) for k in labels],
                        'prediction': answer.choice,
                        'latency_ms': ms,
                        'status': 'ok',
                        'model': args.model,
                        'raw': response.model_dump(mode='json'),
                    }
                except Exception as error:
                    record = {
                        'id': row.get('id'),
                        'status': 'error',
                        'latency_ms': (time.perf_counter() - start) * 1000,
                        'error': type(error).__name__ + ': ' + str(error),
                    }
                stream.write(json.dumps(record, ensure_ascii=False) + '\n')
                stream.flush()
    finally:
        # 外部传入的 Provider 由调用方负责关闭。
        provider.close()
    print(out)


if __name__ == '__main__':
    main()
