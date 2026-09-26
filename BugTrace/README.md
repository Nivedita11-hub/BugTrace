# BugTrace 🐛⚡
> Autonomous AI-assisted debugging workflow for log analysis, test generation, and regression verification.

## 📌 Project Overview
BugTrace automates the end-to-end bug resolution lifecycle:
1. **Log Analysis**: Scans application logs to detect duplicate non-idempotent operations.
2. **Red Test Generation**: Automatically builds unit tests using `pytest` to isolate and reproduce defects.
3. **Automated Fix**: Implements transactional checks to make operations idempotent.
4. **Regression Verification**: Re-runs test suites to ensure 100% pass rates and prevent regressions.

## 🛠️ Demo Scenario
- **Issue Detected**: Duplicate `POST /api/return` requests caused inventory to increment multiple times for a single transaction (`TXN-9981`).
- **Fix Applied**: Added transaction tracking via `processed_transactions` inside `app.py`.
- **Result**: Idempotent stock handling verified with `pytest` (`1 passed in 0.08s`).

## 🚀 How to Run Locally
1. Clone the repository:
   ```bash
   git clone [https://github.com/Nivedita11-hub/BugTrace.git](https://github.com/Nivedita11-hub/BugTrace.git)
   cd BugTrace
