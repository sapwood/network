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
    
    dynamic={}

    for key in request.forms.keys():       
        if key.startswith('sub_name') or key.startswith('sub_size'):
            dynamic[key]=request.forms[key]
            
    subnets = {}

    for key, value in dynamic.items():
        if key.startswith('sub_name-'):
            index = int(key.split('-')[1])
            sub_dict = {'sub_name': value, 'sub_size': dynamic[f'sub_size-{index}']}
            subnets[index] = sub_dict

    print(f'THE FORMATTED DICT IS {subnets}')
    
    return template('submit',init=init,slash=slash,subnet_amount=subnet_amount,subnet_name=subnet_name,subnet_size=subnet_size,subnets=subnets)

@app.route('/static/<filename:path>')
def server_static(filename):
    return static_file(filename,root='./static')

@error(404)
def error404(error):
    return 'Nothing here. ERROR 404'


run(app,host='localhost', port=8080, debug=True)