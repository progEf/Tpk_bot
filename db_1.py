import sqlite3


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute('SELECT * FROM users WHERE user_id = ? ', (user_id,)).fetchmany(1)
            return bool(len(result))

    def add_user(self, user_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO users (user_id) VALUES (?)", (user_id,))

    def set_active(self, user_id, active):
        with self.connection:
            return self.cursor.execute("UPDATE users SET active = ? WHERE user_id = ?", (active, user_id,))

    def get_users(self):
        with self.connection:
            return self.cursor.execute("SELECT user_id, active FROM users").fetchall()
    def see(self):
        while True:
            with self.connection:
                    return self.cursor.execute("SELECT user_id FROM users").fetchall()

    def cou_user(self, INT):
        with self.connection:
            return self.cursor.execute(f"UPDATE users SET con = con + {INT}" )
            #return self.cursor.execute(f"UPDATE users SET con = con + {INT}")
    def col_id(self):
        with self.connection:
            return self.cursor.execute("SELECT user_id FROM users")

    def cou_user_32(self, INT, NAME):
        with self.connection:
            return self.cursor.execute(f"UPDATE users SET con = con + {INT} WHERE user_id LIKE {NAME} ").fetchall()


    def cou_id_2(self,  x):
        with self.connection:
            return self.cursor.execute(f"SELECT con FROM users WHERE user_id == {x} AND con ")

    def cou_id_3(self,  x):
        with self.connection:
            return self.cursor.execute(f"SELECT user_id FROM users  WHERE user_id == {x}")


    def cou_user_del(self,  NAME):
        with self.connection:
            return self.cursor.execute(f"UPDATE users SET con = con - con WHERE user_id LIKE {NAME} ").fetchall()

    def cou_user_del_tim(self):
        with self.connection:
            return self.cursor.execute(f"UPDATE users SET con = con - con")

    def prepo(self, INT1, NAME1):
        with self.connection:
            return self.cursor.execute(f"UPDATE users SET prepod = prepod + {INT1} WHERE user_id LIKE {NAME1}")
    def see_propod(self):
        while True:
            with self.connection:
                    return self.cursor.execute("SELECT prepod FROM users").fetchall()

    def stude(self, INT2, NAME2):
        with self.connection:
            return self.cursor.execute(f"UPDATE users SET stud = stud + {INT2} WHERE user_id LIKE {NAME2}")
    def see_stude(self):
        while True:
            with self.connection:
                    return self.cursor.execute("SELECT stud FROM users").fetchall()

    def del_stut_sum(self):
        with self.connection:
            return self.cursor.execute(f"UPDATE users SET sum_st = sum_st - sum_st")

    def add_mas_stud(self, INT3):
        with self.connection:
            return self.cursor.execute(f"UPDATE users SET sum_st = {INT3}")
    def add_mas_prepod(self, INT4):
        with self.connection:
            return self.cursor.execute(f"UPDATE users SET sum_pr = {INT4}")
    def see_stude_sume(self):
        while True:
            with self.connection:
                    return self.cursor.execute("SELECT sum_st FROM users").fetchall()
    def see_prepod_sume(self):
        while True:
            with self.connection:
                    return self.cursor.execute("SELECT sum_pr FROM users").fetchall()