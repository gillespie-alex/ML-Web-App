// This will contain the dynamic code that will make 'http' calls to our backend, and retrieve the data, the file acts like a server communicator

function onClickedEstimatePrice() {
  console.log("Estimate income button clicked");
  var age = document.getElementById("uiSqft");
  //var location = document.getElementById("uiLocations");
  var education = document.getElementById("uiLocations");
  var workclass = document.getElementById("uiLocations2");
  var marital_status = document.getElementById("uiLocations3");
  var estPrice = document.getElementById("uiEstimatedPrice");

  var url = "http://127.0.0.1:5000/predict_income"; 

  $.post(url, {
      age: parseFloat(age.value),
      workclass: workclass.value,
      education: education.value,
      marital_status: marital_status.value
  },function(data, status) {
      console.log(data.income);
      var income = data.income
      var res = ""
      if (income == 1) {
          res = ">= 50k"
      } else {
          res = "<= 50k"
      }
      estPrice.innerHTML = "<h2>" + res + "</h2>";
      console.log(status);
  });
}

function onPageLoad() {
  console.log( "document loaded" );
  var url = "http://127.0.0.1:5000/get_education_names"; 
  $.get(url,function(data, status) {
      console.log("got response for get_location_names request");
      if(data) {
          var locations = data.education;
          var uiLocations = document.getElementById("uiLocations");
          $('#uiLocations').empty();
          for(var i in locations) {
              var opt = new Option(locations[i]);
              $('#uiLocations').append(opt);
          }
      }
  });
  var url = "http://127.0.0.1:5000/get_workclass_names"; 
  $.get(url,function(data, status) {
      console.log("got response for get_workclass_names request");
      if(data) {
          var locations2 = data.workclass;
          var uiLocations2 = document.getElementById("uiLocations2");
          $('#uiLocations2').empty();
          for(var i in locations2) {
              var opt = new Option(locations2[i]);
              $('#uiLocations2').append(opt);
          }
      }
  });
  var url = "http://127.0.0.1:5000/get_marital_status"; 
  $.get(url,function(data, status) {
      console.log("got response for get_marital_status request");
      if(data) {
          var locations3 = data.marital_status;
          var uiLocations3 = document.getElementById("uiLocations3");
          $('#uiLocations3').empty();
          for(var i in locations3) {
              var opt = new Option(locations3[i]);
              $('#uiLocations3').append(opt);
          }
      }
  });
}

window.onload = onPageLoad;
