from django.shortcuts import render, get_object_or_404, reverse

from .models import Topic

# Create your views here.
def list_topics(request):
    topics = Topic.objects.filter(user=request.user)
    return render(request, 'core/list_topics.html', {'topics': topics})

def topic_detail(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    context = {}
    context['topic'] = topic
    return render(request, 'core/topic_detail.html', context)
