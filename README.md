[![pages-build-deployment](https://github.com/vAHiD55555/NebulaEdge/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/vAHiD55555/NebulaEdge/actions/workflows/pages/pages-build-deployment)
# 🌌 NebulaEdge

## 🇬🇧 English

**NebulaEdge** is a cloud-native proxy orchestration system that collects free proxies from public sources, categorizes them by country and protocol type, and generates multi-format outputs (PAC, V2Ray, Clash, Sing-box). It is fully automated via GitHub Actions and includes obfuscation mechanisms to evade detection by ISPs.

---
# Proxy Pack

Automated proxy collection, validation, and multi-format packaging.

## Scripts

- `scripts/download_proxies.py`  
- `scripts/validate_proxies_advanced.py`  
- `scripts/generate_outputs.py`  

## Usage

```bash
python3 scripts/download_proxies.py
python3 scripts/validate_proxies_advanced.py
python3 scripts/generate_outputs.py

### 🔥 Features

- ✅ Auto-collection from multiple public proxy sources
- 🌍 Categorization by country: US, DE, NL, FI, and “Best”
- 🔀 Multi-format output generation: PAC, Clash, V2Ray, Sing-box
- 🛡️ Obfuscation of files to bypass filtering and DPI
- 💻 GitHub Pages UI for lightweight proxy customization

---

### 📦 Project Structure

```text
├── inputs/        # Raw proxy lists + parser
├── outputs/       # Final configuration files (PAC, Clash, etc.)
├── rules/         # Country-specific filtering logic
├── obfuscator/    # File cleanup and anti-detection engine
├── .github/       # GitHub Actions workflows
```

---

### 🚀 How to Use

1. Clone or fork the repository
2. Customize rules if needed under `/rules`
3. GitHub Actions will run automatically based on schedules
4. Final proxy files are generated under `/outputs`
5. Visit GUI: [https://vAHiD55555.github.io/NebulaEdge](https://vAHiD55555.github.io/NebulaEdge)

---

## 🇮🇷 فارسی

**NebulaEdge** یک سیستم ابری برای ارکستراسیون پراکسی‌هاست که پراکسی‌های رایگان را از منابع عمومی جمع‌آوری کرده، بر اساس کشور و نوع پروتکل دسته‌بندی می‌کند و خروجی‌هایی در قالب‌های PAC، V2Ray، Clash و Sing-box تولید می‌کند. همهٔ مراحل با استفاده از GitHub Actions به‌صورت خودکار انجام می‌شود و مکانیزم‌های مبهم‌سازی برای فرار از شناسایی توسط ISPها را شامل می‌شود.

---

### 🔥 ویژگی‌ها

- ✅ جمع‌آوری خودکار پراکسی‌ها از منابع عمومی
- 🌍 دسته‌بندی بر اساس کشور: آمریکا، آلمان، هلند، فنلاند و «بهترین‌ها»
- 🔀 تولید خروجی در قالب‌های PAC، Clash، V2Ray، Sing-box
- 🛡️ مبهم‌سازی فایل‌ها برای عبور از فیلترینگ و DPI
- 💻 رابط کاربری گرافیکی ساده از طریق GitHub Pages

---

### 📦 ساختار پروژه

```text
├── inputs/        # لیست خام پراکسی‌ها + پارس‌کننده
├── outputs/       # فایل‌های نهایی (PAC، Clash و غیره)
├── rules/         # منطق فیلترینگ خاص هر کشور
├── obfuscator/    # مکانیزم پاک‌سازی و مبهم‌سازی فایل‌ها
├── .github/       # گردش کار خودکار GitHub Actions
```

---

### 🚀 نحوهٔ استفاده

1. ریپو را Fork یا Clone کنید
2. در صورت نیاز، Ruleها را در پوشهٔ `/rules` شخصی‌سازی کنید
3. GitHub Actions به‌صورت خودکار اجرا می‌شود
4. فایل‌های خروجی در پوشهٔ `/outputs` قرار می‌گیرند
5. به رابط گرافیکی بروید: [https://vAHiD55555.github.io/NebulaEdge](https://vAHiD55555.github.io/NebulaEdge)

---

