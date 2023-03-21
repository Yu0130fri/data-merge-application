let title = document.getElementById('chart_title').value;
let question_num = document.getElementById('question_num').value;
let dstr = String(document.getElementById('chart_data').value);
let darr = dstr.split(',');
let dlabel = String(document.getElementById('chart_labels').value);
let larr = dlabel.split(',');
let ctx = document.getElementById('myChart').getContext('2d');
let myRadarChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: larr,
        datasets: [{
            data:darr,//app.pyのchart_data
            backgroundColor: "rgba(255,0,0,0.2)", // 線の下の塗りつぶしの色
            borderColor: "red",                   // 線の色
            borderWidth: 2,                       // 線の幅
            label: question_num //app.pyのchart_question_num
            }
        ]
    },
    // options: {
    //     responsive: true,
    //     title: {                // タイトル
    //         display: true,      // 表示する
    //         fontSize: 20,       // タイトルのフォント
    //         text: title         //app.pyのchart_title
    //     },
    //     legend: {
    //         position: 'bottom', // 凡例の表示位置
    //         labels: {
    //             fontSize: 20,   // 判例のフォントサイズ
    //         },
    //     },
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

