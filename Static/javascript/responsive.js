 

$(window).on('resize load',function(e){
    if($(window).width()<700){$('.gallerytext').attr('data-aos','fade-out')}
    else{$('.gallerytext').css('data-aos','fade-left')}
}) 
$(window).on('resize load',function(e){
    if($(window).width()<700){$('.fadeleft').attr('data-aos','fade-out')}
    else{$('.fadeleft').css('data-aos','fade-left')}
}) 

$(window).on('resize load',function(e){
    if($(window).width()<700){  
        $('..mapboxgl-ctrl-geocoder--icon-search').attr('top','6px') 
        //$('.mapboxgl-ctrl-geocoder--input').attr('height','10') 
    }
    else{       
        $('..mapboxgl-ctrl-geocoder--icon-search').attr('top','13px') 
        //$('.mapboxgl-ctrl-geocoder--input').attr('height','25') 
    }
}) 

