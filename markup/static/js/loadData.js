import buildCard from './buildCard.js'


const loadData = async (url) => {

    return await (async () => await (await fetch(url)).json())()
    .then(({results, next}) => {
        return {next: next, cards: results.map((post) => buildCard(post))}
    })
    .then(({next, cards}) => {
        const gallery_div = document.getElementById('gallery')
        cards.forEach((element) => { gallery_div.appendChild(element) });
        return next
    })
}


export default loadData;