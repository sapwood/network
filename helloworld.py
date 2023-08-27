from bottle import Bottle, run, template, static_file, error, request
import math
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

    sorted_result = sorted(subnets.items(), key=lambda item: (-int(item[1]['sub_size']), item[0]))

    subnets = {index: sub_dict for index, (_, sub_dict) in enumerate(sorted_result, start=1)}
    for key in subnets:
        size=int(subnets[key]['sub_size'])
        fac=math.ceil(math.log2(size))
        range=math.pow(2,fac)
        if range <= size+2:
            fac+=1
        
        

        




    
    return template('submit',init=init,slash=slash,subnet_amount=subnet_amount,subnets=subnets)

@app.route('/static/<filename:path>')
def server_static(filename):
    return static_file(filename,root='./static')

@error(404)
def error404(error):
    return 'Nothing here. ERROR 404'


run(app,host='localhost', port=8080, debug=True)