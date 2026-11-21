# -*- coding: utf-8 -*-
"""
Day 2｜修复版（对应缺陷报告 D01）
改变只有一处：在函数入口增加「类型 + 非法数值」校验，其余逻辑一行未动。
用例与 score_v2.py 完全相同（18 条），修复前后可直接对比通过率。

用法：
    cd /d D:\\qa-career
    py score_fixed.py
"""

import math


def grade(score):
    # 修复 D01：先校验输入类型，再校验数值合法性
    if isinstance(score, bool):                 # bool 是 int 的子类，必须单独拦
        raise TypeError("成绩必须是数字，不能是布尔值")
    if not isinstance(score, (int, float)):      # 挡住 "90"、None、列表等
        raise TypeError("成绩必须是数字")
    if isinstance(score, float) and math.isnan(score):
        raise ValueError("成绩不能是 NaN")        # NaN 与任何数比较都是 False

    if score < 0 or score > 100:
        raise ValueError("成绩需在 0-100 之间")
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 60:
        return "C"
    return "D"


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
    ("TC-13", 89.5,         "B"),
    ("TC-14", "90",         "ERROR"),
    ("TC-15", None,         "ERROR"),
    ("TC-16", float("nan"), "ERROR"),
    ("TC-17", True,         "ERROR"),
    ("TC-18", 100.0,        "A"),
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
    print(f"TOTAL {len(CASES)}: {passed} PASS / {len(CASES)-passed} FAIL")
