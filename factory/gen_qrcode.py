# -*- coding: utf-8 -*-

import os
import subprocess
import qrcode


# 规则文件名列表（与 build_confs.py 保持一致，加上 lazy 规则）
conf_names = [
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
    'lazy',
    'lazy_group',
]


def get_github_owner():
    """从 git remote 获取仓库 owner 名称"""
    try:
        result = subprocess.run(
            ['git', 'config', '--get', 'remote.origin.url'],
            capture_output=True, text=True, check=True
        )
        url = result.stdout.strip()
        # 支持 SSH (git@github.com:user/repo.git) 和 HTTPS (https://github.com/user/repo.git)
        if 'github.com:' in url:
            owner = url.split('github.com:')[1].split('/')[0]
        elif 'github.com/' in url:
            owner = url.split('github.com/')[1].split('/')[0]
        else:
            owner = None
        return owner
    except Exception:
        return None


def get_repo_name():
    """从 git remote 获取仓库名称"""
    try:
        result = subprocess.run(
            ['git', 'config', '--get', 'remote.origin.url'],
            capture_output=True, text=True, check=True
        )
        url = result.stdout.strip()
        if 'github.com:' in url:
            repo = url.split('github.com:')[1].split('/')[1]
        elif 'github.com/' in url:
            repo = url.split('github.com/')[1].split('/')[1]
        else:
            return 'Shadowrocket-ADBlock-Rules-Forever'
        return repo.removesuffix('.git')
    except Exception:
        return 'Shadowrocket-ADBlock-Rules-Forever'


def generate_qrcodes():
    owner = os.environ.get('GITHUB_REPOSITORY_OWNER') or get_github_owner()
    repo = get_repo_name()

    if not owner:
        print('Warning: Could not detect GitHub owner, using default "Johnshall"')
        owner = 'Johnshall'

    base_url = f'https://{owner}.github.io/{repo}'
    figure_dir = os.path.join(os.path.dirname(__file__), '..', 'figure')
    os.makedirs(figure_dir, exist_ok=True)

    print(f'Generating QR codes for: {base_url}')

    for name in conf_names:
        url = f'{base_url}/{name}.conf'
        img = qrcode.make(url, border=2)
        output_path = os.path.join(figure_dir, f'{name}.png')
        img.save(output_path)
        print(f'  -> {name}.png')

    print(f'Done. {len(conf_names)} QR codes generated.')


if __name__ == '__main__':
    generate_qrcodes()
