from flask import Flask, render_template, redirect, url_for, abort, request, jsonify, flash
from flask_sqlalchemy import SQLAlchemy

root_url = 'http://localhost:5000'

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

db = SQLAlchemy(app)


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    feature1 = db.Column(db.Float)
    feature2 = db.Column(db.Float)
    category = db.Column(db.Integer)

    def __init__(self, feature1, feature2, category):
        self.feature1 = feature1
        self.feature2 = feature2
        self.category = category

    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


def create(body):
    if len(body) != 3:
        return jsonify({'error': 'Wrong number of inputs'}), 400

    try:
        if not (isinstance(body['feature1'], float)
                and isinstance(body['feature2'], float)
                and isinstance(body['category'], int)):
            return jsonify({'error': 'Invalid data'}), 400
    except KeyError:
        return jsonify({'error': 'Wrong inputs'}), 400

    data = Data(body['feature1'], body['feature2'], body['category'])
    db.session.add(data)
    db.session.commit()
    return {'id': data.id}, 201


def get_all():
    data = Data.query.all()
    if data is None:
        return []
    return [record.as_dict() for record in data]


def delete_record_func(record_id):
    data = Data.query.get(record_id)
    if data is None:
        return {'error': 'Record not found'}, 404

    db.session.delete(data)
    db.session.commit()
    return {'id': data.id}, 200


with app.app_context():
    db.create_all()
    # db.session.add(Data(1.0, 2.0, 1))
    # db.session.add(Data(1.0, 2.0, 1))
    # db.session.add(Data(1.0, 2.0, 1))
    # db.session.add(Data(1.0, 2.0, 1))
    # db.session.commit()

"""
========================API===============================
"""


@app.route('/api/data', methods=['GET', 'POST'])
def api_data():
    if request.method == 'POST':
        return create(request.json)

    return jsonify(get_all())


@app.route('/api/data/<int:record_id>', methods=['DELETE'])
def delete_record(record_id):
    res_body, status = delete_record_func(record_id)
    if status == 404:
        return {'error': 'Record not found'}, 404
    return jsonify(res_body), status


"""
========================APP===============================
"""


@app.errorhandler(404)
def not_found(status):
    return render_template('404.html'), 404


@app.route('/')
def all_data():
    data = []
    for record in get_all():
        data.append(record)
    return render_template('index.html', data=data)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        feature1 = request.form['feature1']
        feature2 = request.form['feature2']
        category = request.form['category']

        if not (feature1 and feature2 and category):
            flash('Please fill all the fields')
            return redirect(url_for('add'))

        try:
            feature1 = float(feature1)
            feature2 = float(feature2)
            category = int(category)
        except ValueError:
            flash('Invalid data')
            return redirect(url_for('add'))

        body = {'feature1': feature1, 'feature2': feature2, 'category': category}
        res_body, status = create(body)
        if status == 400:
            flash(res_body['error'])
        else:
            flash(f'Record with id {res_body["id"]} added successfully')
            return redirect(url_for('all_data'))
    return render_template('add-form.html')


@app.route('/delete/<int:record_id>', methods=['POST'])
def delete(record_id):
    res_body, status = delete_record_func(record_id)
    if status == 404:
        abort(404)
    flash(f'Record with id {res_body['id']} deleted successfully')
    return redirect(url_for('all_data'))


if __name__ == '__main__':
    app.run()
