$(document).ready(function () {
  $('#add_item').on('click', function () {
    $('UL.my_list').append('<li>Item</li>');
  });
  $('#remove_item').on('click', function () {
    $('UL.my_list li:last').remove();
  });
  $('#clear_list').on('click', function () {
    $('UL.my_list li').remove();
  });
});
