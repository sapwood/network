$(document).ready(function(){
    $('#myform').submit(function(event){
        event.preventDefault();
        var formData = $("#myform").serialize();
        var network=document.getElementById('init_network');
        asIPv4(network);
        $.ajax({
            type:'POST',
            url:'/submit',
            data:formData,
            success:function(response){
                $('#result').html(response);
            }
        });

        $('html, body').animate({
            scrollTop: $("#result").offset().top
         }, 1000);
    });

    

    var number=1;
    sub_letter='A';
    $('#add_rows').click(function(){
        
        
        var rows=parseInt($('#rows').val());

        if (!(isNaN(rows))){
            
            for (var i=0; i<rows;i++){
                // var newDiv=document.createElement('div');
                
                    
                var sub_name=document.createElement('input');
                sub_name.type='text';
                sub_name.name='sub_name-'+number;
                sub_name.className="cell";

                var code=sub_letter.charCodeAt(0);
                sub_letter=String.fromCharCode(code+1);
                sub_name.value=sub_letter;
                sub_name.required=true;
                
                
                var sub_size=document.createElement('input');
                sub_size.type='number';
                sub_size.name='sub_size-'+number;
                sub_size.className="cell";
                sub_size.required=true;

                var delete_button=document.createElement('button');
                delete_button.className="delete_bt cell";
                delete_button.type="button";
                delete_button.id='remove-'+number;
                var icon=document.createElement('i');
                icon.className="fa-solid fa-trash-can";
                
                delete_button.append(icon);
                delete_button.append(' Remove');
                



                // newDiv.append(sub_name);
                // newDiv.append(sub_size);
                number++;

                
                $('#subnet').append(sub_name);
                $('#subnet').append(sub_size);
                $('#subnet').append(delete_button);

            };
        };
    });



});

$(document).on('click', '.delete_bt', function(){
    var bt_id=$(this).attr('id');
    
    var num=bt_id.split('-')[1];
    
    var delete_name=$('input[name="sub_name-'+num+'"]');
    var delete_size=$('input[name="sub_size-'+num+'"]');
    delete_name.remove();
    delete_size.remove();
    $(this).remove()
});

$(document).on('click','.option',function(event){
    event.preventDefault();
    var answer=$(this).text();
    
    $.ajax({
        type:'POST',
        url:'/checkanswer',
        data:{answer:answer},
        success:function(response){
            $('.q_container').html(response);
        }
    });
});



