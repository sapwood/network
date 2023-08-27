$(document).ready(function(){
    $('#myform').submit(function(event){
        event.preventDefault();
        var formData = $("#myform").serialize();
        $.ajax({
            type:'POST',
            url:'/submit',
            data:formData,
            success:function(response){
                $('#result').html(response);
            }
        });
    });

    

    var number=1
    $('#add_rows').click(function(){
        
        var rows=parseInt($('#rows').val());

        if (!(isNaN(rows))){
            console.log('NOT NULL');
            for (var i=0; i<rows;i++){
                var newDiv=document.createElement('div');
                
                    
                var sub_name=document.createElement('input');
                sub_name.type='text';
                sub_name.name='sub_name-'+number;
                
                
                var sub_size=document.createElement('input');
                sub_size.type='text';
                sub_size.name='sub_size-'+number;

                newDiv.append(sub_name);
                newDiv.append(sub_size);
                number++;

                
                $('#subnet').append(newDiv);

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