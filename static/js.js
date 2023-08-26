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

    

    var number=0
    $('#add_rows').click(function(){
        
        var rows=parseInt($('#rows').val());

        if (!(isNaN(rows))){
            console.log('NOT NULL');
            for (var i=0; i<rows;i++){
                
                var newRow=document.createElement('input');
                newRow.type='text';
                newRow.name='test'+number;
                $('#subnet').append(newRow);
                number++;
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