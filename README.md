# Uncommon ZeroDivisionError in Python

This repository demonstrates a subtle bug in a Python function that leads to a `ZeroDivisionError` under an uncommon condition.  The function attempts to handle zero inputs, but fails to account for the specific case where both inputs are zero simultaneously.

## Bug Description

The `function_with_uncommon_error` function aims to safely handle division by checking if either input is zero. However, it misses the edge case where both `a` and `b` are 0, resulting in a division by zero exception.  This highlights the importance of thorough testing and considering all possible input combinations.

## Solution

The solution demonstrates how to correctly handle the missing edge case by adding an explicit check for both inputs being zero.  This prevents the `ZeroDivisionError` from occurring, making the function more robust.