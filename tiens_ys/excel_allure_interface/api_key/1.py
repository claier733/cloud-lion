import pymysql

print(f"pymysql version: {pymysql.__version__}")
print(f"pymysql attributes: {[x for x in dir(pymysql) if not x.startswith('_')]}")

# 测试connect方法是否存在
if hasattr(pymysql, 'connect'):
    print("✓ pymysql.connect exists")
else:
    print("✗ pymysql.connect not found")