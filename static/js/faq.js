document.addEventListener('DOMContentLoaded', function() {
    var collapse = document.querySelectorAll('.collapsible');
    M.Collapsible.init(collapse, {
        accordion: false
    });
});

var elem = document.querySelector('.sidenav');
var instance = new M.Sidenav(elem);
var body = document.getElementsByTagName('body')
var backDrop = document.getElementById('backDrop')

document.getElementById('faqMobile').classList.add('active')

$(".collapsible-header").click(function(){
    $(this).children("i").toggleClass("down")
})
document.addEventListener('submit',(e) => {
    e.preventDefault();
    var choices = ['schol','loan','book','aboutus','guidance']
    var schol = document.getElementById('schol');
    var loan = document.getElementById('loan');
    var book = document.getElementById('book');
    var aboutus = document.getElementById('aboutus');
    var guidance = document.getElementById('guidance');
    if(schol.checked == true){
        choices.splice(choices.indexOf('schol'),1);
        $(`li.schol.remove`).attr('class',`schol`);
    }
    if(loan.checked == true){
        choices.splice(choices.indexOf('loan'),1);
        $(`li.loan.remove`).attr('class',`loan`);
    }
    if(book.checked == true){
        choices.splice(choices.indexOf('book'),1);
        $(`li.book.remove`).attr('class',`book`);
    }
    if(aboutus.checked == true){
        choices.splice(choices.indexOf('aboutus'),1);
        $(`li.aboutus.remove`).attr('class',`aboutus`);
    }
    if(guidance.checked == true){
        choices.splice(choices.indexOf('guidance'),1);
        $(`li.guidance.remove`).attr('class',`guidance`);
    }
    if(choices.length > 0 && choices.length < 5){
        for(choice in choices){
            $(`li.${choices[choice]}`).attr('class',`${choices[choice]} remove`)
        }
    }else{
        location.reload();
    }
    if(window.innerWidth <= 960){
        document.getElementById('filterForm').style.transform = 'translateY(100%)'
        backDrop.setAttribute('style','display:none')
        body[0].removeAttribute('style')
    }
})

document.getElementById('search-trigger').addEventListener('click',()=>{
    document.getElementById('filterForm').style.transform = 'translateY(20%)';
    body[0].setAttribute('style','overflow:hidden;')
    backDrop.setAttribute('style','display:block; opacity:0.5')
})

backDrop.addEventListener('click', () => {
    body[0].removeAttribute('style')
    backDrop.setAttribute('style','display:none')
    if(window.innerWidth <= 960){
        document.getElementById('filterForm').style.transform = 'translateY(100%)'
    }
})