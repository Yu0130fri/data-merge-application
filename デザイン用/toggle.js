function toggleFlag() {
    let toggleBtnChecked = document.getElementById('generateFlg').checked;
    let attributeFlgBtnJudge = document.getElementById('scAttributeFlg').checked;

    let achElem = document.getElementById('anchor-flag');
    if (attributeFlgBtnJudge && toggleBtnChecked){
        toggleBtnChecked = false;
    }

    const inputShowAria = document.getElementById('input-show');
    if (inputShowAria.childElementCount > 0){
        while (inputShowAria.childElementCount > 0){
            inputShowAria.removeChild(inputShowAria.firstChild);
        }
    }

    if (toggleBtnChecked){
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
    }
    
    let anchor_layout = document.getElementById('anchor-layout');
    let child_count = anchor_layout.childElementCount;

    if (child_count > 1){
        for (let _i=0; _i<child_count - 2; _i++){
            anchor_layout.removeChild(anchor_layout.lastChild);
        }
    }
}


function showToggle(){
    // レイアウトフォームを1つにする
    let divInputDataBtn = document.getElementById("anchor-layout");
    let divInputDataBtnLength = divInputDataBtn.childElementCount;
    console.log(divInputDataBtnLength);
    for (let i = 0; i < divInputDataBtnLength - 2; i++) {
      divInputDataBtn.lastChild.remove();
    }

    const toggleCheck = document.getElementById('labelOff').checked;
    let onlyLabel = document.getElementById('onlyLabel');
    let makeLabel = document.getElementById('makeLabel');
    let genBtn = document.getElementById('generateFlg');
    let attributeBtn = document.getElementById('scAttributeFlg');

    if (toggleCheck){
        onlyLabel.className = "row mt-2 toggleBtn";
        makeLabel.className = "row mt-2 toggleBtn";
    }else{
        onlyLabel.className = "row mt-2 toggleBtn hidden";
        makeLabel.className = "row mt-2 toggleBtn hidden";
        genBtn.checked = false;
        attributeBtn.checked = false;
    }
}