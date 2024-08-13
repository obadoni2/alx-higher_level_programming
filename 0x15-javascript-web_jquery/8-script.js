$.get('https://swapi.co/api/film=json', function (data){
    $('Ul#list_movies').append(...data.result.map(movies => ` <li>${movie.title}</li>`));
    
})