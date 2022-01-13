// var url = 'https://34.86.68.175/api/bookbanks/active/?'
var url = 'http://192.168.29.172:8000/api/bookbanks/active/?'
var scholarships;
var page = 1
var modal = document.querySelector('.modal')
var modalTitle = document.querySelector('.modal-title')
var modalDetails = document.querySelector('.modal-body')
var displayItems = ['updated_on', 'books', 'state', 'district', 'address', 'content', 'contact', 'site_url']
var body = document.getElementsByTagName('body')
var backDrop = document.getElementById('backDrop')
var elem = document.querySelector('.sidenav');
var instance = new M.Sidenav(elem);

getscholar(url, page = 1)
    .catch(error => {
        console.log(error)
    })

async function getscholar(url, page = 1) {
    url += `page=${page}`
    console.log(url)
    const schlist = await fetch(url)
    const resp = await schlist.json()
    scholarships = {
        ...resp
    }
    console.log(resp);
    createCard(scholarships)
    createPagination(scholarships.count)
}

async function getfields(url) {

    // var filterFields = 'https://34.86.68.175/api/bookbanks/filterFields/'
    var filterFields = 'http://192.168.29.172:8000/api/bookbanks/filterFields/'
    var fields = await fetch(filterFields)
    var b = await fields.json()

    try {
        var state = document.getElementById('states')
        for (var i = 0; i < b['state'].length; i++) {
            var option = document.createElement('option')
            option.innerHTML = b['state'][i].name
            state.appendChild(option)
        }    
    } catch (error) {
        console.log(error)
    }
    
    /* var district = document.getElementById('districts')
    for (var i = 0; i < b['district'].length; i++) {
        var option = document.createElement('option')
        option.innerHTML = b['district'][i].name
        district.appendChild(option)
    } */

    try {
        var books = document.getElementById('books')
        for (var i = 0; i < b['books'].length; i++) {
            var option = document.createElement('option')
            option.innerHTML = b['books'][i].name
            books.appendChild(option)
    }
    } catch (error) {
        console.log(error)
    }
    
}

getfields()

var form = document.getElementById("filterForm");
form.addEventListener('submit', (e) => {
    e.preventDefault();
    // url = "https://34.86.68.175/api/bookbanks/filter/?"
    url = "http://192.168.29.172:8000/api/bookbanks/filter/?"
    var filterVal = {
        state: document.getElementById('states').value,
        district: document.getElementById('districts').value,
        books: document.getElementById('books').value
    }
    for (const property in filterVal) {
        if (filterVal[property] == '') {
            continue
        }
        url += `${property}=${filterVal[property]}&`
    }
    getscholar(url).catch(error => {
        console.log(error)
    })
    if(screen.width <= 960){
        document.getElementById('search-form').style.transform = 'translateY(100%)';
        backDrop.setAttribute('style','display:none')
        body[0].removeAttribute('style')
    }
});

function createCard(resp) {

    var main = document.getElementById('maincontainer')
    main.setAttribute("class", "row col l10 m9")
    main.innerHTML = ''

    if (resp.results.length == 0) {
        main.innerHTML = 'Oops! Nothing to show!'
        main.style.textAlign = 'center'
    }
    else {
        for (var i = 0; i <= resp.results.length - 1; i++) {

            var subcont = document.createElement('div')
            subcont.setAttribute("class", "col s12 m12 l4")
            main.appendChild(subcont)

            var card = document.createElement('div')
            card.setAttribute("class", "card")
            subcont.appendChild(card)

            var cardcontent = document.createElement('div')
            cardcontent.setAttribute("class", "card-content")
            card.appendChild(cardcontent)

            var title = document.createElement('span')
            title.setAttribute("class", "card-title black-text cardtitle truncate")
            title.setAttribute("style", "padding-bottom: 1.5vmin; margin-bottom: 2.7vmin; border-bottom: 0.2vmin solid rgb(226, 226, 226); line-height: 3.7vmin; font-size: 3vmin")
            title.innerHTML = resp.results[i].title
            cardcontent.appendChild(title)

            var content = document.createElement('div')
            content.setAttribute("class", "row contentrow")
            cardcontent.appendChild(content)

            var image = document.createElement('img')
            image.setAttribute("class", "col s4 m4 l4 offset-m4 offset-s4")
            image.src = resp.results[i].img
            content.appendChild(image)

            if (resp.results[i].image == null) {
                image.style.display = "none"
            }

            var award = document.createElement('p')
            award.setAttribute("class", "cont1 truncate")
            award.innerHTML = `Books: ${resp.results[i].books}`
            content.appendChild(award)

            if (resp.results[i].books == null) {
                award.innerHTML = "Books: Information not available"
                content.appendChild(award)
            }

            content.appendChild(document.createElement('br'))

            var interest = document.createElement('p')
            interest.setAttribute("class", "truncate cont2")
            interest.innerHTML = `District: ${resp.results[i].district}`
            cardcontent.appendChild(interest)
            if (resp.results[i].district == null) {
                award.innerHTML = "District: Information not available"
                content.appendChild(interest)
            }

            cardcontent.appendChild(document.createElement('br'))

            var updt = document.createElement('p')
            updt.setAttribute("class", "truncate cont3")
            updt.innerHTML = `Updated on: ${resp.results[i].updated_on}`
            cardcontent.appendChild(updt)

            if (resp.results[i].updated_on == null) {
                updt.innerHTML = "Deadline : Information not available"
                cardcontent.appendChild(updt)
            }

            cardcontent.appendChild(document.createElement('br'))

            var action = document.createElement('div')
            action.setAttribute("class", "card-action")
            card.appendChild(action)

            var details = document.createElement('a')
            details.id = resp.results[i].id
            details.setAttribute('class', 'modal-trigger')
            details.href = '#!'
            details.innerHTML = "View Details"
            action.appendChild(details)
        }
        document.querySelectorAll('.modal-trigger').forEach(item => {
            item.addEventListener('click', event => {
                body[0].setAttribute('style','overflow:hidden;')
                backDrop.setAttribute('style','display:block; opacity:0.5')
                modal.classList.add('modal-show')
                var scholarshipDetail
                for (var i = 0; i < resp.results.length; i++) {
                    if (item.id == resp.results[i].id) {
                        scholarshipDetail = resp.results[i]
                        break;
                    }
                }
                console.log(scholarshipDetail)
                modalTitle.innerHTML = scholarshipDetail.title
                modalTitle.style.textTransform = 'capitalize'
                modalDetails.innerHTML = ''
                for (var j = 0; j < displayItems.length; j++) {
                    if(scholarshipDetail[displayItems[j]]==null || scholarshipDetail[displayItems[j]]=="" ){
                        continue
                    }
                    var details = document.createElement('p')
                    var dethead = document.createElement('span')
                    dethead.style.fontWeight = 'bold'
                    dethead.style.textTransform = 'uppercase'
                    dethead.innerHTML = `${displayItems[j]}: `
                    details.appendChild(dethead)
                    var deets = document.createElement('span')
                    deets.innerHTML = scholarshipDetail[displayItems[j]]
                    details.appendChild(deets)
                    modalDetails.appendChild(details)
                }
            })
        })
    }
}

btnClose = document.getElementById('btnClose')
btnClose.addEventListener('click', () => {
    modal.classList.remove('modal-show')
    body[0].removeAttribute('style')
    backDrop.setAttribute('style','display:none')
})

backDrop.addEventListener('click', () => {
    modal.classList.remove('modal-show')
    body[0].removeAttribute('style')
    backDrop.setAttribute('style','display:none')
    if(window.innerWidth <= 960){
        document.getElementById('search-form').style.transform = 'translateY(100%)';
    }
})

function createPagination(count) {
    var totalPages = Math.ceil(count / 20)
    console.log(totalPages)
    var pageCont = document.getElementById('pagination')
    pageCont.innerHTML = ''

    if (totalPages > 0) {
        for (var i = 1; i <= totalPages; i++) {
            var btn = document.createElement('li')
            btn.setAttribute('class', 'waves-effect pagebtn')
            pageCont.appendChild(btn)
            var btna = document.createElement('a')
            btna.innerHTML = `${i}`
            btna.setAttribute('class', 'pageBtn')
            btn.appendChild(btna)
        }
    }
    document.querySelectorAll('.pageBtn').forEach(item => {
        item.addEventListener('click', event => {
            getscholar(url, item.innerHTML)
        })
    })
}

var search = document.getElementById("search");
search.addEventListener('submit', (e) => {
    e.preventDefault();
    page = 1
    // url = "https://34.86.68.175/api/bookbanks/search/?"
    url = "http://192.168.29.172:8000/api/bookbanks/search/?"
    var filterVal = {
        q: document.getElementById('search-elem').value,
    }
    for (const property in filterVal) {
        if (filterVal[property] == '') {
            url = url
        }

        url += `${property}=${filterVal[property]}&`

    }

    getscholar(url).catch(error => {
        console.log(error)
    })
    if(window.innerWidth <= 960){
        document.getElementById('search-form').style.transform = 'translateY(100%)';
        backDrop.setAttribute('style','display:none')
        body[0].removeAttribute('style')
    }
});

async function getDistrict(state){
    // url = `https://34.86.68.175/api/bookbanks/getDistrict/?state=${state}`
    url = `http://192.168.29.172:8000/api/bookbanks/getDistrict/?state=${state}`
    const districtList = await fetch(url)
    const resp = await districtList.json()
    try {
        var district = document.getElementById('districts')
        for (var i = 0; i < resp.length; i++) {
            var option = document.createElement('option')
            option.innerHTML = resp[i].name
            district.appendChild(option)
    }
    } catch (error) {
        console.log(error)
    }
    
}

document.getElementById("states").addEventListener('input',()=>{
    document.getElementById('districts').innerHTML=''
    var state = document.getElementById("states").value
    getDistrict(state)
})

document.getElementById('search-trigger').addEventListener('click',()=>{
    document.getElementById('search-form').style.transform = 'translateY(0%)';
    body[0].setAttribute('style','overflow:hidden;')
    backDrop.setAttribute('style','display:block; opacity:0.5')
})