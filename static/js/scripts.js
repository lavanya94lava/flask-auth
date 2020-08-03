
$("#signup_form").submit(function(e){

    e.preventDefault();

    console.log("hiii  AJX")
    var $form = $(this);
    var $error = $form.find(".error");
    console.log($form)
    var data = $form.serialize();

    $.ajax({
        url:"/user/signup",
        type:"POST",
        data: data,
        dataType:"json",
        success: function(res){
            window.location.href ="/dashboard/";
        },
        error:function(res){
            console.log(res)
            $error.text(res.responseJSON)
        }
    })

})

