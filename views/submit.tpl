
<h1>{{init}}/{{slash}}</h1>


<div>
    <div class="table">
        <div class="cell">Subnet Name</div>
        <div class="cell">Network Address</div>
        <div class="cell">Subnet Mask</div>
        <div class="cell">First Address</div>
        <div class="cell">Last Address</div>
        <div class="cell">Usable</div>

        %for key in subnet_res:
            <div class="cell">{{key}}</div>

            <div class="cell">{{subnet_res[key]['net_address']}}</div>
            <div class="cell">{{subnet_res[key]['mask']}}</div>
            <div class="cell">{{subnet_res[key]['first_address']}}</div>
            <div class="cell">{{subnet_res[key]['last_address']}}</div>
            <div class="cell">{{subnet_res[key]['usable']}}</div>
        %end
    </div>
</div>


