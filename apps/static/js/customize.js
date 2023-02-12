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