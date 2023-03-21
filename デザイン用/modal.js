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
              >ラベル${conditionId}:
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
        <!-- 性別ボタン ここから-->
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
              男性
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
              女性
            </label>
          </div>
        </div>
        <!-- 性別ボタン ここまで-->

        <!-- ############### -->
        <div class="my-2"></div>
        <!-- ############### -->

        <!-- 年齢ボタン ここから-->
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
            <input class="form-control" type="number" id="min-age-${conditionId}" placeholder="最小年齢"/>
          </div>
          <div class="form-check hidden age-${conditionId}">
            <input class="form-control" type="number" id="max-age-${conditionId}" placeholder="最大年齢"/>
          </div>
        </div>
        <!-- 年齢ボタン ここまで-->

        <!-- ############### -->
        <div class="my-2"></div>
        <!-- ############### -->

        <!-- 都道府県ボタン ここから-->
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
              <option value="1">北海道</option>
              <option value="2">青森県</option>
              <option value="3">岩手県</option>
              <option value="4">宮城県</option>
              <option value="5">秋田県</option>
              <option value="6">山形県</option>
              <option value="7">福島県</option>
              <option value="8">茨城県</option>
              <option value="9">栃木県</option>
              <option value="10">群馬県</option>
              <option value="11">埼玉県</option>
              <option value="12">千葉県</option>
              <option value="13">東京都</option>
              <option value="14">神奈川県</option>
              <option value="15">新潟県</option>
              <option value="16">富山県</option>
              <option value="17">石川県</option>
              <option value="18">福井県</option>
              <option value="19">山梨県</option>
              <option value="20">長野県</option>
              <option value="21">岐阜県</option>
              <option value="22">静岡県</option>
              <option value="23">愛知県</option>
              <option value="24">三重県</option>
              <option value="25">滋賀県</option>
              <option value="26">京都府</option>
              <option value="27">大阪府</option>
              <option value="28">兵庫県</option>
              <option value="29">奈良県</option>
              <option value="30">和歌山県</option>
              <option value="31">鳥取県</option>
              <option value="32">島根県</option>
              <option value="33">岡山県</option>
              <option value="34">広島県</option>
              <option value="35">山口県</option>
              <option value="36">徳島県</option>
              <option value="37">香川県</option>
              <option value="38">愛媛県</option>
              <option value="39">高知県</option>
              <option value="40">福岡県</option>
              <option value="41">佐賀県</option>
              <option value="42">長崎県</option>
              <option value="43">熊本県</option>
              <option value="44">大分県</option>
              <option value="45">宮崎県</option>
              <option value="46">鹿児島県</option>
              <option value="47">沖縄県</option>
            </select>
          </div>
        </div>

        <!-- 都道府県ボタン ここまで-->

        <div class="my-2"></div>

        <!-- 職業ボタン -->
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
              >公務員
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
              >経営者・役員
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
              >会社員(事務系)
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
              >会社員(技術系)
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
              >会社員(その他)
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
              >自営業
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
              >自由業
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
              >専業主婦
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
              >パート・アルバイト
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
              >学生
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
              >その他
            </label>
          </div>
        </div>
        <!-- 職業ボタン ここまで-->

        <!-- ############### -->
        <div class="my-2"></div>
        <!-- ############### -->
        <!-- 未既婚ボタン ここから-->

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
              >未婚
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
              >既婚
            </label>
          </div>
        </div>
        <!-- 未既婚ボタン ここまで-->

        <!-- ############### -->
        <div class="my-2"></div>
        <!-- ############### -->

        <!-- 子供の有無ボタン ここから-->
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
              子供有り
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
              子供無し
            </label>
          </div>
        </div>
        <!-- 子供の有無ボタン ここまで-->
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
            <h4 class='flag-name'>ラベル名: ${flagName}</h4>
            <input type='hidden' value='${flagName}' name='flag-name-${idNum}'>
        `
    }else{
        html = `
        <h4 class='flag-name'>ラベル名: 名称未設定</h4>
        <input type='hidden' value='名称未設定' name='flag-name-${idNum}'>
        `
    }
    if (sexName != ""){
        html += `
            <p class='sexAttribute'>性別: ${sexName}（${sexDict[sexName]}）</p>
            <input type='hidden' value='${sexName}' name='sexAttribute-${idNum}'>
        `
    }
    if (minAgeName != ""){
        html += `
            <p class='minAgeAttribute'>年齢下限: ${minAgeName}歳 ~</p>
            <input type='hidden' value='${minAgeName}' name='minAgeAttribute-${idNum}'>
        `
    }
    if (maxAgeName != ""){
        html += `
        <p class='maxAgeAttribute'>年齢上限: ${maxAgeName}歳</p>
        <input type='hidden' value='${maxAgeName}' name='maxAgeAttribute-${idNum}'>

        `
    }
    if (preName.length !=0 ){
        let preWord = '<ol id="preAttribute">選択した都道府県';
        for (let i=0; i<preName.length; i++){
            preWord += `<li value='${preName[i]}'>${preDict[preName[i]]}</li>`;
        }
        preWord += '</ol>';
        preWord += `<input type='hidden' value='${preName}' name='preAttribute-${idNum}'>`
        html += preWord;
    }
    if (jobName.length != 0){
        let jobWordList = '<ol id="jobAttribute">選択した職業';
        for (let i = 0; i<jobName.length; i++){
            jobWordList += `<li value='${jobName[i]}'>${jobDict[jobName[i]]}</li>`;
        }
        jobWordList += '</ol>';
        jobWordList += `<input type='hidden' value='${jobName}' name='jobAttribute-${idNum}'>`

        html += jobWordList
    }
    if (marriedName != ""){
        html += `
        <p class='marriedAttribute'>未既婚: ${marriedName}（${marDict[marriedName]}）</p>
        <input type='hidden' value='${marriedName}' name='marriedAttribute-${idNum}'>
        `
    }
    if (childName != ""){
        html += `
        <p class='childAttribute'>子供の有無: ${childName}（${chiDict[childName]}）</p>
        <input type='hidden' value='${childName}' name='childAttribute-${idNum}'>
        `
    }

    return html
}


const sexDict = {1: "男性", 2: "女性"}
const preDict = {
    1: "北海道",
    2: "青森県",
    3: "岩手県",
    4: "宮城県",
    5: "秋田県",
    6: "山形県",
    7: "福島県",
    8: "茨城県",
    9: "栃木県",
    10: "群馬県",
    11: "埼玉県",
    12: "千葉県",
    13: "東京都",
    14: "神奈川県",
    15: "新潟県",
    16: "富山県",
    17: "石川県",
    18: "福井県",
    19: "山梨県",
    20: "長野県",
    21: "岐阜県",
    22: "静岡県",
    23: "愛知県",
    24: "三重県",
    25: "滋賀県",
    26: "京都府",
    27: "大阪府",
    28: "兵庫県",
    29: "奈良県",
    30: "和歌山県",
    31: "鳥取県",
    32: "島根県",
    33: "岡山県",
    34: "広島県",
    35: "山口県",
    36: "徳島県",
    37: "香川県",
    38: "愛媛県",
    39: "高知県",
    40: "福岡県",
    41: "佐賀県",
    42: "長崎県",
    43: "熊本県",
    44: "大分県",
    45: "宮崎県",
    46: "鹿児島県",
    47: "沖縄県"
}

const jobDict = {
    1: "公務員",
    2: "経営者・役員",
    3: "会社員(事務系)",
    4: "会社員(技術系)",
    5: "会社員(その他)",
    6: "自営業",
    7: "自由業",
    8: "専業主婦",
    9: "パート・アルバイト",
    10: "学生",
    11: "その他"
}
const marDict = {1: "未婚", 2: "既婚"}
const chiDict = {1: "子供有り", 2: "子供無し"}