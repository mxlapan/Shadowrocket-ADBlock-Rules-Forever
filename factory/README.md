# 规则文件开发说明

这里是规则文件的生成车间，欢迎访问。


## 目录结构

```
factory/
├── ad.py                  # 从 Adblock 规则源提取广告域名 → resultant/ad.list
├── gfwlist.py             # 解析 GFWList → resultant/gfw.list
├── build_confs.py         # 根据模板生成 .conf 规则文件 → ../rules/
├── gen_qrcode.py          # 为每个规则文件生成二维码 → ../figure/
├── top500_manual.py       # 手动工具：评估 top500 网站可达性（不参与 CI）
├── auto_build.sh          # CI 构建入口脚本
├── data/                  # 源数据（手动维护，提交到 git）
│   ├── manual_direct.txt          # 直连域名
│   ├── manual_proxy.txt           # 代理域名
│   ├── manual_reject.txt          # 屏蔽域名
│   ├── manual_gfwlist.txt         # GFWList 补充
│   ├── manual_gfwlist_excludes.txt # GFWList 误杀排除
│   ├── ad_ignore.list             # 广告白名单
│   ├── top500_direct.list         # 可直连 top500 域名
│   ├── top500_proxy.list          # 需代理 top500 域名
│   ├── top500_manual.list         # top500 评估结果
│   └── top500Domains.csv          # top500 原始数据
├── template/              # 规则模板
│   ├── sr_head.txt        # 公共头部
│   ├── sr_foot.txt        # 公共尾部
│   └── sr_*.txt           # 各规则模板
└── resultant/             # CI 构建产物（gitignore，不提交）
    ├── ad.list            # 广告域名列表
    ├── gfw.list           # GFWList 域名列表
    └── gfw_unhandle.log   # 未处理的 GFWList 规则
```


## 规则模板

`template/` 目录下为规则模板，`build_confs.py` 运行时按模板生成规则文件。

每个规则对应一个模板。`sr_head.txt` 和 `sr_foot.txt` 是所有模板的公共头部和尾部（`sr_ad_only` 除外）。

模板中的 `{{变量名}}` 占位符会在构建时被替换为实际规则内容。


## 手动维护的文件

所有手动维护的源数据都在 `data/` 目录下：

| 文件 | 说明 |
|------|------|
| `data/manual_direct.txt` | 走直连的域名或 IP |
| `data/manual_proxy.txt` | 走代理的域名或 IP |
| `data/manual_reject.txt` | 需要屏蔽的域名或 IP |
| `data/manual_gfwlist.txt` | GFWList 无法无损转换的补充规则 |
| `data/manual_gfwlist_excludes.txt` | GFWList 中误杀的域名 |
| `data/ad_ignore.list` | 广告规则白名单 |


## 构建流程

```
ad.py    → resultant/ad.list       （从规则源下载并提取广告域名）
gfwlist.py → resultant/gfw.list    （下载并解析 GFWList）
build_confs.py → ../rules/*.conf   （将 data/ + resultant/ + template/ 合成规则文件）
gen_qrcode.py  → ../figure/*.png   （为每个规则生成二维码）
```

CI 每日自动执行 `auto_build.sh`，产物部署到 `gh-pages` 分支。
