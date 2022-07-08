import json
import ast
from configparser import ConfigParser
import pprint

import pymysql as mysql

import filepaths 


class TableReader:

    def __init__(self) -> None:
        self.config = ConfigParser()
        self.config.read(filepaths.config_file_path)

        user                 = self.config['DB']['user']
        passwd               = self.config['DB']['password']
        host                 = self.config['DB']['hostname']
        self.db              = self.config['DB']['db']
        self.table_name      = self.config['DB']['table_name']

        self.con = mysql.connect(user=user, passwd=passwd, host=host, db=self.db)
        self.cursor = self.con.cursor()

    def select(self, col_list="*", condition="1 = 1") -> mysql.Connection.cursor:
        try:
            query = f"SELECT {col_list} FROM {self.db}.{self.table_name} where {condition}"
            print("query to be executed:", query)
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Exception as msg:
            print("something went wrong while executing this query: ", query)
            print("Logs from Exception: ", msg)
            return None

    def save(self):
        pass

    def update(self):
        pass
    
    def insert(self):
        pass

    def delete(self):
        pass

    def read_config(self):
        column_list = "*"
        condition = "runflag = 'Y'"
        result = self.select(col_list=column_list, condition=condition)
        print(type(result))
        if result:
            file_schema = list(map(lambda each_row: {
                'file_id': each_row[0], 
                'file_name': each_row[1], 
                'file_name': each_row[2], 
                'num_rows': each_row[3],
                'schema': ast.literal_eval(each_row[5])}, result))
            pprint.pprint(file_schema, indent=2)


if __name__ == "__main__":        
    obj = TableReader()
    obj.read_config()
