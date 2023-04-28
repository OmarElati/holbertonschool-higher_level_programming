$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', (data) => {
  const movies = data.results;
  for (const movie of movies) {
    $('<li></li>').text(movie.title).appendTo('UL#list_movies');
  }
});
