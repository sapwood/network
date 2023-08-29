



<div>
    % if len(subnet_res)!=0:
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
    %else:
        %if len(err)!=0:
        <div class="error-msg">
            <i class="fa fa-times-circle"></i>
            {{err}}
        </div>
        %end
    %end
</div>


