# =========================
# FILE: BUGS.md
# =========================

# 🐞 Bug Report – KelaProject

## 🔐 Login Issues
- ❌ No validation for empty input fields
- ❌ Accepts whitespace as valid input

## 📋 Task Issues
- ❌ Allows creation of empty task
- ❌ Duplicate tasks allowed
- ❌ Tasks are visible between different users (after logging out of one user and logging in with another user)
- ❌ No max length validation (UI may break)

## 📅 Event Issues
- ❌ Accepts past dates
- ❌ Invalid date formats are not validated
- ❌ Duplicate events allowed
- ❌ No confirmation after adding event

## ⚡ Urgent Event Issues
- ❌ No priority sorting
- ❌ Unlimited urgent events allowed