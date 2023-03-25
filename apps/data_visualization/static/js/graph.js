let title = document.getElementById('chart_title').value;
let question_num = document.getElementById('question_num').value;

let chart_data_list = String(document.getElementById('chart_data').value);
let chart_values = chart_data_list.split(',');

let chart_label_list = String(document.getElementById('chart_labels').value);
let chart_labels = chart_label_list.replace("[", "").replace("]", "").replace(" ", "").replace("'", "").split(',');
let ctx = document.getElementById('myChart').getContext('2d');

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

// chart_labels.map((v)=>v.replace('ー','丨').split(""))

let myRadarChart = new Chart(ctx, {
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
            xAxes: [                           // Ｘ軸設定
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
                        maxRotation: 0,
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
    // options: {
        // legend: {
        //     position: 'bottom', // 凡例の表示位置
        //     labels: {
        //         fontSize: 20,   // 判例のフォントサイズ
        //     },
        // },
    //     scale: {
    //         // スケールを隠す。
    //         display: true,      // メモリを表示する
    //         ticks: {            // 目盛り
    //             min: 0,         // 目盛りの最小値
    //             max: 10,        // 目盛りの最大値
    //             stepSize: 1,    // 目盛の間隔
    //             fontSize: 12,   // 目盛り数字の大きさ
    //             fontColor: "purple"  // 目盛り数字の色
    //         },
    //         pointLabels: {
    //             fontSize: 20    // チャートラベルのフォントサイズ
    //         },
    //         angleLines: {        // 軸（放射軸）
    //             display: true,
    //             color: "maroon"
    //         },
    //         gridLines: {         // 補助線（目盛の線）
    //             display: true,
    //             color: "lime"
    //         }
    //     },
    // }
});

