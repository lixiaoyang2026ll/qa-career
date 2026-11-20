# -*- coding: utf-8 -*-
"""
Day 3｜pytest 自动化测试 —— 修复前（被测对象：score.py 原版）
运行：
    cd /d D:\\qa-career
    py -m pytest test_score.py -v --html=reports/report-before.html --self-contained-html
预期：16 passed, 2 failed（TC-16 NaN、TC-17 True）
"""
import pytest

from score import grade

# 与《测试用例表》逐条对应：用例编号 / 输入 / 预期（"ERROR" 表示应抛异常）
CASES = [
    ("TC-01", -1, "ERROR"),
    ("TC-02", 0, "D"),
    ("TC-03", 59, "D"),
    ("TC-04", 60, "C"),
    ("TC-05", 79, "C"),
    ("TC-06", 80, "B"),
    ("TC-07", 89, "B"),
    ("TC-08", 90, "A"),
    ("TC-09", 100, "A"),
    ("TC-10", 101, "ERROR"),
    ("TC-11", 75, "C"),
    ("TC-12", "abc", "ERROR"),
    ("TC-13", 89.5, "B"),
    ("TC-14", "90", "ERROR"),
    ("TC-15", None, "ERROR"),
    ("TC-16", float("nan"), "ERROR"),
    ("TC-17", True, "ERROR"),
    ("TC-18", 100.0, "A"),
]


@pytest.mark.parametrize("cid, value, expected", CASES, ids=[c[0] for c in CASES])
def test_grade(cid, value, expected):
    """预期为 ERROR 的用例要求抛异常；其余要求返回值相等。"""
    if expected == "ERROR":
        with pytest.raises((ValueError, TypeError)):
            grade(value)
    else:
        assert grade(value) == expected
