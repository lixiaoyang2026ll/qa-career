# -*- coding: utf-8 -*-
"""
Day 2｜扩展用例版（18 条）
被测代码与 Day 1 完全一致，一个字都没改 —— 保证基线可对照。
新增 6 条真实场景用例（TC-13 ~ TC-18），用来暴露 Day 1 没覆盖到的情况。

用法：
    cd /d D:\\qa-career
    py score_v2.py
"""


def grade(score):
    # ⚠️ 这就是 Day 1 的原版代码，此文件里刻意不做任何修改
    if score < 0 or score > 100:
        raise ValueError("成绩需在 0-100 之间")
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 60:
        return "C"
    return "D"


# Day 1 的 12 条 + Day 2 新增 6 条
CASES = [
    ("TC-01", -1,           "ERROR"),
    ("TC-02", 0,            "D"),
    ("TC-03", 59,           "D"),
    ("TC-04", 60,           "C"),
    ("TC-05", 79,           "C"),
    ("TC-06", 80,           "B"),
    ("TC-07", 89,           "B"),
    ("TC-08", 90,           "A"),
    ("TC-09", 100,          "A"),
    ("TC-10", 101,          "ERROR"),
    ("TC-11", 75,           "C"),
    ("TC-12", "abc",        "ERROR"),
    # —— Day 2 新增：真实使用中会遇到、但首轮没测的输入 ——
    ("TC-13", 89.5,         "B"),      # 小数成绩
    ("TC-14", "90",         "ERROR"),  # 字符串形式的数字（表单常见）
    ("TC-15", None,         "ERROR"),  # 空值
    ("TC-16", float("nan"), "ERROR"),  # NaN：非数值
    ("TC-17", True,         "ERROR"),  # 布尔值
    ("TC-18", 100.0,        "A"),      # 浮点边界
]


def run_one(value):
    try:
        return grade(value)
    except (ValueError, TypeError):
        return "ERROR"


if __name__ == "__main__":
    passed = 0
    print("ID     INPUT     EXPECT  ACTUAL  RESULT")
    print("-" * 52)
    for cid, value, expected in CASES:
        actual = run_one(value)
        result = "PASS" if actual == expected else "FAIL"
        passed += (result == "PASS")
        print(f"{cid:<6} {str(value):<9} {expected:<7} {actual:<7} {result}")
    print("-" * 52)
    print(f"TOTAL {len(CASES)}: {passed} PASS / {len(CASES) - passed} FAIL")
