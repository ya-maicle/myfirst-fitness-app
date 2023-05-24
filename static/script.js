$(document).ready(function(){
    $("#fitnessForm").submit(function(event){
      event.preventDefault();  // Prevent the form from submitting normally
  
      $("#loading").show();  // Show the loading indicator
  
      $.post("/", $(this).serialize(), function(data){
        $("#loading").hide();  // Hide the loading indicator
        window.location.href = "/response";  // Redirect the user to the response page
      });
    });
  });
  