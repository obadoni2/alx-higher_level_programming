$.get('https://swapi.co/api/people/5/?format=json', function (data){
    $('DiV#character').text(data.name);
});