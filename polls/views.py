from django.http import HttpResponse


def index(_):  # pylint: disable=unused-argument
    return HttpResponse("Hello! Polls index")


def detail(_, question_id):
    return HttpResponse(f"You're looking at question {question_id}.")


def results(_, question_id):
    response = f"You're looking at the results of question {question_id}."
    return HttpResponse(response)


def vote(_, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")
