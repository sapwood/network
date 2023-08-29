from bottle import Bottle, run, template, static_file, error, request
import math
import ipaddress
app=Bottle()

@app.route('/')
def index():
    return template('index')

@app.route('/submit', method='POST')
def submit():
         
    init=request.forms.get('init_network')
    init_slash=request.forms.get('init_slash')
    subnet_name=request.forms.get('subnet_name')
    subnet_size=request.forms.get('subnet_size')

    print (f'First SLASH is {init_slash}')
    
    dynamic={}

    for key in request.forms.keys():       
        if key.startswith('sub_name') or key.startswith('sub_size'):
            value=request.forms[key]
            
            dynamic[key]=value
            
    subnets = {}

    for key, value in dynamic.items():
        if key.startswith('sub_name-'):
            index = int(key.split('-')[1])
            sub_dict = {'sub_name': value, 'sub_size': dynamic[f'sub_size-{index}']}
            subnets[index] = sub_dict

    #Sort the dict in descending order
    sorted_result = sorted(subnets.items(), key=lambda item: (-int(item[1]['sub_size']), item[0]))
    subnets = {index: sub_dict for index, (_, sub_dict) in enumerate(sorted_result, start=1)}


    first_iteration=True
    subnet_res={}
    err=''
    for key in subnets:
        size=int(subnets[key]['sub_size'])
        fac=math.ceil(math.log2(size))
        range=math.pow(2,fac)
        if range <= size+2:
            fac+=1
        
        usable_address=int(math.pow(2,fac)-2)
        
        slash=32-fac
        
        if first_iteration:
           
            try:
                network=ipaddress.IPv4Network(f'{init}/{slash}')

            except ValueError as e:
               err=f'The network address or slash is not correct. {e}'
               break

            subnet_size = 2 ** (32 - slash)
            next_subnet_network_address = ipaddress.IPv4Address(int(network.network_address) + subnet_size)
            first_iteration=False
               
        else:
           
            network=ipaddress.IPv4Network(f'{next_subnet_network_address}/{slash}')
            subnet_size = 2 ** (32 - slash)
            next_subnet_network_address = ipaddress.IPv4Address(int(network.network_address) + subnet_size)


        net_address=f'{network.network_address}/{slash}'
        mask=f'{network.netmask}'
        first_address=f'{network[1]}'
        last_address=f'{network[-2]}'


        subnet_res[subnets[key]['sub_name']]={'net_address':net_address,'mask':mask,'first_address':first_address,'last_address':last_address,'usable':usable_address}

    print (f'FINAL SLASH is {init_slash}')
    return template('submit',init=init,slash=init_slash,subnet_res=subnet_res,err=err)

@app.route('/static/<filename:path>')
def server_static(filename):
    return static_file(filename,root='./static')

@error(404)
def error404(error):
    return 'Nothing here. ERROR 404'


run(app,host='localhost', port=8080, debug=True)