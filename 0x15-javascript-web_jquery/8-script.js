$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
    $('UL#list_movies').append(...data.result.app(movie => `<li>${movie.title}</li>`));
});
