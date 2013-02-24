// set the checkbox according to localstorage current value
$(document).ready(function() {
    $('#mySwitch').bootstrapSwitch('setState', function() {
        var autoSetting = localStorage["auto"];
        return autoSetting == "true";
    });
});

// handle checkbox event
$('#mySwitch').on('switch-change', function (e, data) {
    var $el = $(data.el);
    var value = data.value;
    localStorage["auto"] = value;
});