from flask import Flask, render_template, request
import hackbright_app

app = Flask(__name__)

@app.route("/")
def get_github():
    return render_template("get_github.html")

@app.route("/grades")
def get_grades():
    hackbright_app.connect_to_db()
    student_github = request.args.get("github")
    rows = hackbright_app.report_card(student_github)
    html = render_template("student_grades.html", github=student_github , rows=rows)
    return html

@app.route("/projects")
def get_project_data():
    hackbright_app.connect_to_db()
    project_title = request.args.get("project_title")
    rows = hackbright_app.get_project_details(project_title)
    html = render_template("projects.html", project_title=project_title, rows=rows)
    return html

@app.route("/add_student")
def add_student():
    return render_template("new_student_form.html")

@app.route("/insert_student")
def insert_student():
    hackbright_app.connect_to_db()
    first_name = request.args.get("first_name")
    last_name = request.args.get("last_name")
    github = request.args.get("github")
    hackbright_app.make_new_student(first_name, last_name, github)
    html = render_template("student_info.html", first_name = first_name,
                                                 last_name = last_name,
                                                    github = github)
    return html

@app.route("/student")
def get_student():
    hackbright_app.connect_to_db()
    student_github = request.args.get("github")
    row = hackbright_app.get_student_by_github(student_github)
    html = render_template("student_info.html", first_name = row[0],
                                                 last_name = row[1],
                                                    github = row[2])
    return html

if __name__ == "__main__":
    app.run(debug=True)