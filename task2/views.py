from django.http import HttpResponse
from django.shortcuts import render
from .tasks import send_review_task
from django.views import View


class ReviewView(View):
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        context = dict()
        return render(request, 'review.html', context)

    def post(self, request):
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        review = request.POST.get('review')

        send_review_task.delay(subject, email, review)

        return HttpResponse("Thanks For Your Review")
