function abre_fecha_modal_pronuncia(id){
    modal = document.getElementById('card_verso'+ id)
    if (modal.style.display === 'block') {
        modal.style.display = 'none';
    } else {
        modal.style.display = 'block';
    }
}

function abre_fecha_modal_portugues(id){
    modal = document.getElementById('modal_portugues'+ id)
    if (modal.style.display === 'block') {
        modal.style.display = 'none';
    } else {
        modal.style.display = 'block';
    }

}