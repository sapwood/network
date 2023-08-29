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
    });

    

    var number=1;
    sub_letter='A';
    $('#add_rows').click(function(){
        
        
        var rows=parseInt($('#rows').val());

        if (!(isNaN(rows))){
            console.log('NOT NULL');
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

                // newDiv.append(sub_name);
                // newDiv.append(sub_size);
                number++;

                
                $('#subnet').append(sub_name);
                $('#subnet').append(sub_size);

            };
        };
    });

});

// document.addEventListener('DOMContentLoaded',function(){
//     var subnet=document.getElementById('subnet');
//     var add_button=document.getElementById('add_rows');
//     var number=0
    

//     add_button.addEventListener('click',function(){

//         var rows=parseInt(document.getElementById('rows').value)
//         if (!(isNaN(rows))){
//             for (var i=0; i<rows;i++){
                
//                 var newRow=document.createElement('input');
//                 newRow.type='text';
//                 newRow.name='test'+number;
//                 subnet.appendChild(newRow);
//                 number++;
//             };
//         };
        

//     });
    
// });