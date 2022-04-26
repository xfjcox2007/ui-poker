function updateQuizLogs(selectedOption) {
    console.log("updateQuizLogs")
    let question = window.location.href.split("/").pop()
    $.ajax({
        type: "POST",
        url: "/updateQuiz",
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify({selection: selectedOption, page: question}),
        success: function (result) {
            console.log("success::", result)
            populateDropDowns()
        },
        error: function (request, status, error) {
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

function submitOption() {
    console.log("submitOption")
    updateQuizLogs(selectedOptionQuiz)
    let next = parseInt(quizIndex) + 1
    window.location.href = "/quiz/" + next

}

let selectedOptionQuiz

$(document).ready(function () {
    selectedOptionQuiz = 0;
    if (question.type === 'mcq') {
        $('.mcq .choice:nth-child(1)').attr('selected', 'true');

        $('.choice').click(function (e) {
            selectedOptionQuiz = $(this).index();
            deselectAll();
            console.log(selectedOptionQuiz);

            $(`.mcq .choice:nth-child(${selectedOptionQuiz + 1})`).attr('selected', 'true');
        });

        function deselectAll() {
            for (let i = 0; i < question.options.length; i++) {
                $(`.mcq .choice`).removeAttr('selected');
            }
        }

        //updateQuizLogs(selectedOptionQuiz);
    }
});
