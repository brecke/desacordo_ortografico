// set the checkbox according to localstorage current value

$(function () {
  $('#togglebox').bootstrapToggle(function () {
    var autoSetting = localStorage["auto"];
  });
    
  $('#togglebox').change(function () {
    localStorage["auto"] = $(this).prop('checked');
  });
});
