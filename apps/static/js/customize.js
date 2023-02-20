

function addInputFiles(){
    let toggle_btn = document.getElementById('generate-flag').checked;
    if (toggle_btn){
        addInputFileBtn();
    } else {
        addInputFileBtn();
        addLayoutFileBtn();
    }

}

function deleteInputFileBtn(){
    let toggle_btn = document.getElementById('generate-flag').checked;
    if (toggle_btn){
        deleteBtn();
    }else {
        deleteBtn();
        deleteLayoutBtn();
    }
}

function addInputFileBtn() {
    let countElemNum = document.getElementsByClassName('input-data-btn').length + 1;
    
    let achElem = document.getElementById('anchor');
    let divElem = document.createElement('div');
    divElem.className = 'input-data-btn my-2'
    
    let divId = 'div-main-data-' + countElemNum.toString();
    let inputDataLabelName = 'label-main-'+countElemNum.toString();
    let inputDataBtnName = 'main-'+countElemNum.toString();
    
    divElem.innerHTML = `
        <label for="${divId}" class="form-label fs-5 card-text" id="${inputDataLabelName}">本調査-${countElemNum + 1}</label>
        <input type="file" class="form-control form-control-lg" name="${inputDataBtnName}" id="${divId}">
    `

    achElem.append(divElem);

    let achFlagElem = document.getElementById('anchor-flag');
    let diff;
    if (achFlagElem.childElementCount > 0){
        if (achFlagElem.childElementCount > countElemNum){
            diff = achFlagElem.childElementCount - countElemNum;
            let flag_text_div = document.getElementsByClassName('flag-text');
            let flag_text_div_length = flag_text_div.length;
            for (let i=1; i<diff; i++){
                flag_text_div[flag_text_div_length-i].remove();
            }
        }else if(achFlagElem.childElementCount <= countElemNum){
            diff = countElemNum - achFlagElem.childElementCount + 1;
            for (let i=1; i<=diff; i++){
                let divElem = document.createElement('div');
                divElem.className = 'flag-text my-2'
                let idName= achFlagElem.childElementCount + i;
                let divId = 'flag-name-' + (idName).toString();
            
                divElem.innerHTML = `
                <label for="${divId}" class="form-label fs-10 card-text">本調査-${idName}</label>
                <input type="text" class="form-control" name="${divId}" id="${divId}" placeholder="本調査-${idName}のラベル">
                `
                achFlagElem.append(divElem);
            }
        }

    }

}

function deleteBtn() {
    let countElemNum = document.getElementsByClassName("input-data-btn").length;
    if (countElemNum == 0) {
        alert('本調査データは1つ以上必要です');
    } else {
        let divInputDataBtn = document.getElementsByClassName("input-data-btn");
        let divInputDataBtnLength = divInputDataBtn.length

        divInputDataBtn[divInputDataBtnLength - 1].remove();
    }

    let achFlagElem = document.getElementById('anchor-flag');
    let divInputDataBtn = document.getElementsByClassName("input-data-btn");
    let divInputDataBtnLength = divInputDataBtn.length;
    let diff;
    if (achFlagElem.childElementCount > 0){
        if (achFlagElem.childElementCount > divInputDataBtnLength){
            diff = achFlagElem.childElementCount - divInputDataBtnLength;
            let flag_text_div = document.getElementsByClassName('flag-text');
            let flag_text_div_length = flag_text_div.length;
            for (let i=1; i<diff; i++){
                flag_text_div[flag_text_div_length-i].remove();
            }
        }else if(achFlagElem.childElementCount <= divInputDataBtnLength){
            diff = divInputDataBtnLength - achFlagElem.childElementCount + 1;
            for (let i=1; i<=diff; i++){
                let divElem = document.createElement('div');
                divElem.className = 'flag-text my-2 row'
                let idName= achFlagElem.childElementCount + i;
                let divId = 'flag-name-' + (idName).toString();
            
                divElem.innerHTML = `
                <label for="${divId}" class="col-sm-2 col-form-label card-text">本調査-${idName}</label>
                <div class="col-sm-5">
                <input type="text" class="form-control" name="${divId}" id="${divId}" placeholder="本調査-${idName}のラベル">
                </div>
                
                `
                achFlagElem.append(divElem);
            }
        }
    }
}

function addLayoutFileBtn() {
    let countElemNum = document.getElementsByClassName('input-layout-btn').length + 1;
    
    let achElem = document.getElementById('anchor-layout');
    let divElem = document.createElement('div');
    divElem.className = 'input-layout-btn my-2'
    
    let divId = 'div-main-layout-' + countElemNum.toString();
    let inputDataLabelName = 'label-main-layout-'+countElemNum.toString();
    let inputDataBtnName = 'main-layout-'+countElemNum.toString();
    
    divElem.innerHTML = `
        <label for="${divId}" class="form-label fs-5 card-text" id="${inputDataLabelName}">本調査レイアウト-${countElemNum + 1}</label>
        <input type="file" class="form-control form-control-lg" name="${inputDataBtnName}" id="${divId}">
    `

    achElem.append(divElem);
}

function deleteLayoutBtn() {
    let countElemNum = document.getElementsByClassName("input-layout-btn").length;
    if (countElemNum == 0) {
        alert('本調査のレイアウトデータは1つ以上必要です');
    } else {
        let divInputDataBtn = document.getElementsByClassName("input-layout-btn");
        let divInputDataBtnLength = divInputDataBtn.length

        divInputDataBtn[divInputDataBtnLength - 1].remove();
    }
}