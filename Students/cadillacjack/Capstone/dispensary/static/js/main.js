jQuery(document).ready(function($){

    if (sessionStorage.getItem('advertOnce') !== 'true') {
    //sessionStorage.setItem('advertOnce','true');
      $('.box').show();
    }else{
      $('.overlay-verify').remove();
      $('.age-modal').remove();
    }
     
    $('#refresh-page').on('click',function(){
    $('.box').hide();
    sessionStorage.setItem('advertOnce','true');
    });
      
    $('#reset-session').on('click',function(){
    $('.box').show();
    sessionStorage.setItem('advertOnce','');
    });
     
    });