// var url = 'https://34.86.68.175/api/ngo/active/?'
var url = 'http://192.168.29.182:8000/api/ngo/active/?'
var scholarships;
var page = 1
var modal = document.querySelector('.modal')
var modalTitle = document.querySelector('.modal-title')
var modalDetails = document.querySelector('.modal-body')
var displayItems = ['updated_on', 'state', 'country', 'category', 'stype', 'religion', 'gender', 'eligibility', 'content', 'site_url', 'location', 'contact', 'email']
var elem = document.querySelector('.sidenav');
var body = document.getElementsByTagName('body')
var backDrop = document.getElementById('backDrop')
var instance = new M.Sidenav(elem);

getscholar(url, page = 1)
    .catch(error => {
        console.log(error)
    })

async function getscholar(url, page = 1) {
    url += `page=${page}`
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

    // var filterFields = 'https://34.86.68.175/api/ngo/filterFields/'
    var filterFields = 'http://192.168.29.182:8000/api/ngo/filterFields/'
    var fields = await fetch(filterFields)
    var b = await fields.json()

    try{
        var country = document.getElementById('countries')
        for (var i = 0; i < b['country'].length; i++) {
            var option = document.createElement('option')
            option.innerHTML = b['country'][i].name
            country.appendChild(option)
        }
    }
    catch(error){
        console.log(error)
    }

    /* var state = document.getElementById('states')
    for (var i = 0; i < b['state'].length; i++) {
        var option = document.createElement('option')
        option.innerHTML = b['state'][i].name
        state.appendChild(option)
    } */
    try {
        var category = document.getElementById('categories')
        for (var i = 0; i < b['category'].length; i++) {
            var option = document.createElement('option')
            option.innerHTML = b['category'][i].name
            category.appendChild(option)
    }
    } catch (error) {
        console.log(error)
    }
 
    try {
        var stype = document.getElementById('types')
        for (var i = 0; i < b['type'].length; i++) {
            var option = document.createElement('option')
            option.innerHTML = b['type'][i].name
            stype.appendChild(option)
    }
    } catch (error) {
        console.log(error)
    }
    
    try {
        var religion = document.getElementById('religions')
        for (var i = 0; i < b['religion'].length; i++) {
            var option = document.createElement('option')
            option.innerHTML = b['religion'][i].name
            religion.appendChild(option)
    }
    } catch (error) {
        console.log(error)
    }
    
    try {
        var gender = document.getElementById('genders')
        for (var i = 0; i < b['gender'].length; i++) {
            var option = document.createElement('option')
            option.innerHTML = b['gender'][i].name
            gender.appendChild(option)
    }
    } catch (error) {
        console.log(error)
    }
    
}

getfields()

var form = document.getElementById("filterForm");
form.addEventListener('submit', (e) => {
    e.preventDefault();
    // url = "https://34.86.68.175/api/ngo/filter/?"
    url = "http://192.168.29.182:8000/api/ngo/filter/?"
    var filterVal = {
        state: document.getElementById('states').value,
        category: document.getElementById('categories').value,
        stype: document.getElementById('types').value,
        religion: document.getElementById('religions').value,
        gender: document.getElementById('genders').value,
    }
    for (const property in filterVal) {
        if (filterVal[property] == '') {
            continue
        }
        url += `${property}=${filterVal[property]}&`
    }
    console.log(url)
    getscholar(url).catch(error => {
        console.log(error)
    })
    if(window.innerWidth <= 960){
        document.getElementById('search-form').style.transform = 'translateY(100%)';
        backDrop.setAttribute('style','display:none')
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
            award.innerHTML = `Type: ${resp.results[i].stype}`
            content.appendChild(award)

            if (resp.results[i].stype == null) {
                award.innerHTML = "Type: Information not available"
                content.appendChild(award)
            }

            content.appendChild(document.createElement('br'))

            var interest = document.createElement('p')
            interest.setAttribute("class", "truncate cont2")
            interest.innerHTML = `Contact: ${resp.results[i].contact}`
            cardcontent.appendChild(interest)
            if (resp.results[i].contact == null) {
                award.innerHTML = "Contact: Information not available"
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
                    if(displayItems[j] == "stype"){
                        dethead.innerHTML = "Type: "
                    }
                    else{
                        dethead.innerHTML = `${displayItems[j]}: `
                    }
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
            btn = document.createElement('li')
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
    // url = "https://34.86.68.175/api/ngo/search/?"
    url = "http://192.168.29.182/api/ngo/search/?"
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
        document.getElementById('search-form').style.transform = 'translayeY(100%)';
        backDrop.setAttribute('style','display:none')
    }
});

async function getState(country){
    // url = `https://34.86.68.175/api/ngo/getState/?country=${country}`
    url = `https://192.168.29.182:8000/api/ngo/getState/?country=${country}`
    const stateList = await fetch(url)
    const resp = await stateList.json()
    console.log(resp)
    var state = document.getElementById('states')
    for (var i = 0; i < resp.length; i++) {
        var option = document.createElement('option')
        option.innerHTML = resp[i].name
        state.appendChild(option)
    }
}

document.getElementById("countries").addEventListener('input',()=>{
    document.getElementById('states').innerHTML=''
    var country = document.getElementById("countries").value
    console.log(country)
    getState(country)
})

document.getElementById('search-trigger').addEventListener('click',()=>{
    document.getElementById('search-form').style.transform = 'translateY(0%)';
    body[0].setAttribute('style','overflow:hidden;')
    backDrop.setAttribute('style','display:block; opacity:0.5')
})