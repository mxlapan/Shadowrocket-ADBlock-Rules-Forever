"""下载并解析 GFWList，转换为 Shadowrocket 代理域名列表。"""

import base64
import re
import time

import requests


unhandle_rules = []


def get_rule(url, rule_type='raw'):
    """下载规则源，支持 raw 和 base64 两种格式。"""
    r = None
    for _ in range(5):
        r = requests.get(url)
        if r.status_code == 200:
            break
        time.sleep(1)
    else:
        raise Exception(f'请求失败 {url}\n\t状态码: {r.status_code}')

    if rule_type == 'base64':
        return base64.b64decode(r.text).decode('utf-8').replace('\\n', '\n')
    return r.text


def parse_rules(raw_text):
    """清洗原始规则文本，提取域名列表。"""
    rules = []
    for row in raw_text.split('\n'):
        row = row.strip()

        # 跳过注释和例外规则
        if not row or row.startswith('!') or row.startswith('@@') or row.startswith('[AutoProxy'):
            continue

        # 清除前缀
        row = re.sub(r'^\|?https?://', '', row)
        row = re.sub(r'^\|\|', '', row)
        row = row.lstrip('.*')

        # 清除后缀
        row = row.rstrip('/^*')

        rules.append(row)
    return rules


def filter_rules(rules, excludes=None):
    """过滤规则：只保留合法域名，排除指定域名。"""
    excludes = excludes or []
    result = []

    for rule in rules:
        original = rule

        # 只取主机名部分
        if '/' in rule:
            rule = rule.split('/')[0]

        if not re.match(r'^[\w.-]+$', rule):
            unhandle_rules.append(original)
            continue

        if rule in excludes:
            continue

        result.append(rule)

    return sorted(set(result))


# 下载 GFWList 主源
rule = get_rule(
    'https://raw.githubusercontent.com/gfwlist/gfwlist/master/gfwlist.txt',
    rule_type='base64',
)
# 补充来源：https://github.com/Loyalsoldier/cn-blocked-domain
rule += get_rule('https://raw.githubusercontent.com/Johnshall/cn-blocked-domain/release/domains.txt')

rules = parse_rules(rule)

# 读取排除列表
excludes = []
with open('data/manual_gfwlist_excludes.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith('#'):
            excludes.append(line)

rules = filter_rules(rules, excludes)
rules = sorted(set(rules))

with open('resultant/gfw.list', 'w', encoding='utf-8') as f:
    f.write('\n'.join(rules))

with open('resultant/gfw_unhandle.log', 'w', encoding='utf-8') as f:
    f.write('\n'.join(unhandle_rules))
