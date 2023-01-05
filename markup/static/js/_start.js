import loadData from "./loadData.js";

// (() => {
//     let url = 'api/gallery/v1/posts/';

//     const btn = document.getElementById('loadData')

//     btn.addEventListener('click', (e) => {
//         if (!url) return
        
//         loadData(url).then((value) => url = value)
//     })   
// })();

(() => {
    let url = 'api/gallery/v1/posts/'; // initial url (hardcode)

    const handleScroll = () => {
        if (!url) return
        if(window.scrollY + window.innerHeight >= document.documentElement.scrollHeight) {
            loadData(url).then((value) => url = value)
        }
    }

    window.addEventListener('scroll', handleScroll)
})();



