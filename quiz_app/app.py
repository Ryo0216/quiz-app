from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# クイズデータ（無限に出題できるようにランダム化）
quiz_data = [
    {
        "id": 1,
        "question": "地球の周囲の長さは何キロメートルですか？",
        "choices": ["4000km", "24000km", "40000km"],
        "correct_answer": "40000km"
    },
    {
        "id": 2,
        "question": "最も長い川はどれですか？",
        "choices": ["アマゾン川", "ナイル川", "長江"],
        "correct_answer": "ナイル川"
    },
    {
        "id": 3,
        "question": "世界で最も高い山はどれですか？",
        "choices": ["エベレスト山", "キリマンジャロ", "富士山"],
        "correct_answer": "エベレスト山"
    },
    {
        "id": 4,
        "question": "イギリスの首都はどこですか？",
        "choices": ["ロンドン", "パリ", "ベルリン"],
        "correct_answer": "ロンドン"
    }
]

@app.route('/')
def index():
    # ランダムにシャッフルして新しい順番で問題を表示
    random.shuffle(quiz_data)
    return render_template('quiz.html', quiz=quiz_data[0], total=len(quiz_data), question_index=0)

@app.route('/submit', methods=['POST'])
def submit():
    question_index = int(request.form['question_index'])
    answers = request.form
    score = 0
    correct_answer = quiz_data[question_index]['correct_answer']
    
    # 正解した場合のスコア加算
    if answers.get(str(quiz_data[question_index]['id'])) == correct_answer:
        score += 1
    
    # 次の問題に移動
    next_question_index = question_index + 1 if question_index + 1 < len(quiz_data) else 0  # 最後の問題なら最初に戻る

    return render_template('quiz.html', quiz=quiz_data[next_question_index], total=len(quiz_data), question_index=next_question_index, score=score)

if __name__ == '__main__':
    app.run(debug=True)
