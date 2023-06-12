import time
from plyer import notification

# 設置工作和休息時間（以秒為單位）
work_time = 25 * 60
break_time = 5 * 60

# 設置工作和休息階段的數量
work_sessions = 4
break_sessions = work_sessions - 1

# 創建一個函數來發送通知
def notify(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = None,
        timeout = 5
    )

# 創建一個循環來執行專注時鐘
for i in range(work_sessions):
    # 開始工作階段
    notify("工作時間", "開始您的第{}個工作階段".format(i+1))
    time.sleep(work_time)
    # 結束工作階段
    notify("休息時間", "您的第{}個工作階段已結束".format(i+1))
    # 檢查是否需要休息階段
    if i < break_sessions:
        time.sleep(break_time)
        # 結束休息階段
        notify("休息時間結束", "請開始您的下一個工作階段")

# 完成所有專注時鐘
notify("恭喜", "您已完成所有專注時鐘")

print("Time up!")
