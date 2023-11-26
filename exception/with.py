class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        self.connection = self.connect_to_database()
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection:
            self.disconnect_from_database()

    def connect_to_database(self):
        # 执行数据库连接操作
        print(f"连接到数据库 {self.db_name}")
        return "数据库连接对象"

    def disconnect_from_database(self):
        # 执行数据库断开连接操作
        print(f"断开与数据库 {self.db_name} 的连接")
        self.connection = None


# 使用自定义上下文管理器打开数据库连接
with DatabaseConnection("mydb") as db:
    # 使用数据库连接执行操作
    print("执行数据库操作")

# 此处已自动断开与数据库的连接