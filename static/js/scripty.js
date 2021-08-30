$(document).ready(function(){
    console.log("loaded");
    $.material.init();

    $(document).on("submit", "#register-form", function(e){
        e.preventDefault()
        console.log("form submitted");
        var form = $("#register-form").serialize();
        $.ajax({
            url: '/postregistration',
            type: 'POST',
            data: form,
            success: function(response){
                console.log(response);
            }
        });
    });
    $(document).on("submit", "#login-form", function(e){
        e.preventDefault()
        console.log("form submitted");
        var form = $(this).serialize();
        $.ajax({
            url: '/check-login',
            type: 'POST',
            data: form,
            success: function(res){
                if(res == "error"){
                    alert("Could not log in");
                }else{
                    console.log("login as",res);
                }
            }
        });
    });
});