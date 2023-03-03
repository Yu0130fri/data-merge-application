function toggleFlag() {
    let toggle_btn = document.getElementById('generate-flag').checked;

    let achElem = document.getElementById('anchor-flag');

    if (toggle_btn){
        if (achElem.childElementCount == 0) {
            let countElemNum = document.getElementsByClassName("input-data-btn").length;
            for (let i=0; i <= countElemNum; i++){
                let divElem = document.createElement('div');
                divElem.className = 'flag-text my-2 row'
                let divId = 'flag-name-' + i.toString();
            
                divElem.innerHTML = `
                <label for="${divId}" class="col-sm-2 col-form-label card-text">本調査-${i + 1}</label>
                <div class="col-sm-5">
                <input type="text" class="form-control" name="${divId}" id="${divId}" placeholder="本調査-${i+1}のラベル">
                </div>
                `
                achElem.append(divElem);
            }
        }else{
            while(achElem.firstChild){
                achElem.removeChild(achElem.firstChild);
            }
        }
    } else {
        while(achElem.firstChild){
            achElem.removeChild(achElem.firstChild);
        }
    }
    
    let anchor_layout = document.getElementById('anchor-layout');
    let child_count = anchor_layout.childElementCount;

    if (child_count > 1){
        for (let _i=0; _i<child_count - 2; _i++){
            anchor_layout.removeChild(anchor_layout.lastChild);
        }
    }
}


function toggle_checkbox(className, idName){
    idElem = document.getElementById(idName);
    if (idElem.checked){
        let elems = document.getElementsByClassName(className);
        let class_name;
        if (className == 'pre'){
            class_name = "form-check form-check-inline col-12 "+className;
        } else if (className == 'job') {
            class_name = "form-check form-check-inline col-12 mt-2 "+className;
        }else {
            class_name = "form-check form-check-inline col-4 "+className;
        }

        for (let i=0; i<elems.length; i++){
            elems[i].className = class_name;
        }
    }else{
        let elems = document.getElementsByClassName(className);
        for (let i=0; i<elems.length; i++){
            elems[i].className = "form-check hidden "+className;
            elems[i].firstElementChild.checked = false;
        }
    }

}

function submitClick(){
    let btnModal = document.getElementById('submit-form');
    btnModal.click();
    let inputShow = document.getElementById("input-show");
    inputShow.innerHTML = `
        <h4>${getRadioValue('sex')}</h4>
        <h4>${getRadioValue('optionMarried')}</h4>
        <h4>${getRadioValue('optionChild')}</h4>
    `;
}

function getRadioValue(name){
    let checkedName = document.getElementsByName(name);
    let checked_id;
    for (let i = 0; i < checkedName.length; i++){
        if (checkedName[i].checked){
            checked_id =  checkedName[i].value;
            break;
        }
    }
    if (checked_id == undefined){
        return ''
    }else{
        return checked_id;
    }
}