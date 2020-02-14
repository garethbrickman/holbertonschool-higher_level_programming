$(document).ready(function () {
  $('#add_item').on('click', function () {
    $('UL.my_list').append('<li>Item</li>');
  });
});
