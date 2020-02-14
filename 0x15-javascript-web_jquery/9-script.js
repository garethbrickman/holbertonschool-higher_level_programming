$(document).ready(function () {
  $.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
    const translation = data.hello;
    $('#hello').append(translation);
  });
});
