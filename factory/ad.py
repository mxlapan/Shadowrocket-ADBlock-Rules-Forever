"""提取广告规则：从 Adblock 规则源中提取全域禁止的域名和 IP。"""

# 参考 Adblock 广告规则格式：https://adblockplus.org/filters

import re
import sys
import time

import requests

# 广告规则源
RULES_URLS = [
    # EasyList China
    'https://easylist-downloads.adblockplus.org/easylistchina.txt',
    # EasyList + China
    'https://easylist-downloads.adblockplus.org/easylistchina+easylist.txt',
    # 乘风广告过滤规则
    'https://raw.githubusercontent.com/xinggsf/Adblock-Plus-Rule/master/rule.txt',
    # Peter Lowe 广告和隐私跟踪域名
    'https://pgl.yoyo.org/adservers/serverlist.php?hostformat=adblockplus;showintro=0',
]

rule = ''
domains = []  # 包含域名和 IP

# 下载规则源
for rule_url in RULES_URLS:
    print('正在下载... ' + rule_url)

    success = False
    r = None
    for _ in range(5):
        r = requests.get(rule_url)
        if r.status_code == 200:
            success = True
            break
        time.sleep(1)

    if not success:
        sys.exit(f'请求失败 {rule_url}\n\t状态码: {r.status_code}')

    rule += r.text + '\n'

# 读取忽略列表
ignore = []
try:
    with open('data/ad_ignore.list', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                ignore.append(line)
except FileNotFoundError:
    pass

# 解析规则
for row in rule.split('\n'):
    row = row.strip()
    row0 = row

    # 处理广告例外规则（@@）
    if row.startswith('@@'):
        domains = [d for d in domains if d not in row]
        continue

    # 跳过无关行
    if not row or row.startswith('!') or '$' in row or '##' in row:
        continue

    # 清除前缀
    row = re.sub(r'^\|?https?://', '', row)
    row = re.sub(r'^\|\|', '', row)
    row = row.lstrip('.*')

    # 清除后缀
    row = row.rstrip('/*')
    if row.endswith('^'):
        row = row.rstrip('^')
    row = re.sub(r':\d{2,5}$', '', row)  # 清除端口

    # 不能含有的字符
    if re.search(r'[/^:*]', row):
        print('忽略: ' + row0)
        continue

    # 去除忽略列表中的内容
    if row in ignore:
        continue

    # 只匹配域名或 IP
    if re.match(r'^\.?[a-zA-Z0-9][-a-zA-Z0-9]{0,62}(\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})*\.[a-zA-Z0-9][-a-zA-Z0-9]{1,}$', row) \
       or re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', row):
        domains.append(row)

print('解析完成。')

# 去重排序并写入文件
domains = sorted(set(domains))

with open('resultant/ad.list', 'w', encoding='utf-8') as f:
    f.write('# adblock rules refresh time: ' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')
    for item in domains:
        f.write(item + '\n')
