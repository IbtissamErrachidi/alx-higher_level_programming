$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  type: 'GET',
  success: function (result) {
    $.each(result.results, function (index, film) {
      $('#list_movies').append('<li>' + film.title + '</li>');
    });
  }
});
