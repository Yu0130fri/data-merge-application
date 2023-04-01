let canvas_count = document.getElementsByClassName("canvas-container").length;

for(let i = 1; i<=canvas_count; i++){

    title = document.getElementById(`chart_title-${i}`).value;
    console.log(title);
    console.log(`chart_title-${i}`);
    question_num = document.getElementById(`question_num-${i}`).value;

    chart_data_list = String(document.getElementById(`chart_data-${i}`).value).replace("[", "").replace("]", "");
    chart_values = chart_data_list.split(',');
    console.log(chart_values);

    chart_label_list = String(document.getElementById(`chart_labels-${i}`).value);
    chart_labels = chart_label_list.replace("[", "").replace("]", "").replace(" ", "").replace("'", "").split(',');
    ctx = document.getElementById(`myChart-${i}`).getContext('2d');

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: split_word_20letters(chart_labels), // 選択肢の項目名　縦書きで表示
            datasets: [{
                data:chart_values, //各データの集計地
                backgroundColor: "rgba(255,0,0,0.2)", // 線の下の塗りつぶしの色
                borderColor: "red",                   // 線の色
                borderWidth: 1,                       // 線の幅
                label: question_num //app.pyのchart_question_num
                }
            ]
        },
        options: {
            responsive: true,
            title: {                // タイトル
                display: true,      // 表示する
                fontSize: 20,       // タイトルのフォント
                text: title         //app.pyのchart_title
            },
            scales: { // 軸設定
                ticks: {
                    beginAtZero: true,
                },
                xAxes: [ // Ｘ軸設定
                    {
                        display: true,                // 表示の有無
                        barPercentage: 0.8,           // カテゴリ幅に対する棒の幅の割合
                        //categoryPercentage: 0.8,    // 複数棒のスケールに対する幅の割合
                        scaleLabel: {                 // 軸ラベル
                            display: true,                // 表示設定
                            // labelString: '横軸ラベル', // ラベル
                            fontColor: "red", // 文字の色
                            fontSize: 7 // フォントサイズ
                        },
                        gridLines: { // 補助線
                            display: false // 補助線なし
                        },
                        ticks: { // 目盛り
                            fontColor: "red", // 目盛りの色
                            fontSize: 14, // フォントサイズ
                            autoSkip: false,
                            maxRotation: 90,
                            minRotation: 90,
                        },
                    }
                ],
                yAxes: [
                    {
                        ticks: {
                            beginAtZero: true,
                            suggestedMin: 0,
                        }
                    }
                ],
            },
            layout: {
                padding: {x: 20, y: 30}
            }
        }
    });


}


function split_word_20letters(word_list){
    let splitted_word_list = []
    word_list.forEach(word => {
        let chunk_list = []
        if (word.length > 14){
            for(let i = 0; i < word.length % 14; i++){
                chunk_list.push(word.substr(i * 14, 14))
            }
        }else{
            chunk_list.push(word)
        }
        splitted_word_list.push(chunk_list)
    });

    return splitted_word_list
}