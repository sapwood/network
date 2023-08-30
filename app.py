from flask import Flask, request ,render_template
import math
import ipaddress

app=Flask(__name__)

@app.get('/')
def hello():
	return render_template('index.html')


@app.post('/submit')
def submit():
         
    init=request.form['init_network']
    init_slash=request.form['init_slash']
    # subnet_name=request.form['sub_name-0']
    # subnet_size=request.form['sub_size-0']

   
    
    dynamic={}

    for key in request.form:       
        if key.startswith('sub_name') or key.startswith('sub_size'):
            value=request.form[key]
            
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

    
    return render_template('submit.html',init=init,slash=init_slash,subnet_res=subnet_res,err=err)




@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404

app.run(host='localhost', port=5000, debug=True)