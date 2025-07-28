# Regional Proxy Collector & PAC Generator

این پروژه طراحی شده برای جمع‌آوری پروکسی‌های عمومی، دسته‌بندی بر اساس کشور (USA, Germany, Netherlands, Finland) و تولید فایل‌های PAC به‌صورت خودکار. همچنین شامل مکانیزم‌هایی برای obfuscation جهت جلوگیری از شناسایی توسط ISPهاست.

## ویژگی‌ها
- جمع‌آوری پروکسی‌های SOCKS5 و HTTPS از منابع عمومی
- دسته‌بندی هوشمند بر اساس موقعیت جغرافیایی
- تولید فایل‌های `.pac` برای استفاده در مرورگر و سیستم عامل
- اجرای خودکار به کمک GitHub Actions

## نصب اولیه
```bash
git clone https://github.com/<username>/<repo>
cd <repo>
pip install -r requirements.txt# NebulaEdge
