// set the checkbox according to localstorage current value

$(function () {
  $('#togglebox').bootstrapToggle(function () {
    var autoSetting = localStorage["auto"];
  });
    
  $('#togglebox').change(function () {
    console.log("yay!");
    localStorage["auto"] = $(this).prop('checked');
  });
});