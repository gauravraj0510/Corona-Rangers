from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Category, Donation
from django.views.generic import (ListView, DetailView, CreateView,UpdateView, DeleteView)
from .forms import PostForm, Form
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages



def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

# def DonateView(request):
#     if request.method == 'POST':
#         form = Form(request.POST)
#         if form.is_valid():
#             form.save()
#             model = Donation()
#             model.donor = self.request.user
#             messages.success(request, f'Thankyou!')
#             return redirect('dashboard')
#     else:
#         form = Form()
#     return render(request, 'blog/donate.html', {'form': form})

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

def PostDetailView(request,pk):
    form = ""
    if request.method== 'POST':
        form=Form(request.POST)
        if form.is_valid():
            print(type(request.user))
            form.save()
            donation =Donation()
            post = get_object_or_404(Post, pk=pk)
            qty=form.cleaned_data.get('quantity')
            donation.quantity=qty
            donation.receiver= post.author
            donation.donor= request.user
            donation.category= post.category
            donation.save()
            send_mail('Corona Rangers has some great news for you',f' {donation.donor} ({request.user.email}) wants to donate  {qty} { donation.category}',settings.EMAIL_HOST_USER,[f'{post.author.email}'],fail_silently=False)
            messages.success(request, f'We have notified the NGO, thankyou for the donation.The NGO will contact you')
            return redirect('dashboard')
        else:
            pass
    else:
        form=Form()
        context = {
            "form": form,
            "post": get_object_or_404(Post, pk=pk),
        }
        return render(request,'blog/post_detail.html',{
                "form": form,
                "post": get_object_or_404(Post, pk=pk),
            })
 

def DashboardView(request):
    donations = Donation.objects.filter(donor=request.user)
    recieved = Donation.objects.filter(receiver=request.user)
    context = {
        'donations': donations,
        'recieved': recieved
    }
    return render(request, 'blog/dashboard.html', context)
    
# class DonateView(DetailView):
#     model=Donation
#     form_class = Form
#     template_name = 'blog/donate.html'

#     def form_valid(self, form):
#         form.instance.donor = self.request.user
#         return super().form_valid(form)


# def Donate(request,pk):
#     if request.method== 'POST':
#         forms=Form(request.POST)
#         if form.is_valid():
#             user=form.save()
#             donation =Donation()
#             post =Post()
#             qty=form.clean_data.get('quantity')
#             donation.quantity=qty
#             donation.receiver= post.author
#             donation.donor= self.request.user
#             donation.categories= post.categories
#             donation.save()
#             messages.success(request, f'Thankyou for donating!')
#             return redirect('dashboard')
#     else:
#         form=Form()
#         post = Post.objects.filter(id=pk)
#         context = {
#             "form": form,
#             "post": post
#         }
#     return render(request,'blog/post_detail.html',context)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# class AddCategoryView(CreateView):
#     model = Post
#     template_name = 'blog/add_category.html'
#     fields = '__all__'

# class PostCreateView(LoginRequiredMixin, CreateView):
#     model = Post
#     fields = ['title', 'content','category']

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content','category']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/blogs/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', {'posts': Post.objects.all()})
    
def mainhome(request):
    return render(request, 'blog/index.html')

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats)
    return render(request, 'blog/categories.html', {'cats': cats, 'category_posts': category_posts})