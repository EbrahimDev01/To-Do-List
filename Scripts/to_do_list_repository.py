from to_do_list_context import ToDoListContext


class ToDoListRepository:
    def __init__(self):
        self.to_do_list_context = ToDoListContext('to_do_list_db')

    def get_all_to_do_items(self):
        self.locking_table_read()
        sql = 'SELECT * FROM todolist'
        self.to_do_list_context.execute_database(sql)
        result = self.to_do_list_context.fetchall_database()
        self.unlocking_table()
        return result

    def delete_to_do_item(self, to_do_item_id):
        sql = 'DELETE FROM todolist WHERE ToDoListID=%s'
        self.to_do_list_context.execute_database(sql, (to_do_item_id,))
        self.to_do_list_context.commit_database()

    def search_to_do_item(self, text):
        self.locking_table_read()
        sql = '''
SELECT 
    *
FROM 
    todolist
WHERE 
    ToDoListTitle LIKE %s OR 
    ToDoListDetails LIKE %s OR
    ToDoListActive LIKE %s OR
    ToDoListStartDateTime LIKE %s OR
    ToDoListEndDateTime LIKE %s;
    '''
        text = '%' + text + '%'
        self.to_do_list_context.execute_database(sql, (text, text, text, text, text))
        result = self.to_do_list_context.fetchall_database()
        self.unlocking_table()
        return result

    def get_to_do_list_item_by_id(self, to_do_item_id):
        self.locking_table_read()
        sql = '''
            SELECT 
                * 
            FROM 
                todolist
            WHERE
                ToDoListID = %s            
        '''
        self.to_do_list_context.execute_database(sql, (str(to_do_item_id),))
        result = self.to_do_list_context.fetchone_database()
        self.unlocking_table()
        return result

    def to_or_do(self, to_do_item_id):
        self.locking_table_write()
        sql = '''
UPDATE 
    todolist 
SET 
    ToDoListActive = NOT ToDoListActive 
WHERE 
    ToDoListID = %s;   
        '''
        self.to_do_list_context.execute_database(sql, (to_do_item_id,))
        self.to_do_list_context.commit_database()
        self.unlocking_table()

    def close_database(self):
        self.to_do_list_context.close_database()

    def insert_to_do_item(self, title_to_do_item, details_to_do_item, start_datetime_to_do_item,
                          end_datetime_to_do_item):
        self.locking_table_write()
        sql = '''
            INSERT INTO `todolist`(
                `ToDoListID`,
                `ToDoListTitle`,
                `ToDoListDetails`,
                `ToDoListActive`,
                `ToDoListStartDateTime`,
                `ToDoListEndDateTime`
            )
            VALUES(NULL,%s,%s,%s,%s,%s);
        '''
        self.to_do_list_context.execute_database(sql, (
            title_to_do_item, details_to_do_item, 0, start_datetime_to_do_item, end_datetime_to_do_item))
        self.to_do_list_context.commit_database()
        self.unlocking_table()

    def update_to_do_item(self, to_do_item_id, title_to_do_item, details_to_do_item, start_datetime_to_do_item,
                          end_datetime_to_do_item):
        self.locking_table_write()
        sql = '''
            UPDATE 
                todolist
            SET 
                ToDoListTitle = %s,
                ToDoListDetails = %s,
                ToDoListStartDateTime = %s,
                ToDoListEndDateTime = %s
            WHERE
                ToDoListID = %s
        '''
        self.to_do_list_context.execute_database(sql, (
            title_to_do_item, details_to_do_item, start_datetime_to_do_item, end_datetime_to_do_item, to_do_item_id))
        self.to_do_list_context.commit_database()
        self.unlocking_table()

    def locking_table_write(self):
        sql = 'LOCK TABLES todolist WRITE;'
        self.to_do_list_context.execute_database(sql)

    def locking_table_read(self):
        sql = 'LOCK TABLES todolist READ;'
        self.to_do_list_context.execute_database(sql)

    def unlocking_table(self):
        sql = 'UNLOCK TABLES;'
        self.to_do_list_context.execute_database(sql)


if __name__ == '__main__':
    to_do_list_repository = ToDoListRepository()
    to_do_list_repository.to_or_do(7)
    print(to_do_list_repository.get_to_do_list_item_by_id(7)[3])


def initialize_database():
    to_do_list_context_instantiation = ToDoListContext()
    to_do_list_context_instantiation.create_database('to_do_list_db')
    to_do_list_context_instantiation.close_database()

    to_do_list_context_instantiation = ToDoListContext('to_do_list_db')
    sql_create_table_to_do_list = '''
            CREATE TABLE IF NOT EXISTS ToDoList (
            ToDoListID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
            ToDoListTitle VARCHAR(150) NOT NULL,
            ToDoListDetails TEXT NOT NULL,
            ToDoListActive BOOLEAN NOT NULL DEFAULT FALSE,
            ToDoListStartDateTime DATETIME NULL,
            ToDoListEndDateTime DATETIME NULL
            );
    '''

    to_do_list_context_instantiation.execute_database(sql_create_table_to_do_list)
    to_do_list_context_instantiation.close_database()
