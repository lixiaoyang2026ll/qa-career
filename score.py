# -*- coding: utf-8 -*-
"""
被测对象：成绩等级换算（Day 1）
需求：90 分及以上 A；80-89 B；60-79 C；其余 D；超出 0-100 报错。

用法（在这台机器上）：
    cd /d D:\\qa-career
    py score.py
"""

def grade(score):
    if score < 0 or score > 100:
        raise ValueError("成绩需在 0-100 之间")
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 60:
        return "C"
    return "D"


# 12 条用例的输入与预期（与《测试用例表》逐条对应）
# 预期为 "ERROR" 表示该输入应被拒绝（抛 ValueError 或 TypeError）
CASES = [
    ("TC-01", -1,    "ERROR"),
    ("TC-02", 0,     "D"),
    ("TC-03", 59,    "D"),
    ("TC-04", 60,    "C"),
    ("TC-05", 79,    "C"),
    ("TC-06", 80,    "B"),
    ("TC-07", 89,    "B"),
    ("TC-08", 90,    "A"),    # 关键边界：最容易在这里写错
    ("TC-09", 100,   "A"),
    ("TC-10", 101,   "ERROR"),
    ("TC-11", 75,    "C"),
    ("TC-12", "abc", "ERROR"),
]


def run_one(value):
    """执行一条用例，把异常统一记成 ERROR，方便和预期比对。"""
    try:
        return grade(value)
    except (ValueError, TypeError):
        return "ERROR"


if __name__ == "__main__":
    # 不依赖 pytest，直接 `py score.py` 就能拿到 12 条用例的执行结果，截图即可存证
    passed = 0
    print("ID     INPUT   EXPECT  ACTUAL  RESULT")
    print("-" * 46)
    for cid, value, expected in CASES:
        actual = run_one(value)
        result = "PASS" if actual == expected else "FAIL"
        passed += (result == "PASS")
        print(f"{cid:<6} {str(value):<7} {expected:<7} {actual:<7} {result}")
    print("-" * 46)
    print(f"TOTAL {len(CASES)}: {passed} PASS / {len(CASES) - passed} FAIL")
