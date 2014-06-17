import sqlite3

DB = None
CONN = None


def report_card(student_github):
    query = """SELECT project_title, grade FROM Grades WHERE student_github = ?"""
    DB.execute(query, (student_github, ))
    row = DB.fetchone()
    while row:
        print """\
        Title: %s
        Grade: %d
        """ % (row[0], row[1])
        row = DB.fetchone()

def make_new_grade(student_github, project_title, grade):
    query = """INSERT into Grades values (?, ?, ?)"""
    DB.execute(query, (student_github, project_title, grade))
    CONN.commit()
    print "Successfully added grade: %s %s" % (student_github, project_title)

def get_grade_by_project(student_github, project_title):
    query = """SELECT grade FROM Grades WHERE student_github = ? AND project_title = ?"""
    DB.execute(query, (student_github, project_title))
    row = DB.fetchone()
    print """\
    Grade: %s"""% row[0]

def get_project_by_title(title):
    query = """SELECT title, description, max_grade FROM Projects WHERE title = ?"""
    DB.execute(query, (title, ))
    row = DB.fetchone()
    print """\
    Title: %s
    Description: %s
    Total points: %d
    """ % (row[0], row[1], row[2])

def make_new_project(title, description, max_grade):
    query = """INSERT into Projects (title, description, max_grade) values (?, ?, ?)"""
    DB.execute(query, (title, description, max_grade))
    CONN.commit()
    print "Successfully added project: %s %s" % (title, description)

def make_new_student(first_name, last_name, github):
    query = """INSERT into Students values (?, ?, ?)"""
    DB.execute(query, (first_name, last_name, github))
    CONN.commit()
    print "Successfully added student: %s %s" % (first_name, last_name)

def get_student_by_github(github):
    query = """SELECT first_name, last_name, github FROM Students WHERE github = ?"""
    DB.execute(query, (github,))
    row = DB.fetchone()
    print """\
    Student: %s %s
    Github account: %s"""%(row[0], row[1], row[2])

def connect_to_db():
    global DB, CONN
    CONN = sqlite3.connect("hackbright.db")
    DB = CONN.cursor()

def main():
    connect_to_db()
    command = None

    while command != "quit":
        command = raw_input("HBA Database> ")
        if command != "quit":
            arg = raw_input("args> ")
            args = []

            while arg != "":
                args.append(arg)
                arg = raw_input("args> ")

        if command == "student":
            get_student_by_github(*args) 
        elif command == "new_student":
            make_new_student(*args)
        elif command == "projects":
            get_project_by_title(*args)
        elif command == "new_project":
            make_new_project(*args)
        elif command == "grade":
            get_grade_by_project(*args)
        elif command == "new_grade":
            make_new_grade(*args)
        elif command == "report_card":
            report_card(*args)


    CONN.close()

if __name__ == "__main__":
    main()
