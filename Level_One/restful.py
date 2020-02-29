from flask import Flask,jsonify,request
app = Flask(__name__)

students = [{'name' : 'Putter' } , {'name' : 'Fluke'}]

@app.route('/', methods=['GET'])
def test():
    return jsonify({'message' : 'It works!'})

@app.route('/students', methods=['GET'])
def returnAll():
    return jsonify({'students' : students})

@app.route('/students/<string:name>', methods=['GET'])
def returnOne(name):
    stds = [student for student in students if student['name'] == name]
    return jsonify({'student' : stds[0]})


@app.route('/students', methods=['POST'])
def addOne():
    student = {"name" : request.json["name"]}
    print(student)
    students.append(student)
    return jsonify({'students' : students})
if __name__ == '__main__':
    app.run(debug=True)
