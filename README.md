# Day 1 文件包｜放哪里、怎么用

把下面 6 个文件**全部复制到 `D:/qa-career/`**（路径全英文、无空格、别放桌面）。

| 文件 | 今天要用吗 | 作用 |
|---|---|---|
| `score.py` | ⭐ 必用 | 被测对象＋12 条用例执行器，`py score.py` 直接出结果 |
| `测试用例表.md` | ⭐ 必用 | 12 条用例，可抄进 WPS/Excel 再截图 |
| `素材日志.md` | ⭐ 必用 | 每天三句，Day 10 拼报告用 |
| `访谈邀约话术.md` | ⭐ 必用 | 今天就要发邀约，直接复制 |
| `缺陷报告_D01模板.md` | 留空 | Day 2 才填，今天别动 |
| `README.md` | 本文件 | 说明 |

另需在 `D:/qa-career/` 下手动建两个文件夹：`证据\` 和 `reports\`。

完整操作步骤见 **`/workspace/Day1详细步骤.md`**（主文档）。

---

## 这台机器的命令写法（重要）

装的是 **Python Install Manager**，所以：

```bat
py -V                          :: 不是 python --version
py -m pip --version            :: 不是 pip --version
py -m pip install pytest pytest-html pytest-cov   :: 不是 pip install ...
py score.py                    :: 不是 python score.py
py -m pytest ...               :: 不是 pytest ...（Day 3 才用）
```

**所有命令开头都是 `py`，装包一律 `py -m pip`。**

---

## 诚信提醒

- 12 条用例的执行结果按终端真实输出填写，**不要为了写缺陷报告故意改错代码**。
- 首轮 12 PASS / 0 FAIL 是完全有效、可核验的成果。
- 行业数据、访谈、截图都必须真实；报名已勾诚信声明。
