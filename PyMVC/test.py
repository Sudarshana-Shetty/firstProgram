from flask import Flask
app = Flask(__name__)

# @app.route('/ghi/')
# def hello_world():
#     return 'hello %s'

# app.add_url_rule(‘/’, ‘hello’, hello_world)    
# if __name__ == '__main__':
#     app.run(debug=True)
    
@app.route('/hello')
def hello_world():
   return 'hello world'
app.run(debug=True)