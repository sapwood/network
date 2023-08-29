
<h1>{{init}}/{{slash}}</h1>


<div>
    <div class="table">
        <div class="cell head">Subnet Name</div>
        <div class="cell head">Network Address</div>
        <div class="cell head">Subnet Mask</div>
        <div class="cell head">First Address</div>
        <div class="cell head">Last Address</div>
        <div class="cell head">Usable</div>

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


