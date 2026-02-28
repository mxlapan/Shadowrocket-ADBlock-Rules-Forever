# Shadowrocket-ADBlock-Rules-Forever

iOS [Shadowrocket](https://liguangming.com/Shadowrocket) 分流规则，支持广告过滤，每日自动更新。

> 本项目 Fork 自 [Johnshall/Shadowrocket-ADBlock-Rules-Forever](https://github.com/Johnshall/Shadowrocket-ADBlock-Rules-Forever)，进行了定制化修改。原项目基于 [h2y/Shadowrocket-ADBlock-Rules](https://github.com/h2y/Shadowrocket-ADBlock-Rules)。

## 特性

- 黑名单由 [GFWList](https://github.com/gfwlist/gfwlist) + [Greatfire Analyzer](https://github.com/Loyalsoldier/cn-blocked-domain) 自动生成
- 广告过滤整合 `EasyList`、`EasyList China`、`Peter Lowe`、`乘风规则`，自动去重
- 包含 iOS 端网页广告、App 广告的过滤规则
- [Apple 及 CDN 域名](https://raw.githubusercontent.com/felixonmars/dnsmasq-china-list/master/apple.china.conf) 直连优化
- 提供多种规则方案，自由切换
- 懒人配置（同步自 [LOWERTOP/Shadowrocket](https://github.com/LOWERTOP/Shadowrocket)）
- 规则每日北京时间 8:00 自动构建发布

## 规则列表

![规则选择指南](https://mxlapan.github.io/Shadowrocket-ADBlock-Rules-Forever/figure/guide.png)

| 规则 | 代理 | 直连 |
|------|------|------|
| [黑名单 + 去广告](#黑名单过滤--广告) | 被墙网站 (GFWList) | 正常网站 |
| [黑名单](#黑名单过滤) | 同上 | 同上 |
| [白名单 + 去广告](#白名单过滤--广告) | 其他网站 | top500 可直连网站、中国网站 |
| [白名单](#白名单过滤) | 同上 | 同上 |
| [国内外划分 + 去广告](#国内外划分--广告) | 国外网站 | 中国网站 |
| [国内外划分](#国内外划分) | 同上 | 同上 |
| [全局直连 + 去广告](#直连去广告) | / | 全部 |
| [全局代理 + 去广告](#代理去广告) | 全部 | / |
| [回国规则 + 去广告](#回国规则--广告) | 中国网站 | 国外网站 |
| [回国规则](#回国规则) | 同上 | 同上 |
| [仅去广告](#仅去广告规则) | — | — |
| [懒人配置](#懒人配置) | 国外网站 | 国内网站 |
| [懒人配置（含策略组）](#懒人配置含策略组) | 国外网站 | 国内网站 |

> 以上所有规则，局域网内请求均直连。可下载多个规则切换使用。

## 使用方法

**方法一**：用 Safari 或 Shadowrocket 扫描下方规则对应的二维码。

**方法二**：在 Shadowrocket → 配置 → 右上角 `+` → 粘贴规则地址 → 下载。

导入后建议断开并重新连接一次以确保生效。

### 自动更新规则

1. 安装 [捷径](https://www.icloud.com/shortcuts/20bd590bc99e4ef0a157d2fe6e8c273d)，填写规则地址
2. 快捷指令 → 自动化 → `+` → 创建个人自动化 → 特定时间（建议 8:05 之后）→ 运行快捷指令 → 选择「Shadowrocket 规则自动更新」

---

## 黑名单过滤 + 广告

- 代理：被墙网站（GFWList）
- 直连：正常网站
- 包含广告过滤

```
https://mxlapan.github.io/Shadowrocket-ADBlock-Rules-Forever/rules/sr_top500_banlist_ad.conf
```

![二维码](https://mxlapan.github.io/Shadowrocket-ADBlock-Rules-Forever/figure/sr_top500_banlist_ad.png)

## 黑名单过滤

- 代理：被墙网站（GFWList）
- 直连：正常网站
- 不含广告过滤

```
https://mxlapan.github.io/Shadowrocket-ADBlock-Rules-Forever/rules/sr_top500_banlist.conf
```

![二维码](https://mxlapan.github.io/Shadowrocket-ADBlock-Rules-Forever/figure/sr_top500_banlist.png)

## 白名单过滤 + 广告

- 直连：top500 可直连境外网站、中国网站
- 代理：其余所有境外网站
- 包含广告过滤

```
https://mxlapan.github.io/Shadowrocket-ADBlock-Rules-Forever/rules/sr_top500_whitelist_ad.conf
```

![二维码](https://mxlapan.github.io/Shadowrocket-ADBlock-Rules-Forever/figure/sr_top500_whitelist_ad.png)

## 白名单过滤

- 直连：top500 可直连境外网站、中国网站
- 代理：其余所有境外网站
- 不含广告过滤

```
https://mxlapan.github.io/Shadowrocket-ADBlock-Rules-Forever/rules/sr_top500_whitelist.conf
```

![二维码](https://mxlapan.github.io/Shadowrocket-ADBlock-Rules-Forever/figure/sr_top500_whitelist.png)

## 国内外划分 + 广告

中国网站直连，国外网站代理，包含广告过滤。

```
https://mxlapan.github.io/Shadowrocket-ADBlock-Rules-Forever/rules/sr_cnip_ad.conf
```

![二维码](https://mxlapan.github.io/Shadowrocket-ADBlock-Rules-Forever/figure/sr_cnip_ad.png)

## 国内外划分

中国网站直连，国外网站代理，不含广告过滤。

```
https://mxlapan.github.io/Shadowrocket-ADBlock-Rules-Forever/rules/sr_cnip.conf
```

![二维码](https://mxlapan.github.io/Shadowrocket-ADBlock-Rules-Forever/figure/sr_cnip.png)

## 直连去广告

全局直连，仅过滤广告。适合将 SR 作为全局去广告工具。

```
https://mxlapan.github.io/Shadowrocket-ADBlock-Rules-Forever/rules/sr_direct_banad.conf
```

![二维码](https://mxlapan.github.io/Shadowrocket-ADBlock-Rules-Forever/figure/sr_direct_banad.png)

## 代理去广告

全局代理 + 去广告（局域网直连）。

```
https://mxlapan.github.io/Shadowrocket-ADBlock-Rules-Forever/rules/sr_proxy_banad.conf
```

![二维码](https://mxlapan.github.io/Shadowrocket-ADBlock-Rules-Forever/figure/sr_proxy_banad.png)

## 回国规则

海外用户使用，代理中国网站，直连国外网站。

```
https://mxlapan.github.io/Shadowrocket-ADBlock-Rules-Forever/rules/sr_backcn.conf
```

![二维码](https://mxlapan.github.io/Shadowrocket-ADBlock-Rules-Forever/figure/sr_backcn.png)

## 回国规则 + 广告

海外用户使用，代理中国网站，直连国外网站，包含广告过滤。

```
https://mxlapan.github.io/Shadowrocket-ADBlock-Rules-Forever/rules/sr_backcn_ad.conf
```

![二维码](https://mxlapan.github.io/Shadowrocket-ADBlock-Rules-Forever/figure/sr_backcn_ad.png)

## 仅去广告规则

仅包含去广告规则，不含代理/直连配置。可与其他规则搭配使用。

```
https://mxlapan.github.io/Shadowrocket-ADBlock-Rules-Forever/rules/sr_ad_only.conf
```

![二维码](https://mxlapan.github.io/Shadowrocket-ADBlock-Rules-Forever/figure/sr_ad_only.png)

---

## 懒人配置

同步自 [LOWERTOP/Shadowrocket](https://github.com/LOWERTOP/Shadowrocket)，开箱即用。

```
https://mxlapan.github.io/Shadowrocket-ADBlock-Rules-Forever/rules/lazy.conf
```

![二维码](https://mxlapan.github.io/Shadowrocket-ADBlock-Rules-Forever/figure/lazy.png)

## 懒人配置（含策略组）

同步自 [LOWERTOP/Shadowrocket](https://github.com/LOWERTOP/Shadowrocket)，支持通过「代理分组」灵活调整分流策略。

```
https://mxlapan.github.io/Shadowrocket-ADBlock-Rules-Forever/rules/lazy_group.conf
```

![二维码](https://mxlapan.github.io/Shadowrocket-ADBlock-Rules-Forever/figure/lazy_group.png)

---

## 常见问题

<details>
<summary>上千行的规则会影响网速吗？</summary>

不会。SR 加载规则时会生成搜索树（DFA），匹配时间复杂度为 O(1)，与规则行数无关。
</details>

<details>
<summary>如何选择适合的规则？</summary>

最常用的是黑名单和白名单。区别在于对「未知网站」的处理：黑名单默认直连，白名单默认代理。不确定就两个都下载，切换使用。
</details>

<details>
<summary>广告过滤不完全？</summary>

无法保证 100% 过滤所有广告，尤其是视频广告。App 每次升级可能更换广告策略。
</details>

<details>
<summary>无法正常跳转 google.cn？</summary>

配置 → 使用中的规则 ℹ️ → HTTPS 解密 → 开启 → 安装证书 → 信任证书。
</details>

## 项目结构

```
main (源代码分支)
├── factory/          # 构建脚本和源数据
│   ├── ad.py         # 广告规则生成
│   ├── gfwlist.py    # GFWList 解析
│   ├── build_confs.py # 规则文件生成
│   ├── gen_qrcode.py # 二维码自动生成
│   ├── template/     # 规则模板
│   ├── resultant/    # 中间数据
│   └── manual_*.txt  # 手动维护的规则
├── figure/
│   └── guide.png     # 规则选择指南
├── .github/workflows/
│   └── build.yml     # 每日自动构建
└── readme.md

gh-pages (部署分支，自动生成)
├── rules/            # 规则文件 (.conf)
├── figure/           # 二维码图片
├── readme.md
└── LICENSE
```

## 贡献

修改 [factory/](https://github.com/mxlapan/Shadowrocket-ADBlock-Rules-Forever/tree/main/factory) 下的 `manual_*.txt` 文件，PR 请提交至 `main` 分支。

**定制自己的规则：** Fork 本仓库 → 启用 Actions 即可。

## 问题反馈

欢迎在 [Issues](https://github.com/mxlapan/Shadowrocket-ADBlock-Rules-Forever/issues) 中反馈。

## 致谢

- [h2y/Shadowrocket-ADBlock-Rules](https://github.com/h2y/Shadowrocket-ADBlock-Rules)（原始项目）
- [Johnshall/Shadowrocket-ADBlock-Rules-Forever](https://github.com/Johnshall/Shadowrocket-ADBlock-Rules-Forever)（上游项目）
- [gfwlist](https://github.com/gfwlist/gfwlist) / [Greatfire Analyzer](https://github.com/Loyalsoldier/cn-blocked-domain)
- [乘风广告过滤规则](https://github.com/xinggsf/Adblock-Plus-Rule) / [EasyList China](https://adblockplus.org/) / [Peter Lowe](https://pgl.yoyo.org/)
- [blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script) / [LOWERTOP/Shadowrocket](https://github.com/LOWERTOP/Shadowrocket)

## License

[MIT](LICENSE)
