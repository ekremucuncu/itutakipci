from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Distribution,Lecturer,Lecture,Comment
from .forms import CommentForm
from django.urls import reverse_lazy,reverse
from django.views.generic.edit import ModelFormMixin,FormMixin


# Create your views here.

class Index(generic.ListView):
    template_name='home.html'
    models=Lecturer
    queryset = Lecturer.objects.all()


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['lecturer_list'] = Lecturer.objects.order_by('lecturer')
        return context



class LecturerDistribution(FormMixin, generic.DetailView):
    model = Lecturer
    template_name = 'lecturer.html'
    context_object_name = 'post'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super(LecturerDistribution, self).get_context_data(**kwargs)
        context ['lecturer'] = self.object
        context ['distribution'] = Distribution.objects.filter(lecturer=self.object).order_by('lecture')
        context ['commentmodel_list'] = Comment.objects.filter(lecturer=self.object).order_by('-created_on')
        context['form'] = CommentForm(initial={'lecturer': self.object})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.lecturer=self.object
        form.instance.author_security = self.request.user
        if form.instance.anon==True:
            pass
        else:
            form.instance.author=self.request.user
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('distribution:lecturer_distribution', kwargs={'slug': self.object.slug})


class LectureDistribution(generic.DetailView):
    model=Lecture
    template_name='lecture.html'

    def get_success_url(self):
        return reverse('lecture_distribution', kwargs={'slug': self.object.slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['distribution_'] = Distribution.objects.filter(lecture=self.object).order_by('-created_on')
        return context
