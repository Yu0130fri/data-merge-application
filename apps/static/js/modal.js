function toggle_checkbox(className, idName){
    idElem = document.getElementById(idName);
    if (idElem.checked){
        let elems = document.getElementsByClassName(className);
        let class_name;
        if (className.slice(0, 3) == 'pre'){
            class_name = "form-check form-check-inline col-12 "+className;
        } else if (className.slice(0, 3) == 'job') {
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
    let btnModal = document.getElementById('closeModal');
    btnModal.click();
    let inputShow = document.getElementById("input-show");
    let countCondition = document.getElementById('conditions').childElementCount;
    
    let flagName1 = getFlagName(`flag-name-1`);
    let sexName1 = getRadioValue('sex');
    let minAgeName1 = getInputNumValue(`min-age`, `max-age`)["min-age"];
    let maxAgeName1 = getInputNumValue(`min-age`, `max-age`)["max-age"];
    let preName1 = getSelectValues(`pre`);
    let jobName1 = getCheckBoxValues(`job`);
    let marriedName1 = getRadioValue(`optionMarried`);
    let childName1 = getRadioValue(`optionChild`);

    let html = makeHtmlElem(flagName1, sexName1, minAgeName1, maxAgeName1, preName1, jobName1, marriedName1, childName1, 1)
    if (countCondition == 1){
        inputShow.innerHTML = html;
        
    }else if (countCondition > 1){
        for (let i = 2; i<countCondition+1; i++){
            let flagName = getFlagName(`flag-name-${i}`);
            let sexName = getRadioValue(`sex-${i}`);
            let minAgeName = getInputNumValue(`min-age-${i}`, `max-age-${i}`)["min-age"];
            let maxAgeName = getInputNumValue(`min-age-${i}`, `max-age-${i}`)["max-age"];
            let preName = getSelectValues(`pre-${i}`);
            let jobName = getCheckBoxValues(`job-${i}`);
            let marriedName = getRadioValue(`optionMarried-${i}`);
            let childName = getRadioValue(`optionChild-${i}`);
            
            html += makeHtmlElem(flagName, sexName, minAgeName, maxAgeName, preName, jobName, marriedName, childName, i)
        }
        inputShow.innerHTML = html
    }

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

function getFlagName(flagId){
    return document.getElementById(flagId).value;
}

function getCheckBoxValues(name){
    let elementChildren = document.getElementsByName(name)
    let checked_list = [];
    for (let i = 0; i < elementChildren.length; i++){
        if (elementChildren[i].checked){
            checked_list.push(Number(elementChildren[i].value));
        }
    }
    if (checked_list.length == 0){
        return []
    }else{
        return checked_list;
    }
}

function getInputNumValue(minId, maxId){
    let minAgeIdValue = document.getElementById(minId).value;
    let maxAgeIdValue = document.getElementById(maxId).value;
    return {"min-age": minAgeIdValue, "max-age": maxAgeIdValue};

}

function getSelectValues(idName){
    let checkedId = document.getElementById(idName);
    let checkedIdOptions = checkedId.options;
    let checked_list = [];
    for (let i = 0; i < checkedIdOptions.length; i++){
        if (checkedIdOptions[i].selected){
            checked_list.push(Number(checkedIdOptions[i].value));
        }
    }
    if (checked_list.length == 0){
        return []
    }else{
        return checked_list;
    }
}

function cloneConditions(){
    let conditionClass = document.getElementsByClassName('condition');
    let countConditionClass = conditionClass.length;
    let conditionId = (countConditionClass + 1).toString();

    let conditionHTML = `
      <div id="condition-${conditionId}" class="condition">
        <div class="row g-3 align-items-center">
          <div class="col-2">
            <label for="flag-name-${conditionId}" class="col-form-label fs-6"
              >?????????${conditionId}:
            </label>
          </div>
          <div class="col-auto">
            <input
              type="text"
              id="flag-name-${conditionId}"
              class="form-control"
              required
            />
          </div>
        </div>
        <hr />
        <!-- ??????????????? ????????????-->
        <div class="row">
          <div class="form-check form-check-inline col-2 ms-2 fs-5">
            <input
              class="form-check-input"
              type="checkbox"
              value=""
              id="attribute-sex-${conditionId}"
              onclick="toggle_checkbox('sex-${conditionId}', 'attribute-sex-${conditionId}')"
            />
            <label class="form-check-label" for="attribute-sex-${conditionId}">
              SEX
            </label>
          </div>

          <div class="form-check hidden sex-${conditionId}">
            <input
              class="btn-check"
              type="radio"
              name="sex-${conditionId}"
              id="male-${conditionId}"
              value="1"
              autocomplete="off"
            />
            <label class="btn btn-outline-success col-10" for="male-${conditionId}">
              ??????
            </label>
          </div>
          <div class="form-check hidden sex-${conditionId}">
            <input
              class="btn-check"
              type="radio"
              name="sex-${conditionId}"
              id="female-${conditionId}"
              value="2"
              autocomplete="off"
            />
            <label class="btn btn-outline-success col-10" for="female-${conditionId}">
              ??????
            </label>
          </div>
        </div>
        <!-- ??????????????? ????????????-->

        <!-- ############### -->
        <div class="my-2"></div>
        <!-- ############### -->

        <!-- ??????????????? ????????????-->
        <div class="row">
          <div class="form-check form-check-inline col-1 ms-2 fs-5">
            <input
              class="form-check-input"
              type="checkbox"
              id="attribute-age-${conditionId}"
              onclick="toggle_checkbox('age-${conditionId}', 'attribute-age-${conditionId}')"
            />
            <label class="form-check-label" for="attribute-age-${conditionId}">
              AGE
            </label>
          </div>

          <div class="form-check hidden age-${conditionId}">
            <input class="form-control" type="number" id="min-age-${conditionId}" placeholder="????????????"/>
          </div>
          <div class="form-check hidden age-${conditionId}">
            <input class="form-control" type="number" id="max-age-${conditionId}" placeholder="????????????"/>
          </div>
        </div>
        <!-- ??????????????? ????????????-->

        <!-- ############### -->
        <div class="my-2"></div>
        <!-- ############### -->

        <!-- ????????????????????? ????????????-->
        <div class="row">
          <div class="form-check form-check-inline ms-2 fs-5">
            <input
              class="form-check-input"
              type="checkbox"
              id="attribute-pre-${conditionId}"
              onclick="toggle_checkbox('pre-${conditionId}', 'attribute-pre-${conditionId}')"
            />
            <label class="form-check-label-${conditionId}" for="attribute-pre">
              PRE
            </label>

            <select
              class="form-select form-select-sm pre-${conditionId} hidden"
              multiple
              size="7"
              id="pre-${conditionId}"
              aria-label="multiple .form-select-sm"
            >
              <option value="1">?????????</option>
              <option value="2">?????????</option>
              <option value="3">?????????</option>
              <option value="4">?????????</option>
              <option value="5">?????????</option>
              <option value="6">?????????</option>
              <option value="7">?????????</option>
              <option value="8">?????????</option>
              <option value="9">?????????</option>
              <option value="10">?????????</option>
              <option value="11">?????????</option>
              <option value="12">?????????</option>
              <option value="13">?????????</option>
              <option value="14">????????????</option>
              <option value="15">?????????</option>
              <option value="16">?????????</option>
              <option value="17">?????????</option>
              <option value="18">?????????</option>
              <option value="19">?????????</option>
              <option value="20">?????????</option>
              <option value="21">?????????</option>
              <option value="22">?????????</option>
              <option value="23">?????????</option>
              <option value="24">?????????</option>
              <option value="25">?????????</option>
              <option value="26">?????????</option>
              <option value="27">?????????</option>
              <option value="28">?????????</option>
              <option value="29">?????????</option>
              <option value="30">????????????</option>
              <option value="31">?????????</option>
              <option value="32">?????????</option>
              <option value="33">?????????</option>
              <option value="34">?????????</option>
              <option value="35">?????????</option>
              <option value="36">?????????</option>
              <option value="37">?????????</option>
              <option value="38">?????????</option>
              <option value="39">?????????</option>
              <option value="40">?????????</option>
              <option value="41">?????????</option>
              <option value="42">?????????</option>
              <option value="43">?????????</option>
              <option value="44">?????????</option>
              <option value="45">?????????</option>
              <option value="46">????????????</option>
              <option value="47">?????????</option>
            </select>
          </div>
        </div>

        <!-- ????????????????????? ????????????-->

        <div class="my-2"></div>

        <!-- ??????????????? -->
        <div class="row">
          <div class="form-check form-check-inline col-1 ms-2 fs-5">
            <input
              class="form-check-input"
              type="checkbox"
              id="attribute-job-${conditionId}"
              onclick="toggle_checkbox('job-${conditionId}', 'attribute-job-${conditionId}')"
            />
            <label class="form-check-label" for="attribute-job-${conditionId}">
              JOB
            </label>
          </div>
        </div>
        <div class="row">
          <div class="form-check hidden job-${conditionId}">
            <input
              class="btn-check"
              type="checkbox"
              id="public-servant-${conditionId}"
              autocomplete="off"
              name="job-${conditionId}"
              value="1"
            />
            <label
              class="btn btn-outline-success col-12"
              for="public-servant-${conditionId}"
              >?????????
            </label>
          </div>
          <div class="form-check hidden job-${conditionId}">
            <input
              class="btn-check"
              type="checkbox"
              id="ceo-${conditionId}"
              autocomplete="off"
              name="job-${conditionId}"
              value="2"
            />
            <label class="btn btn-outline-success col-12" for="ceo-${conditionId}"
              >??????????????????
            </label>
          </div>
          <div class="form-check hidden job-${conditionId}">
            <input
              class="btn-check"
              type="checkbox"
              id="paper-work-${conditionId}"
              autocomplete="off"
              name="job-${conditionId}"
              value="3"
            />
            <label class="btn btn-outline-success col-12" for="paper-work-${conditionId}"
              >?????????(?????????)
            </label>
          </div>
          <div class="form-check hidden job-${conditionId}">
            <input
              class="btn-check"
              type="checkbox"
              id="engineer-${conditionId}"
              autocomplete="off"
              name="job-${conditionId}"
              value="4"
            />
            <label class="btn btn-outline-success col-12" for="engineer-${conditionId}"
              >?????????(?????????)
            </label>
          </div>
          <div class="form-check hidden job-${conditionId}">
            <input
              class="btn-check"
              type="checkbox"
              id="worker-other-${conditionId}"
              autocomplete="off"
              name="job-${conditionId}"
              value="5"
            />
            <label class="btn btn-outline-success col-12" for="worker-other-${conditionId}"
              >?????????(?????????)
            </label>
          </div>
          <div class="form-check hidden job-${conditionId}">
            <input
              class="btn-check"
              type="checkbox"
              id="self-employed-${conditionId}"
              autocomplete="off"
              name="job-${conditionId}"
              value="6"
            />
            <label
              class="btn btn-outline-success col-12"
              for="self-employed-${conditionId}"
              >?????????
            </label>
          </div>
          <div class="form-check hidden job-${conditionId}">
            <input
              class="btn-check"
              type="checkbox"
              id="freelance-${conditionId}"
              autocomplete="off"
              name="job-${conditionId}"
              value="7"
            />
            <label class="btn btn-outline-success col-12" for="freelance-${conditionId}"
              >?????????
            </label>
          </div>
          <div class="form-check hidden job-${conditionId}">
            <input
              class="btn-check"
              type="checkbox"
              id="housewife-${conditionId}"
              autocomplete="off"
              name="job-${conditionId}"
              value="8"
            />
            <label class="btn btn-outline-success col-12" for="housewife-${conditionId}"
              >????????????
            </label>
          </div>
          <div class="form-check hidden job-${conditionId}">
            <input
              class="btn-check"
              type="checkbox"
              id="part-time-${conditionId}"
              autocomplete="off"
              name="job-${conditionId}"
              value="9"
            />
            <label class="btn btn-outline-success col-12" for="part-time-${conditionId}"
              >???????????????????????????
            </label>
          </div>
          <div class="form-check hidden job-${conditionId}">
            <input
              class="btn-check"
              type="checkbox"
              id="student-${conditionId}"
              autocomplete="off"
              name="job-${conditionId}"
              value="10"
            />
            <label class="btn btn-outline-success col-12" for="student-${conditionId}"
              >??????
            </label>
          </div>
          <div class="form-check hidden job-${conditionId}">
            <input
              class="btn-check"
              type="checkbox"
              id="other-${conditionId}"
              autocomplete="off"
              name="job-${conditionId}"
              value="11"
            />
            <label class="btn btn-outline-success col-12" for="other-${conditionId}"
              >?????????
            </label>
          </div>
        </div>
        <!-- ??????????????? ????????????-->

        <!-- ############### -->
        <div class="my-2"></div>
        <!-- ############### -->
        <!-- ?????????????????? ????????????-->

        <div class="row">
          <div class="form-check form-check-inline col-2 ms-2 fs-5">
            <input
              class="form-check-input"
              type="checkbox"
              id="attribute-marriage-${conditionId}"
              onclick="toggle_checkbox('marriage-${conditionId}', 'attribute-marriage-${conditionId}')"
            />
            <label class="form-check-label" for="attribute-marriage-${conditionId}">
              MAR
            </label>
          </div>
          <div class="form-check hidden marriage-${conditionId}">
            <input
              class="btn-check"
              type="radio"
              name="optionMarried-${conditionId}"
              id="unmarried-${conditionId}"
              value="1"
              autocomplete="off"
            />
            <label class="btn btn-outline-success col-10" for="unmarried-${conditionId}"
              >??????
            </label>
          </div>
          <div class="form-check hidden marriage-${conditionId}">
            <input
              class="btn-check"
              type="radio"
              name="optionMarried-${conditionId}"
              id="married-${conditionId}"
              value="2"
              autocomplete="off"
            />
            <label class="btn btn-outline-success col-10" for="married-${conditionId}"
              >??????
            </label>
          </div>
        </div>
        <!-- ?????????????????? ????????????-->

        <!-- ############### -->
        <div class="my-2"></div>
        <!-- ############### -->

        <!-- ???????????????????????? ????????????-->
        <div class="row">
          <div class="form-check form-check-inline col-2 ms-2 fs-5">
            <input
              class="form-check-input"
              type="checkbox"
              value=""
              id="attribute-child-${conditionId}"
              onclick="toggle_checkbox('child-${conditionId}', 'attribute-child-${conditionId}')"
            />
            <label class="form-check-label" for="attribute-child-${conditionId}">
              CHI
            </label>
          </div>
          <div class="form-check hidden child-${conditionId}">
            <input
              class="btn-check"
              type="radio"
              name="optionChild-${conditionId}"
              id="having-child-${conditionId}"
              value="1"
              autocomplete="off"
            />
            <label
              class="btn btn-outline-success col-10"
              for="having-child-${conditionId}"
            >
              ????????????
            </label>
          </div>
          <div class="form-check hidden child-${conditionId}">
            <input
              class="btn-check"
              type="radio"
              name="optionChild-${conditionId}"
              id="not-having-child-${conditionId}"
              value="2"
              autocomplete="off"
            />
            <label
              class="btn btn-outline-success col-10"
              for="not-having-child-${conditionId}">
              ????????????
            </label>
          </div>
        </div>
        <!-- ???????????????????????? ????????????-->
        <div class="my-2"></div>
      </div>
    `
    let conditionArea = document.getElementById('conditions');

    conditionArea.insertAdjacentHTML('beforeend', conditionHTML);

}

function deleteConditions(){
    let conditionArea = document.getElementById('conditions');

    if (conditionArea.lastChild.length == 5){
        conditionArea.lastChild.remove();
    }
    if (conditionArea.childElementCount != 1){
        conditionArea.lastChild.remove();
    }
}


function makeHtmlElem(
    flagName,
    sexName,
    minAgeName,
    maxAgeName,
    preName,
    jobName,
    marriedName,
    childName,
    idNum,
){
    let html;
    if (flagName.length > 0 && flagName != undefined){
        html = `
            <h4 class='flag-name'>????????????: ${flagName}</h4>
            <input type='hidden' value='${flagName}' name='flag-name-${idNum}'>
        `
    }else{
        html = `
        <h4 class='flag-name'>????????????: ???????????????</h4>
        <input type='hidden' value='???????????????' name='flag-name-${idNum}'>
        `
    }
    if (sexName != ""){
        html += `
            <p class='sexAttribute'>??????: ${sexName}???${sexDict[sexName]}???</p>
            <input type='hidden' value='${sexName}' name='sexAttribute-${idNum}'>
        `
    }
    if (minAgeName != ""){
        html += `
            <p class='minAgeAttribute'>????????????: ${minAgeName}??? ~</p>
            <input type='hidden' value='${minAgeName}' name='minAgeAttribute-${idNum}'>
        `
    }
    if (maxAgeName != ""){
        html += `
        <p class='maxAgeAttribute'>????????????: ${maxAgeName}???</p>
        <input type='hidden' value='${maxAgeName}' name='maxAgeAttribute-${idNum}'>

        `
    }
    if (preName.length !=0 ){
        let preWord = '<ol id="preAttribute">????????????????????????';
        for (let i=0; i<preName.length; i++){
            preWord += `<li value='${preName[i]}'>${preDict[preName[i]]}</li>`;
        }
        preWord += '</ol>';
        preWord += `<input type='hidden' value='${preName}' name='preAttribute-${idNum}'>`
        html += preWord;
    }
    if (jobName.length != 0){
        let jobWordList = '<ol id="jobAttribute">??????????????????';
        for (let i = 0; i<jobName.length; i++){
            jobWordList += `<li value='${jobName[i]}'>${jobDict[jobName[i]]}</li>`;
        }
        jobWordList += '</ol>';
        jobWordList += `<input type='hidden' value='${jobName}' name='jobAttribute-${idNum}'>`

        html += jobWordList
    }
    if (marriedName != ""){
        html += `
        <p class='marriedAttribute'>?????????: ${marriedName}???${marDict[marriedName]}???</p>
        <input type='hidden' value='${marriedName}' name='marriedAttribute-${idNum}'>
        `
    }
    if (childName != ""){
        html += `
        <p class='childAttribute'>???????????????: ${childName}???${chiDict[childName]}???</p>
        <input type='hidden' value='${childName}' name='childAttribute-${idNum}'>
        `
    }

    return html
}


const sexDict = {1: "??????", 2: "??????"}
const preDict = {
    1: "?????????",
    2: "?????????",
    3: "?????????",
    4: "?????????",
    5: "?????????",
    6: "?????????",
    7: "?????????",
    8: "?????????",
    9: "?????????",
    10: "?????????",
    11: "?????????",
    12: "?????????",
    13: "?????????",
    14: "????????????",
    15: "?????????",
    16: "?????????",
    17: "?????????",
    18: "?????????",
    19: "?????????",
    20: "?????????",
    21: "?????????",
    22: "?????????",
    23: "?????????",
    24: "?????????",
    25: "?????????",
    26: "?????????",
    27: "?????????",
    28: "?????????",
    29: "?????????",
    30: "????????????",
    31: "?????????",
    32: "?????????",
    33: "?????????",
    34: "?????????",
    35: "?????????",
    36: "?????????",
    37: "?????????",
    38: "?????????",
    39: "?????????",
    40: "?????????",
    41: "?????????",
    42: "?????????",
    43: "?????????",
    44: "?????????",
    45: "?????????",
    46: "????????????",
    47: "?????????"
}

const jobDict = {
    1: "?????????",
    2: "??????????????????",
    3: "?????????(?????????)",
    4: "?????????(?????????)",
    5: "?????????(?????????)",
    6: "?????????",
    7: "?????????",
    8: "????????????",
    9: "???????????????????????????",
    10: "??????",
    11: "?????????"
}
const marDict = {1: "??????", 2: "??????"}
const chiDict = {1: "????????????", 2: "????????????"}