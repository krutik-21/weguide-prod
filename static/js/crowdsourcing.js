var elem = document.querySelector('.sidenav');
var instance = new M.Sidenav(elem);

top.visible_div_id = 'north';

function toggle_visibility(id) {
    var old_e = document.getElementById(top.visible_div_id);
    old_e.style.display = 'none';
    var new_e = document.getElementById(id);
    console.log('new', new_e, 'block');
    new_e.style.display = 'block';
    top.visible_div_id = id
}

function getData(formName){
    var arr = formName.split(" ");
    data = {}
    if(arr[0] === "Scholarship"){
        var selected = [];
        for (var option of document.getElementById('scholfor').options)
        {
            if (option.selected) {
                selected.push(option.value);
            }
        }
        data["title"] = document.getElementById('scholname').value,
        data["amount"] = document.getElementById('scholamt').value,
        data["eligibility"] = selected.toString(),
        data["contact"] = document.getElementById('scholcontact').value,
        data["desc"] = document.getElementById('scholdesc').value,
        data["person_name"] = document.getElementById('schol-info-name').value,
        data["person_email"] = document.getElementById('schol-info-email').value,
        data["person_contact"] = document.getElementById('schol-info-number').value
    }else if(arr[0] === "Loan"){
        var selected = [];
        for (var option of document.getElementById('loanfor').options)
        {
            if (option.selected) {
                selected.push(option.value);
            }
        }
        data["title"] = document.getElementById('loanname').value,
        data["interest"] = document.getElementById('loanint').value,
        data["eligibility"] = selected.toString(),
        data["contact"] = document.getElementById('loancontact').value,
        data["desc"] = document.getElementById('loandesc').value,
        data["person_name"] = document.getElementById('loan-info-name').value,
        data["person_email"] = document.getElementById('loan-info-email').value,
        data["person_contact"] = document.getElementById('loan-info-number').value
    }else if(arr[0] === "Bookbank"){
        data["title"] = document.getElementById('bbname').value,
        data["location"] = document.getElementById('bbloc').value,
        data["contact"] = document.getElementById('bbcontact').value,
        data["desc"] = document.getElementById('bbdesc').value,
        data["person_name"] = document.getElementById('bb-info-name').value,
        data["person_email"] = document.getElementById('bb-info-email').value,
        data["person_contact"] = document.getElementById('bb-info-number').value
    }else if(arr[0] === "NGO"){
        var selected = [];
        for (var option of document.getElementById('ngofor').options)
        {
            if (option.selected) {
                selected.push(option.value);
            }
        }
        data["title"] = document.getElementById('ngoname').value,
        data["location"] = document.getElementById('ngoloc').value,
        data["eligibility"] = selected.toString(),
        data["contact"] = document.getElementById('ngocontact').value,
        data["desc"] = document.getElementById('ngodesc').value,
        data["person_name"] = document.getElementById('ngo-info-name').value,
        data["person_email"] = document.getElementById('ngo-info-email').value,
        data["person_contact"] = document.getElementById('ngo-info-number').value
    }

    return data;
}

scholform = document.getElementById("crowdsource-schol");
loanform = document.getElementById("crowdsource-loan");
bookbankform = document.getElementById("crowdsource-bookbank");
ngoform = document.getElementById("crowdsource-ngo");

scholform.addEventListener('submit',(e)=>{
    e.preventDefault();
    url = "http://192.168.29.172:3587/api/scholarship/crowdSource/";
    var data = getData(e.target.children[0].children[0].innerText);
    fetch(url,{
        method: "POST",
        body: JSON.stringify(data),
        headers:{
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then(function (response) {
        if (response.ok) {
            return response.json();
        }
        return Promise.reject(response);
    }).then(function (data) {
        alert("Your data has been recorded. Thank you for the information.");
        location.reload()
    }).catch(function (error) {
        console.warn('Something went wrong.', error);
    });
});

loanform.addEventListener('submit',(e)=>{
    e.preventDefault();
    url = "http://192.168.29.172:3587/api/loans/crowdSource/";
    var data = getData(e.target.children[0].children[0].innerText);
    fetch(url,{
        method: "POST",
        body: JSON.stringify(data),
        headers:{
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then(function (response) {
        if (response.ok) {
            return response.json();
        }
        return Promise.reject(response);
    }).then(function (data) {
        alert("Your data has been recorded. Thank you for the information.");
        location.reload();
    }).catch(function (error) {
        console.warn('Something went wrong.', error);
    });
});
bookbankform.addEventListener('submit',(e)=>{
    e.preventDefault();
    url = "http://192.168.29.172:3587/api/bookbanks/crowdSource/";
    var data = getData(e.target.children[0].children[0].innerText);
    fetch(url,{
        method: "POST",
        body: JSON.stringify(data),
        headers:{
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then(function (response) {
        if (response.ok) {
            return response.json();
        }
        return Promise.reject(response);
    }).then(function (data) {
        alert("Your data has been recorded. Thank you for the information.");
        location.reload();
    }).catch(function (error) {
        console.warn('Something went wrong.', error);
    });
});
ngoform.addEventListener('submit',(e)=>{
    e.preventDefault();
    url = "http://192.168.29.172:3587/api/ngo/crowdSource/";
    var data = getData(e.target.children[0].children[0].innerText);
    fetch(url,{
        method: "POST",
        body: JSON.stringify(data),
        headers:{
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then(function (response) {
        if (response.ok) {
            return response.json();
        }
        return Promise.reject(response);
    }).then(function (data) {
        alert("Your data has been recorded. Thank you for the information.");
        location.reload();
    }).catch(function (error) {
        console.warn('Something went wrong.', error);
    });
});
