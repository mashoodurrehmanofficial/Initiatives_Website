
document.addEventListener('DOMContentLoaded', function() {
    var collapsibleElem = document.querySelector('.collapsible');
    var collapsibleInstance = M.Collapsible.init(collapsibleElem, {Collapsible:true});
      var elems = document.querySelectorAll('.dropdown-trigger');
      var instances = M.Dropdown.init(elems, {
        'Dropdown': true,
        'coverTrigger':false
      });
    });
    document.addEventListener('DOMContentLoaded', function() {
      var elems = document.querySelectorAll('.collapsible');
      var instances = M.Collapsible.init(elems, {
        Collapsible:true
      });
    });
    document.addEventListener('DOMContentLoaded', function() {
      var elems = document.querySelectorAll('.sidenav');
      var instances = M.Sidenav.init(elems, {
        Sidenav:true
      });
    });
    document.addEventListener('DOMContentLoaded', function() {
      var elems = document.querySelectorAll('.sidenav');
      var instances = M.Sidenav.init(elems, {
        Sidenav:true
      });
    });
    document.addEventListener('DOMContentLoaded', function() {
      var elems = document.querySelectorAll('select');
      var instances = M.FormSelect.init(elems, {
        "FormSelect":true
      });
    });
    document.addEventListener('DOMContentLoaded', function() {
      var elems = document.querySelectorAll('.modal');
      var instances = M.Modal.init(elems, {
        Modal:true,
        onOpenStart: function(){ 
        }
      });
    });
    document.addEventListener('DOMContentLoaded', function() {
      var elems = document.querySelectorAll('.datepicker');
      var instances = M.Datepicker.init(elems, {
        Datepicker:true,
        showClearBtn:true,
        autoClose:true,

      });
    });
 


function Populate_Initiative_Profile(data){
  $('#modal-content').html('')
  $('#modal-content').html(`
  
  <!-- Title and Buttons -->
  <div style="display:flex;flex-direction: row;align-items: center;justify-content: space-between">
    <h4 >${data.title}</h4>
    <div id='my_status_div' style="display:flex;flex-direction: column;align-items: center;justify-content: space-between">
        
    <button id='join_btn' class="btn green"  style="border-radius: 50px;" >Join +</button>  
      
    </div>
  </div>
  <br>

  <!-- Info Cards -->

  <div class="row">
    <div class="col s6 m4 l4"> 
      <div class="z-depth-2" style="margin: 0px 10%;padding:0px 5%;border-radius: 50px;display:flex;flex-direction: row;justify-content: start;align-items:center">
          <i class="material-icons left">date_range</i>
          <p class="right" style="margin: 4%;">${data.event_date}</p>
      </div>
    </div>    <div class="col s6 m4 l4"> 
      <div class="z-depth-2" style="margin: 0px 10%;padding:0px 5%;border-radius: 50px;display:flex;flex-direction: row;justify-content: start;align-items:center">
          <i class="material-icons left">person_add</i>
          <p class="right" style="margin: 4%;" id='enrolled_count_text'>${data.enrolled} enrolled</p>
      </div>
    </div>
    <div class="col s6 m4 l4"> 
      <div class="z-depth-2" style="margin: 0px 10%;padding:0px 5%;border-radius: 50px;display:flex;flex-direction: row;justify-content: start;align-items:center">
          <i class="material-icons left">person_pin</i>
          <p class="right" style="margin: 4%;">${data.owner}</p>
      </div>
    </div>

    </div>





<br> 

<!-- Description and Map -->
<div class="row">
  <div class="col s12 m12 l6">  
    <p>${data.description}</p>
  </div>
  <div class="col s12 m12 l6">
    <div class="z-depth-2">
         <div id="initiative_card_profile_map" style="width: 100% !important;"></div>
    </div>
       
  </div>
</div>

  
  `) 
 
  if (data.my_status) {
    $('#my_status_div').html('')
    $('#my_status_div').html(`
      <button id='leave_btn' class="btn grey"  style="border-radius: 50px;" >Leave</button>  
    `)
    
  }
 

  function Handle_Membership(membership_status,initiative_id){ 
    $.ajax({
      url: "/api/Handle_Membership/",
      data: {
        'membership_status':membership_status, 
        'initiative_id':initiative_id, 
      },
      method: 'GET',
      success: function (data) { 
        var results = data.results
        var enrolled = data.enrolled
        $('#enrolled_count_text').html(`${enrolled} enrolled`)
        $('#my_status_div').html('')
        if(results=='added'){
          $('#my_status_div').html(`
            <button id='leave_btn' class="btn grey"  style="border-radius: 50px;" >Leave</button>  
          `)
          
        }else if(results=='removed'){
          $('#my_status_div').html(`
          <button id='join_btn' class="btn green"  style="border-radius: 50px;" >Join +</button>  
          `)

        }else if(results=='auth_error'){
          alert("User must be logged in to to perform this functionality")
        }
        
        
      $('#join_btn, #leave_btn').click(function(e){
        membership_status = this.id
        Handle_Membership(membership_status,initiative_id)
      }) 
  }})
}

  $('#join_btn, #leave_btn').click(function(e){
    membership_status = this.id
    Handle_Membership(membership_status,data.id)
  }) 
  
  // $('#leave_btn').click(function(e){ 
  //   alert(this.id)
  //   // Handle_Membership(e.id)
  // }) 
 
  

  mapboxgl.accessToken = 'pk.eyJ1IjoibWFzaG9vZDEyMyIsImEiOiJja3JpcTAwcXE0M3YyMzByMmxuM25yaGlkIn0.-7kWuyQlkkj0m9X-EuNnFw';
  const initiative_card_profile_map = new mapboxgl.Map({
  container: 'initiative_card_profile_map', // container ID
  style: 'mapbox://styles/mapbox/streets-v11', // style URL
  center: [data.longitude, data.latitude], // starting position [lng, lat]
  zoom: 9 // starting zoom
  });
  const initiative_lication = new mapboxgl.Marker({
    'color':'#4668F2'
  })
  .setLngLat([data.longitude,data.latitude])
  .addTo(initiative_card_profile_map);

  // initiative_card_profile_map.on('idle',function(){ 
  //   initiative_card_profile_map.resize()
  //   })
  initiative_card_profile_map.on('load',function(){
    initiative_card_profile_map.resize()
    
  })
 
  $('#main_page_initiative_card_profile_btn')[0].click()
 

}


  


var markers = []
function Extract_Cluster(map,ClickableMarker){
  for(var x=0;x<markers.length;x++){
      markers[x].remove();
    } 
    markers = []
  
  var longitude = localStorage.getItem("main_page_filter_longitude")
  var latitude = localStorage.getItem("main_page_filter_latitude")
  var range_in_km = localStorage.getItem("main_page_filter_range_in_km")
  var date = localStorage.getItem("main_page_filter_date")
  var checked_catgories = localStorage.getItem("main_page_filter_checked_catgories")
  $.ajax({
    url: "/api/get_cluster/",
    data: {
      'longitude':longitude,
      'latitude':latitude,
      'range_in_km':range_in_km,
      'date':date,
      'checked_catgories':checked_catgories,
    },
    method: 'GET',
    success: function (data) { 
      
      var cluster = data.results 
      cluster.forEach((initative) => {
        var marker = new ClickableMarker({
          'color':'#4668F2'
        })
          .setLngLat([initative.longitude,initative.latitude])
          .onClick(() => {   
            Populate_Initiative_Profile(initative)
          

 
           console.log("initative.longitude")
          })
          markers.push(marker)
      }); 
        $( ".mapboxgl-marker.mapboxgl-marker-anchor-center" ).remove();
         
      for(var x=0;x<markers.length;x++){
        markers[x].addTo(map);
      }
      
    }
  });
}