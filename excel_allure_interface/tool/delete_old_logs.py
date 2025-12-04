import os
import time

def delete_old_logs(log_dir, days_to_keep):
    """删除指定目录中超过指定天数的日志文件"""
    # 获取当前时间
    current_time = time.time()
    # 计算保留时间的时间戳
    time_threshold = current_time - (days_to_keep * 86400)  # 86400秒 = 1天

    # 遍历日志目录
    for filename in os.listdir(log_dir):
        file_path = os.path.join(log_dir, filename)
        # 检查是否是文件
        if os.path.isfile(file_path):
            # 获取文件的最后修改时间
            file_mtime = os.path.getmtime(file_path)
            # 如果文件最后修改时间早于时间阈值，则删除文件
            if file_mtime < time_threshold:
                print(f"删除文件: {file_path}")
                os.remove(file_path)

if __name__ == "__main__":
    # 日志目录路径
    log_directory = r"D:\Users\86138\pythonProject\tiens\excel_allure_interface\log"
    # 保留最近3天的日志
    days_to_keep = 3

    # 调用函数删除旧日志
    delete_old_logs(log_directory, days_to_keep)

