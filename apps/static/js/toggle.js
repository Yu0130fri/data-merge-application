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
    }
    
    let anchor_layout = document.getElementById('anchor-layout');
    let child_count = anchor_layout.childElementCount;

    if (child_count > 1){
        for (let _i=0; _i<child_count - 2; _i++){
            anchor_layout.removeChild(anchor_layout.lastChild);
        }
    }

}