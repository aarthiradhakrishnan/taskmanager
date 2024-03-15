from flask import Flask, render_template, request, redirect
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    file=pd.read_csv('storage.csv')  
    return render_template('main.html', dataframe=file)

@app.route('/submit', methods=['POST'])
def submit():
    file = pd.read_csv('storage.csv', index_col='index')
    if request.method == 'POST':
        data = request.form.to_dict()
        data['status'] = ''
        data['remark'] = ''
        data['completed'] = False
        print(data)
        file=file._append(data,ignore_index=True)
        file.reset_index(inplace=True)
        file.to_csv('storage.csv', index=False)

    return redirect('/')

@app.route('/update', methods=['POST'])
def update():
    file = pd.read_csv('storage.csv', dtype=str)
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        index = data['index']
        print(index)
        print(file)
        file.loc[file['index'] == index, 'status'] = data['status']
        file.loc[file['index'] == index, 'remark'] = data['remark']
        file.loc[file['index'] == index, 'completed'] = data['completed']
        file.to_csv('storage.csv', index=False)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
