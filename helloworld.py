from bottle import Bottle, run, template, static_file, error, request
app=Bottle()

@app.route('/')
def index():
    return template('index')

@app.route('/submit', method='POST')
def submit():
         
    init=request.forms.get('init_network')
    slash=request.forms.get('init_slash')
    subnet_amount=request.forms.get('subnet_amount')
    subnet_name=request.forms.get('subnet_name')
    subnet_size=request.forms.get('subnet_size')
        
    
    
    return template('submit',init=init,slash=slash,subnet_amount=subnet_amount,subnet_name=subnet_name,subnet_size=subnet_size)

@app.route('/static/<filename:path>')
def server_static(filename):
    return static_file(filename,root='./static')

@error(404)
def error404(error):
    return 'Nothing here. ERROR 404'


run(app,host='localhost', port=8080, debug=True)