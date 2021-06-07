from app2email.forms import ReviewForm
from django.views.generic.edit import FormView
from django.http import HttpResponse


class ReviewEmailView(FormView):
    template_name = 'review.html'
    form_class = ReviewForm

    def form_valid(self, form):
        print('r1')
        form.send_email()
        msg = 'thank for the review'

        return HttpResponse(msg)
