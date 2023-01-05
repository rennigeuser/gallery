const buildCard = (() => {

    let id = 0;

    function buildCard({author, likes, title, icon, icon_alt, created_at}) {
        ++id;

        const col_div = document.createElement('div');
        col_div.classList.add('col');

        const fdiv = document.createElement('div');
        fdiv.classList.add('card');
        fdiv.style.width = '20rem'

        const a_btn = document.createElement('a');
        a_btn.classList.add('btn');
        a_btn.setAttribute('data-bs-toggle', 'collapse');
        a_btn.setAttribute('href', `#collapse_${id}`);
        a_btn.setAttribute('role', 'button');
        a_btn.setAttribute('aria-expanded', 'false');

        const inner_img = document.createElement("img");
        inner_img.classList.add('card-img-top');
        inner_img.setAttribute('src', icon);
        inner_img.setAttribute('alt', icon_alt);

        const cdiv = document.createElement('div');
        cdiv.classList.add('collapse');
        cdiv.setAttribute('id', `collapse_${id}`);

        const cdiv_child = document.createElement('div');
        cdiv_child.classList.add("card", "card-body");
        cdiv_child.innerText = title;

        
        cdiv.appendChild(cdiv_child);
        a_btn.appendChild(inner_img);
        fdiv.appendChild(a_btn);
        fdiv.appendChild(cdiv);
        col_div.appendChild(fdiv);

        return col_div;
    }

    return buildCard;
})()


export default buildCard;