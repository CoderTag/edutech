$(document).ready(function () {
    $(window).resize(function () {
        if ($(window).width() < 768) {
            $('.sidebarCollapse').on('click', function () {
                $("#sidebar").toggleClass('active');        
            });           
        }
        else{
            $('#sidebar').on('mouseenter', function () {
                $('#sidebar,#content').removeClass('active');        
            });
            $('#sidebar').on('mouseleave', function () {
                $('#sidebar,#content').addClass('active');        
            });
        }
    }).resize(); //to initialize the value

});