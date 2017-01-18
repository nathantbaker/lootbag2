import sys
import sqlite3

class LootBag():

    def add_toy_for_child(self, child, toy):
        with sqlite3.connect('lootbag.db') as conn:
            c = conn.cursor()

            try:
                c.execute("INSERT INTO Child VALUES (?, ?, ?)",
                    (None, child, 0))
            except sqlite3.OperationalError:
                pass

            c.execute("SELECT ChildId FROM Child WHERE Name='{}'".format(child))
            results = c.fetchall()

            try:
                c.execute("INSERT INTO Toy VALUES (?, ?, ?)",
                    (None, toy, results[0][0]))
            except sqlite3.OperationalError:
                pass


    def remove_toy_for_child(self, child, toy):
        with sqlite3.connect('lootbag.db') as conn:
            c = conn.cursor()

            c.execute("SELECT ChildId FROM Child WHERE Name='{}'".format(child))
            results = c.fetchall()

            try:
                c.execute("DELETE FROM Toy WHERE ChildId={} AND Name='{}'"
                    .format(results[0][0], toy))
            except sqlite3.OperationalError:
                pass


    def get_by_child(self, child):
        with sqlite3.connect('lootbag.db') as conn:
            c = conn.cursor()

            c.execute("""SELECT t.Name
                FROM Toy t, Child c
                WHERE c.Name='{}'
                AND c.ChildId = t.ChildId
            """.format(child))

            toys = c.fetchall()
            # print(toys)


    def get_list_of_kids(self):
        # desired result: return ["Ben", "Drew", "Trent"]

        # get the data
        with sqlite3.connect('lootbag.db') as conn:
            c = conn.cursor()

            c.execute("SELECT Name FROM Child")
            list_of_tuples = c.fetchall()

            # format list
            formated_list = []
            for tuple in list_of_tuples:
                formated_list.append(tuple[0])

            return formated_list


    def is_child_happy(self, child):
        return self.good_children[child]["delivered"]

    def deliver_toys_to_child(self, child):
        self.good_children[child]["delivered"] = True





if __name__ == "__main__":
    bag = LootBag()
    if sys.argv[1] == "add":
      bag.add_toy_for_child(sys.argv[3], sys.argv[2])
      # print(bag.get_by_child(sys.argv[3]))
    elif sys.argv[1] == "remove":
      bag.remove_toy_for_child(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == "ls":
      bag.get_by_child(sys.argv[2])











