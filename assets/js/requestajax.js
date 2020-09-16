window.addEventListener("DOMcontentLoaded", function(){
    load_page('admin_view')

    document.querySelectorAll('.testform').forEach(link =>{
        link.onclick = () => {
            load_page(link.dataset.page);
            return false;
        };
    });
});

function load_page(name) {
    const request = new XMLHttpRequest();
    request.open('GET', `/${name}`);
    request.onload = () => {
        const response = request.responseURL;
        document.querySelector('#main_id').innerHTML = response;

        document.title = name;
        history.pushState({'title':name, 'text': response}, name, name);
    };

    request.send();
}

var c = 3;
console.log(c)