# BugTrace Operational Rules

Follow this pipeline strictly when resolving a bug report:

1. DIAGNOSTICS: Parse raw logs/reports. Identify duplicate transactions or state errors.
2. CODE TRACING: Search codebase to map the error to specific files/functions. Do NOT edit code yet.
3. REPRODUCE (RED TEST): Write a test in `tests/test_bugs.py` isolating the issue. RUN `pytest` IN TERMINAL TO VERIFY FAILURE.
4. FIX (GREEN TEST): Apply a minimal code fix. RE-RUN `pytest` IN TERMINAL TO VERIFY PASS.
5. REGRESSION: Run `pytest` across all tests to ensure no breaking changes.
6. REPORT: Output a markdown summary detailing root cause, git diff, and terminal test logs.