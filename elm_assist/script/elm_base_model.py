# /usr/bin/env python3
# -*- coding:utf-8 -*-

import openpyxl

# 模型1 获取数据库中的数据 再对excel中的每一行进行处理
class BaseOneByOne:
    def __init__(self, filename, sheet = 0, startline = 0, server = None):
        print ("init", filename, sheet, startline, server)
        self.db = None
        self.filename = filename
        self.workbook = openpyxl.load_workbook(filename = filename)
        self.sheet = self.workbook.get_sheet_by_name(self.workbook.get_sheet_names()[sheet])
        self.startline = startline

    def before_run_start(self):
        pass

    def readline(self, line_no, row):
        print (line_no, row[0].value)
    
    def create_sql(self):
        pass

    def run_query(self):
        pass

    def handle_line(self, line_no, row):
        print (line_no, row[0].value)

    def after_run_end(self):
        pass

    def run(self):
        self.before_run_start()

        rows = tuple(self.sheet.rows)
        for index, item in enumerate(rows[self.startline:], self.startline):
            self.readline(index, item)
        
        self.run_query()
        # sql select
        print ("start handle ===================================")
        for index, item in enumerate(rows[self.startline:], self.startline):
            self.handle_line(index, item)

        self.after_run_end()

    def __del__(self):
        print("de init")
        if self.db:
            self.db.close()

class Test(BaseOneByOne):

    def __init__(self, filename, sheet = 0, startline = 0, server = None):
        super().__init__(filename)
        print ("init in Test Obj")
        self.query_data = list()

    def readline(self, line_no, row):
        print ("this is in Test ", line_no, row[0].value)
        self.query_data.append(str(row[0].value))
    
    def create_sql(self):
        pass

    def run_query(self):
        print("run query... " + ";".join(self.query_data))
        self.query_data = "query date"

    def handle_line(self, line_no, row):
        print ("this is in handle", line_no, row[0].value)



def run():
    # base1 = BaseOneByOne(filename = "/home/david/sample.xlsx", startline = 1)
    base1 = Test(filename = "/home/david/sample.xlsx", startline = 1)
    base1.run()

if __name__ == "__main__":
    run()
