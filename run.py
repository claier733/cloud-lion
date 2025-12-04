import os
import pytest
import sys

from excel_allure_interface.tool.send_email import send_email,get_test_statistics

# 添加项目根目录到Python路径，确保可以导入邮件模块
project_root = r'D:\Users\86138\pythonProject\tiens_ys'
sys.path.append(project_root)

# 导入邮件发送模块
try:
    from excel_allure_interface.tool.send_email import send_email, get_test_statistics
    EMAIL_AVAILABLE = True
except ImportError:
    print("⚠️  邮件发送模块未找到，将跳过邮件发送")
    EMAIL_AVAILABLE = False


def run(send_email_flag=True, recipients=None):
    """一键运行测试并生成报告

    Args:
        send_email_flag: 是否发送邮件
        recipients: 收件人列表，如果为None则使用默认收件人
    """
    # 指定正确的测试文件路径
    test_file = r'D:\Users\86138\pythonProject\tiens_ys\excel_allure_interface\do_interface_excel_allure\test_restart.py'

    # 切换到测试文件所在目录，确保相对路径正确
    test_dir = os.path.dirname(test_file)
    os.chdir(test_dir)

    print(f"🚀 开始执行测试文件: {test_file}")
    print(f"📁 工作目录: {os.getcwd()}")

    # 运行指定的测试文件
    exit_code = pytest.main([test_file, '-v', '--alluredir=./allure-results'])

    # 生成Allure报告
    report_dir = os.path.join(test_dir, '..', 'report')
    os.system(f'allure generate ./allure-results -o {report_dir} --clean')

    # 发送邮件报告
    if EMAIL_AVAILABLE and send_email_flag:
        try:
            # 获取测试统计数据
            passed_count, failed_count, error_count, total, pass_rate = get_test_statistics()

            # 根据测试结果确定邮件主题
            if exit_code == 0:
                subject = "✅ 云狮智选接口自动化测试报告 - 所有用例通过"
            else:
                subject = "⚠️ 云狮智选接口自动化测试报告 - 存在失败的用例"

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

            # 确定收件人
            if recipients is None:
                to_emails = ["641870413@qq.com"]  # 默认收件人
            else:
                to_emails = recipients

            # 报告目录（作为附件）
            attachment_dir = os.path.abspath(report_dir)

            print(f"📊 测试统计: 通过{passed_count}, 失败{failed_count}, 错误{error_count}, 通过率{pass_rate:.2f}%")
            print(f"📧 准备发送邮件给: {', '.join(to_emails)}")

            # 发送邮件
            send_email(subject, body, to_emails, attachment_dir)
            print("✅ 测试报告已发送至邮箱")

        except Exception as e:
            print(f"❌ 发送邮件失败: {e}")
    else:
        print("ℹ️  跳过邮件发送")

    print("✅ 测试完成！")
    print(f"📊 报告位置: {report_dir}")
    print("🌐 查看报告命令: allure serve ./allure-results")

    return exit_code


if __name__ == '__main__':
    # 使用方法1: 默认发送邮件
    run()

    # 使用方法2: 不发送邮件
    # run(send_email_flag=False)

    # 使用方法3: 发送给特定收件人
    # custom_recipients = ["user1@example.com", "user2@example.com"]
    # run(recipients=custom_recipients)