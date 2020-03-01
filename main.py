from flask import Flask, render_template, request, redirect
import json
from pathlib import Path

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":

        req = request.form

        name = req["name"].lower()

        data = read_json('users')
        if not name in data:
            return render_template(
            'user not found.html',
            username=name
            )

        return redirect("/user/{}".format(name))

    return render_template("home.html")

@app.route("/user/<name>/")
def getUser(name):
    data = read_json('users')
    if not name in data:
        return render_template(
        'user not found.html',
        username=name
        )

    list = data[name]['timetable']
    name = name.title()

    cssList = []
    for item in list:
        if item == "":
            cssList.append("")
        else:
            cssList.append("selected")
    return render_template(
    'timetable template.html', list=list, cssList=cssList, username=name)

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        req = request.form

        name = req["name"].lower()

        data = read_json('users')
        if not name in data:
            data[name] = {}

        data[name]['email'] = req["email"]
        data[name]['timetable'] = []

        for item in req:
            if item not in ['name', 'email']:
                data[name]['timetable'].append(req[item])

        write_json(data, 'users')

        return redirect("/user/{}".format(name))


    return render_template(
    'input form.html',
    nameList=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
    idList=['monday8am', 'tuesday8am', 'wednesday8am', 'thursday8am', 'friday8am', 'monday9am', 'tuesday9am', 'wednesday9am', 'thursday9am', 'friday9am', 'monday10am', 'tuesday10am', 'wednesday10am', 'thursday10am', 'friday10am', 'monday11am', 'tuesday11am', 'wednesday11am', 'thursday11am', 'friday11am', 'monday12pm', 'tuesday12pm', 'wednesday12pm', 'thursday12pm', 'friday12pm', 'monday1pm', 'tuesday1pm', 'wednesday1pm', 'thursday1pm', 'friday1pm', 'monday2pm', 'tuesday2pm', 'wednesday2pm', 'thursday2pm', 'friday2pm', 'monday3pm', 'tuesday3pm', 'wednesday3pm', 'thursday3pm', 'friday3pm', 'monday4pm', 'tuesday4pm', 'wednesday4pm', 'thursday4pm', 'friday4pm'],
    typeList=['text', 'text', 'text', 'text', 'text'],
    placeholder=['Please enter your monday class here', 'Please enter your tuesday class here', 'Please enter your wednesday class here', 'Please enter your thursday class here', 'Please enter your friday class here']
    )

def get_path():
    cwd = Path(__file__).parents[0]
    cwd = str(cwd)
    return cwd

def read_json(filename):
    cwd = get_path()
    with open(cwd+'/'+filename+'.json', 'r') as file:
        data = json.load(file)
    return data

def write_json(data, filename):
    cwd = get_path()
    with open(cwd+'/'+filename+'.json', 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    app.run(debug=True)
