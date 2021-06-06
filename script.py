from flask import Flask,render_template

app = Flask(__name__)

@app.route('/home')
def home():
	return render_template('index.html')

host_add = '127.0.0.1'
port_add = 5000


# Running the app
if __name__ =="__main__":
    app.run(host=host_add, port=port_add, debug=True)