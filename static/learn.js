function toHtml(p) {
    let text = p.text
    p.highlight.forEach(t => {
        text = text.replace(t, "<u><b>$&</b></u>")
    })
    return text
}

function renderReturnToQuiz() {
    $('#returntoQuiz').empty()
    fetch("/fetchData")
        .then(function (response) {
            return response.json()
        })
        .then(function (data) {
            let quiz = data["quiz"]
            let quizKeys = Object.keys(quiz)
            console.log(quiz)
            for (let i = 0; i < quizKeys.length; i++) {
                key = quizKeys[i]
                if (quiz[key]["status"] === "unattempted") {
                    $('#returntoQuiz').append(`<a
							href="/quiz/${key}"
							class="btn btn-next">
							<h3 class="mx-4 my-0">Return</h3>
						  </a>`)
                    break
                }
            }

        })

}

$(document).ready(function () {
    renderReturnToQuiz()
});
