from api.models import CheckProject


def add_variable_to_context(request):
    checkproject = CheckProject.objects.first()
    title = checkproject.name
    credit = checkproject.credit
    left_credit = checkproject.left_credit
    return {
        'testme': 'Hello world!',
        'credit': credit,
        'left_credit': left_credit,
        'project_title': title
    }
