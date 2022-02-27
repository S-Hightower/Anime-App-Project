var animeForm = document.querySelector('#anime-form')
animeForm.addEventListener('submit', function(e){
    e.preventDefault('')

let anime = document.querySelector('#anime-name').value
    fetch(`https://api.myanimelist.net/v2/anime/${anime}`)
    .then( response => response.json())
    .then( data => {
        
    })
})