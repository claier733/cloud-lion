import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os
import shutil
import pytest
from excel_allure_interface.excel_reader.exscel_driver import ReadExcel

#获取成功失败用例数据统计
def get_test_statistics():
    """获取测试统计数据"""
    data = ReadExcel().excel_read()

    # 从数据中提取所有测试结果（每个元组的第10个元素，索引9）
    results = [row[9] for row in data]  # 直接提取每个元组的第10个元素(通过失败的结果)

    # 统计通过数量
    passed_count = sum(1 for status in results if status == '通过')

    # 统计失败数量
    failed_count = sum(1 for status in results if status == '失败')

    # 统计错误数量（如果有其他状态）
    error_count = len(results) - passed_count - failed_count

    total = len(results)
    pass_rate = (passed_count / total) * 100 if total > 0 else 0

    return passed_count, failed_count, error_count, total, pass_rate

def send_email(subject, body, to_emails, attachment_dir=None):
    """发送带附件的邮件（支持 HTML 正文和压缩包附件）"""

    # 邮件配置
    smtp_server = "smtp.163.com"
    smtp_port = 465
    smtp_username = "13831577754@163.com"
    smtp_password = "YSSTwHZKhwq9mgnr"

    # 创建邮件
    msg = MIMEMultipart()
    msg["From"] = smtp_username
    msg["To"] = ", ".join(to_emails)
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "html"))

    # 处理附件
    temp_zip_path = None
    try:
        if attachment_dir:
            abs_path = os.path.abspath(attachment_dir)
            if not os.path.exists(abs_path):
                raise FileNotFoundError(f"附件目录不存在: {abs_path}")

            # 压缩目录
            temp_zip_path = "temp_report.zip"
            shutil.make_archive("temp_report", "zip", attachment_dir)

            # 添加附件
            with open(temp_zip_path, "rb") as f:
                attach = MIMEApplication(f.read(), _subtype="zip")
                attach.add_header("Content-Disposition", "attachment",
                                  filename=f"Report_{os.path.basename(attachment_dir)}.zip")
                msg.attach(attach)

        # 发送邮件
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.login(smtp_username, smtp_password)
        server.send_message(msg)
        print("✅ 邮件发送成功！")

    except Exception as e:
        print(f"❌ 邮件发送失败: {e}")
        raise  # 重新抛出异常以便上层捕获
    finally:
        if temp_zip_path and os.path.exists(temp_zip_path):
            os.remove(temp_zip_path)
        if 'server' in locals():
            server.quit()



if __name__ == "__main__":

    # 获取测试统计数据
    passed_count, failed_count, error_count, total, pass_rate = get_test_statistics()

    # 构建邮件正文
    body = f"""
    <h1>每日巡检接口测试完成</h1>
    <h2>测试结果概览</h2>
    <p style="color: #20c997;">✓ 通过用例: {passed_count}</p>
    <p style="color: #dc3545;">✗ 失败用例: {failed_count}</p>
    <p style="color: #ffc107;">⚠ 错误用例: {error_count}</p>
    <p>总用例数: {total}</p>
    <p>通过率: {pass_rate:.2f}%</p>
    <p>详细测试报告请查看附件。</p>
    """

    try:
        send_email(
            subject="云狮接口自动化测试报告",
            body=body,
            to_emails=["641870413@qq.com"],
            attachment_dir=r"D:\Users\86138\pythonProject\tiens_yqc\excel_allure_interface\allure-report"
        )
    except Exception as e:
        print(f"程序异常终止: {e}")