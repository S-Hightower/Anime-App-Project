var animeForm = document.querySelector('#anime-form')
animeForm.addEventListener('submit', function(e){
    e.preventDefault('')

let anime = document.querySelector('#anime-name').value
    fetch(`https://api.myanimelist.net/v2/anime?q=${anime}`)
    .then( response => response.json())
    .then( data => {
        var img = data['images']['jpg']['image_url']
        var imgdiv = document.querySelector('#anime-img')
        imgdiv.innerHTML = `<img src = "${img}" alt="">`
    })
})