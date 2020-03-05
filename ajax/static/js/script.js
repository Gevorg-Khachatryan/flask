$(document).ready(function(){

    $('form').on('submit',function(event){

         $.ajax({
            data:{
            name:$('#name').val(),
            email:$('#email').val(),
            },
            type:'POST',
            url:'/process'
            })
            .done(function(data){
            console.log(data)

                if(data.error){
                    $('#message').text(data.error)

                }
                else {
                    var x=$('#d1')
                    x.append($('<li>').text(data.name))
                    $('#message').text(data.name)
                }
            })
            event.preventDefault()



})



})