1. نصب پیش‌نیازها:
   pip install -r requirements.txt

2. اجرای ربات:
   python bot.py

3. تنظیم زمان‌بندی:
   در bot.py بخش auto_report قابل ویرایش است.

توجه: باید آی‌دی عددی شما به جای AUTHORIZED_USER_ID در فایل bot.py قرار بگیرد.
برای دریافت آن می‌توانید موقتاً print(update.effective_chat.id) بگذارید.