$(document).ready(function () {
  $.getJSON('https://swapi.co/api/films/?format=json', function (data) {
    const array = data.results;
    for (let i = 0; i < array.length; i++) {
      const filmName = array[i].title;
      $('#list_movies').append('<li>' + filmName + '</li>');
    }
  });
});
