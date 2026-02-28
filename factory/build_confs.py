import os
import re
import time

# IPv6 地址匹配正则
_IPV6_PATTERN = re.compile(
    r'((([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:))'
    r'|(([0-9A-Fa-f]{1,4}:){6}(:[0-9A-Fa-f]{1,4}|((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)'
    r'(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))'
    r'|(([0-9A-Fa-f]{1,4}:){5}(((:[0-9A-Fa-f]{1,4}){1,2})|:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)'
    r'(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))'
    r'|(([0-9A-Fa-f]{1,4}:){4}(((:[0-9A-Fa-f]{1,4}){1,3})|((:[0-9A-Fa-f]{1,4})?:((25[0-5]|2[0-4]\d'
    r'|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))'
    r'|(([0-9A-Fa-f]{1,4}:){3}(((:[0-9A-Fa-f]{1,4}){1,4})|((:[0-9A-Fa-f]{1,4}){0,2}:((25[0-5]'
    r'|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))'
    r'|(([0-9A-Fa-f]{1,4}:){2}(((:[0-9A-Fa-f]{1,4}){1,5})|((:[0-9A-Fa-f]{1,4}){0,3}:((25[0-5]'
    r'|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))'
    r'|(([0-9A-Fa-f]{1,4}:){1}(((:[0-9A-Fa-f]{1,4}){1,6})|((:[0-9A-Fa-f]{1,4}){0,4}:((25[0-5]'
    r'|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))'
    r'|(:(((:[0-9A-Fa-f]{1,4}){1,7})|((:[0-9A-Fa-f]{1,4}){0,5}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)'
    r'(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:)))(%.+)?'
)

# 规则配置名称列表（对应 template/ 下的模板，不含 sr_head 和 sr_foot）
CONF_NAMES = [
    'sr_top500_banlist_ad',
    'sr_top500_banlist',
    'sr_top500_whitelist_ad',
    'sr_top500_whitelist',
    'sr_adb',
    'sr_direct_banad',
    'sr_proxy_banad',
    'sr_cnip', 'sr_cnip_ad',
    'sr_backcn', 'sr_backcn_ad',
    'sr_ad_only',
]


def get_rules_from_file(path, kind):
    """读取规则列表文件，转换为 Shadowrocket 规则格式。"""
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    result = ''
    for line in lines:
        line = line.strip('\r\n')
        if not line:
            continue

        if line.startswith('#'):
            result += line + '\n'
            continue

        # 判断规则类型：IPv4 / IPv6 / 关键字 / 域名后缀
        prefix = 'DOMAIN-SUFFIX'
        if re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line):
            prefix = 'IP-CIDR'
            if '/' not in line:
                line += '/32'
        elif _IPV6_PATTERN.match(line):
            prefix = 'IP-CIDR'
            if '/' not in line:
                line += '/128'
        elif '.' not in line and len(line) > 1:
            prefix = 'DOMAIN-KEYWORD'

        result += f'{prefix},{line},{kind}\n'

    return result


# 读取公共头部和尾部模板
with open('template/sr_head.txt', 'r', encoding='utf-8') as f:
    str_head = f.read()
with open('template/sr_foot.txt', 'r', encoding='utf-8') as f:
    str_foot = f.read()

# 构建模板变量
values = {
    'build_time':    time.strftime('%Y-%m-%d %H:%M:%S'),
    'top500_proxy':  get_rules_from_file('data/top500_proxy.list', 'Proxy'),
    'top500_direct': get_rules_from_file('data/top500_direct.list', 'Direct'),
    'ad':            get_rules_from_file('resultant/ad.list', 'Reject'),
    'manual_direct': get_rules_from_file('data/manual_direct.txt', 'Direct'),
    'manual_proxy':  get_rules_from_file('data/manual_proxy.txt', 'Proxy'),
    'manual_reject': get_rules_from_file('data/manual_reject.txt', 'Reject'),
    'gfwlist':       get_rules_from_file('resultant/gfw.list', 'Proxy')
                   + get_rules_from_file('data/manual_gfwlist.txt', 'Proxy'),
}

# 生成规则文件
rules_dir = os.path.join('..', 'rules')
os.makedirs(rules_dir, exist_ok=True)

for conf_name in CONF_NAMES:
    with open(f'template/{conf_name}.txt', 'r', encoding='utf-8') as f:
        template = f.read()

    if conf_name != 'sr_ad_only':
        template = str_head + template + str_foot

    # 替换模板变量 {{xxx}}
    for mark in re.findall(r'{{(.+)}}', template):
        template = template.replace('{{' + mark + '}}', values[mark])

    with open(os.path.join(rules_dir, f'{conf_name}.conf'), 'w', encoding='utf-8') as f:
        f.write(template)