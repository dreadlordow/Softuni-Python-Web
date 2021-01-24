function expandCollapse(){
    if (this.nextElementSibling.style.display === 'none'){
        this.nextElementSibling.style.display = '';
    } else {
        this.nextElementSibling.style.display = 'none';
    }
}

function initExpand (){
    const items =  [...document.getElementsByClassName('todo-title')];
    items.forEach(item =>{
        item.addEventListener('click', expandCollapse);
    });
}

initExpand()