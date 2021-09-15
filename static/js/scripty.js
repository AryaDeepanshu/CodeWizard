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
                    window.location.href = "/";
                }
            }
        });
    });
    $(document).on("click", "#logout-link", function(e){
        e.preventDefault()
        console.log("form submitted");
        var form = $(this).serialize();
        $.ajax({
            url: '/logout',
            type: 'GET',
            success: function(res){
                if(res == "success"){
                    window.location.href = "/login"
                }else{
                    alert("something went wrong");
                }
            }
        });
    });
    $(document).on("submit", "#post-activity", function(e){
        e.preventDefault();
        form = $(this).serialize();
        $.ajax({
            url: '/post-activity',
            type: 'POST',
            data: form,
            success: function(res){
                console.log(res)
                window.location.href = window.location.href;
            }
        });
    });

    $(document).on("submit", "#settings-form", function(e){
        e.preventDefault();
        form = $(this).serialize();
        $.ajax({
            url: '/update-settings',
            type: 'POSt',
            data: form,
            success: function(res){
                if(res == 'success'){
                    window.location.href = window.location.href;
                }else{
                    alert(res);
                }
            }
        })
    })
});